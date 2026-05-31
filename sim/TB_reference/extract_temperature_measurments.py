import sys
import pandas as pd



args = sys.argv[1:]
tempeartures = [-40, 0, 40, 80, 125]
files = list()

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


if "ttVt" in args:
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

    df['time'] = df['time'] * 1e9 # in ns

    idx = df[df["v(correct_output_found)"] >= 0.99 * 1.8].index[-1] if not df[df["v(correct_output_found)"] >= 0.99 * 1.8].empty else None
    timestamps.append(df["time"][idx] if idx is not None else None)
    pwr_off_idx = df[df["v(slp)"] > 0.90 * 1.8].index[-10] if len(df[df["v(slp)"] > 0.90 * 1.8]) > 10 else 0
    pwr_timestamp = df["time"][pwr_off_idx] if pwr_off_idx is not None else None
    print(f"Sleep power measured at {pwr_timestamp:.2f} ns")

    df["verror"] = df["v(bgr.v1)"] - df["v(bgr.v2)"]
    df["vifeed"] = df["v(xdut.ifeed)"]
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

df_out = pd.DataFrame({"Output voltage (V)": output_voltages,
                       "Process corner": process_corners,
                       "Voltage supply (V)": voltage_supplies,
                       "Temperature (°C)": circuit_temperatures,
                       "Coarse code": coarse_codes,
                       "Fine code": fine_codes,
                       "Timestamp (ns)": timestamps,
                       "Mean active power (uW)": mean_active_pwr,
                       "Minimum active power (uW)": min_active_pwr,
                       "Maximum active power (uW)": max_active_pwr,
                       "Sleep power (uW)": sleep_pwr,
                       "Error voltage (V)": error_voltages,
                       "Feed voltage (V)": feed_voltages
                       }).sort_values(by=["Temperature (°C)", "Process corner", "Voltage supply (V)"], ascending=[True, True, True])
df_out.to_csv(f"plot_data/{'_'.join(args)}_stepping_{stepping_direction}.csv", index=False)

