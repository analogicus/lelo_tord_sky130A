import pandas as pd
import yaml
import matplotlib.pyplot as plt
import sys

fig_width = 3
fig_height = 3
font_size = 10
title_fontsize = font_size + 2
label_fontsize = font_size
legend_fontsize = font_size
ticks_fontsize = font_size

fend = ".out" # File extension for output files, can be changed to ".yaml", ".csv" or others if needed
view = "Sch" # Sets schematic as default view if noen is specified
# view = "Lay" # Sets layout as default view if noen is specified

args = sys.argv[1:]

if len(args) == 0 or all(arg not in ["typical", "etc", "mc"] for arg in args):
    print("Wrong/No arguments provided. Please specify a combination of 'typical', 'etc', and 'mc' to be plotted.")
    sys.exit(1)

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

fig, axs = plt.subplot_mosaic([['idd', 'ref', 'bias', 'comb']], 
                                figsize=(16, 8))
fig.suptitle('Bias Currents Comparison (target 1.2 uA)', fontsize=title_fontsize)
axs['idd'].set_title('half of supply current')
axs['ref'].set_title('calculated over unit resistor')
axs['bias'].set_title('calculated over total resistance')
axs['comb'].set_title('combined plots')

fig_idd, ax_idd = plt.subplots(1, 1, figsize=(fig_width, fig_height), dpi=300)  
ax_idd.set_title('supply current halfed')
fig_ref, ax_ref = plt.subplots(1, 1, figsize=(fig_width, fig_height), dpi=300)
ax_ref.set_title('calculated over unit resistor')
fig_bias, ax_bias = plt.subplots(1, 1, figsize=(fig_width, fig_height), dpi=300)
ax_bias.set_title('calculated over total resistance')
fig_comb, ax_comb = plt.subplots(1, 1, figsize=(fig_width, fig_height), dpi=300)
ax_comb.set_title('combined plots')

for file in files:
    fname = file + fend
    print(f"Processing file: {fname}")
    df = pd.read_csv(fname, sep='\s+')

    df['i(vss)'] = -df['i(vss)'] * 1e6 # in uA
    df['i(vdd)'] = -df['i(vdd)'] * 1e6 # in uA
    df['iref'] = df['iref'] * 1e6 # in uA
    df['ibias'] = df['ibias'] * 1e6 # in uA

    df['time'] = df['time'] * 1e9 # in ns

    # print(df.columns)
    # print(df.head())

    labelname = file.split('/')[-1]

    axs['idd'].plot(df['time'], (df['i(vdd)']/2), label=f'{labelname}', linestyle='solid')
    axs['ref'].plot(df['time'], df['iref'], label=f'{labelname}', linestyle='dashed')
    axs['bias'].plot(df['time'], df['ibias'], label=f'{labelname}', linestyle='dotted')
    
    line_color = axs['ref'].lines[-1].get_color()

    axs['comb'].plot(df['time'], (df['i(vdd)']/2), color=line_color, linestyle='solid', label=f'{labelname}')
    axs['comb'].plot(df['time'], df['iref'], color=line_color, linestyle='dashed')
    axs['comb'].plot(df['time'], df['ibias'], color=line_color, linestyle='dotted')

    ax_idd.plot(df['time'], (df['i(vdd)']/2), label=f'{labelname}', linestyle='solid')
    ax_ref.plot(df['time'], df['iref'], label=f'{labelname}', linestyle='dashed')
    ax_bias.plot(df['time'], df['ibias'], label=f'{labelname}', linestyle='dotted')
    
    line_color = axs['ref'].lines[-1].get_color()

    ax_comb.plot(df['time'], (df['i(vdd)']/2), color=line_color, linestyle='solid', label=f'{labelname}')
    ax_comb.plot(df['time'], df['iref'], color=line_color, linestyle='dashed')
    ax_comb.plot(df['time'], df['ibias'], color=line_color, linestyle='dotted')

for ax in axs.values():
    ax.set_xlabel("Time (ns)", fontsize=10)
    ax.set_ylabel("Current (uA)", fontsize=10)
    ax.tick_params(axis='both', which='major', labelsize=10)
    ax.legend(fontsize=10)
    ax.grid()
    ax.set_ylim(-0.1, 2.6)

for ax in [ax_idd, ax_ref, ax_bias, ax_comb]:
    ax.set_xlabel("Time (ns)", fontsize=label_fontsize)
    ax.set_ylabel("Current (uA)", fontsize=label_fontsize)
    ax.tick_params(axis='both', which='major', labelsize=ticks_fontsize)
    # ax.legend(fontsize=legend_fontsize)
    ax.grid()
    ax.set_ylim(-0.1, 2.6)

fig.tight_layout()
fig_idd.tight_layout()
fig_ref.tight_layout()
fig_bias.tight_layout()
fig_comb.tight_layout()

image_path = f"./figures/plot_bias_{'_'.join(args)}.png"
plt.savefig(image_path)
print("Figure saved to " + image_path)

plt.show()
