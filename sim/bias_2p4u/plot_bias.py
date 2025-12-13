import pandas as pd
import yaml
import matplotlib.pyplot as plt
import sys

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

if len(args) == 0 or all(arg not in ["typical", "etc", "mc", "sch", "lay", "Sch", "Lay"] for arg in args):
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
fig.suptitle('Bias Currents Comparison  (target 2.4 uA)', fontsize=16)

fig_bias, ax_bias = plt.subplots(1,1, figsize=(5, 4))
fig_idd, ax_idd = plt.subplots(1,1)
fig_comb, ax_comb = plt.subplots(1,1)

for file in files:
    fname = file + fend
    # print(f"Processing file: {fname}")
    df = pd.read_csv(fname, sep='\s+')

    df['time'] = df['time'] * 1e9 # in ns

    # print(df.columns)
    # print(df.head())

    labelname = fname.split('/')[-1].replace(fend, '')

    axs['top_left'].plot(df['time'], df['ibias']*1e6, label=f'{labelname}, ibias') # in uA
    ax_bias.plot(df['time'], df['ibias']*1e6, label=f'{labelname}, ibias') # in uA
    # ax_bias.plot(df['time'], df['v(sleep)'], label=f'{labelname}, i(sleep)') # dont plot
    print(f"Plotted ibias for {labelname}: {df['ibias'].iloc[10]*1e6} uA")

    line_color = axs['top_left'].lines[-1].get_color()

    axs['bottom_left'].plot(df['time'], -df['i(vdd)']/2*1e6, color=line_color, linestyle='--', label=f'{labelname}, i(vdd)/2') # in uA
    ax_idd.plot(df['time'], -df['i(vdd)']/2*1e6, color=line_color, linestyle='--', label=f'{labelname}, i(vdd)/2') # in uA

    axs['right'].plot(df['time'], df['ibias']*1e6, color=line_color, label=f'{labelname}, ibias') # in uA
    axs['right'].plot(df['time'], -df['i(vdd)']/2*1e6, color=line_color, linestyle='--', label=f'{labelname}, i(vdd)/2') # in uA
    ax_comb.plot(df['time'], df['ibias']*1e6, color=line_color, label=f'{labelname}, ibias') # in uA
    ax_comb.plot(df['time'], -df['i(vdd)']/2*1e6, color=line_color, linestyle='--', label=f'{labelname}, i(vdd)/2') # in uA

for ax in axs.values():
    ax.set(xlabel='Time (ns)', ylabel='Current (uA)')
    ax.grid()

axs['top_left'].set_title("Bias Current Comparison")
axs['bottom_left'].set_title("Bias Current Comparison (half of measured VDD current)")
axs['right'].set_title("Bias Current Comparison (Both methods)")

axs['right'].legend(fontsize='small')


fig.tight_layout()

image_path = f"./figures/plot_bias_{view}_{'_'.join(args)}.png"
fig.savefig(image_path)
print("Figure saved to " + image_path)

# ax_bias.sharey(ax_idd)
# ax_idd.sharey(ax_comb)

ax_bias.set_title("Bias Current Comparison", fontsize=16)
ax_idd.set_title("Bias Current Comparison (half of measured VDD current)", fontsize=16)
ax_comb.set_title("Bias Current Comparison (Both methods)", fontsize=16)

ax_bias.set(xlabel='Time (ns)', ylabel='Current (uA)')
ax_bias.grid()

ax_idd.set(xlabel='Time (ns)', ylabel='Current (uA)')
ax_idd.grid()

ax_comb.set(xlabel='Time (ns)', ylabel='Current (uA)')
ax_comb.grid()

ax_bias.legend(fontsize=8, loc='center')
ax_idd.legend(fontsize=8)
ax_comb.legend(fontsize=8)

fig_bias.tight_layout()
fig_idd.tight_layout()
fig_comb.tight_layout()

fig_bias.savefig(f"./figures/plot_bias_ax_bias_{view}_{'_'.join(args)}.png")
fig_idd.savefig(f"./figures/plot_bias_ax_idd_{view}_{'_'.join(args)}.png")
fig_comb.savefig(f"./figures/plot_bias_ax_comb_{view}_{'_'.join(args)}.png")

plt.show()
