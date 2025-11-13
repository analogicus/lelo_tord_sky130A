import pandas as pd
import yaml
import matplotlib.pyplot as plt
import sys

fend = ".out" # File extension for output files, can be changed to ".yaml", ".csv" or others if needed
view = "Sch" # Sets schematic is default view if noen is specified
# view = "Lay" # Sets schematic is default view if noen is specified

args = sys.argv[1:]

for arg in args:
    print(f"Argument {arg} of type: {type(arg)} recieved.")
    if arg in ["Sch", "Lay"]:
        view = arg
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

fig, axs = plt.subplot_mosaic([['top_left', 'right'],
                                ['bottom_left', 'right']],
                                figsize=(12, 12))
fig.suptitle('Bias Currents Comparison', fontsize=16)

for file in files:
    fname = file + fend
    print(f"Processing file: {fname}")
    df = pd.read_csv(fname, sep='\s+')

    df['time'] = df['time'] * 1e9 # in ns

    # print(df.columns)
    # print(df.head())

    labelname = fname.split('/')[-1].replace(fend, '')

    axs['top_left'].plot(df['time'], df['ibias1']*1e6, label=f'{labelname}, ibias1') # in uA

    line_color = axs['top_left'].lines[-1].get_color()

    axs['bottom_left'].plot(df['time'], df['ibias3']*1e6, color=line_color, linestyle='--', label=f'{labelname}, ibias3') # in uA
    
    axs['right'].plot(df['time'], df['ibias1']*1e6, color=line_color, label=f'{labelname}, ibias1') # in uA
    axs['right'].plot(df['time'], df['ibias3']*1e6, color=line_color, linestyle='--', label=f'{labelname}, ibias3') # in uA

for ax in axs.values():
    ax.set(xlabel='Time (ns)', ylabel='Current (uA)')
    ax.grid()

axs['top_left'].set_title("Bias Current Comparison (1st calculation method)")
axs['bottom_left'].set_title("Bias Current Comparison (2nd calculation method)")
axs['right'].set_title("Bias Current Comparison (Both calculations methods)")

axs['right'].legend(fontsize='small')


fig.tight_layout()

image_path = "./figures/plot_bias.png"
plt.savefig(image_path)
print("Figure saved to " + image_path)

plt.show()
