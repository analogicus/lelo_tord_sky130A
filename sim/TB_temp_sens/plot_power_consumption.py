import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
import glob

# Example input arguments: typical -40 -20 0 20 27 40 60 80 100 125

if __name__ == "__main__":

    fig_width = 5
    fig_height = 5
    font_size = 8
    title_fontsize = font_size
    label_fontsize = font_size
    legend_fontsize = font_size
    ticks_fontsize = font_size

    fig, ax = plt.subplots(3, 1, figsize=(fig_width, fig_height), sharex=True)
    
    view = "Sch"
    # view = "Lay"

    args = sys.argv[1:]
    files = list()

    if len(args) == 0:
        print("No arguments provided. Plotting for typical corner, voltage (1.8 Volt) and temperature (27 Celsius).")
        args.append("typical")

    if "typical" in args:
        files.append("output_tran/tran_SchGtKttTtVt_temperature27celsius_frequency2mhz_dutycycle35percent_vdd1.8volt.out")
    elif "all" in args:
        for temperature in [-40, 0, 27, 125]: # Celsius (degree C)
            for frequency in [1, 2, 5, 10]: # Mega Hertz (MHz)
                for dutycycle in [5, 35, 65, 95]: # Percent (%)
                    for voltage in [1.7, 1.8, 1.9]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_{view}GtKttTt{Vx}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
    elif "report" in args:
        for temperature in [-40, 0, 27, 125]: # Celsius (degree C)
            for frequency in [2]: # Mega Hertz (MHz)
                for dutycycle in [35]: # Percent (%)
                    for voltage in [1.7, 1.9]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_{view}GtKttTt{Vx}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
    elif "test" in args:
        for temperature in [0]: # Celsius (degree C)
            for frequency in [2]: # Mega Hertz (MHz)
                for dutycycle in [35]: # Percent (%)
                    for voltage in [1.8]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_{view}GtKttTt{Vx}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
    else:
        print("Plotting with file data passed as argument.")
        xx = "tt" if args[0] == "tt" else "ff" if args[0] == "ff" else "ss" if args[0] == "ss" else "sf" if args[0] == "sf" else "fs" if args[0] == "fs" else "Oops, Somethings wrong!"
        Vx = "Vl" if float(args[4]) == 1.7 else "Vt" if float(args[4]) == 1.8 else "Vh" if float(args[4]) == 1.9 else "Oops"
        files.append(f"output_tran/tran_{view}GtK{xx}Tt{Vx}_temperature{args[1]}celsius_frequency{args[2]}mhz_dutycycle{args[3]}percent_vdd{args[4]}volt.out") # plots file name passed as argument

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

        ax[0].plot(df['time'], df['v(vdd)'], label=f"{process_corner} corner, {voltage_supply} V, {circuit_temperature} °C, {clock_frequency} MHz, {duty_cycle} %", linestyle="solid")
        last_color = ax[0].lines[-1].get_color()
        ax[0].plot(df['time'], df['v(vss)'], linestyle='dashed', color=last_color)
        
        ax[1].plot(df['time'], -df['i(vdd)']*1e6, label=f"{process_corner} corner, {voltage_supply} V, {circuit_temperature} °C, {clock_frequency} MHz, {duty_cycle} %", linestyle="solid")
        last_color = ax[1].lines[-1].get_color()
        ax[1].plot(df['time'], -df['i(vss)']*1e6, linestyle='dashed' , color=last_color)

        ax[2].plot(df['time'], df["v(vdd)"]*df["i(vdd)"], label=f"{process_corner} corner, {voltage_supply} V, {circuit_temperature} °C, {clock_frequency} MHz, {duty_cycle} %", linestyle="solid")

    ax[0].tick_params(axis='both', which='major', labelsize=ticks_fontsize)
    ax[0].set_ylabel("Voltage (V)", fontsize=label_fontsize)
    ax[0].set_title("Vdd", fontsize=title_fontsize)
    ax[0].legend(fontsize=legend_fontsize)
    ax[0].grid()

    ax[1].tick_params(axis='both', which='major', labelsize=ticks_fontsize)
    ax[1].set_ylabel("Current (uA)", fontsize=label_fontsize)
    ax[1].set_title("Idd", fontsize=title_fontsize)
    ax[1].legend(fontsize=legend_fontsize)
    ax[1].grid()

    ax[2].tick_params(axis='both', which='major', labelsize=ticks_fontsize)
    ax[2].set_ylabel("Power (uW)", fontsize=label_fontsize)
    ax[2].set_title("Power", fontsize=title_fontsize)
    ax[2].legend(fontsize=legend_fontsize)
    ax[2].grid()

    ax[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)

    fig.tight_layout()
    fig.savefig(f"figures/plot_power_consumption.png", dpi=300, bbox_inches="tight")

    plt.show()