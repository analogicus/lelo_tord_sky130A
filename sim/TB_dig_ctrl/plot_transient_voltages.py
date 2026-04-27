import pandas as pd
import matplotlib.pyplot as plt
import sys

args = sys.argv[1:]
files = list()

xx = "xx"

# example input arguments: python plot_temperature_transients.py ss Tl 125 2 30 1.7 0

bgr = ""
if "bgr" in args:
    bgr = "_bgr"
    print("bgr")

if len(args) == 0:
    print("No arguments provided. Plotting for typical corner, voltage (1.8 Volt) and temperature (27 Celsius).")
    files.append("output_tran/tran_SchGtKttTtVt_temperature27celsius_frequency2mhz_dutycycle40percent_vdd1.8volt.out")
if "typical" in args:
    for corner in ["tt"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
            for frequency in [1]: # Mega Hertz (MHz)
                for dutycycle in [50]: # Percent (%)
                    for voltage in [1.8]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
if "slow" in args:
    for corner in ["ss"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
            for frequency in [1]: # Mega Hertz (MHz)
                for dutycycle in [50]: # Percent (%)
                    for voltage in [1.7]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
if "fast" in args:
    for corner in ["ff"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
            for frequency in [1]: # Mega Hertz (MHz)
                for dutycycle in [50]: # Percent (%)
                    for voltage in [1.9]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
if "all" in args:
    for corner in ["tt", "ss", "ff", "sf", "fs"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
            for frequency in [0.5, 1, 2]: # Mega Hertz (MHz)
                for dutycycle in [20, 30, 40, 50, 60, 70, 80]: # Percent (%)
                    for voltage in [1.7, 1.8, 1.9]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
if "etc" in args:
    for corner in ["ss", "ff", "sf", "fs"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
            for frequency in [0.5, 1, 2]: # Mega Hertz (MHz)
                for dutycycle in [20, 30, 40, 50, 60, 70, 80]: # Percent (%)
                    for voltage in [1.7, 1.9]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
if "test" in args:
    for corner in ["tt", "ss", "ff"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
            for frequency in [1]: # Mega Hertz (MHz)
                for dutycycle in [50]: # Percent (%)
                    for voltage in [1.8]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
if "temp" in args:
    for corner in ["tt"]:
        for temperature in [110]: # Celsius (degree C)
            for frequency in [1]: # Mega Hertz (MHz)
                for dutycycle in [50]: # Percent (%)
                    for voltage in [1.8]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
if "temps" in args:
    for corner in ["tt"]:
        for temperature in [-40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]: # Celsius (degree C)
            for frequency in [1]: # Mega Hertz (MHz)
                for dutycycle in [50]: # Percent (%)
                    for voltage in [1.8]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
if "partialtemps" in args:
    for corner in ["tt"]:
        for temperature in [-40, 0, 40, 80, 125]: # Celsius (degree C)
            for frequency in [1]: # Mega Hertz (MHz)
                for dutycycle in [50]: # Percent (%)
                    for voltage in [1.8]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
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

coarse_code = []
fine_code = []
cir_temp = []
outp_volt = []
min_pwr = []
max_pwr = []
avg_pwr = []

coarse_code2 = []
fine_code2 = []
cir_temp2 = []
outp_volt2 = []
min_pwr2 = []
max_pwr2 = []
avg_pwr2 = []

for file in files:
    print(f"Plotting Vout transient results from file: {file}")

    circuit_temperature = float(file.split("temperature")[-1].split("celsius")[0]) # in Celsius degree
    clock_frequency = float(file.split("frequency")[-1].split("mhz")[0]) # in Mega Hertz
    clock_periode = 1 / clock_frequency  # in micro seconds
    duty_cycle = float(file.split("dutycycle")[-1].split("percent")[0]) # in Percent
    voltage_supply = float(file.split("vdd")[-1].split("volt")[0]) # in Volt
    process_corner = "Typical" if "tt" in file else "Slow-Slow" if "ss" in file else "Slow-Fast" if "sf" in file else "Fast-Slow" if "fs" in file else "Fast-Fast" if "ff" in file else "Oops, something is wrong!"

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

    # if df['v(dec_b)'].max() < 4:
    #     print(f"Skipping plot for file {file} because dec_b counts less than 4V.")
    #     continue    
    # else:
    #     print(f"Plotting results from: {file}")

    fig, axs = plt.subplots(5, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)

    # ax_iout = axs[0].twinx()
    # ax_iout.plot(df["time"], df["i(v.xdut.v1)"]*1e6, label="iout", color="tab:orange") # in uA
    # axs[0].plot(df["time"], df["v(vout)"], label="vout", color="tab:blue") # in V

    axs[0].plot(df["time"], df["v(v1)"]-df["v(v2)"], label="v1-v2", linestyle="solid")
    axs[0].plot(df["time"], df["v(v1a)"]-df["v(v2a)"], label="v1a-v2a", linestyle="dashed")
    axs[0].plot(df["time"], df["v(v1b)"]-df["v(v2b)"], label="v1b-v2b", linestyle="dotted")
    
    axs[1].plot(df["time"], df["v(v1)"], label="v1")
    # axs[1].plot(df["time"], df["v(v1a)"], label="v1a")
    # axs[1].plot(df["time"], df["v(v1b)"], label="v1b")
    axs[1].plot(df["time"], df["v(v2)"], label="v2")
    # axs[1].plot(df["time"], df["v(v2a)"], label="v2a")
    # axs[1].plot(df["time"], df["v(v2b)"], label="v2b")
    # axs[1].plot(df["time"], df["v(v2c)"], label="v2c")
    axs[1].plot(df["time"], df["v(vout)"], label="vout")

    axs[2].plot(df["time"], df["v(clk)"], label="clk")
    axs[2].plot(df["time"], df["v(bt)"], label="bt")
    axs[2].plot(df["time"], df["v(x1.ctl)"], label="ctl")
    # axs[2].plot(df["time"], df["v(slp)"], label="slp")
    axs[2].plot(df["time"], df["v(cmp)"], label="cmp")
    axs[2].plot(df["time"], df["v(rst)"], label="rst")
    # axs[2].plot(df["time"], df["v(timeout)"], label="timeout")
    # axs[3].plot(df["time"], df["v(dec_finetuning_counter)"], label="finetuning_counter")
    axs[3].plot(df["time"], df["v(dec_coarse_step_counter)"], label="coarse_step_counter")
    # axs[3].plot(df["time"], df["v(dec_coarse_step1)"], label="coarse_step1")
    # axs[3].plot(df["time"], df["v(dec_coarse_step2)"], label="coarse_step2")
    axs[3].plot(df["time"], df["v(dec_finetuning_duty_cycle)"], label="finetuning_duty_cycle")
    axs[4].plot(df["time"], df["v(dec_timeout_counter)"], label="timeout_counter")
    axs[4].plot(df["time"], df["v(dec_cmp_switching_counter)"], label="v(dec_cmp_switching_counter)")

    for ax in axs:
        ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
        ax.tick_params(axis="both", labelsize=ticks_fontsize)
        ax.grid()
        ax.legend(loc="upper left", ncol=2, fontsize=legend_fontsize)

    axs[0].set_title(f"{process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_fontsize, fontweight='bold')
    axs[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)

    # ax_iout.set_ylabel("Current (uA)", fontsize=label_fontsize)
    # ax_iout.legend(loc="lower right", fontsize=legend_fontsize)
    # ax_iout.tick_params(axis='both', labelsize=ticks_fontsize)

    fig.tight_layout()
    fig.savefig(f"figures/{file.split('/')[-1].split('.out')[0]}.png", dpi=300, bbox_inches="tight")


    fig_2, axs_2 = plt.subplots(6, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)
    
    axs_2[0].plot(df["time"], df["v(clk)"], label="v(clk)")
    axs_2[0].plot(df["time"], df["v(bt)"], label="v(bt)")
    axs_2[1].plot(df["time"], df["v(cmp)"], label="v(cmp)")
    axs_2[2].plot(df["time"], df["v(cmp_sync1)"], label="v(cmp_sync1)")
    axs_2[3].plot(df["time"], df["v(cmp_sync2)"], label="v(cmp_sync2)")
    axs_2[4].plot(df["time"], df["v(cmp_rising)"], label="v(cmp_rising)")
    axs_2[4].plot(df["time"], df["v(cmp_falling)"], label="v(cmp_falling)")
    axs_2[5].plot(df["time"], df["v(dec_cmp_rising_counter)"], label="v(dec_cmp_rising_counter)")
    axs_2[5].plot(df["time"], df["v(dec_cmp_switching_counter)"], label="v(dec_cmp_switching_counter)")

    for i, ax in enumerate(axs_2):
        ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
        ax.tick_params(axis="both", labelsize=ticks_fontsize)
        ax.grid()
        ax.legend(loc="best", fontsize=legend_fontsize)

    axs_2[0].set_title(f"Comparator signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C, {clock_frequency} MHz, {duty_cycle} %", fontsize=title_fontsize, fontweight='bold')
    axs_2[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)
    fig_2.tight_layout()


    # fig_3, axs_3 = plt.subplots(8, 2, figsize=(fig_width, fig_height), sharex=True, dpi=300)
    
    # axs_3[0, 0].plot(df["time"], df["v(b1)"], label="v(b1)")
    # axs_3[1, 0].plot(df["time"], df["v(b2)"], label="v(b2)")
    # axs_3[2, 0].plot(df["time"], df["v(b3)"], label="v(b3)")
    # axs_3[3, 0].plot(df["time"], df["v(b4)"], label="v(b4)")
    # axs_3[4, 0].plot(df["time"], df["v(b5)"], label="v(b5)")
    # axs_3[5, 0].plot(df["time"], df["v(b6)"], label="v(b6)")
    # axs_3[6, 0].plot(df["time"], df["v(b7)"], label="v(b7)")
    # axs_3[7, 0].plot(df["time"], df["v(b8)"], label="v(b8)")
    # axs_3[0, 1].plot(df["time"], df["v(b9)"], label="v(b9)")
    # axs_3[1, 1].plot(df["time"], df["v(b10)"], label="v(b10)")
    # axs_3[2, 1].plot(df["time"], df["v(b11)"], label="v(b11)")
    # axs_3[3, 1].plot(df["time"], df["v(b12)"], label="v(b12)")
    # axs_3[4, 1].plot(df["time"], df["v(b13)"], label="v(b13)")
    # axs_3[5, 1].plot(df["time"], df["v(b14)"], label="v(b14)")
    # axs_3[6, 1].plot(df["time"], df["v(b15)"], label="v(b15)")
    # axs_3[7, 1].plot(df["time"], df["v(dec_coarse_step1)"], label="v(dec_coarse_step1)")
    # axs_3[7, 1].plot(df["time"], df["v(dec_coarse_step2)"], label="v(dec_coarse_step2)")

    # for i, ax in enumerate(axs_3.flat):
    #     ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
    #     ax.tick_params(axis="both", labelsize=ticks_fontsize)
    #     ax.grid()
    #     ax.legend(loc="best", fontsize=legend_fontsize)

    # # axs_3[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)
    # fig_3.tight_layout()


    # fig_4, axs_4 = plt.subplots(4, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)
    
    # axs_4[0].plot(df["time"], df["v(clk)"], label="v(clk)")
    # axs_4[1].plot(df["time"], df["v(finetuning_signal)"], label="v(finetuning_signal)")
    # axs_4[2].plot(df["time"], df["v(dec_finetuning_counter)"], label="v(dec_finetuning_counter)")
    # axs_4[3].plot(df["time"], df["v(dec_finetuning_duty_cycle)"], label="v(dec_finetuning_duty_cycle)")
    # axs_4[3].plot(df["time"], df["v(dec_finetuning_periode)"], label="v(dec_finetuning_periode)")
    # axs_4[3].plot(df["time"], df["v(dec_coarse_step_counter)"], label="v(dec_coarse_step_counter)")

    # for i, ax in enumerate(axs_4):
    #     ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
    #     ax.tick_params(axis="both", labelsize=ticks_fontsize)
    #     ax.grid()
    #     ax.legend(loc="best", fontsize=legend_fontsize)

    # axs_4[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)
    # fig_4.tight_layout()


    fig_5, axs_5 = plt.subplots(3, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)

    axs_5[0].plot(df["time"], df["v(clk)"], label="v(clk)")
    # axs_5[0].plot(df["time"], df["v(bt)"], label="bt")
    axs_5[0].plot(df["time"], df["v(swbrn1)"], label="v(swbrn1)")
    axs_5[1].plot(df["time"], df["v(swbrn2)"], label="v(swbrn2)")
    axs_5[2].plot(df["time"], df["v(swbrn3)"], label="v(swbrn3)")
    # axs_5[1].plot(df["time"], df["v(swbgr1)"], label="v(swbgr1)")
    # axs_5[1].plot(df["time"], df["v(swbgr2)"], label="v(swbgr2)")
    axs_5[0].plot(df["time"], df["v(swcap1)"], label="v(swcap1)")
    axs_5[1].plot(df["time"], df["v(swcap2)"], label="v(swcap2)")
    axs_5[2].plot(df["time"], df["v(swcap3)"], label="v(swcap3)")
    # axs_5[3].plot(df["time"], df["v(swdrn1)"], label="v(swdrn1)")
    # axs_5[3].plot(df["time"], df["v(swdrn2)"], label="v(swdrn2)")
    # axs_5[3].plot(df["time"], df["v(swdrn3)"], label="v(swdrn3)")

    for i, ax in enumerate(axs_5):
        ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
        ax.tick_params(axis="both", labelsize=ticks_fontsize)
        ax.grid()
        ax.legend(loc="best", fontsize=legend_fontsize)

    axs_5[0].set_title(f"Switch signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_fontsize, fontweight='bold')
    axs_5[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)
    fig_5.tight_layout()

    
    fig_6, axs_6 = plt.subplots(5, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)

    axs_6[0].plot(df["time"], df["v(v1)"], label="v1")
    axs_6[0].plot(df["time"], df["v(v2)"], label="v2")
    axs_6[0].plot(df["time"], df["v(vout)"], label="vout")
    axs_6[1].plot(df["time"], df["v(clk)"], label="clk")
    axs_6[1].plot(df["time"], df["v(bt)"], label="bt")
    axs_6[1].plot(df["time"], df["v(x1.ctl)"], label="ctl")
    axs_6[1].plot(df["time"], df["v(cmp)"], label="cmp")
    axs_6[1].plot(df["time"], df["v(rst)"], label="rst")
    axs_6[1].plot(df["time"], df["v(slp)"], label="slp")
    axs_6[2].plot(df["time"], df["v(dec_coarse_step_counter)"], label="coarse_step_counter")
    axs_6[2].plot(df["time"], df["v(dec_finetuning_duty_cycle)"], label="finetuning_duty_cycle")
    axs_6[3].plot(df["time"], df["v(stepping_up)"], label="v(stepping_up)")
    axs_6[4].plot(df["time"], df["v(dec_cmp_switching_counter)"], label="v(dec_cmp_switching_counter)")

    for i, ax in enumerate(axs_6):
        ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
        ax.tick_params(axis="both", labelsize=ticks_fontsize)
        ax.grid()
        ax.legend(loc="best", fontsize=legend_fontsize)

    axs_6[0].set_title(f"Switch signals, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_fontsize, fontweight='bold')
    axs_6[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)
    fig_6.tight_layout()


    fig_7, axs_7 = plt.subplots(4, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)
    
    axs_7[0].plot(df["time"], df["v(v1)"], label="v1")
    axs_7[0].plot(df["time"], df["v(v2)"], label="v2")
    axs_7[0].plot(df["time"], df["v(vout)"], label="vout")
    axs_7[1].plot(df["time"], df["v(clk)"], label="clk")
    axs_7[1].plot(df["time"], df["v(bt)"], label="bt")
    axs_7[1].plot(df["time"], df["v(x1.ctl)"], label="ctl")
    axs_7[1].plot(df["time"], df["v(cmp)"], label="cmp")
    axs_7[1].plot(df["time"], df["v(rst)"], label="rst")
    axs_7[1].plot(df["time"], df["v(slp)"], label="slp")
    axs_7[2].plot(df["time"], df["v(vdd)"], label="vdd", color="tab:blue")
    axs_7[3].plot(df["time"], df["v(vdd)"] * -(df["i(vdd)"]) * 1e6, label="pwr", color="tab:blue") # in uW (micro Watt)

    # moving average filter with window size of 10 applied to the power plot
    window_size = 100
    axs_7[3].plot(df["time"], (df["v(vdd)"] * -(df["i(vdd)"]) * 1e6).rolling(window=window_size).mean(), label=f"pwr (moving avg, window={window_size})", color="tab:orange")
    
    # plot the current in axs_7[2] with a secondary y-axis
    ax_iout_7 = axs_7[2].twinx()
    ax_iout_7.plot(df["time"], -df["i(vdd)"]*1e6, label="iout", color="tab:orange") # in uA
    ax_iout_7.set_ylabel("Current (uA)", fontsize=label_fontsize)
    ax_iout_7.legend(loc="upper right", fontsize=legend_fontsize)
    ax_iout_7.tick_params(axis="both", labelsize=ticks_fontsize)

    for i, ax in enumerate(axs_7):
        if ax == axs_7[3]:
            ax.set_ylabel("Power Consumption (uW)", fontsize=label_fontsize)
        else:   
            ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
        ax.tick_params(axis="both", labelsize=ticks_fontsize)
        ax.grid()
        ax.legend(loc="upper left", fontsize=legend_fontsize)

    axs_7[0].set_title(f"Power consumption, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_fontsize, fontweight='bold')
    axs_7[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)
    fig_7.tight_layout()


    # append the last value of v(vout) to y list
    outp_volt.append(df["v(vout)"].iloc[-1])
    cir_temp.append(circuit_temperature)
    coarse_code.append(df["v(dec_coarse_step_counter)"].iloc[-1])
    fine_code.append(df["v(dec_finetuning_duty_cycle)"].iloc[-1])
    min_pwr.append((df["v(vdd)"] * df["i(vdd)"]).min())
    max_pwr.append((df["v(vdd)"] * df["i(vdd)"]).max())
    avg_pwr.append((df["v(vdd)"] * df["i(vdd)"]).mean())

    idx = df[df["v(swbrn3)"] >= 1.69].index[2400] if not df[df["v(swbrn3)"] >= 1.69].empty else None
    outp_volt2.append(df.loc[idx, "v(vout)"] if idx is not None else None)
    cir_temp2.append(circuit_temperature)
    coarse_code2.append(df.loc[idx, "v(dec_coarse_step_counter)"] if idx is not None else None)
    fine_code2.append(df.loc[idx, "v(dec_finetuning_duty_cycle)"] if idx is not None else None)
    min_pwr2.append((df["v(vdd)"] * df["i(vdd)"]).min())
    max_pwr2.append((df["v(vdd)"] * df["i(vdd)"]).max())
    avg_pwr2 = (df["v(vdd)"] * df["i(vdd)"]).mean()


    if not "temp" in args:
        plt.close("all")
    
df_1 = pd.DataFrame({"Temperature (°C)": cir_temp, "Output voltage (V)": outp_volt, "Coarse code": coarse_code, "Fine code": fine_code}).sort_values(by="Temperature (°C)")
df_1.to_csv(f"figures/{'_'.join(args)}_df1.csv", index=False)

df_2 = pd.DataFrame({"Temperature (°C)": cir_temp2, "Output voltage (V)": outp_volt2, "Coarse code": coarse_code2, "Fine code": fine_code2}).sort_values(by="Temperature (°C)")
df_2.to_csv(f"figures/{'_'.join(args)}_df2.csv", index=False)

if "temp" in args:
    plt.show()