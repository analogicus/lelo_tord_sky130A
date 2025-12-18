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
            avg_diffs = []

            for temp in temperatures:
                print()
                out_files = glob.glob(f"output_tran/tran_SchGtK{corner}Tt{Vx}_temperature{temp}celsius_frequency*mhz_dutycycle*percent_vdd{voltage}volt.out")
                print(f'Found files: {out_files}')

                prev_smallest_avg_diff = np.inf
                final_zero_crossings = pd.Series([0])
                final_zero_crossings_vout_values = pd.Series([1])
                for file in out_files:
                    print(f'Plotting transient results from file: {file}')

                    circuit_temperature = int(file.split("temperature")[-1].split("celsius")[0]) # in Celsius degree
                    clock_frequency = int(file.split("frequency")[-1].split("mhz")[0]) # in Mega Hertz
                    clock_periode = 1 / clock_frequency  # in micro seconds
                    duty_cycle = int(file.split("dutycycle")[-1].split("percent")[0]) # in Percent
                    voltage_supply = float(file.split("vdd")[-1].split("volt")[0]) # in Volt
                    process_corner = "Typical" if "tt" in file else "Slow-Slow" if "ss" in file else "Slow-Fast" if "sf" in file else "Fast-Slow" if "fs" in file else "Fast-Fast" if "ff" in file else "Oops, something is wrong!"

                    df = pd.read_csv(file, sep="\s+")
                    
                    # print(df.columns)
                    # print(df.head())
                    # print(df.tail())

                    df['time'] = df['time'] * 1e9 # in ns
                    df['diff'] = df['v(v1)']-df['v(v2)']

                    zero_crossings = df.index[(df['diff'].shift(1) * df['diff']) < 0]
                    zero_crossings_time_values = df.loc[zero_crossings, 'time'].values
                    zero_crossings_vout_values = df.loc[zero_crossings, 'v(vout)'].values
                    
                    if len(zero_crossings) > 8:
                        print(f'Zero crossings found at indices: {zero_crossings.tolist()}')
                        print(f'Zero crossings found at time values (ns): {zero_crossings_time_values.tolist()}')
                        print(f'Zero crossings found at vout values (V): {zero_crossings_vout_values.tolist()}')

                        # average diff from first to last zero crossing
                        avg_diff = df.loc[zero_crossings[-8]:zero_crossings[-2], 'diff'].mean()
                        print(f'Average diff between first ({zero_crossings[-8]}) and last ({zero_crossings[-2]}) zero crossing (V): {avg_diff}')

                        if (np.abs(avg_diff) < prev_smallest_avg_diff): # threshold to consider stable operation
                            print(f'Updating from previous avg diff: {prev_smallest_avg_diff}, to new smallest avg diff: {np.abs(avg_diff)}')
                            prev_smallest_avg_diff = np.abs(avg_diff)
                            final_temp = circuit_temperature
                            final_clock_frequency = clock_frequency
                            final_duty_cycle = duty_cycle
                            final_process_corner = process_corner
                            final_voltage_supply = voltage_supply
                            final_zero_crossings = zero_crossings
                            final_zero_crossings_vout_values = df.loc[final_zero_crossings, 'v(vout)'].values
                            final_zero_crossings_time_values = df.loc[final_zero_crossings, 'time'].values
                

                if len(final_zero_crossings_vout_values.tolist()) > 8:
                    times.append(final_zero_crossings_time_values.tolist()[-2]) # second last (-2) instead of last (-1) value because that is when we shift DAC
                    vouts.append(final_zero_crossings_vout_values.tolist()[-2]) # second last (-2) instead of last (-1) value because that is when we shift DAC
                    temps.append(int(final_temp))
                    duty_cycles.append(final_duty_cycle)
                    frequencies.append(final_clock_frequency)
                    avg_diffs.append(prev_smallest_avg_diff)
                else:
                    print(f'No stable zero crossings found for temp {temp} C, corner {corner}, voltage {voltage} V')


            print(f'temps: {temps}')
            print(f'vouts: {vouts}')
            print(f'times: {times}')
            print(f'duty_cycles: {duty_cycles}')
            print(f'frequencies: {frequencies}')
            print(f'avg_diffs: {avg_diffs}')

            # data[f"{corner}_{voltage}"] = {[temps, vouts, times]}

            axs.plot(temps, vouts, label=f"{process_corner} corner, {voltage_supply} V", marker='o', linestyle= 'dashed') # in V
            last_color = axs.lines[-1].get_color()
            
            # find linear fit coefficients
            # fit_coeffs = np.polyfit(temps, vouts, 1)
            # fit_line = np.poly1d(fit_coeffs)
            # axs.plot(temps, fit_line(temps), color=last_color, linestyle='dotted')

    # axs.plot([], [], label=f"best fits", color="black", linestyle='dotted')

    axs.tick_params(axis='both', labelsize=ticks_fontsize)
    axs.grid()
    axs.set_ylabel('Voltage (V)', fontsize=label_fontsize)
    axs.set_xlabel('Temperature [°C]', fontsize=label_fontsize)
    # axs.set_title('Vout vs Temperature', fontsize=title_fontsize)
    axs.legend(loc="upper left", fontsize=legend_fontsize)

    fig.tight_layout()
    fig.savefig(f'figures/vout_vs_temp_{corners}_{voltages}.png', dpi=300, bbox_inches="tight")

    plt.show()

