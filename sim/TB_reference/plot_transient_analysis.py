import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from matplotlib.patches import FancyBboxPatch

args = sys.argv[1:]
files = list()

xx = "xx"


stepping_direction = ""
if "up" in args:
    stepping_direction = "up"
    print("Plotting for transient signals stepping upwards")
else: 
    stepping_direction = "down"
    print("Plotting for transient signals stepping downwards")


if len(args) == 0:
    print("No arguments provided. Plotting for typical corner, voltage (1.8 Volt) and temperature (27 Celsius).")
    files.append("output_tran/tran_SchGtKttTtVt_stepping_" + stepping_direction + "_0celsius_1.8volt.out")


if "temp" in args:
    if args[-1] == "temp": 
        temp = 27
    else: 
        temp = int(args[-1])
    for corner in ["tt"]:
        for temperature in [temp]: # Celsius (degree C)
            for voltage in [1.8]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")


figure_width = 4
figure_height = 4
font_size = 6
title_font_size = font_size
label_font_size = font_size
legend_font_size = font_size
ticks_font_size = font_size


for file in files:
    print(f"Plotting transient results from file: {file}")

    figure_name = file.split("/")[-1].split(".out")[0]

    circuit_temperature = float(figure_name.split("_")[-2].replace("celsius", "")) # in degrees Celsius
    voltage_supply = float(figure_name.split("_")[-1].replace("volt", "")) # in Volt
    shorthand_name = figure_name.split("GtK")[-1].split("Tt")[0] # tt/ss/ff/sf/fs

    if shorthand_name == "tt":
        process_corner = "Typical"
    elif shorthand_name == "ss":
        process_corner = "Slow-Slow"
    elif shorthand_name == "ff":
        process_corner = "Fast-Fast"
    elif shorthand_name == "sf":
        process_corner = "Slow-Fast"
    elif shorthand_name == "fs":
        process_corner = "Fast-Slow"
    else:
        process_corner = "Oops, something is wrong!"

    df = pd.read_csv(file, sep="\s+")

    df['time'] = df['time'] * 1e6 # in us
    df['diff'] = df['v(bgr.v1)']-df['v(bgr.v2)']


    #
    # plot switch voltages
    #

    fig, axs = plt.subplots(4, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

    axs[0].plot(df["time"], df["v(clk)"], label="clk")
    axs[0].plot(df["time"], df["v(b0)"], label="b0")
    axs[0].plot(df["time"], df["v(dac.vctl)"], label="vctl")
    axs[0].plot(df["time"], df["v(cmp_async)"], label="cmp")
    axs[0].plot(df["time"], df["v(rst)"], label="rst")
    axs[0].plot(df["time"], df["v(slp)"], label="slp")
    axs[0].plot(df["time"], df["v(mode)"], label="mode")

    axs[1].plot(df["time"], df["v(bgr.v1)"], label="v1")
    axs[1].plot(df["time"], df["v(bgr.v2)"], label="v2")
    axs[1].plot(df["time"], df["v(vout)"], label="vout")
    axs[1].plot(df["time"], df["v(correct_output_found)"], label="out_en")

    axs[2].plot(df["time"], df["v(dec_finetuning_duty_cycle)"]*1e3, label="dec_finetune_dutycycle")
    axs[2].plot(df["time"], df["v(dec_coarse_step_counter)"]*1e3, label="dec_coarse_step")

    window = 100 # in number of samples
    df["pwr"] = df["v(vdd)"] * -(df["i(vdd)"]) * 1e6 # in uW (micro Watt)
    df["mov_avg_pwr"] = df["pwr"].rolling(window=window).mean() # moving average filter with window size of 100 applied to the power plot

    axs[3].plot(df["time"], df["pwr"], label="pwr")
    axs[3].plot(df["time"], df["mov_avg_pwr"], label=f"mov. avg. pwr (w={window})")

    axs[0].set_ylabel("Voltage (V)", fontsize=label_font_size)
    axs[1].set_ylabel("Voltage (V)", fontsize=label_font_size)
    axs[2].set_ylabel("Count", fontsize=label_font_size)
    axs[3].set_ylabel("Power (uW)", fontsize=label_font_size)

    for i, ax in enumerate(axs):
        ax.tick_params(axis="both", labelsize=ticks_font_size)
        ax.grid()
        ax.legend(loc="best", ncol=2, fontsize=legend_font_size)

    axs[0].set_title(f"Transient analysis, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_font_size, fontweight='bold')
    axs[-1].set_xlabel("Time (us)", fontsize=label_font_size)
    axs[-1].set_ylim(-df["mov_avg_pwr"].max()*0.1, df["mov_avg_pwr"].max()*1.15)
    fig.tight_layout()
    fig.savefig(f"figures/{figure_name}_transient_analysis.png", dpi=300, bbox_inches="tight")


if args[-1] == "temp":
    plt.show()
else:
    plt.close("all")