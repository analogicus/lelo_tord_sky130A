import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from matplotlib.patches import FancyBboxPatch


args = sys.argv[1:]
files = list()
tempeartures = [-40, 0, 40, 80, 125] # Degrees Celsius (°C)


stepping_direction = ""
if "up" in args:
    args.remove("up")
    stepping_direction = "up"
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


if "typical" in args:
    for corner in ["tt"]:
        for voltage in [1.8]: # Volt (V)
            Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
            for temperature in tempeartures: # Celsius (degree C)
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


figure_width1 = 4
figure_height1 = 4
font_size = 6
title_size = font_size
label_size = font_size
legend_size = font_size
ticks_size = font_size

figure_width = 6
figure_height = 2.5
font_size = 10


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
    elif process_shorthand == "ttmm":
        process_corner = "Monte Carlo"
    else:
        process_corner = "Oops, something is wrong!"

    df = pd.read_csv(file, sep="\s+")

    df['time'] = df['time'] * 1e6 # in us
    df['diff'] = df['v(bgr.v1)']-df['v(bgr.v2)']

    idx = df[df["v(correct_output_found)"] > 0.99 * 1.8].index[-1] if not df[df["v(correct_output_found)"] > 0.99 * 1.8].empty else 0
    timestamp = df["time"][idx] if idx is not None else None

    fig, axs = plt.subplots(4, 1, figsize=(figure_width1, figure_height1), sharex=True, dpi=300)

    axs[0].plot(df["time"], df["v(clk)"], label="clk")
    axs[0].plot(df["time"], df["v(b0)"], label="b0")
    axs[0].plot(df["time"], df["v(dac.vctl)"], label="vctl")
    axs[0].plot(df["time"], df["v(cmp_async)"], label="cmp")
    axs[0].plot(df["time"], df["v(rst)"], label="rst")
    axs[0].plot(df["time"], df["v(slp)"], label="slp")
    axs[0].plot(df["time"], df["v(mode)"], label="mode")
    axs[0].plot(df["time"], df["v(correct_output_found)"], label="out_en")

    axs[1].plot(df["time"], df["v(bgr.v1)"], label="v1")
    axs[1].plot(df["time"], df["v(bgr.v2)"], label="v2")
    axs[1].plot(df["time"], df["v(vout)"], label="vout")

    axs[2].plot(df["time"], df["v(dec_finetuning_duty_cycle)"]*1e3, label="dec_finetune")
    axs[2].plot(df["time"], df["v(dec_coarse_step_counter)"]*1e3, label="dec_coarse")

    w = 100 # in number of samples
    df["pwr"] = df["v(vdd)"] * -(df["i(vdd)"]) * 1e6 # in uW (micro Watt)
    df["mov_avg_pwr"] = df["pwr"].rolling(window=w).mean() # moving average filter with window size of 100 applied to the power plot

    axs[3].plot(df["time"], df["pwr"], label="pwr")
    axs[3].plot(df["time"], df["mov_avg_pwr"], label=f"mov. avg.")

    axs[0].set_ylabel("Voltage (V)", fontsize=label_size)
    axs[1].set_ylabel("Voltage (V)", fontsize=label_size)
    axs[2].set_ylabel("Count", fontsize=label_size)
    axs[3].set_ylabel("Power (uW)", fontsize=label_size)

    axs[0].axvline(x=timestamp, color="black", linestyle="dashed")
    axs[1].axvline(x=timestamp, color="black", linestyle="dashed", label=f"Measured at {timestamp:.2f} us")
    axs[2].axvline(x=timestamp, color="black", linestyle="dashed")
    axs[3].axvline(x=timestamp, color="black", linestyle="dashed")

    for i, ax in enumerate(axs):
        ax.tick_params(axis="both", labelsize=ticks_size)
        ax.grid()
        ax.legend(loc="best", ncol=2, fontsize=legend_size)

    axs[0].set_title(f"Transient analysis, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_size, fontweight='bold')
    axs[-1].set_xlabel("Time (us)", fontsize=label_size)
    axs[-1].set_ylim(-df["mov_avg_pwr"].max()*0.1, df["mov_avg_pwr"].max()*1.15)

    fig.tight_layout()
    fig.savefig(f"plots/{filename}_transient_analysis.png", dpi=300, bbox_inches="tight")
    print(f"Saved figure to plots/{filename}_transient_analysis.png")


    fig_input = plt.figure(dpi=300, figsize=(figure_width, figure_height))
    ax_input = fig_input.add_subplot(1, 1, 1)
    ax_input.set_title(f"BGR core inputs during operation", fontsize=font_size, fontweight='bold')

    # ax_input.plot(df["time"], df["v(clk)"], label="clk")
    # ax_input.plot(df["time"], df["v(b0)"], label="b0")
    # ax_input.plot(df["time"], df["v(dac.vctl)"], label="vctl")
    ax_input.plot(df["time"], df["v(mode)"], label="mode")
    ax_input.plot(df["time"], df["v(cmp_async)"], label="cmp")
    ax_input.plot(df["time"], df["v(rst)"], label="rst")
    ax_input.plot(df["time"], df["v(slp)"], label="slp")
    # ax_input.plot(df["time"], df["v(correct_output_found)"], label="out_en")

    # ax_input.set_xlim(45, 82.5)
    ax_input.set_xlabel("Time (us)", fontsize=font_size)
    ax_input.set_ylabel("Voltage (V)", fontsize=font_size)
    ax_input.legend(loc="best", fontsize=font_size)
    ax_input.tick_params(axis='both', labelsize=font_size)
    ax_input.grid(True)

    fig_input.tight_layout()
    fig_input.savefig(f"plots/{filename}_transient_analysis_input.png")


    fig_output = plt.figure(dpi=300, figsize=(figure_width, figure_height))
    ax_output = fig_output.add_subplot(1, 1, 1)
    ax_output.set_title(f"BGR core outputs during operation", fontsize=font_size, fontweight='bold')

    ax_output.plot(df["time"], df["v(bgr.v1)"], label="v1")
    ax_output.plot(df["time"], df["v(bgr.v2)"], label="v2")
    ax_output.plot(df["time"], df["v(vout)"], label="vout")

    ax_output.axvline(x=timestamp, color="black", linestyle="dashed", label=f"Measured at {timestamp:.2f} us")

    # ax_output.set_xlim(45, 82.5)
    ax_output.set_xlabel("Time (us)", fontsize=font_size)
    ax_output.set_ylabel("Voltage (V)", fontsize=font_size)
    ax_output.legend(loc="best", fontsize=font_size)
    ax_output.tick_params(axis='both', labelsize=font_size)
    ax_output.grid(True)

    fig_output.tight_layout()
    fig_output.savefig(f"plots/{filename}_transient_analysis_output.png")


    fig_count = plt.figure(dpi=300, figsize=(figure_width, figure_height))
    ax_count = fig_count.add_subplot(1, 1, 1)
    ax_count.set_title(f"DAC inputs during operation", fontsize=font_size, fontweight='bold')

    ax_count.plot(df["time"], df["v(dec_finetuning_duty_cycle)"]*1e3, label="dec_finetune")
    ax_count.plot(df["time"], df["v(dec_coarse_step_counter)"]*1e3, label="dec_coarse")

    # ax_count.set_xlim(45, 82.5)
    ax_count.set_xlabel("Time (us)", fontsize=font_size)
    ax_count.set_ylabel("Count", fontsize=font_size)
    ax_count.legend(loc="best", fontsize=font_size)
    ax_count.tick_params(axis='both', labelsize=font_size)
    ax_count.grid(True)

    fig_count.tight_layout()
    fig_count.savefig(f"plots/{filename}_transient_analysis_count.png")

    fig_power = plt.figure(dpi=300, figsize=(figure_width, figure_height))
    ax_power = fig_power.add_subplot(1, 1, 1)
    ax_power.set_title(f"Power consumption during operation", fontsize=font_size, fontweight='bold')

    ax_power.plot(df["time"], df["pwr"], label="pwr = idd * vdd")
    ax_power.plot(df["time"], df["mov_avg_pwr"], label=f"mov. avg. (w={w})")

    # ax_power.set_xlim(45, 82.5)
    ax_power.set_xlabel("Time (us)", fontsize=font_size)
    ax_power.set_ylabel("Power (uW)", fontsize=font_size)
    ax_power.legend(loc="best", fontsize=font_size)
    ax_power.tick_params(axis='both', labelsize=font_size)
    ax_power.grid(True)
    ax_power.set_ylim(-df["mov_avg_pwr"].max()*0.1, df["mov_avg_pwr"].max()*1.15)

    fig_power.tight_layout()
    fig_power.savefig(f"plots/{filename}_transient_analysis_power.png")

plt.close("all")