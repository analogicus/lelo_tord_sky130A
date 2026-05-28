import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np

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
if "typical" in args:
    for corner in ["tt"]:
        for temperature in [-40, -20, 0, 30 ,60, 90, 125]: # Celsius (degree C)
                for voltage in [1.8]: # Volt (V)
                    Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                    files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")
if "slow" in args:
    for corner in ["ss"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
            for voltage in [1.7]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")
if "fast" in args:
    for corner in ["ff"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
            for voltage in [1.9]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")
if "all" in args:
    for corner in ["tt", "ss", "ff", "sf", "fs"]:
        for temperature in [-40, 0, 40, 80, 125]: # Celsius (degree C)
            for voltage in [1.7, 1.8, 1.9]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")
if "etc" in args:
    for corner in ["ss", "ff", "sf", "fs"]:
        for temperature in [-40, 0, 40, 80, 125]: # Celsius (degree C)
            for voltage in [1.7, 1.9]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

if "test" in args:
    for corner in ["tt"]:
        for temperature in [-40, 0, 40, 80, 125]: # Celsius (degree C)
            for voltage in [1.8]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

if "temp" in args:
    if args[-1] == "temp": 
        temp = -40
    else: 
        temp = int(args[-1])
    for corner in ["tt"]:
        for temperature in [temp]: # Celsius (degree C)
            for voltage in [1.8]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

if "temps" in args:
    for corner in ["tt"]:
        for temperature in [-40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]: # Celsius (degree C)
            for voltage in [1.8]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

if "partialtemps" in args:
    if args[-1] == "partialtemps": 
        temps = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    else: 
        temps = [int(temp) for temp in args[-1].split(",")]
    for corner in ["tt"]:
        for temperature in temps : # Celsius (degree C)
            for voltage in [1.8]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

runs = 30

if "mc" in args:
    for corner in ["ttmm"]:
        for temperature in [-40, 0, 40, 80, 125]: # Celsius (degree C)
            for voltage in [1.8]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                for run in range(21, runs): # Assuming 30 Monte Carlo runs
                    if run == 0:
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")
                    else:
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_{run}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")
                    print(f"added output_tran/tran_SchGtK{corner}Tt{Vx}_{run}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out to files")

figure_width = 4
figure_height = 4.5
font_size = 6
title_font_size = font_size
label_font_size = font_size
legend_font_size = font_size
ticks_font_size = font_size


for file in files:
    print(f"Plotting Vout transient results from file: {file}")

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

    df['time'] = df['time'] * 1e9 # in ns
    df['diff'] = df['v(bgr.v1)']-df['v(bgr.v2)']


    #
    # plot BGR voltages
    #

    fig, axs = plt.subplots(6, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)
    
    axs[0].plot(df["time"], df["v(xdut.ifeed)"], label="v(ifeed)", color="tab:blue") # in V

    # ax_ifeed = axs[0].twinx()
    # ax_ifeed.plot(df["time"], (df["v(xdut.ifeed)"] / (8*7535))*1e6, label="ifeed", color="tab:orange") # in uA

    # axs[0].plot(df["time"], df["v(bgr.v1)"]-df["v(bgr.v2)"], label="v1-v2", linestyle="solid")
    # axs[0].plot(df["time"], df["v(v1a)"]-df["v(v2a)"], label="v1a-v2a", linestyle="dashed")
    # axs[0].plot(df["time"], df["v(v1b)"]-df["v(v2b)"], label="v1b-v2b", linestyle="dotted")
    
    axs[1].plot(df["time"], df["v(bgr.v1a)"], label="v1a")
    axs[1].plot(df["time"], df["v(bgr.v1b)"], label="v1b")
    axs[1].plot(df["time"], df["v(bgr.v2a)"], label="v2a")
    axs[1].plot(df["time"], df["v(bgr.v2b)"], label="v2b")
    axs[1].plot(df["time"], df["v(bgr.v2c)"], label="v2c")
    axs[1].plot(df["time"], df["v(bgr.vref)"], label="vref")

    axs[2].plot(df["time"], df["v(bgr.v1)"], label="v(v1)")
    axs[2].plot(df["time"], df["v(bgr.v2)"], label="v(v2)")
    axs[2].plot(df["time"], df["v(vout)"], label="v(vout)")
    axs[2].plot(df["time"], df["v(correct_output_found)"], label="correct_output_found")

    axs[3].plot(df["time"], df["v(clk)"], label="clk")
    axs[3].plot(df["time"], df["v(b0)"], label="b0")
    axs[3].plot(df["time"], df["v(dac.vctl)"], label="vctl")
    axs[3].plot(df["time"], df["v(cmp_async)"], label="cmp")
    axs[3].plot(df["time"], df["v(rst)"], label="rst")
    axs[3].plot(df["time"], df["v(slp)"], label="slp")
    
    axs[4].plot(df["time"], df["v(dac.vbn)"], label="vbn")
    axs[4].plot(df["time"], df["v(dac.vbp)"], label="vbp")

    axs[5].plot(df["time"], df["v(dac.vt)"], label="vt")
    axs[5].plot(df["time"], df["v(dac.vctlb)"], label="vctlb")
    axs[5].plot(df["time"], df["v(dac.vctl)"], label="vctl")

    for ax in axs:
        ax.set_ylabel("Voltage (V)", fontsize=label_font_size)
        ax.tick_params(axis="both", labelsize=ticks_font_size)
        ax.grid()
        ax.legend(loc="best", ncols=2, fontsize=legend_font_size)

    axs[0].set_title(f"BGR core signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_font_size, fontweight='bold')
    axs[-1].set_xlabel("Time (ns)", fontsize=label_font_size)

    # ax_ifeed.set_ylabel("Current (uA)", fontsize=label_font_size)
    # ax_ifeed.legend(loc="lower right", fontsize=legend_font_size)
    # ax_ifeed.tick_params(axis='both', labelsize=ticks_font_size)

    fig.tight_layout()
    fig.savefig(f"figures/{figure_name}_bgr_core_signals.png", dpi=300, bbox_inches="tight")


    #
    # plot external comparator voltages
    #

    fig_2, axs_2 = plt.subplots(5, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)
    
    axs_2[0].plot(df["time"], df["v(clk)"], label="v(clk)")
    axs_2[0].plot(df["time"], df["v(b0)"], label="v(b0)")
    axs_2[0].plot(df["time"], df["v(dac.vctl)"], label="v(vctl)")
    axs_2[0].plot(df["time"], df["v(cmp_async)"], label="v(cmp)")
    axs_2[0].plot(df["time"], df["v(rst)"], label="v(rst)")
    axs_2[0].plot(df["time"], df["v(slp)"], label="v(slp)")

    axs_2[1].plot(df["time"], df["v(bgr.v1)"], label="v(v1)")
    axs_2[1].plot(df["time"], df["v(bgr.v2)"], label="v(v2)")
    axs_2[1].plot(df["time"], df["v(vout)"], label="v(vout)")
    axs_2[1].plot(df["time"], df["v(cmp_meta)"], label="v(cmp_meta)")

    axs_2[2].plot(df["time"], df["v(cmp_sync)"], label="v(cmp_sync)")

    axs_2[3].plot(df["time"], df["v(cmp_rising)"], label="v(cmp_rising)")
    axs_2[3].plot(df["time"], df["v(cmp_falling)"], label="v(cmp_falling)")
    axs_2[3].plot(df["time"], df["v(stepping_up)"], label="v(stepping_up)")
    axs_2[3].plot(df["time"], df["v(correct_output_found)"], label="correct_output_found")

    axs_2[4].plot(df["time"], df["v(dec_cmp_rising_counter)"], label="v(dec_cmp_rising_counter)")
    axs_2[4].plot(df["time"], df["v(dec_cmp_switching_counter)"], label="v(dec_cmp_switching_counter)")

    for i, ax in enumerate(axs_2):
        ax.set_ylabel("Voltage (V)", fontsize=label_font_size)
        ax.tick_params(axis="both", labelsize=ticks_font_size)
        ax.grid()
        ax.legend(loc="best", ncols=2, fontsize=legend_font_size)

    axs_2[0].set_title(f"External comparator signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C,", fontsize=title_font_size, fontweight='bold')
    axs_2[-1].set_xlabel("Time (ns)", fontsize=label_font_size)
    fig_2.tight_layout()
    fig_2.savefig(f"figures/{figure_name}_external_comparator_signals.png", dpi=300, bbox_inches="tight")



    #
    # plot internal voltages in comparator
    #
    
    fig_3, axs_3 = plt.subplots(5, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

    axs_3[0].plot(df["time"], df["v(bgr.v1)"], label="vin = v1")
    axs_3[0].plot(df["time"], df["v(bgr.v2)"], label="vip = v2")
    axs_3[0].plot(df["time"], df["v(cmp_async)"], label="vout = cmp_async")
    axs_3[0].plot(df["time"], df["v(rst)"], label="rst")
    axs_3[0].plot(df["time"], df["v(slp)"], label="slp")

    axs_3[1].plot(df["time"], df["v(cmp.vbn)"], label="vbn (bias)")

    axs_3[2].plot(df["time"], df["v(cmp.vindrn)"], label="vindrn")
    axs_3[3].plot(df["time"], df["v(cmp.vipdrn)"], label="vipdrn")
    axs_3[4].plot(df["time"], df["v(cmp.vsrc)"], label="vsrc")

    for i, ax in enumerate(axs_3):
        ax.set_ylabel("Voltage (V)", fontsize=label_font_size)
        ax.tick_params(axis="both", labelsize=ticks_font_size)
        ax.grid()
        ax.legend(loc="best", ncols=2, fontsize=legend_font_size)

    axs_3[0].set_title(f"Internal comparator signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_font_size, fontweight='bold')
    axs_3[-1].set_xlabel("Time (ns)", fontsize=label_font_size)
    fig_3.tight_layout()
    fig_3.savefig(f"figures/{figure_name}_internal_comparator_signals.png", dpi=300, bbox_inches="tight")

    #
    # plot control DAC voltages
    #

    fig_4, axs_4 = plt.subplots(8, 2, figsize=(figure_width*2, figure_height), sharex=True, dpi=300)
    
    axs_4[0, 0].plot(df["time"], df["v(b1)"], label="v(b1)")
    # axs_4[0, 0].plot(df["time"], df["v(dac.b1_mid)"], label="v(b1_mid)")
    axs_4[1, 0].plot(df["time"], df["v(b2)"], label="v(b2)")
    # axs_4[1, 0].plot(df["time"], df["v(dac.b2_mid)"], label="v(b2_mid)")
    axs_4[2, 0].plot(df["time"], df["v(b3)"], label="v(b3)")
    # axs_4[2, 0].plot(df["time"], df["v(dac.b3_mid)"], label="v(b3_mid)")
    axs_4[3, 0].plot(df["time"], df["v(b4)"], label="v(b4)")
    # axs_4[3, 0].plot(df["time"], df["v(dac.b4_mid)"], label="v(b4_mid)")
    axs_4[4, 0].plot(df["time"], df["v(b5)"], label="v(b5)")
    # axs_4[4, 0].plot(df["time"], df["v(dac.b5_mid)"], label="v(b5_mid)")
    axs_4[5, 0].plot(df["time"], df["v(b6)"], label="v(b6)")
    # axs_4[5, 0].plot(df["time"], df["v(dac.b6_mid)"], label="v(b6_mid)")
    axs_4[6, 0].plot(df["time"], df["v(b7)"], label="v(b7)")
    # axs_4[6, 0].plot(df["time"], df["v(dac.b7_mid)"], label="v(b7_mid)")
    axs_4[7, 0].plot(df["time"], df["v(b8)"], label="v(b8)")
    # axs_4[7, 0].plot(df["time"], df["v(dac.b8_mid)"], label="v(b8_mid)")
    axs_4[0, 1].plot(df["time"], df["v(b9)"], label="v(b9)")
    # axs_4[0, 1].plot(df["time"], df["v(dac.b9_mid)"], label="v(b9_mid)")
    axs_4[1, 1].plot(df["time"], df["v(b10)"], label="v(b10)")
    # axs_4[1, 1].plot(df["time"], df["v(dac.b10_mid)"], label="v(b10_mid)")
    axs_4[2, 1].plot(df["time"], df["v(b11)"], label="v(b11)")
    # axs_4[2, 1].plot(df["time"], df["v(dac.b11_mid)"], label="v(b11_mid)")
    axs_4[3, 1].plot(df["time"], df["v(b12)"], label="v(b12)")
    # axs_4[3, 1].plot(df["time"], df["v(dac.b12_mid)"], label="v(b12_mid)")
    axs_4[4, 1].plot(df["time"], df["v(b13)"], label="v(b13)")
    # axs_4[4, 1].plot(df["time"], df["v(dac.b13_mid)"], label="v(b13_mid)")
    axs_4[5, 1].plot(df["time"], df["v(b14)"], label="v(b14)")
    # axs_4[5, 1].plot(df["time"], df["v(dac.b14_mid)"], label="v(b14_mid)")
    axs_4[6, 1].plot(df["time"], df["v(b15)"], label="v(b15)")
    # axs_4[6, 1].plot(df["time"], df["v(dac.b15_mid)"], label="v(b15_mid)")
    axs_4[6, 1].plot(df["time"], df["v(xdut.ifeed)"], label="v(ifeed)")
    axs_4[7, 1].plot(df["time"], df["v(dec_coarse_step1)"], label="v(dec_coarse_step1)")
    axs_4[7, 1].plot(df["time"], df["v(dec_coarse_step2)"], label="v(dec_coarse_step2)")

    for i, ax in enumerate(axs_4.flat):
        ax.set_ylabel("Voltage (V)", fontsize=label_font_size)
        ax.tick_params(axis="both", labelsize=ticks_font_size)
        ax.grid()
        ax.legend(loc="best", ncols=2, fontsize=legend_font_size)

    # axs_4[-1].set_xlabel("Time (ns)", fontsize=label_font_size)
    axs_4[0, 0].set_title(f"DAC control signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_font_size, fontweight='bold')
    fig_4.tight_layout()
    fig_4.savefig(f"figures/{figure_name}_dac_control_signals.png", dpi=300, bbox_inches="tight")


    #
    # plot counter signals
    #

    fig_5, axs_5 = plt.subplots(5, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)
    
    axs_5[0].plot(df["time"], df["v(clk)"], label="v(clk)")
    axs_5[0].plot(df["time"], df["v(b0)"], label="v(b0)")
    axs_5[0].plot(df["time"], df["v(dac.vctl)"], label="v(vctl)")
    axs_5[0].plot(df["time"], df["v(cmp_async)"], label="v(cmp_async)")
    axs_5[0].plot(df["time"], df["v(rst)"], label="v(rst)")
    axs_5[0].plot(df["time"], df["v(slp)"], label="v(slp)")

    axs_5[1].plot(df["time"], df["v(bgr.v1)"], label="v(v1)")
    axs_5[1].plot(df["time"], df["v(bgr.v2)"], label="v(v2)")
    axs_5[1].plot(df["time"], df["v(vout)"], label="v(vout)")
    axs_5[1].plot(df["time"], df["v(correct_output_found)"], label="correct_output_found")

    axs_5[2].plot(df["time"], df["v(dec_finetuning_duty_cycle)"], label="v(dec_finetuning_duty_cycle)")
    axs_5[2].plot(df["time"], df["v(dec_coarse_step_counter)"], label="v(dec_coarse_step_counter)")
    
    axs_5[3].plot(df["time"], df["v(dec_finetuning_counter)"], label="v(dec_finetuning_counter)")
    axs_5[3].plot(df["time"], df["v(dec_timeout_counter)"], label="timeout_counter")

    axs_5[4].plot(df["time"], df["v(dec_cmp_switching_counter)"], label="v(dec_cmp_switching_counter)")

    for i, ax in enumerate(axs_5):
        ax.set_ylabel("Voltage (V)", fontsize=label_font_size)
        ax.tick_params(axis="both", labelsize=ticks_font_size)
        ax.grid()
        ax.legend(loc="best", ncols=2, fontsize=legend_font_size)

    axs_5[0].set_title(f"Counter signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_font_size, fontweight='bold')
    axs_5[-1].set_xlabel("Time (ns)", fontsize=label_font_size)
    fig_5.tight_layout()
    fig_5.savefig(f"figures/{figure_name}_counter_signals.png", dpi=300, bbox_inches="tight")


    #
    # plot switch voltages
    #

    fig_6, axs_6 = plt.subplots(4, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

    axs_6[0].plot(df["time"], df["v(clk)"], label="clk")
    axs_6[0].plot(df["time"], df["v(b0)"], label="b0")
    axs_6[0].plot(df["time"], df["v(rst)"], label="rst")
    axs_6[0].plot(df["time"], df["v(slp)"], label="slp")
    axs_6[0].plot(df["time"], df["v(mode)"], label="mode")
    axs_6[0].plot(df["time"], df["v(cmp_async)"], label="cmp")
    # axs_6[0].plot(df["time"], df["v(mode_meta)"], label="v(mode_meta)")
    # axs_6[0].plot(df["time"], df["v(operation)"], label="v(operation)")

    axs_6[1].plot(df["time"], df["v(swbgr1)"], label="swbgr1")
    axs_6[1].plot(df["time"], df["v(swbrn1)"], label="swbrn1")
    axs_6[1].plot(df["time"], df["v(swcap1)"], label="swcap1")
    axs_6[1].plot(df["time"], df["v(swdrn1)"], label="swdrn1")

    axs_6[2].plot(df["time"], df["v(swbgr2)"], label="swbgr2")
    axs_6[2].plot(df["time"], df["v(swbrn2)"], label="swbrn2")
    axs_6[2].plot(df["time"], df["v(swcap2)"], label="swcap2")
    axs_6[2].plot(df["time"], df["v(swdrn2)"], label="swdrn2")

    axs_6[3].plot(df["time"], df["v(swbrn3)"], label="swbrn3")
    axs_6[3].plot(df["time"], df["v(swcap3)"], label="swcap3")
    axs_6[3].plot(df["time"], df["v(swdrn3)"], label="swdrn3")

    for i, ax in enumerate(axs_6    ):
        ax.set_ylabel("Voltage (V)", fontsize=label_font_size)
        ax.tick_params(axis="both", labelsize=ticks_font_size)
        ax.grid()
        ax.legend(loc="best", ncol=2, fontsize=legend_font_size)

    axs_6[0].set_title(f"Switch signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_font_size, fontweight='bold')
    axs_6[-1].set_xlabel("Time (ns)", fontsize=label_font_size)
    fig_6.tight_layout()
    fig_6.savefig(f"figures/{figure_name}_switch_signals.png", dpi=300, bbox_inches="tight")


    #
    # Plot power consumption
    #

    window_size = 100 # in number of samples
    df["pwr"] = df["v(vdd)"] * -(df["i(vdd)"]) * 1e6 # in uW (micro Watt)
    df["moving_avg_pwr"] = df["pwr"].rolling(window=window_size).mean() # moving average filter with window size of 100 applied to the power plot
    # df["filtered_pwr"] = df.loc[df['v(slp)'] >= 0.99 * df['v(vdd)'], 'moving_avg_pwr'] # moving average filter with window size of 100 applied to the power plot, but only for the datapoints where v(slp) is above 0.99 * VDD
    df["filtered_pwr"] = df.loc[df['moving_avg_pwr'] < 0.025, 'moving_avg_pwr'] # moving average filter with window size of 100 applied to the power plot, but only for the datapoints where v(slp) is above 0.99 * VDD

    fig_7, axs_7 = plt.subplots(5, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)
    
    axs_7[0].plot(df["time"], df["v(bgr.v1)"], label="v1")
    axs_7[0].plot(df["time"], df["v(bgr.v2)"], label="v2")
    axs_7[0].plot(df["time"], df["v(vout)"], label="vout")
    axs_7[0].plot(df["time"], df["v(correct_output_found)"], label="correct_output_found")

    axs_7[1].plot(df["time"], df["v(clk)"], label="clk")
    axs_7[1].plot(df["time"], df["v(b0)"], label="b0")
    axs_7[1].plot(df["time"], df["v(dac.vctl)"], label="vctl")

    axs_7[1].plot(df["time"], df["v(cmp_async)"], label="cmp")
    axs_7[1].plot(df["time"], df["v(rst)"], label="rst")
    axs_7[1].plot(df["time"], df["v(slp)"], label="slp")

    axs_7[2].plot(df["time"], df["v(dec_finetuning_duty_cycle)"], label="v(dec_finetuning_duty_cycle)")
    axs_7[2].plot(df["time"], df["v(dec_coarse_step_counter)"], label="v(dec_coarse_step_counter)")

    # plot the current in axs_7[2] with a secondary y-axis
    ax_ifeed_7 = axs_7[3].twinx()
    ax_ifeed_7.plot(df["time"], -df["i(vdd)"]*1e6, label="idd", color="tab:orange") # in uA
    ax_ifeed_7.set_ylabel("Current (uA)", fontsize=label_font_size)
    ax_ifeed_7.legend(loc="upper right", ncols=2, fontsize=legend_font_size)
    ax_ifeed_7.tick_params(axis="both", labelsize=ticks_font_size)
    ax_ifeed_7.set_ylim(bottom=-5, top=(df["i(vdd)"]*1e6).max())

    axs_7[3].plot(df["time"], df["v(vdd)"], label="vdd", color="tab:blue")
    axs_7[4].plot(df["time"], df["pwr"], label="pwr", color="tab:blue") # remember: in uW (micro Watt)

    axs_7[4].plot(df["time"], df["moving_avg_pwr"], label=f"moving avg pwr, window={window_size})", color="tab:orange")

    # plot the filtered power togheter with the moving average  power, but only for the datapoints where v(slp) is above 0.99 * VDD, the rest is set to NaN and will not be plotted

    filtered_pwr_plot = df["filtered_pwr"].copy()
    filtered_pwr_plot[df['v(slp)'] < 0.99 * df['v(vdd)']] = np.nan # set the datapoints where v(slp) is below 0.99 * VDD to NaN, so that they will not be plotted

    axs_7[4].plot(df["time"], filtered_pwr_plot, label=f"filtered pwr", color="tab:green")

    delay = 0 # in ns (nanosecond)
    # idx = df[df["v(correct_output_found)"] >= 0.99*df["v(vdd)"]].index[-1] if not df[df["v(correct_output_found)"] >= 0.99*df["v(vdd)"]].empty else None
    # timestamp = df["time"][idx] - delay if idx is not None else None
    # idx_timestamp = df[df["time"] >= timestamp].index[0] if timestamp is not None else None

    # axs_7[0].axvline(x=timestamp, color="black", linestyle="dashed", label=f"Measurment done\nat {df.loc[idx_timestamp, 'time']} ns")
    # axs_7[1].axvline(x=timestamp, color="black", linestyle="dashed")
    # axs_7[2].axvline(x=timestamp, color="black", linestyle="dashed")
    # axs_7[3].axvline(x=timestamp, color="black", linestyle="dashed")
    # axs_7[4].axvline(x=df.loc[idx_timestamp, "time"], color="black", linestyle="dashed")

    for i, ax in enumerate(axs_7):
        if ax == axs_7[4]:
            ax.set_ylabel("Power Consumption (uW)", fontsize=label_font_size)
            ax.set_ylim(bottom=-5, top=(df["moving_avg_pwr"]).max()*1.2) # set y-axis limit to 20% more than the maximum moving average power consumption
            # ax.set_yticks([0, 20, 40, 60])
            # ax.set_xticks(x)   
        else:   
            ax.set_ylabel("Voltage (V)", fontsize=label_font_size)
        ax.tick_params(axis="both", labelsize=ticks_font_size)
        ax.grid()
        ax.legend(loc="upper left", ncols=2, fontsize=legend_font_size)

    axs_7[0].set_title(f"Power consumption, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_font_size, fontweight='bold')
    axs_7[-1].set_xlabel("Time (ns)", fontsize=label_font_size)
    
    fig_7.tight_layout()
    fig_7.savefig(f"figures/{figure_name}_power_consumption.png", dpi=300, bbox_inches="tight")


    # close the plots if "temp" is not among the arguments
    if not "temp" in args:
        plt.close("all")


# show the plots if "temp" is among the arguments
if "temp" in args:
    plt.show()