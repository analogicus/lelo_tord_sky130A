import pandas as pd
import yaml
import matplotlib.pyplot as plt
import sys
import pickle
import numpy as np

fend = ".out" # File extension for output files, can be changed to ".yaml", ".csv" or others if needed
view = "Sch" # Sets schematic is default view if none is specified
# view = "Lay" # Sets schematic is default view if none is specified

args = sys.argv[1:]

if len(args) == 0 or all(arg not in ["typical", "etc", "mc", "custom"] for arg in args):
    print("Wrong/No arguments provided. Please specify a combination of 'typical', 'etc', 'mc', and 'custom' to plot. View may be specified with 'Sch' or 'Lay' as arguments.")
    sys.exit(1)

for arg in args:
    print(f"Argument {arg} of type: {type(arg)} recieved.")
    if arg in ["Sch", "Lay"]:
        view = arg
        print(f"View set to: {view}")
    elif arg =="sch":
        view = "Sch"
        print(f"View set to: {view}")
    elif arg =="lay":
        view = "Lay"
        print(f"View set to: {view}")

files = []
if "typical" in args:
    files.append(f"output_tran/tran_{view}GtKttTtVt")
if "etc" in args:
    for corner in ["ff", "ss", "sf", "fs"]:
        for temperature in ["Tl", "Th"]:
            for voltage in ["Vl", "Vh"]:
                files.append(f"output_tran/tran_{view}GtK{corner}{temperature}{voltage}")
if "mc" in args:
    for n in range(1, 30):
        files.append(f"output_tran/tran_{view}GtKttmmTtVt_{n}")
if "custom" in args:
    for corner in ["ss"]:
        for temperature in ["Th"]:
            for voltage in ["Vl"]:
                files.append(f"output_tran/tran_{view}GtK{corner}{temperature}{voltage}")

fig_iout, axs_iout = plt.subplots(1, 1, figsize=(7, 6))
fig_iout.suptitle('DAC Output Current')

for file in files:
    fname = file + fend
    print(f"Processing file: {fname}")
    df = pd.read_csv(fname, sep='\s+')

    df['time'] = df['time'] * 1e9 # in ns

    # print(df.columns)
    # print(df.head())
    # print(df.tail())

    name = fname.split('/')[-1].replace(fend, '')

    #
    # Plot DAC output current and calculate average, min, max values
    #

    axs_iout.plot(df['time'], df['i(v.xdut.v1)']*1e6, label=f'{name.split("_")[-1]} iout')

    step_start = 500 # ns
    step_length = 2000 # ns

    # Calculate and plot average output value
    for i, b in enumerate(["b0", "b1", "b2", "b3", "b4", "b5", "b6", "b7"]):      
        print(f'Calculating {name} avg, min and max iout values for {b}...')

        tstart = step_start + i*step_length + 150 # ns
        tstop = step_start + (i+1)*step_length - 150 # ns
        
        avg_iout = np.mean(df[f'i(v.xdut.v1)'][(df['time'] >= tstart) & (df['time'] <= tstop)])*1e6 # in uA
        max_iout = np.max(df[f'i(v.xdut.v1)'][(df['time'] >= tstart) & (df['time'] <= tstop)])*1e6 # in uA
        min_iout = np.min(df[f'i(v.xdut.v1)'][(df['time'] >= tstart) & (df['time'] <= tstop)])*1e6 # in uA
        time_vals = df['time'][(df['time'] >= tstart) & (df['time'] <= tstop)]
        print(f'Max iout value between {tstart} ns and {tstop} ns: {max_iout:.3f} V')
        print(f'Avg iout value between {tstart} ns and {tstop} ns: {avg_iout:.3f} V')
        print(f'Min iout value between {tstart} ns and {tstop} ns: {min_iout:.3f} V')
        # axs_iout.plot(time_vals, [max_iout]*len(time_vals), label=f'max {b}: {max_iout:.3f} V', linestyle=':')
        # line_color2 = axs_iout.lines[-1].get_color()
        # axs_iout.plot(time_vals, [avg_iout]*len(time_vals), label=f'avg {b}: {avg_iout:.3f} V', linestyle='--', color=line_color2)
        # axs_iout.plot(time_vals, [min_iout]*len(time_vals), label=f'min {b}: {min_iout:.3f} V', linestyle='-.', color=line_color2)

    axs_iout.set_xlabel('Time (ns)')
    axs_iout.set_ylabel('Current (uA)')
    axs_iout.legend(bbox_to_anchor=(1.01, 1), loc='upper left')
    axs_iout.grid()
    # axs_iout.set_title("DAC Output Current")
    fig_iout.tight_layout()
    fig_iout.savefig(f"./figures/tb_dac_plot_iout_{view}_{'_'.join(args)}.png")

plt.show() 