import sys
import pandas as pd



args = sys.argv[1:]
tempeartures = [-40, 0, 40, 80, 125]
files = list()
t_high_res = [-40, -39, -38, -37, -36, -35, -34, -33, -32, -31, 
              -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, 
              -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, 
              -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 
              0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
              20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
              30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 
              40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 
              50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
              60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
              70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
              80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
              90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
              100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
            #   110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
            #   120, 121, 122, 123, 124, 125]
stepping_direction = "down"
print(f"Plotting for transient signals stepping {stepping_direction}")

if "highres" in args:
    for corner in ["tt"]:
        for voltage in [1.8]: # Volt (V)
            Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
            for temperature in t_high_res: # Celsius (degree C)
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")


if "ttVt" in args:
    for corner in ["tt"]:
        for voltage in [1.8]: # Volt (V)
            Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
            for temperature in tempeartures: # Celsius (degree C)
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

if "tfs" in args:
    for corner in ["tt"]:
        for voltage in [1.8]: # Volt (V)
            Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
            for temperature in tempeartures: # Celsius (degree C)
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")
    for corner in ["ff"]:
        for voltage in [1.9]: # Volt (V)
            Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
            for temperature in tempeartures: # Celsius (degree C)
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")
    for corner in ["ss"]:
        for voltage in [1.7]: # Volt (V)
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


timestamps = []
coarse_codes = []
fine_codes = []
circuit_temperatures = []
voltage_supplies = []
process_corners = []
output_voltages = []

mean_active_pwr = []
min_active_pwr = []
max_active_pwr = []
sleep_pwr = []

error_voltages = []
feed_voltages = []
start_up_times = []


for file in files:
    print(f"Processing transient results from file: {file}")

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

    df['time'] = df['time'] * 1e6 # in u

    idx = df[df["v(correct_output_found)"] >= 0.99 * 1.8].index[-1] if not df[df["v(correct_output_found)"] >= 0.99 * 1.8].empty else None
    timestamps.append(df["time"][idx] if idx is not None else None)
    pwr_off_idx = df[df["v(slp)"] > 0.90 * 1.8].index[-10] if len(df[df["v(slp)"] > 0.90 * 1.8]) > 10 else 0
    pwr_timestamp = df["time"][pwr_off_idx] if pwr_off_idx is not None else None
    print(f"Sleep power measured at {pwr_timestamp:.2f} us")

    df["verror"] = df["v(bgr.v1)"] - df["v(bgr.v2)"]
    df["vifeed"] = df["v(xdut.ifeed)"] if "v(xdut.ifeed)" in df.columns else df["v(xdut.iout)"]
    df["pwr"] = df["v(vdd)"] * -(df["i(vdd)"]) * 1e6 # in uW (micro Watt)
    df["mov_avg_pwr"] = df["pwr"].rolling(window=100).mean() # moving average filter with window size of 100 applied to the power plot

    mean_active_pwr.append((df["mov_avg_pwr"]).mean())
    min_active_pwr.append((df["mov_avg_pwr"]).min())
    max_active_pwr.append((df["mov_avg_pwr"]).max())

    sleep_pwr.append(df.loc[pwr_off_idx, "mov_avg_pwr"] if pwr_off_idx is not None else None)
    print(f"{(df.loc[pwr_off_idx, 'mov_avg_pwr'] if pwr_off_idx is not None else None)}")

    process_corners.append(process_corner)
    voltage_supplies.append(voltage_supply)
    circuit_temperatures.append(circuit_temperature)

    output_voltages.append(df.loc[idx, "v(vout)"] if idx is not None else None)
    coarse_codes.append(df.loc[idx, "v(dec_coarse_step_counter)"] if idx is not None else None)
    fine_codes.append(df.loc[idx, "v(dec_finetuning_duty_cycle)"] if idx is not None else None)

    error_voltages.append(df.loc[idx, "verror"] if idx is not None else None)
    feed_voltages.append(df.loc[idx, "vifeed"] if idx is not None else None)

    correct_output_found_time = df.loc[df["v(correct_output_found)"] > 0.99*1.8, "time"].max() # in us
    slp_low_time = df.loc[(df["v(slp)"] > 0.99*1.8) & (df["time"] < correct_output_found_time), "time"].max() # in us
    start_up_time = correct_output_found_time - slp_low_time # in us
    print(f"Correct output found at {correct_output_found_time:.2f} us, slp low at {slp_low_time:.2f} us, start-up time is {start_up_time:.2f} us")
    start_up_times.append(start_up_time)

df_out = pd.DataFrame({"Output voltage (V)": output_voltages,
                       "Process corner": process_corners,
                       "Voltage supply (V)": voltage_supplies,
                       "Temperature (°C)": circuit_temperatures,
                       "Coarse code": coarse_codes,
                       "Fine code": fine_codes,
                       "Timestamp (us)": timestamps,
                       "Mean active power (uW)": mean_active_pwr,
                       "Minimum active power (uW)": min_active_pwr,
                       "Maximum active power (uW)": max_active_pwr,
                       "Sleep power (uW)": sleep_pwr,
                       "Error voltage (V)": error_voltages,
                       "Feed voltage (V)": feed_voltages,
                       "Start-up time (us)": start_up_times
                       }).sort_values(by=["Temperature (°C)", "Process corner", "Voltage supply (V)"], ascending=[True, True, True])
df_out.to_csv(f"plotdata/{'_'.join(args)}_stepping_{stepping_direction}.csv", index=False)

