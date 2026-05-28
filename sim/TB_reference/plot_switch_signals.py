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


figure_width = 2.8
figure_height = 4.5
font_size = 6
title_font_size = font_size
label_font_size = font_size
legend_font_size = font_size
ticks_font_size = font_size

zoom_start = 190  # in us
zoom_stop = 345  # in us

superzoom_start = 205  # in us
superzoom_stop = 245  # in us

supersuperzoom_start = 232.4
supersuperzoom_stop = 233.5

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

    print(f"plotting full view")

    fig_full, axs_full = plt.subplots(5, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

    axs_full[0].plot(df["time"], df["v(clk)"], label="clk")
    # axs_full[0].plot(df["time"], df["v(b0)"], label="b0")
    # axs_full[0].plot(df["time"], df["v(rst)"], label="rst")
    axs_full[0].plot(df["time"], df["v(mode)"], label="mode")
    axs_full[0].plot(df["time"], df["v(slp)"], label="slp")
    axs_full[0].plot(df["time"], df["v(cmp_async)"], label="cmp")
    # axs_full[0].plot(df["time"], df["v(mode_meta)"], label="v(mode_meta)")
    # axs_full[0].plot(df["time"], df["v(operation)"], label="v(operation)")

    axs_full[1].plot(df["time"], df["v(bgr.v1)"], label="v1")
    axs_full[1].plot(df["time"], df["v(bgr.v2)"], label="v2")
    axs_full[1].plot(df["time"], df["v(vout)"], label="vout")
    axs_full[1].plot(df["time"], df["v(correct_output_found)"], label="out_en")

    axs_full[2].plot(df["time"], df["v(swbgr1)"], label="swbgr1")
    axs_full[2].plot(df["time"], df["v(swbrn1)"], label="swbrn1")
    axs_full[2].plot(df["time"], df["v(swcap1)"], label="swcap1")
    axs_full[2].plot(df["time"], df["v(swdrn1)"], label="swdrn1")

    axs_full[3].plot(df["time"], df["v(swbgr2)"], label="swbgr2")
    axs_full[3].plot(df["time"], df["v(swbrn2)"], label="swbrn2")
    axs_full[3].plot(df["time"], df["v(swcap2)"], label="swcap2")
    axs_full[3].plot(df["time"], df["v(swdrn2)"], label="swdrn2")

    axs_full[4].plot(df["time"], df["v(swbrn3)"], label="swbrn3")
    axs_full[4].plot(df["time"], df["v(swcap3)"], label="swcap3")
    axs_full[4].plot(df["time"], df["v(swdrn3)"], label="swdrn3")

    for i, ax in enumerate(axs_full):
        ax.set_ylabel("Voltage (V)", fontsize=label_font_size)
        ax.tick_params(axis="both", labelsize=ticks_font_size)
        ax.grid()
        ax.legend(loc="best", ncol=2, fontsize=legend_font_size)

        # y_min, y_max = ax.get_ylim()
        # rect = mpatches.Rectangle(
        #     (zoom_start, y_min),
        #     zoom_stop - zoom_start,
        #     y_max - y_min,
        #     linewidth=1.25,
        #     edgecolor="black",
        #     facecolor="none",
        #     linestyle="--",
        #     transform=ax.transData,
        #     clip_on=True,
        #     zorder=5,
        # )
        # ax.add_patch(rect)

    axs_full[0].set_title(f"Switch signals,\n{process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_font_size, fontweight='bold')
    axs_full[-1].set_xlabel("Time (us)", fontsize=label_font_size)
    fig_full.tight_layout()
    fig_full.savefig(f"figures/{figure_name}_plot_switch_signals_full.png", dpi=300, bbox_inches="tight")


    #
    # plot switch voltages (zoomed view: zoom_start to zoom_stop us)
    #

    print(f"plotting zoomed between {zoom_start} us and {zoom_stop} us")

    fig_zoom, axs_zoom = plt.subplots(5, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

    axs_zoom[0].plot(df["time"], df["v(clk)"], label="clk")
    axs_zoom[0].plot(df["time"], df["v(mode)"], label="mode")
    axs_zoom[0].plot(df["time"], df["v(slp)"], label="slp")
    axs_zoom[0].plot(df["time"], df["v(cmp_async)"], label="cmp")

    axs_zoom[1].plot(df["time"], df["v(bgr.v1)"], label="v1")
    axs_zoom[1].plot(df["time"], df["v(bgr.v2)"], label="v2")
    axs_zoom[1].plot(df["time"], df["v(vout)"], label="vout")
    axs_zoom[1].plot(df["time"], df["v(correct_output_found)"], label="out_en")

    axs_zoom[2].plot(df["time"], df["v(swbgr1)"], label="swbgr1")
    axs_zoom[2].plot(df["time"], df["v(swbrn1)"], label="swbrn1")
    axs_zoom[2].plot(df["time"], df["v(swcap1)"], label="swcap1")
    axs_zoom[2].plot(df["time"], df["v(swdrn1)"], label="swdrn1")

    axs_zoom[3].plot(df["time"], df["v(swbgr2)"], label="swbgr2")
    axs_zoom[3].plot(df["time"], df["v(swbrn2)"], label="swbrn2")
    axs_zoom[3].plot(df["time"], df["v(swcap2)"], label="swcap2")
    axs_zoom[3].plot(df["time"], df["v(swdrn2)"], label="swdrn2")

    axs_zoom[4].plot(df["time"], df["v(swbrn3)"], label="swbrn3")
    axs_zoom[4].plot(df["time"], df["v(swcap3)"], label="swcap3")
    axs_zoom[4].plot(df["time"], df["v(swdrn3)"], label="swdrn3")

    for ax in axs_zoom:
        ax.set_xlim(zoom_start, zoom_stop)
        ax.set_ylabel("Voltage (V)", fontsize=label_font_size)
        ax.tick_params(axis="both", labelsize=ticks_font_size)
        ax.grid()
        ax.legend(loc="best", ncol=2, fontsize=legend_font_size)

        # y_min, y_max = ax.get_ylim()
        # rect = mpatches.Rectangle(
        #     (superzoom_start, y_min),
        #     superzoom_stop - superzoom_start,
        #     y_max - y_min,
        #     linewidth=1.25,
        #     edgecolor="black",
        #     facecolor="none",
        #     linestyle="--",
        #     transform=ax.transData,
        #     clip_on=True,
        #     zorder=5,
        # )
        # ax.add_patch(rect)

    axs_zoom[0].set_title(f"Switch signals zoomed in,\n{process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_font_size, fontweight='bold')
    axs_zoom[-1].set_xlabel("Time (us)", fontsize=label_font_size)
    fig_zoom.tight_layout()
    fig_zoom.savefig(f"figures/{figure_name}_plot_switch_signals_zoom.png", dpi=300, bbox_inches="tight")


    #
    # plot switch voltages (super-zoomed view: superzoom_start to superzoom_stop us)
    #

    print(f"plotting super-zoomed between {superzoom_start} us and {superzoom_stop} us")

    fig_superzoom, axs_superzoom = plt.subplots(5, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

    axs_superzoom[0].plot(df["time"], df["v(clk)"], label="clk")
    axs_superzoom[0].plot(df["time"], df["v(mode)"], label="mode")
    axs_superzoom[0].plot(df["time"], df["v(slp)"], label="slp")
    axs_superzoom[0].plot(df["time"], df["v(cmp_async)"], label="cmp")

    axs_superzoom[1].plot(df["time"], df["v(bgr.v1)"], label="v1")
    axs_superzoom[1].plot(df["time"], df["v(bgr.v2)"], label="v2")
    axs_superzoom[1].plot(df["time"], df["v(vout)"], label="vout")
    axs_superzoom[1].plot(df["time"], df["v(correct_output_found)"], label="out_en")

    axs_superzoom[2].plot(df["time"], df["v(swbgr1)"], label="swbgr1")
    axs_superzoom[2].plot(df["time"], df["v(swbrn1)"], label="swbrn1")
    axs_superzoom[2].plot(df["time"], df["v(swcap1)"], label="swcap1")
    axs_superzoom[2].plot(df["time"], df["v(swdrn1)"], label="swdrn1")

    axs_superzoom[3].plot(df["time"], df["v(swbgr2)"], label="swbgr2")
    axs_superzoom[3].plot(df["time"], df["v(swbrn2)"], label="swbrn2")
    axs_superzoom[3].plot(df["time"], df["v(swcap2)"], label="swcap2")
    axs_superzoom[3].plot(df["time"], df["v(swdrn2)"], label="swdrn2")

    axs_superzoom[4].plot(df["time"], df["v(swbrn3)"], label="swbrn3")
    axs_superzoom[4].plot(df["time"], df["v(swcap3)"], label="swcap3")
    axs_superzoom[4].plot(df["time"], df["v(swdrn3)"], label="swdrn3")

    for ax in axs_superzoom:
        ax.set_xlim(superzoom_start, superzoom_stop)
        ax.set_ylabel("Voltage (V)", fontsize=label_font_size)
        ax.tick_params(axis="both", labelsize=ticks_font_size)
        ax.grid()
        ax.legend(loc="best", ncol=2, fontsize=legend_font_size)

        # y_min, y_max = ax.get_ylim()
        # rect = mpatches.Rectangle(
        #     (supersuperzoom_start, y_min),
        #     supersuperzoom_stop - supersuperzoom_start,
        #     y_max - y_min,
        #     linewidth=1.25,
        #     edgecolor="black",
        #     facecolor="none",
        #     linestyle="--",
        #     transform=ax.transData,
        #     clip_on=True,
        #     zorder=5,
        # )
        # ax.add_patch(rect)

    axs_superzoom[0].set_title(f"Switch signals zoomed in,\n{process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_font_size, fontweight='bold')
    axs_superzoom[-1].set_xlabel("Time (us)", fontsize=label_font_size)
    fig_superzoom.tight_layout()
    fig_superzoom.savefig(f"figures/{figure_name}_plot_switch_signals_superzoom.png", dpi=300, bbox_inches="tight")

    # 
    # plot switch voltages (super-super-zoomed view: superzoom_start to superzoom_stop us)
    #

    print(f"plotting super-super-zoomed between {supersuperzoom_start} us and {supersuperzoom_stop} us")

    fig_supersuperzoom, axs_supersuperzoom = plt.subplots(5, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

    axs_supersuperzoom[0].plot(df["time"], df["v(clk)"], label="clk")
    axs_supersuperzoom[0].plot(df["time"], df["v(mode)"], label="mode")
    axs_supersuperzoom[0].plot(df["time"], df["v(slp)"], label="slp")
    axs_supersuperzoom[0].plot(df["time"], df["v(cmp_async)"], label="cmp")

    axs_supersuperzoom[1].plot(df["time"], df["v(bgr.v1)"], label="v1")
    axs_supersuperzoom[1].plot(df["time"], df["v(bgr.v2)"], label="v2")
    axs_supersuperzoom[1].plot(df["time"], df["v(vout)"], label="vout")
    axs_supersuperzoom[1].plot(df["time"], df["v(correct_output_found)"], label="out_en")

    axs_supersuperzoom[2].plot(df["time"], df["v(swbgr1)"], label="swbgr1")
    axs_supersuperzoom[2].plot(df["time"], df["v(swbrn1)"], label="swbrn1")
    axs_supersuperzoom[2].plot(df["time"], df["v(swcap1)"], label="swcap1")
    axs_supersuperzoom[2].plot(df["time"], df["v(swdrn1)"], label="swdrn1")

    axs_supersuperzoom[3].plot(df["time"], df["v(swbgr2)"], label="swbgr2")
    axs_supersuperzoom[3].plot(df["time"], df["v(swbrn2)"], label="swbrn2")
    axs_supersuperzoom[3].plot(df["time"], df["v(swcap2)"], label="swcap2")
    axs_supersuperzoom[3].plot(df["time"], df["v(swdrn2)"], label="swdrn2")

    axs_supersuperzoom[4].plot(df["time"], df["v(swbrn3)"], label="swbrn3")
    axs_supersuperzoom[4].plot(df["time"], df["v(swcap3)"], label="swcap3")
    axs_supersuperzoom[4].plot(df["time"], df["v(swdrn3)"], label="swdrn3")

    for ax in axs_supersuperzoom:
        ax.set_xlim(supersuperzoom_start, supersuperzoom_stop)
        ax.set_ylabel("Voltage (V)", fontsize=label_font_size)
        ax.tick_params(axis="both", labelsize=ticks_font_size)
        ax.grid()
        ax.legend(loc="best", ncol=2, fontsize=legend_font_size)

    axs_supersuperzoom[0].set_title(f"Switch signals zoomed in,\n{process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_font_size, fontweight='bold')
    axs_supersuperzoom[-1].set_xlabel("Time (us)", fontsize=label_font_size)
    fig_supersuperzoom.tight_layout()
    fig_supersuperzoom.savefig(f"figures/{figure_name}_plot_switch_signals_supersuperzoom.png", dpi=300, bbox_inches="tight")

    if args[-1] == "temp":
        plt.show()
    else:
        plt.close("all")