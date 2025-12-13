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

if len(args) == 0 or all(arg not in ["typical", "etc", "mc"] for arg in args):
    print("Wrong/No arguments provided. Please specify a combination of 'typical', 'etc', and 'mc' to plot. View may be specified with 'Sch' or 'Lay' as arguments.")
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

fig, axs = plt.subplot_mosaic([['top_left', 'top_right'],
                               ['bottom_left', 'bottom_right']],
                                sharex=True,
                                figsize=(8, 4))
fig.suptitle('DAC Output Comparison', fontsize=18)

for file in files:
    fname = file + fend
    print(f"Processing file: {fname}")
    df = pd.read_csv(fname, sep='\s+')

    df['time'] = df['time'] * 1e9 # in ns

    # print(df.columns)
    # print(df.head())
    # print(df.tail())

    labelname = fname.split('/')[-1].replace(fend, '')

    axs['top_left'].plot(df['time'], df['v(vout1)'], label=f'{labelname}', linestyle='solid')
    line_color = axs['top_left'].lines[-1].get_color()
    axs['bottom_left'].plot(df['time'], df['v(vout1)'], color=line_color, linestyle='solid')
    axs['top_left'].plot(df['time'], df['v(vout2)'], color=line_color, linestyle='dashed')
    axs['top_right'].plot(df['time'], df['v(vout2)'], color=line_color, linestyle='dashed')
    axs['top_left'].plot(df['time'], df['v(vout3)'], color=line_color, linestyle='dotted')
    axs['bottom_right'].plot(df['time'], df['v(vout3)'], color=line_color, linestyle='dotted')

    if file == f"output_tran/tran_{view}GtKttTtVt":
        
        step_start = 500 # ns
        step_length = 2000 # ns

        # Calculate and plot average output value
        for ax in axs.values():
            for i, b in enumerate(["b0", "b1", "b2", "b3", "b4", "b5", "b6", "b7"]):
                
                if ax == axs['bottom_left']:
                    vout = 'vout1'
                elif ax == axs['top_right']:
                    vout = 'vout2'
                elif ax == axs['bottom_right']:
                    vout = 'vout3'
                else:
                    vout = None

                print(f'Calculating average {vout} output values for {b}...')

                tstart = step_start + i*step_length + 150 # ns
                tstop = step_start + (i+1)*step_length - 150 # ns
                
                if vout == 'vout1' or vout == 'vout2' or vout == 'vout3':
                    avg_ctl = np.mean(df[f'v({vout})'][(df['time'] >= tstart) & (df['time'] <= tstop)])
                    max_ctl = np.max(df[f'v({vout})'][(df['time'] >= tstart) & (df['time'] <= tstop)])
                    min_ctl = np.min(df[f'v({vout})'][(df['time'] >= tstart) & (df['time'] <= tstop)])
                    time_vals = df['time'][(df['time'] >= tstart) & (df['time'] <= tstop)]
                    print(f'Max ouptut value between {tstart} ns and {tstop} ns: {max_ctl:.3f} V')
                    print(f'Avg output value between {tstart} ns and {tstop} ns: {avg_ctl:.3f} V')
                    print(f'Min output value between {tstart} ns and {tstop} ns: {min_ctl:.3f} V')
                    ax.plot(time_vals, [max_ctl]*len(time_vals), label=f'max {b}: {max_ctl:.3f} V', linestyle=':')
                    line_color2 = ax.lines[-1].get_color()
                    ax.plot(time_vals, [avg_ctl]*len(time_vals), label=f'avg {b}: {avg_ctl:.3f} V', linestyle='--', color=line_color2)
                    ax.plot(time_vals, [min_ctl]*len(time_vals), label=f'min {b}: {min_ctl:.3f} V', linestyle='-.', color=line_color2)

for ax in axs.values():
    ax.set_ylabel('Voltage (V)')
    ax.grid()

axs['bottom_left'].set_xlabel('Time (ns)')
axs['bottom_right'].set_xlabel('Time (ns)')

axs['top_left'].set_title("All DAC Output Voltages Compared")
axs['bottom_left'].set_title("DAC Output Voltage over diode connected BJT")
axs['top_right'].set_title("DAC Output Voltage over small resistor")
axs['bottom_right'].set_title("DAC Output Voltage over large resistor")

axs['top_left'].legend(fontsize='small')
axs['bottom_left'].legend(fontsize='small')
axs['top_right'].legend(fontsize='small')
axs['bottom_right'].legend(fontsize='small')

fig.tight_layout()

image_path = f"./figures/plot_tb_dac_{view}_{'_'.join(args)}"
fig.savefig(image_path + ".png")
print("Figure saved to " + image_path + ".png")

# with open(f"{image_path}.fig.pickle", 'wb') as file:
#     pickle.dump(fig, file)
# print("Figure pickled to " + image_path + ".fig.pickle")

# with open(f"{image_path_ideal}.fig.pickle", 'wb') as file:  
#     pickle.dump(fig_videal, file)
# print("Figure pickled to " + image_path_ideal + ".fig.pickle") 

plt.show()

