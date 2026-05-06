import pandas as pd
import matplotlib.pyplot as plt
import sys

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
        for temperature in [-40, -20, 0, 30, 60, 90, 125]: # Celsius (degree C)
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
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
            for voltage in [1.7, 1.8, 1.9]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")
if "etc" in args:
    for corner in ["ss", "ff", "sf", "fs"]:
        for temperature in [-40, -20, 0, 25, 50, 75, 100, 125]: # Celsius (degree C)
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
    for corner in ["tt"]:
        for temperature in [-40]: # Celsius (degree C)
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
    for corner in ["tt"]:
        for temperature in [-40, 0, 125]: # Celsius (degree C)
            for voltage in [1.8]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")
if "montecarlo" in args:
    for corner in ["ttmm"]:
        for temperature in [25]: # Celsius (degree C)
            for voltage in [1.8]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                for run in range(1, 30 + 1): # Assuming 30 Monte Carlo runs
                    files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_{run}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

coarse_code = []
fine_code = []
cir_temp = []
volt_sup = []
proc_cor = []
outp_volt = []
min_pwr = []
max_pwr = []
avg_pwr = []

coarse_code2 = []
fine_code2 = []
cir_temp2 = []
volt_sup2 = []
proc_cor2 = []
outp_volt2 = []
min_pwr2 = []
max_pwr2 = []
avg_pwr2 = []

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

    print("process corner:" + process_corner + ", circuit temperature: " + str(circuit_temperature) + " °C, voltage supply: " + str(voltage_supply) + " V")

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
    volt_sup.append(voltage_supply)
    proc_cor.append(process_corner)

    delay = 2400 # in number of data points, which corresponds to 2.4 micro seconds (us) after v(swbrn3) first reaches VDD V, which is approximately the time when the output voltage stabilizes after the step response

    # append the value of v(vout) when v(swbrn3) first reaches VDD V to y list
    idx = df[df["v(swbrn3)"] >= 0.99*df["v(vdd)"]].index[delay] if not df[df["v(swbrn3)"] >= 0.99*df["v(vdd)"]].empty else None
    outp_volt2.append(df.loc[idx, "v(vout)"] if idx is not None else None)
    cir_temp2.append(circuit_temperature)
    coarse_code2.append(df.loc[idx, "v(dec_coarse_step_counter)"] if idx is not None else None)
    fine_code2.append(df.loc[idx, "v(dec_finetuning_duty_cycle)"] if idx is not None else None)
    min_pwr2.append((df["pwr"]).min())
    max_pwr2.append((df["pwr"]).max())
    avg_pwr2.append((df["pwr"]).mean())
    volt_sup2.append(voltage_supply)
    proc_cor2.append(process_corner)

df1 = pd.DataFrame({"Temperature (°C)": cir_temp, "Output voltage (V)": outp_volt, "Coarse code": coarse_code, "Fine code": fine_code, "Minimum power (uW)": min_pwr, "Maximum power (uW)": max_pwr, "Average power (uW)": avg_pwr, "Voltage supply (V)": volt_sup, "Process corner": proc_cor}).sort_values(by="Temperature (°C)")
df1.to_csv(f"figures/{'_'.join(args)}_stepping_{stepping_direction}_df1.csv", index=False)

df2 = pd.DataFrame({"Temperature (°C)": cir_temp2, "Output voltage (V)": outp_volt2, "Coarse code": coarse_code2, "Fine code": fine_code2, "Minimum power (uW)": min_pwr2, "Maximum power (uW)": max_pwr2, "Average power (uW)": avg_pwr2, "Voltage supply (V)": volt_sup2, "Process corner": proc_cor2}).sort_values(by="Temperature (°C)")
df2.to_csv(f"figures/{'_'.join(args)}_stepping_{stepping_direction}_df2.csv", index=False)
