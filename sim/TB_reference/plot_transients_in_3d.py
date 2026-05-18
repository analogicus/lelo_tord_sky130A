import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

arguments = sys.argv[1:]

stepping_direction = ""
if "up" in arguments:
    stepping_direction = "up"
    print("Plotting for transient signals stepping upwards")
else: 
    stepping_direction = "down"
    print("Plotting for transient signals stepping downwards")

files = list()

if len(arguments) == 0:
    print("No arguments provided. Plotting for typical corner, voltage (1.8 Volt) and temperature (27 Celsius).")
    files.append("output_tran/tran_SchGtKttTtVt_stepping_" + stepping_direction + "_0celsius_1.8volt.out")

if "typical" in arguments:
    for corner in ["tt"]:
        for temperature in [125, 25, -40]: # Celsius (degree C)
                for voltage in [1.8]: # Volt (V)
                    Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                    files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

if "slow" in arguments:
    for corner in ["ss"]:
        for temperature in [125, 25, -40]: # Celsius (degree C)
            for voltage in [1.7]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

if "fast" in arguments:
    for corner in ["ff"]:
        for temperature in [125, 25, -40]: # Celsius (degree C)
            for voltage in [1.9]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

number_of_runs = 1

if "montecarlo" in arguments:
    for corner in ["ttmm"]:
        for temperature in [125, 25, -40]: # Celsius (degree C)
            for voltage in [1.8]: # Volt (V)
                Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                for run in range(1, number_of_runs + 1):
                    files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_{run}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

# fig, axs = plt.subplots(2, 2, subplot_kw={'projection': '3d'})
# ax_v = axs[0]
# ax_a = axs[1]
# ax_c = axs[2]
# ax_p = axs[3]

fig = plt.figure(dpi=300)
ax_v = fig.add_subplot(2, 2, 1, projection='3d') # voltage plots
ax_a = fig.add_subplot(2, 2, 2, projection='3d') # additional plots
# ax_i = fig.add_subplot(5, 1, 2, projection='3d') # current plots
ax_c = fig.add_subplot(2, 2, 3, projection='3d') # counter plots
ax_p = fig.add_subplot(2, 2, 4, projection='3d') # power plots

for file in files:

    print(f"Plotting Vout transient results from file: {file}")

    figure_name = file.split("/")[-1].split(".out")[0]
    
    # PVT variations corner
    process = figure_name.split("GtK")[-1].split("Tt")[0] # Process corner in shorthand notation (tt/ss/ff/sf/fs)
    voltage = float(figure_name.split("_")[-1].replace("volt", "")) # Voltage corner in Volt
    temperature = float(figure_name.split("_")[-2].replace("celsius", "")) # Temperature corner in degrees Celsius

    if "montecarlo" in arguments:
        run = int(figure_name.split("_")[1].replace("celsius", "")) # in degrees Celsius
    else: 
        run = None

    if process == "tt":
        process_corner = "Typical"
    elif process == "ss":
        process_corner = "Slow-Slow"
    elif process == "ff":
        process_corner = "Fast-Fast"
    elif process == "sf":
        process_corner = "Slow-Fast"
    elif process == "fs":
        process_corner = "Fast-Slow"
    else:
        process_corner = "Oops, something is wrong!"

    print(f"Process: {process}, voltage: {voltage}, temperature: {temperature}")
    
    df = pd.read_csv(file, sep="\s+")

    df['time'] = df['time'] * 1e6 # in us
    df["power"] = df["v(vdd)"] * -(df["i(vdd)"]) * 1e6 # in uW

    df["fine"] = df["v(dec_coarse_step_counter)"] * 1e3 # in whole numbers, not parts of thousand
    df["coarse"] = df["v(dec_finetuning_duty_cycle)"] * 1e3 # in whole numbers, not parts of thousand
    
    df["moving_average_power"] = df["power"].rolling(window=100).mean()
    df["filtered_average_power"] = df.loc[df['moving_average_power'] < 0.025, 'moving_average_power']

    ax_v.plot(df["time"], df["v(bgr.v1)"], zs=temperature, zdir="y", color="tab:blue")
    ax_v.plot(df["time"], df["v(bgr.v2)"], zs=temperature, zdir="y", color="tab:orange")
    ax_v.plot(df["time"], df["v(vout)"], zs=temperature, zdir="y", color="tab:green")
    ax_v.plot(df["time"], df["v(correct_output_found)"], zs=temperature, zdir="y", color="tab:red")

    ax_a.plot(df["time"], df["v(clk)"], zs=temperature, zdir="y", color="tab:blue")
    ax_a.plot(df["time"], df["v(b0)"], zs=temperature, zdir="y", color="tab:orange")
    ax_a.plot(df["time"], df["v(dac.vctl)"], zs=temperature, zdir="y", color="tab:green")
    ax_a.plot(df["time"], df["v(cmp_async)"], zs=temperature, zdir="y", color="tab:red")
    ax_a.plot(df["time"], df["v(rst)"], zs=temperature, zdir="y", color="tab:purple")
    ax_a.plot(df["time"], df["v(slp)"], zs=temperature, zdir="y", color="tab:cyan")

    ax_c.plot(df["time"], df["fine"], label="v(dec_finetuning_duty_cycle)", zs=temperature, zdir="y", color="tab:blue")
    ax_c.plot(df["time"], df["coarse"], label="v(dec_coarse_step_counter)",  zs=temperature, zdir="y", color="tab:orange")

    ax_p.plot(df["time"], df["moving_average_power"], zs=temperature, zdir="y", color="tab:blue")
    ax_p.plot(df["time"], df["filtered_average_power"], zs=temperature, zdir="y", color="tab:orange")


ax_v.view_init(elev=20, azim=-30)
ax_a.view_init(elev=20, azim=-30)
# ax_i.view_init(elev=20, azim=-30)
ax_c.view_init(elev=20, azim=-30)
ax_p.view_init(elev=20, azim=-30)

ax_v.set_zlabel("Voltage (V)")
ax_v.legend(["v1", "v2", "vout", "out_en"], loc="lower left", bbox_to_anchor=(-0.1, 0.8), ncols=2)

ax_a.set_zlabel("Voltage (V)")
ax_a.legend(["clk", "b0", "vctl", "cmp", "rst", "slp"], loc="lower left", bbox_to_anchor=(-0.1, 0.8), ncols=2)

ax_c.set_xlabel('Time (us)')
ax_c.set_ylabel('Temperature (°C)')
ax_c.set_zlabel("Count")
ax_c.legend(["fine", "coarse"], loc="lower left", bbox_to_anchor=(-0.1, 0.8), ncols=2)

ax_p.set_xlabel('Time (us)')
ax_p.set_ylabel('Temperature (°C)')
ax_p.set_zlabel('Power (uW)')
ax_p.legend(["power", "sleeping power"], loc="lower left", bbox_to_anchor=(-0.1, 0.8), ncols=2)

fig.savefig("../../media/simulations_matrix_visualized.png")
plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # 1. Setup Data
# x = np.linspace(0, 10, 100)
# # Create 5 different curves
# data_sets = [np.sin(x + i) for i in range(5)] 

# # 2. Setup 3D Figure
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')

# # 3. Loop and Plot
# for i, y in enumerate(data_sets):
#     # i is the Z-dimension (the "stack" axis)
#     # x is the X-axis
#     # y is the 2D data (Y-axis)
#     ax.plot(x, y, zs=i, zdir='y', label=f'Set {i}')

# # 4. Final Touches
# ax.set_xlabel('X Axis')
# ax.set_ylabel('Y Axis')
# ax.set_zlabel('Stack Dimension (Z)')
# plt.legend()
# plt.show()