import pandas as pd
import yaml
import matplotlib.pyplot as plt
import sys
import pickle

fend = ".out" # File extension for output files, can be changed to ".yaml", ".csv" or others if needed
view = "Sch" # Sets schematic is default view if none is specified
# view = "Lay" # Sets schematic is default view if none is specified

args = sys.argv[1:]

for arg in args:
    print(f"Argument {arg} of type: {type(arg)} recieved.")
    if arg in ["Sch", "Lay"]:
        view = arg
        print(f"View set to: {view}")
    elif arg in ["sch"]:
        view = "Sch"
        print(f"View set to: {view}")
    elif arg in ["lay"]:
        view = "Lay"
        print(f"View set to: {view}")

if len(args) == 0 or all(arg not in ["typical", "etc", "mc"] for arg in args):
    print("Wrong/No arguments provided. Please specify a combination of 'typical', 'etc', and 'mc' to be plotted.")
    sys.exit(1)

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
                                figsize=(12, 12))
fig.suptitle('DAC Currents Comparison')

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

for ax in axs.values():
    ax.set_ylabel('Voltage (V)')
    ax.grid()

axs['bottom_left'].set_xlabel('Time (ns)')
axs['bottom_right'].set_xlabel('Time (ns)')

axs['top_left'].set_title("DAC Output Voltages Comparison")
axs['bottom_left'].set_title("DAC1 Output Voltage over transistor")
axs['top_right'].set_title("DAC2 Output Voltage over small resistor")
axs['bottom_right'].set_title("DAC3 Output Voltage over large resistor")

axs['top_left'].legend(fontsize='small')

# fig.tight_layout()

image_path = f"./figures/plot_{view}_{'_'.join(args)}_tb_dac"
fig.savefig(image_path + ".png")
print("Figure saved to " + image_path + ".png")

with open(f"{image_path}.fig.pickle", 'wb') as file:
    pickle.dump(fig, file)
print("Figure pickled to " + image_path + ".fig.pickle")

plt.show()

