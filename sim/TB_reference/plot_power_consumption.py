import sys
import pandas as pd
import matplotlib.pyplot as plt


args = sys.argv[1:]
files = list()
tempeartures = [-40, 0, 40, 80, 125] # Degrees Celsius (°C)

stepping_direction = ""
if "up" in args:
    args.remove("up")
    stepping_direction = "up"
elif "down" in args:
    args.remove("down")
    stepping_direction = "down"
else: 
    stepping_direction = "down"
print(f"Plotting for transient signals stepping {stepping_direction}")


if "custom" in args:
    corner = args[-3]
    voltage = float(args[-2]) # Volt (V)
    Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
    temperature = int(args[-1]) # Celsius (degree C)
    print(f"Custom settings: corner={corner}, voltage={voltage} V, Vx={Vx}, temperature={temperature} °C")
    files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

if "etc" in args:
    for corner in ["ss", "ff", "sf", "fs"]:
        for voltage in [1.7, 1.9]: # Volt (V)
            Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
            for temperature in tempeartures: # Celsius (degree C)
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

runs = 30

if "mc" in args:
    for corner in ["ttmm"]:
        for voltage in [1.8]: # Volt (V)
            Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
            for temperature in tempeartures: # Celsius (degree C)
                for run in range(1, runs): # Assuming 30 Monte Carlo runs
                    if run == 0:
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")
                    else:
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_{run}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")


if "mccustom" in args:
    corner = "ttmm"
    run = args[-3]
    voltage = float(args[-2]) # Volt (V)
    Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
    temperature = int(args[-1]) # Celsius (degree C)
    print(f"Custom settings: corner={corner}, voltage={voltage} V, Vx={Vx}, temperature={temperature} °C")
    if run == 0:
        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")
    else:
        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_{run}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")


figure_width = 4
figure_height = 4
font_size = 6
title_size = font_size
label_size = font_size
legend_size = font_size
ticks_size = font_size










for file in files:
    print(f"Plotting transient results from file: {file}")

    filename = file.split("/")[-1].split(".out")[0]

    circuit_temperature = float(filename.split("_")[-2].replace("celsius", "")) # in degrees Celsius
    voltage_supply = float(filename.split("_")[-1].replace("volt", "")) # in Volt
    process_shorthand = filename.split("GtK")[-1].split("Tt")[0] # tt/ss/ff/sf/fs

    if process_shorthand == "tt":
        process_corner = "Typical"
    elif process_shorthand == "ss":
        process_corner = "Slow-Slow"
    elif process_shorthand == "ff":
        process_corner = "Fast-Fast"
    elif process_shorthand == "sf":
        process_corner = "Slow-Fast"
    elif process_shorthand == "fs":
        process_corner = "Fast-Slow"
    else:
        process_corner = "Oops, something is wrong!"

    fig, axs = plt.subplots(3, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

    df = pd.read_csv(file, sep="\s+")

    df['time'] = df['time'] * 1e6 # in us

    idx = df[df["v(slp)"] > 0.90 * 1.8].index[-10] if len(df[df["v(slp)"] > 0.90 * 1.8]) > 10 else 0
    timestamp = df["time"][idx] if idx is not None else None

    window = 100 # in number of samples
    df["pwr"] = df["v(vdd)"] * -(df["i(vdd)"]) * 1e6 # in uW (micro Watt)
    df["mov_avg_pwr"] = df["pwr"].rolling(window=window).mean() # moving average filter with window size of 100 applied to the power plot
    df["fil_pwr"] = df.loc[df['mov_avg_pwr'] < 0.025, 'mov_avg_pwr'] # moving average filter with window size of 100 applied to the power plot, but only for the datapoints where v(slp) is above 0.99 * VDD

    slp_pwr = df.loc[idx, 'mov_avg_pwr']
    print(f"{slp_pwr} uW")

    idd_pwr = -df.loc[idx, "i(vdd)"] * 1e6 # in uA (micro Ampere)
    print(f"{idd_pwr} uA")

    axs[0].plot(df["time"], df["v(rst)"], label="rst")
    axs[0].plot(df["time"], df["v(slp)"], label="slp")
    axs[0].plot(df["time"], df["v(mode)"], label="mode")

    axs[1].plot(df["time"], -(df["i(vdd)"]) * 1e6, label="idd") # in uA (micro Ampere)

    axs[2].plot(df["time"], df["pwr"], label="pwr")
    axs[2].plot(df["time"], df["mov_avg_pwr"], label=f"mov. avg. (w={window})")

    axs[0].set_ylabel("Voltage (V)", fontsize=label_size)
    axs[1].set_ylabel("Current (uA)", fontsize=label_size)
    axs[2].set_ylabel("Power (uW)", fontsize=label_size)

    axs[0].axvline(x=timestamp, color="black", linestyle="dashed")
    axs[1].axvline(x=timestamp, color="black", linestyle="dashed", label=f"Sleep current measured \nat {timestamp:.2f} us = {idd_pwr:.4f} uA")
    axs[2].axvline(x=timestamp, color="black", linestyle="dashed", label=f"Sleep power measured at \n{timestamp:.2f} us = {slp_pwr*1e3:.2f} nW")

    for i, ax in enumerate(axs):
        ax.tick_params(axis="both", labelsize=ticks_size)
        ax.grid()
        ax.legend(loc="best", fontsize=legend_size)

    axs[0].set_title(f"Power Consumption, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_size, fontweight='bold')
    axs[-1].set_xlabel("Time (us)", fontsize=label_size)
    axs[-1].set_ylim(-df["mov_avg_pwr"].max()*0.1, df["mov_avg_pwr"].max()*1.15)

    fig.tight_layout()
    fig.savefig(f"plots/{filename}_power_consumption.png", dpi=300, bbox_inches="tight")
    print(f"Saved figure to plots/{filename}_power_consumption.png")


if args[0] == "custom":
    plt.show()
else:
    plt.close("all")