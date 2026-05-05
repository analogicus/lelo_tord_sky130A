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
    for corner in ["tt"]:
        for temperature in [-40, 0, 40, 80, 125]: # Celsius (degree C)
            for frequency in [1]: # Mega Hertz (MHz)
                for dutycycle in [50]: # Percent (%)
                    for voltage in [1.8]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}{bgr}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")
if "temp" in args:
    for corner in ["tt"]:
        for temperature in [-40]: # Celsius (degree C)
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
        for temperature in [60, 65, 70, 75, 80]: # Celsius (degree C)
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
    voltage_supply = float(file.split("vdd")[-1].split("volt")[0]) # in Volt
    
    df = pd.read_csv(file, sep="\s+")

    df["pwr"] = df["v(vdd)"] * -(df["i(vdd)"]) * 1e6 # in uW (micro Watt)
    df["moving_avg_pwr"] = df["pwr"].rolling(window=100).mean() # moving average filter with window size of 100 applied to the power plot

    # append the last value of v(vout) to y list
    outp_volt.append(df["v(vout)"].iloc[-1])
    cir_temp.append(circuit_temperature)
    coarse_code.append(df["v(dec_coarse_step_counter)"].iloc[-1])
    fine_code.append(df["v(dec_finetuning_duty_cycle)"].iloc[-1])
    min_pwr.append((df["v(vdd)"] * -df["i(vdd)"]).min())
    max_pwr.append((df["v(vdd)"] * -df["i(vdd)"]).max())
    avg_pwr.append((df["v(vdd)"] * -df["i(vdd)"]).mean())

    delay = 2400 # in number of data points, which corresponds to 2.4 micro seconds (us) after v(swbrn3) first reaches 1.69 V, which is approximately the time when the output voltage stabilizes after the step response

    # append the value of v(vout) when v(swbrn3) first reaches 1.69 V to y list
    idx = df[df["v(swbrn3)"] >= 0.99*df["v(vdd)"]].index[delay] if not df[df["v(swbrn3)"] >= 0.99*df["v(vdd)"]].empty else None
    outp_volt2.append(df.loc[idx, "v(vout)"] if idx is not None else None)
    cir_temp2.append(circuit_temperature)
    coarse_code2.append(df.loc[idx, "v(dec_coarse_step_counter)"] if idx is not None else None)
    fine_code2.append(df.loc[idx, "v(dec_finetuning_duty_cycle)"] if idx is not None else None)
    min_pwr2.append((df["pwr"]).min())
    max_pwr2.append((df["pwr"]).max())
    avg_pwr2.append((df["pwr"]).mean())

df1 = pd.DataFrame({"Temperature (°C)": cir_temp, "Output voltage (V)": outp_volt, "Coarse code": coarse_code, "Fine code": fine_code, "Minimum power (uW)": min_pwr, "Maximum power (uW)": max_pwr, "Average power (uW)": avg_pwr}).sort_values(by="Temperature (°C)")
df1.to_csv(f"figures/{'_'.join(args)}_df1.csv", index=False)

df2 = pd.DataFrame({"Temperature (°C)": cir_temp2, "Output voltage (V)": outp_volt2, "Coarse code": coarse_code2, "Fine code": fine_code2, "Minimum power (uW)": min_pwr2, "Maximum power (uW)": max_pwr2, "Average power (uW)": avg_pwr2}).sort_values(by="Temperature (°C)")
df2.to_csv(f"figures/{'_'.join(args)}_df2.csv", index=False)
