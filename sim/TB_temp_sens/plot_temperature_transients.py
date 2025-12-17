import pandas as pd
import matplotlib.pyplot as plt
import sys

args = sys.argv[1:]

files = list()

# example input arguments: python plot_temperature_transients.py ss 125 2 30 1.7

if len(args) == 0:
    print("No arguments provided. Plotting for typical corner, voltage (1.8 Volt) and temperature (27 Celsius).")
    files.append("output_tran/tran_SchGtKttTtVt_temperature27celsius_frequency2mhz_dutycycle35percent_vdd1.8volt.out")
elif "typical" in args:
    files.append("output_tran/tran_SchGtKttTtVt_temperature27celsius_frequency2mhz_dutycycle35percent_vdd1.8volt.out")
elif "all" in args:
    for temperature in [-40, 0, 27, 125]: # Celsius (degree C)
        for frequency in [1, 2, 5, 10]: # Mega Hertz (MHz)
            for dutycycle in [5, 35, 65, 95]: # Percent (%)
                for voltage in [1.7, 1.8, 1.9]: # Volt (V)
                    Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                    files.append(f"output_tran/tran_SchGtKttTt{Vx}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
elif "report" in args:
    for temperature in [-40, 27, 125]: # Celsius (degree C)
        for frequency in [2]: # Mega Hertz (MHz)
            for dutycycle in [35]: # Percent (%)
                for voltage in [1.7, 1.9]: # Volt (V)
                    Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                    files.append(f"output_tran/tran_SchGtKttTt{Vx}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
elif "test" in args:
    for temperature in [0]: # Celsius (degree C)
        for frequency in [2]: # Mega Hertz (MHz)
            for dutycycle in [35]: # Percent (%)
                for voltage in [1.8]: # Volt (V)
                    Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                    files.append(f"output_tran/tran_SchGtKttTt{Vx}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
else:
    print("Plotting with file data passed as argument.")
    xx = "tt" if args[0] == "tt" else "ff" if args[0] == "ff" else "ss" if args[0] == "ss" else "sf" if args[0] == "sf" else "fs" if args[0] == "fs" else "Oops, Somethings wrong!"
    Vx = "Vl" if float(args[4]) == 1.7 else "Vt" if float(args[4]) == 1.8 else "Vh" if float(args[4]) == 1.9 else "Oops"
    files.append(f"output_tran/tran_SchGtK{xx}Tt{Vx}_temperature{args[1]}celsius_frequency{args[2]}mhz_dutycycle{args[3]}percent_vdd{args[4]}volt.out") # plots file name passed as argument

fig_width = 3
fig_height = 5
font_size = 8
title_fontsize = font_size
label_fontsize = font_size
legend_fontsize = font_size
ticks_fontsize = font_size

for file in files:
    print(f"Plotting Vout transient results from file: {file}")

    circuit_temperature = int(file.split("temperature")[-1].split("celsius")[0]) # in Celsius degree
    clock_frequency = int(file.split("frequency")[-1].split("mhz")[0]) # in Mega Hertz
    clock_periode = 1 / clock_frequency  # in micro seconds
    duty_cycle = int(file.split("dutycycle")[-1].split("percent")[0]) # in Percent
    voltage_supply = float(file.split("vdd")[-1].split("volt")[0]) # in Volt
    process_corner = "Typical" if "tt" in file else "Slow-Slow" if "ss" in file else "Slow-Fast" if "sf" in file else "Fast-Slow" if "fs" in file else "Fast-Fast" if "ff" in file else "Oops, something is wrong!"

    print(f"Circuit temperature: {circuit_temperature} Celsius degree.")
    print(f"Clock frequency of finetuning signal: {clock_frequency} Mega Hertz, and clock periode is: {clock_periode} micro seconds.")
    print(f"Duty cycle of fine tuning signal: {duty_cycle} %.")
    print(f"Supply voltage (VDD): {voltage_supply} Volt.")
    print(f"Circuit process corners: {process_corner}.")

    df = pd.read_csv(file, sep="\s+")

    print(f"Data columns: {df.columns.tolist()}")
    print(f"Dataframe shape: {df.shape}")
    print(f"Dataframe head:\n{df.head()}")
    print(f"Dataframe tail:\n{df.tail()}")

    df['time'] = df['time'] * 1e9 # in ns
    df['diff'] = df['v(v1)']-df['v(v2)']

    fig, axs = plt.subplots(4, 1, figsize=(fig_width, fig_height), sharex=True)
    ax_iout = axs[0].twinx()

    ax_iout.plot(df["time"], df["i(v.xdut.v1)"]*1e6, label="iout", color="tab:orange") # in uA
    axs[0].plot(df["time"], df["v(vout)"], label="vout", color="tab:blue") # in V

    axs[1].plot(df["time"], df["v(v1)"]-df["v(v2)"], label="v1-v2", linestyle="solid")
    axs[1].plot(df["time"], df["v(v1a)"]-df["v(v2a)"], label="v1a-v2a", linestyle="dashed")
    axs[1].plot(df["time"], df["v(v1b)"]-df["v(v2b)"], label="v1b-v2b", linestyle="dotted")
    
    axs[2].plot(df["time"], df["v(v1)"], label="v1")
    # axs[2].plot(df["time"], df["v(v1a)"], label="v1a")
    # axs[2].plot(df["time"], df["v(v1b)"], label="v1b")
    axs[2].plot(df["time"], df["v(v2)"], label="v2")
    # axs[2].plot(df["time"], df["v(v2a)"], label="v2a")
    # axs[2].plot(df["time"], df["v(v2b)"], label="v2b")
    # axs[2].plot(df["time"], df["v(v2c)"], label="v2c")

    axs[3].plot(df["time"], df["v(bt)"], label="bt", linestyle="solid")
    axs[3].plot(df["time"], df["v(x1.ctl)"], label="ctl")
    axs[3].plot(df["time"], df["v(slp)"], label="slp")

    for ax in axs:
        ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
        ax.tick_params(axis="both", labelsize=ticks_fontsize)
        ax.grid()

    axs[0].legend(loc="upper left", fontsize=legend_fontsize)
    axs[1].legend(loc="upper left", fontsize=legend_fontsize)
    axs[2].legend(loc="upper left", fontsize=legend_fontsize)
    axs[3].legend(loc="upper right", fontsize=legend_fontsize)

    ax_iout.set_ylabel("Current (uA)", fontsize=label_fontsize)
    ax_iout.legend(loc="lower right", fontsize=legend_fontsize)
    ax_iout.tick_params(axis='both', labelsize=ticks_fontsize)

    axs[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)

    axs[0].set_title(f"{process_corner} corner, {voltage_supply} V, {circuit_temperature} °C, {clock_frequency} MHz, {duty_cycle} %", fontsize=title_fontsize, fontweight='bold')

    fig.tight_layout()
    fig.savefig(f"figures/{file.split('/')[-1].split('.out')[0]}.png", dpi=300, bbox_inches="tight")

plt.show()