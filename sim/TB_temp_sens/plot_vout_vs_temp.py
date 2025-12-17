import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
import glob

# Example input arguments: typical -40 -20 0 20 27 40 60 80 100 125

if __name__ == "__main__":

    fig_width = 3
    fig_height = 3
    font_size = 8
    title_fontsize = font_size
    label_fontsize = font_size
    legend_fontsize = font_size
    ticks_fontsize = font_size
    view = "Sch"
    # view = "Lay"

    names = list()
    data = dict()

    args = sys.argv[1:]
    case = args[0] if len(args) > 0 else "typical"

    corners = list()
    voltages = list()
    temperatures = args[1:] if len(args) > 1 else [-40, 0, 27, 125]

    print(args)

    if case == "all":
        corners = ["tt", "ff", "ss", "sf", "fs"]
        voltages = ["1.7", "1.8", "1.9"]
    elif case == "typical":
        corners = ["tt"]
        voltages = ["1.8"]
    elif case == "etc":
        corners = ["ff", "ss", "sf", "fs"]
        voltages = ["1.7", "1.9"]
    elif case == "test":
        corners = ["tt"]
        voltages = ["1.7", "1.8", "1.9"]

    print(f'corners: {corners}')
    print(f'voltages: {voltages}')
    print(f'temperatures: {temperatures}')

    fig, axs = plt.subplots(1, 1, figsize=(fig_width, fig_height), sharex=True)

    for corner in corners:  

        for voltage in voltages:

            Vx = "Vl" if voltage == "1.7" else "Vt" if voltage == "1.8" else "Vh" if voltage == "1.9" else "Oops"
    
            temps = []
            vouts = []
            times = []
            duty_cycles = []
            frequencies = []

            for temp in temperatures:
                out_files = glob.glob(f"output_tran/tran_SchGtK{corner}Tt{Vx}_temperature{temp}celsius_frequency*mhz_dutycycle*percent_vdd{voltage}volt.out")
                print(f'Found file(s): {out_files}')

                for file in out_files:
                    print(f'Plotting transient results from file: {file}')

                    circuit_temperature = int(file.split("temperature")[-1].split("celsius")[0]) # in Celsius degree
                    clock_frequency = int(file.split("frequency")[-1].split("mhz")[0]) # in Mega Hertz
                    clock_periode = 1 / clock_frequency  # in micro seconds
                    duty_cycle = int(file.split("dutycycle")[-1].split("percent")[0]) # in Percent
                    voltage_supply = float(file.split("vdd")[-1].split("volt")[0]) # in Volt
                    process_corner = "Typical" if "tt" in file else "Slow-Slow" if "ss" in file else "Slow-Fast" if "sf" in file else "Fast-Slow" if "fs" in file else "Fast-Fast" if "ff" in file else "Oops, something is wrong!"

                    df = pd.read_csv(file, sep="\s+")
                    
                    print(df.columns)
                    print(df.head())
                    print(df.tail())

                    df['time'] = df['time'] * 1e9 # in ns
                    df['diff'] = df['v(v1)']-df['v(v2)']

                    zero_crossings = df.index[(df['diff'].shift(1) * df['diff']) < 0]

                    times.append(df.loc[zero_crossings[-2], 'time']) # second last (-2) instead of last (-1) value because that is when we shift DAC
                    vouts.append(df.loc[zero_crossings[-2], 'v(vout)']) # second last (-2) instead of last (-1) value because that is when we shift DAC
                    temps.append(int(temp))
                    duty_cycles.append(duty_cycle)
                    frequencies.append(clock_frequency)
        
            print(f'temps: {temps}')
            print(f'vouts: {vouts}')
            print(f'times: {times}')
            print(f'duty_cycles: {duty_cycles}')
            print(f'frequencies: {frequencies}')

            # data[f"{corner}_{voltage}"] = {[temps, vouts, times]}

            axs.plot(temps, vouts, label=f"{process_corner} corner, {voltage_supply} V", marker='o', linestyle= 'dashed') # in V
            last_color = axs.lines[-1].get_color()
            
            # find linear fit coefficients
            fit_coeffs = np.polyfit(temps, vouts, 1)
            fit_line = np.poly1d(fit_coeffs)
            axs.plot(temps, fit_line(temps), color=last_color, linestyle='dotted')

    axs.plot([], [], label=f"best fits", color="black", linestyle='dotted')

    axs.tick_params(axis='both', labelsize=ticks_fontsize)
    axs.grid()
    axs.set_ylabel('Voltage (V)', fontsize=label_fontsize)
    axs.set_xlabel('Temperature [$^\\circ$C]', fontsize=label_fontsize)
    # axs.set_title('Vout vs Temperature', fontsize=title_fontsize)
    axs.legend(fontsize=legend_fontsize)

    fig.tight_layout()
    fig.savefig(f'figures/vout_vs_temp_{corners}_{voltages}.png', dpi=300, bbox_inches="tight")

    plt.show()

