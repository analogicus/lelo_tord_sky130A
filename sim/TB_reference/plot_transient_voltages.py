import pandas as pd
import matplotlib.pyplot as plt
import sys

args = sys.argv[1:]
files = list()

xx = "xx"

# example input arguments: python plot_temperature_transients.py ss Tl 125 2 30 1.7 0

bgr = ""
if "bgr" in args:
    bgr = "_sim2"
    print("bgr/sim2")

if len(args) == 0:
    print("No arguments provided. Plotting for typical corner, voltage (1.8 Volt) and temperature (27 Celsius).")
    files.append("output_tran/tran_SchGtKttTtVt_temperature27.0C_vdd1.8V.out")
if "typical" in args:
    for corner in ["tt"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
                for voltage in [1.8]: # Volt (V)
                    Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                    files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}C_vdd{voltage}V.out")
if "slow" in args:
    for corner in ["ss"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
            for voltage in [1.7]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}C_vdd{voltage}V.out")
if "fast" in args:
    for corner in ["ff"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
            for voltage in [1.9]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}C_vdd{voltage}V.out")
if "all" in args:
    for corner in ["tt", "ss", "ff", "sf", "fs"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
            for voltage in [1.7, 1.8, 1.9]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}C_vdd{voltage}V.out")
if "etc" in args:
    for corner in ["ss", "ff", "sf", "fs"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
            for voltage in [1.7, 1.9]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}C_vdd{voltage}V.out")
if "test" in args:
    for corner in ["tt"]:
        for temperature in [-40, 0, 40, 80, 125]: # Celsius (degree C)
            for voltage in [1.8]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}C_vdd{voltage}V.out")
if "temp" in args:
    for corner in ["tt"]:
        for temperature in [-40]: # Celsius (degree C)
            for voltage in [1.8]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}C_vdd{voltage}V.out")
if "temps" in args:
    for corner in ["tt"]:
        for temperature in [-40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]: # Celsius (degree C)
            for voltage in [1.8]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}C_vdd{voltage}V.out")
if "partialtemps" in args:
    for corner in ["tt"]:
        for temperature in [-40, 0, 125]: # Celsius (degree C)
            for voltage in [1.8]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}C_vdd{voltage}V.out")
# else:
#     print("Plotting with file data passed as argument.")
#     xx = "tt" if args[0] == "tt" else "ff" if args[0] == "ff" else "ss" if args[0] == "ss" else "sf" if args[0] == "sf" else "fs" if args[0] == "fs" else "ttmm" if args[0] == "ttmm" else "Oops, Somethings wrong!"
#     print(f'Process corner: {xx}')
#     Tx = args[1]
#     print(f'Temperature corner: {Tx}')
#     Vx = "Vl" if float(args[5]) == 1.7 else "Vt" if float(args[5]) == 1.8 else "Vh" if float(args[5]) == 1.9 else "Oops"
#     print(f'Voltage corner: {Vx}')
#     files.append(f"output_tran/tran_SchGtK{xx}{Tx}{Vx}{bgr}_temperature{args[2]}celsius_frequency{args[3]}mhz_dutycycle{args[4]}percent_vdd{args[5]}volt.out") # plots file name passed as argument

if xx == "ttmm" and len(args) > 6:   
    c = args[6]
    # insert c in the file names
    files = [f.replace("SchGtKttmmTtVt_", f"SchGtKttmmTtVt_{c}_") for f in files]

fig_width = 4
fig_height = 4.5
font_size = 6
title_fontsize = font_size
label_fontsize = font_size
legend_fontsize = font_size
ticks_fontsize = font_size


for file in files:
    print(f"Plotting Vout transient results from file: {file}")

    circuit_temperature = float(file.split("temperature")[-1].split("C")[0]) # in Celsius degree
    voltage_supply = float(file.split("vdd")[-1].split("V")[0]) # in Volt
    process_corner = "Typical" if "tt" in file else "Slow-Slow" if "ss" in file else "Slow-Fast" if "sf" in file else "Fast-Slow" if "fs" in file else "Fast-Fast" if "ff" in file else "Oops, something is wrong!"
    
    name = file.split("/")[-1].split("_temperature")[0:1]
    name = name[0] + "_temp_" + str(circuit_temperature) + "C_vdd_" + str(voltage_supply) + "V"

    # print(f"Circuit temperature: {circuit_temperature} Celsius degree.")
    # print(f"Clock frequency of finetuning signal: {clock_frequency} Mega Hertz, and clock periode is: {clock_periode} micro seconds.")
    # print(f"Duty cycle of fine tuning signal: {duty_cycle} %.")
    # print(f"Supply voltage (VDD): {voltage_supply} Volt.")
    # print(f"Circuit process corners: {process_corner}.")

    df = pd.read_csv(file, sep="\s+")

    # print(f"Data columns: {df.columns.tolist()}")
    # print(f"Dataframe shape: {df.shape}")
    # print(f"Dataframe head:\n{df.head()}")    
    # print(f"Dataframe tail:\n{df.tail()}")

    df['time'] = df['time'] * 1e9 # in ns
    df['diff'] = df['v(v1)']-df['v(v2)']


    #
    # plot BGR voltages
    #

    fig, axs = plt.subplots(6, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)
    
    axs[0].plot(df["time"], df["v(xdut.iout)"], label="v(iout)", color="tab:blue") # in V

    # ax_iout = axs[0].twinx()
    # axs[0].plot(df["time"], (df["v(xdut.iout)"] / (8*7535))*1e6, label="iout", color="tab:orange") # in uA

    # axs[0].plot(df["time"], df["v(v1)"]-df["v(v2)"], label="v1-v2", linestyle="solid")
    # axs[0].plot(df["time"], df["v(v1a)"]-df["v(v2a)"], label="v1a-v2a", linestyle="dashed")
    # axs[0].plot(df["time"], df["v(v1b)"]-df["v(v2b)"], label="v1b-v2b", linestyle="dotted")
    
    axs[1].plot(df["time"], df["v(v1a)"], label="v1a")
    axs[1].plot(df["time"], df["v(v1b)"], label="v1b")
    axs[1].plot(df["time"], df["v(v2a)"], label="v2a")
    axs[1].plot(df["time"], df["v(v2b)"], label="v2b")
    axs[1].plot(df["time"], df["v(v2c)"], label="v2c")
    axs[1].plot(df["time"], df["v(vref)"], label="vref")

    axs[2].plot(df["time"], df["v(v1)"], label="v(v1)")
    axs[2].plot(df["time"], df["v(v2)"], label="v(v2)")
    axs[2].plot(df["time"], df["v(vout)"], label="v(vout)")

    axs[3].plot(df["time"], df["v(clk)"], label="clk")
    axs[3].plot(df["time"], df["v(b0)"], label="b0")
    axs[3].plot(df["time"], df["v(x1.ctl)"], label="ctl")
    axs[3].plot(df["time"], df["v(cmp_async)"], label="cmp")
    axs[3].plot(df["time"], df["v(rst)"], label="rst")
    axs[3].plot(df["time"], df["v(slp)"], label="slp")
    
    axs[4].plot(df["time"], df["v(xdut.x1.nbias)"], label="nbias")
    axs[4].plot(df["time"], df["v(xdut.x1.pbias)"], label="pbias")

    axs[5].plot(df["time"], df["v(x1.vt)"], label="vt")
    axs[5].plot(df["time"], df["v(x1.ctlb)"], label="ctlb")
    axs[5].plot(df["time"], df["v(x1.ctl)"], label="ctl")

    for ax in axs:
        ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
        ax.tick_params(axis="both", labelsize=ticks_fontsize)
        ax.grid()
        ax.legend(loc="upper left", ncols=2, fontsize=legend_fontsize)

    axs[0].set_title(f"BGR core signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_fontsize, fontweight='bold')
    axs[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)

    # ax_iout.set_ylabel("Current (uA)", fontsize=label_fontsize)
    # ax_iout.legend(loc="lower right", fontsize=legend_fontsize)
    # ax_iout.tick_params(axis='both', labelsize=ticks_fontsize)

    fig.tight_layout()
    fig.savefig(f"figures/{name}_bgr_core_signals.png", dpi=300, bbox_inches="tight")


    #
    # plot external comparator voltages
    #

    fig_2, axs_2 = plt.subplots(5, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)
    
    axs_2[0].plot(df["time"], df["v(clk)"], label="v(clk)")
    axs_2[0].plot(df["time"], df["v(b0)"], label="v(b0)")
    axs_2[0].plot(df["time"], df["v(x1.ctl)"], label="v(x1.ctl)")
    axs_2[0].plot(df["time"], df["v(cmp_async)"], label="v(cmp_async)")
    axs_2[0].plot(df["time"], df["v(rst)"], label="v(rst)")
    axs_2[0].plot(df["time"], df["v(slp)"], label="v(slp)")

    axs_2[1].plot(df["time"], df["v(v1)"], label="v(v1)")
    axs_2[1].plot(df["time"], df["v(v2)"], label="v(v2)")
    axs_2[1].plot(df["time"], df["v(vout)"], label="v(vout)")
    axs_2[1].plot(df["time"], df["v(cmp_meta)"], label="v(cmp_meta)")

    axs_2[2].plot(df["time"], df["v(cmp_sync)"], label="v(cmp_sync)")

    axs_2[3].plot(df["time"], df["v(cmp_rising)"], label="v(cmp_rising)")
    axs_2[3].plot(df["time"], df["v(cmp_falling)"], label="v(cmp_falling)")
    axs_2[3].plot(df["time"], df["v(stepping_up)"], label="v(stepping_up)")

    axs_2[4].plot(df["time"], df["v(dec_cmp_rising_counter)"], label="v(dec_cmp_rising_counter)")
    axs_2[4].plot(df["time"], df["v(dec_cmp_switching_counter)"], label="v(dec_cmp_switching_counter)")

    for i, ax in enumerate(axs_2):
        ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
        ax.tick_params(axis="both", labelsize=ticks_fontsize)
        ax.grid()
        ax.legend(loc="best", ncols=2, fontsize=legend_fontsize)

    axs_2[0].set_title(f"External comparator signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C,", fontsize=title_fontsize, fontweight='bold')
    axs_2[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)
    fig_2.tight_layout()
    fig_2.savefig(f"figures/{name}_external_comparator_signals.png", dpi=300, bbox_inches="tight")



    #
    # plot internal voltages in comparator
    #
    
    fig_3, axs_3 = plt.subplots(5, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)

    axs_3[0].plot(df["time"], df["v(v1)"], label="v1/vin")
    axs_3[0].plot(df["time"], df["v(v2)"], label="v2/vip")
    axs_3[0].plot(df["time"], df["v(cmp_async)"], label="cmp_async/vout")
    axs_3[0].plot(df["time"], df["v(rst)"], label="rst")
    axs_3[0].plot(df["time"], df["v(slp)"], label="slp")

    axs_3[1].plot(df["time"], df["v(xdut.x2.x1.vbias)"], label="vbias")

    axs_3[2].plot(df["time"], df["v(xdut.x2.x1.vindrn)"], label="vindrn")
    axs_3[3].plot(df["time"], df["v(xdut.x2.x1.vipdrn)"], label="vipdrn")
    axs_3[4].plot(df["time"], df["v(xdut.x2.x1.vsrc)"], label="vsrc")

    for i, ax in enumerate(axs_3):
        ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
        ax.tick_params(axis="both", labelsize=ticks_fontsize)
        ax.grid()
        ax.legend(loc="best", ncols=2, fontsize=legend_fontsize)

    axs_3[0].set_title(f"Internal comparator signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_fontsize, fontweight='bold')
    axs_3[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)
    fig_3.tight_layout()
    fig_3.savefig(f"figures/{name}_internal_comparator_signals.png", dpi=300, bbox_inches="tight")

    #
    # plot control DAC voltages
    #

    fig_4, axs_4 = plt.subplots(8, 2, figsize=(fig_width*2, fig_height), sharex=True, dpi=300)
    
    axs_4[0, 0].plot(df["time"], df["v(b1)"], label="v(b1)")
    axs_4[0, 0].plot(df["time"], df["v(xdut.x1.b1_mid)"], label="v(b1_mid)")
    axs_4[1, 0].plot(df["time"], df["v(b2)"], label="v(b2)")
    axs_4[1, 0].plot(df["time"], df["v(xdut.x1.b2_mid)"], label="v(b2_mid)")
    axs_4[2, 0].plot(df["time"], df["v(b3)"], label="v(b3)")
    axs_4[2, 0].plot(df["time"], df["v(xdut.x1.b3_mid)"], label="v(b3_mid)")
    axs_4[3, 0].plot(df["time"], df["v(b4)"], label="v(b4)")
    axs_4[3, 0].plot(df["time"], df["v(xdut.x1.b4_mid)"], label="v(b4_mid)")
    axs_4[4, 0].plot(df["time"], df["v(b5)"], label="v(b5)")
    axs_4[4, 0].plot(df["time"], df["v(xdut.x1.b5_mid)"], label="v(b5_mid)")
    axs_4[5, 0].plot(df["time"], df["v(b6)"], label="v(b6)")
    axs_4[5, 0].plot(df["time"], df["v(xdut.x1.b6_mid)"], label="v(b6_mid)")
    axs_4[6, 0].plot(df["time"], df["v(b7)"], label="v(b7)")
    axs_4[6, 0].plot(df["time"], df["v(xdut.x1.b7_mid)"], label="v(b7_mid)")
    axs_4[7, 0].plot(df["time"], df["v(b8)"], label="v(b8)")
    axs_4[7, 0].plot(df["time"], df["v(xdut.x1.b8_mid)"], label="v(b8_mid)")
    axs_4[0, 1].plot(df["time"], df["v(b9)"], label="v(b9)")
    axs_4[0, 1].plot(df["time"], df["v(xdut.x1.b9_mid)"], label="v(b9_mid)")
    axs_4[1, 1].plot(df["time"], df["v(b10)"], label="v(b10)")
    axs_4[1, 1].plot(df["time"], df["v(xdut.x1.b10_mid)"], label="v(b10_mid)")
    axs_4[2, 1].plot(df["time"], df["v(b11)"], label="v(b11)")
    axs_4[2, 1].plot(df["time"], df["v(xdut.x1.b11_mid)"], label="v(b11_mid)")
    axs_4[3, 1].plot(df["time"], df["v(b12)"], label="v(b12)")
    axs_4[3, 1].plot(df["time"], df["v(xdut.x1.b12_mid)"], label="v(b12_mid)")
    axs_4[4, 1].plot(df["time"], df["v(b13)"], label="v(b13)")
    axs_4[4, 1].plot(df["time"], df["v(xdut.x1.b13_mid)"], label="v(b13_mid)")
    axs_4[5, 1].plot(df["time"], df["v(b14)"], label="v(b14)")
    axs_4[5, 1].plot(df["time"], df["v(xdut.x1.b14_mid)"], label="v(b14_mid)")
    axs_4[6, 1].plot(df["time"], df["v(b15)"], label="v(b15)")
    axs_4[6, 1].plot(df["time"], df["v(xdut.x1.b15_mid)"], label="v(b15_mid)")
    axs_4[6, 1].plot(df["time"], df["v(xdut.iout)"], label="v(iout)")
    axs_4[7, 1].plot(df["time"], df["v(dec_coarse_step1)"], label="v(dec_coarse_step1)")
    axs_4[7, 1].plot(df["time"], df["v(dec_coarse_step2)"], label="v(dec_coarse_step2)")

    for i, ax in enumerate(axs_4.flat):
        ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
        ax.tick_params(axis="both", labelsize=ticks_fontsize)
        ax.grid()
        ax.legend(loc="best", ncols=2, fontsize=legend_fontsize)

    # axs_4[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)
    axs_4[0, 0].set_title(f"DAC control signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_fontsize, fontweight='bold')
    fig_4.tight_layout()
    fig_4.savefig(f"figures/{name}_dac_control_signals.png", dpi=300, bbox_inches="tight")


    #
    # plot counter signals
    #

    fig_5, axs_5 = plt.subplots(5, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)
    
    axs_5[0].plot(df["time"], df["v(clk)"], label="v(clk)")
    axs_5[0].plot(df["time"], df["v(b0)"], label="v(b0)")
    axs_5[0].plot(df["time"], df["v(x1.ctl)"], label="v(x1.ctl)")
    axs_5[0].plot(df["time"], df["v(cmp_async)"], label="v(cmp_async)")
    axs_5[0].plot(df["time"], df["v(rst)"], label="v(rst)")
    axs_5[0].plot(df["time"], df["v(slp)"], label="v(slp)")

    axs_5[1].plot(df["time"], df["v(v1)"], label="v(v1)")
    axs_5[1].plot(df["time"], df["v(v2)"], label="v(v2)")
    axs_5[1].plot(df["time"], df["v(vout)"], label="v(vout)")

    axs_5[2].plot(df["time"], df["v(dec_finetuning_duty_cycle)"], label="v(dec_finetuning_duty_cycle)")
    axs_5[2].plot(df["time"], df["v(dec_coarse_step_counter)"], label="v(dec_coarse_step_counter)")
    
    axs_5[3].plot(df["time"], df["v(dec_finetuning_counter)"], label="v(dec_finetuning_counter)")
    axs_5[3].plot(df["time"], df["v(dec_timeout_counter)"], label="timeout_counter")

    axs_5[4].plot(df["time"], df["v(dec_cmp_switching_counter)"], label="v(dec_cmp_switching_counter)")

    for i, ax in enumerate(axs_5):
        ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
        ax.tick_params(axis="both", labelsize=ticks_fontsize)
        ax.grid()
        ax.legend(loc="best", ncols=2, fontsize=legend_fontsize)

    axs_5[0].set_title(f"Counter signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_fontsize, fontweight='bold')
    axs_5[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)
    fig_5.tight_layout()
    fig_5.savefig(f"figures/{name}_counter_signals.png", dpi=300, bbox_inches="tight")


    #
    # plot switch voltages
    #

    fig_6, axs_6 = plt.subplots(4, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)

    axs_6[0].plot(df["time"], df["v(clk)"], label="v(clk)")
    axs_6[0].plot(df["time"], df["v(b0)"], label="b0")
    axs_6[0].plot(df["time"], df["v(rst)"], label="v(rst)")
    axs_6[0].plot(df["time"], df["v(slp)"], label="v(slp)")
    axs_6[0].plot(df["time"], df["v(mode)"], label="v(mode)")
    axs_6[0].plot(df["time"], df["v(mode_meta)"], label="v(mode_meta)")
    axs_6[0].plot(df["time"], df["v(operation)"], label="v(operation)")

    axs_6[1].plot(df["time"], df["v(swbgr1)"], label="v(swbgr1)")
    axs_6[1].plot(df["time"], df["v(swbrn1)"], label="v(swbrn1)")
    axs_6[1].plot(df["time"], df["v(swcap1)"], label="v(swcap1)")
    axs_6[1].plot(df["time"], df["v(swdrn1)"], label="v(swdrn1)")

    axs_6[2].plot(df["time"], df["v(swbgr2)"], label="v(swbgr2)")
    axs_6[2].plot(df["time"], df["v(swbrn2)"], label="v(swbrn2)")
    axs_6[2].plot(df["time"], df["v(swcap2)"], label="v(swcap2)")
    axs_6[2].plot(df["time"], df["v(swdrn2)"], label="v(swdrn2)")

    axs_6[3].plot(df["time"], df["v(swbrn3)"], label="v(swbrn3)")
    axs_6[3].plot(df["time"], df["v(swcap3)"], label="v(swcap3)")
    axs_6[3].plot(df["time"], df["v(swdrn3)"], label="v(swdrn3)")

    for i, ax in enumerate(axs_6    ):
        ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
        ax.tick_params(axis="both", labelsize=ticks_fontsize)
        ax.grid()
        ax.legend(loc="best", ncol=2, fontsize=legend_fontsize)

    axs_6[0].set_title(f"Switch signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_fontsize, fontweight='bold')
    axs_6[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)
    fig_6.tight_layout()
    fig_6.savefig(f"figures/{name}_switch_signals.png", dpi=300, bbox_inches="tight")


    #
    # Plot power consumption
    #

    df["pwr"] = df["v(vdd)"] * -(df["i(vdd)"]) * 1e6 # in uW (micro Watt)
    df["moving_avg_pwr"] = df["pwr"].rolling(window=100).mean() # moving average filter with window size of 100 applied to the power plot

    fig_7, axs_7 = plt.subplots(5, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)
    
    axs_7[0].plot(df["time"], df["v(v1)"], label="v1")
    axs_7[0].plot(df["time"], df["v(v2)"], label="v2")
    axs_7[0].plot(df["time"], df["v(vout)"], label="vout")

    axs_7[1].plot(df["time"], df["v(clk)"], label="clk")
    axs_7[1].plot(df["time"], df["v(b0)"], label="b0")
    axs_7[1].plot(df["time"], df["v(x1.ctl)"], label="ctl")

    axs_7[1].plot(df["time"], df["v(cmp_async)"], label="cmp")
    axs_7[1].plot(df["time"], df["v(rst)"], label="rst")
    axs_7[1].plot(df["time"], df["v(slp)"], label="slp")

    axs_7[2].plot(df["time"], df["v(dec_finetuning_duty_cycle)"], label="v(dec_finetuning_duty_cycle)")
    axs_7[2].plot(df["time"], df["v(dec_coarse_step_counter)"], label="v(dec_coarse_step_counter)")

    # plot the current in axs_7[2] with a secondary y-axis
    ax_iout_7 = axs_7[3].twinx()
    ax_iout_7.plot(df["time"], -df["i(vdd)"]*1e6, label="idd", color="tab:orange") # in uA
    ax_iout_7.set_ylabel("Current (uA)", fontsize=label_fontsize)
    ax_iout_7.legend(loc="upper right", ncols=2, fontsize=legend_fontsize)
    ax_iout_7.tick_params(axis="both", labelsize=ticks_fontsize)
    ax_iout_7.set_ylim(bottom=-5, top=(df["i(vdd)"]*1e6).max())

    axs_7[3].plot(df["time"], df["v(vdd)"], label="vdd", color="tab:blue")
    axs_7[4].plot(df["time"], df["pwr"], label="pwr", color="tab:blue") # remember: in uW (micro Watt)

    # moving average filter with window size of 10 applied to the power plot
    window_size = 100
    axs_7[4].plot(df["time"], df["moving_avg_pwr"], label=f"moving avg pwr, window={window_size})", color="tab:orange")

    for i, ax in enumerate(axs_7):
        if ax == axs_7[4]:
            ax.set_ylabel("Power Consumption (uW)", fontsize=label_fontsize)
            ax.set_ylim(bottom=-5, top=(df["moving_avg_pwr"]).max()) # set y-axis limit to 20% more than the maximum moving average power consumption
            # ax.set_yticks([0, 20, 40, 60])
            # ax.set_xticks(x)   
        else:   
            ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
        ax.tick_params(axis="both", labelsize=ticks_fontsize)
        ax.grid()
        ax.legend(loc="upper left", ncols=2, fontsize=legend_fontsize)

    axs_7[0].set_title(f"Power consumption, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_fontsize, fontweight='bold')
    axs_7[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)
    fig_7.tight_layout()
    fig_7.savefig(f"figures/{name}_power_consumption.png", dpi=300, bbox_inches="tight")


    # close the plots if "temp" is not among the arguments
    if not "temp" in args:
        plt.close("all")


# show the plots if "temp" is among the arguments
if "temp" in args:
    plt.show()