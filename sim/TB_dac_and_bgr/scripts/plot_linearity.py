import pandas as pd
import yaml
import matplotlib.pyplot as plt
import sys
import pickle
import numpy as np
import matplotlib.lines as mlines
from matplotlib.patches import Rectangle

fend = ".out" # File extension for output files, can be changed to ".yaml", ".csv" or others if needed
view = "Sch" # Sets schematic is default view if none is specified
# view = "Lay" # Sets schematic is default view if none is specified
number_of_linearity_points = 8

args = sys.argv[1:]

fits = []

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
    elif arg in ["bestfit", "endpoints"]:
        fits.append(arg)
        print(f"Linearization method '{arg}' added to fits.")

if len(args) == 0 or all(arg not in ["typical", "etc", "mc"] for arg in args):
    print("Wrong/No arguments provided. Please specify a combination of 'typical', 'etc', and 'mc' to be plotted.")
    sys.exit(1)

if all(arg not in ["bestfit", "endpoints"] for arg in args):
    fits = ['bestfit']
    print("No linearization method provided. Assumes best fit.")

colors = [
    'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 
    'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan',
    'blue', 'green', 'red', 'gold', 'purple', 
    'navy', 'deeppink', 'yellowgreen', 'peru', 'darkslateblue', 
    'brown', 'maroon', 'olive', 'salmon', 'pink', 
    'dodgerblue', 'indigo', 'aquamarine', 'cadetblue', 'sienna'
]

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

fig, axs = plt.subplot_mosaic([['top_left', 'top_middle', 'top_right'], 
                               ['bottom_left', 'bottom_middle', 'bottom_right']],
                                sharex=True, figsize=(18, 10))
fig.suptitle('DAC Linearity', fontsize=16)

target_times = [2400 + i*2000 for i in range(number_of_linearity_points)] # 62 ns is Tclk and should have been 62.5 ns, but with rise and fall times it might be better to add a bit more
print(f'x = {target_times}')

axs_list1 = [axs['top_left'], axs['top_middle'], axs['top_right']]
axs_list2 = [axs['bottom_left'], axs['bottom_middle'], axs['bottom_right']]

solid_lines = []

i=0
for file in files:

    fname = file + fend
    print(f"Processing file: {fname}")
    df = pd.read_csv(fname, sep='\s+')

    df['time'] = df['time'] * 1e9 # in ns

    # print(df.columns)
    print(df.head())
    print(df.tail())

    # target_times_idx = [df.index[df['time'] == xi][0] for xi in target_times]

    # determine target times indices with tolerance
    target_times_idx = []
    tolerance = 50e-6*1e9  # small tolerance to account for floating point precision
    print(tolerance)
    for xi in target_times:
        idx = df.index[(df['time'] >= xi - tolerance) & (df['time'] <= xi + tolerance)]
        if not idx.empty:
            target_times_idx.append(idx[0])
        else:
            raise ValueError(f"Time value {xi} ns not found in the data.")
        
    print(f'target_times_idx = {target_times_idx}')


    labelname = fname.split('_')[-1].replace(fend, '')

    if labelname.endswith("Vt"):
        VDD = 1.8
    elif labelname.endswith("Vh"):
        VDD = 1.9
    elif labelname.endswith("Vl"):
        VDD = 1.7
    else:
        VDD = 1.8
        print("Warning: Voltage corner not recognized, assuming VDD = 1.8V")

    x = np.array(range(number_of_linearity_points))

    y1 = df.loc[target_times_idx]['v(vout1)']/VDD
    y2 = df.loc[target_times_idx]['v(vout2)']/VDD
    y3 = df.loc[target_times_idx]['v(vout3)']/VDD

    line_color = colors[i]
    i += 1
    if i >= len(colors):
        i = 0

    axs['top_left'].plot(x, y1, marker='o', color=line_color, linestyle='solid', label=labelname)
    last_color = axs['top_left'].lines[-1].get_color()
    solid_line = mlines.Line2D([], [], color=last_color, linestyle='solid', marker='o', label=labelname)
    solid_lines.append(solid_line)
    axs['top_middle'].plot(x, y2, marker='o', linestyle='solid', color=last_color)
    axs['top_right'].plot(x, y3, marker='o', linestyle='solid', color=last_color)

    ys = [y1, y2, y3]
    
    for yi, axi1, axi2 in zip(ys, axs_list1, axs_list2):
    
        y_ep_start = yi.iloc[0]
        y_ep_end   = yi.iloc[-1]
        y_ep = y_ep_start + (y_ep_end - y_ep_start) * (x - x[0]) / (x[-1] - x[0])
        
        if 'endpoints' in fits:
            axi1.plot(x, y_ep, linestyle='dashed', color=last_color)

        coeffs = np.polyfit(x, yi, 1)
        a, b = coeffs
        y_fit = a*x + b

        if 'bestfit' in fits:
            axi1.plot(x, y_fit, linestyle='dotted', color=last_color)

        inl_ep = yi - y_ep
        inl_fit = yi - y_fit

        if 'endpoints' in fits:
            axi2.plot(x, inl_ep, marker='s', linestyle='dashed', color=last_color, label='INL (end-point)')
        if 'bestfit' in fits:
            axi2.plot(x, inl_fit, marker='v', linestyle='dotted', color=last_color, label='INL (best-fit)')
        
        max_inl_ep  = np.max(np.abs(inl_ep))
        max_inl_fit = np.max(np.abs(inl_fit))

        rms_inl_ep  = np.sqrt(np.mean(inl_ep**2))
        rms_inl_fit = np.sqrt(np.mean(inl_fit**2))

        y_mean = np.mean(yi)
        ss_tot = np.sum((yi - y_mean)**2)
        ss_res = np.sum((yi - y_fit)**2)
        r_squared = 1 - ss_res/ss_tot

        if labelname.endswith("GtKttTtVt"): # If file is typical case, print the results
            print(f"File: {labelname}")
            print(f"Max INL (end-point): {max_inl_ep}")
            print(f"RMS INL (end-point): {rms_inl_ep}")
            print(f"Max INL (best-fit):  {max_inl_fit}")
            print(f"RMS INL (best-fit):  {rms_inl_fit}")
            print(f"R^2 (fit) = {r_squared:.6f}")

            axi1.text(x=0.5, y=0.01, s=f'R^2 of best fit line: {r_squared:.6f}\n(when in typical corner)', transform=axi1.transAxes, fontsize=8, verticalalignment='bottom', horizontalalignment='center')
            axi2.text(x=0.5, y=0.01, s=f'Max INL (ep): {max_inl_ep:.6f}\nRMS INL (ep): {rms_inl_ep:.6f}\nMax INL (bf): {max_inl_fit:.6f}\nRMS INL (bf): {rms_inl_fit:.6f}\n(when in typical corner)', transform=axi2.transAxes, fontsize=8, verticalalignment='bottom', horizontalalignment='center')

if 'endpoints' in fits:
    black_dashed_line = mlines.Line2D([], [], color='black', linestyle='dashed', label='end points')
if 'bestfit' in fits:
    black_dotted_line = mlines.Line2D([], [], color='black', linestyle='dotted', label='best fit')

handles = solid_lines
if 'endpoints' in fits:
    handles.append(black_dashed_line)
if 'bestfit' in fits:
    handles.append(black_dotted_line)
labels = [h.get_label() for h in handles]

for ax in axs_list1:
    ax.legend(handles, labels, ncol=3)

if 'endpoints' in fits:
    black_dashed_line = mlines.Line2D([], [], color='black', linestyle='dashed', marker='s', label='end points')
if 'bestfit' in fits:
    black_dotted_line = mlines.Line2D([], [], color='black', linestyle='dotted', marker='v', label='best fit')

handles = []
if 'endpoints' in fits:
    handles.append(black_dashed_line)
if 'bestfit' in fits:
    handles.append(black_dotted_line)
labels = [h.get_label() for h in handles]

for ax in axs_list2:
    ax.legend(handles, labels)

for ax in axs_list1:
    ax.set_xlabel('DAC Input Code')
    ax.set_ylabel('Vout/VDD')
    ax.set_title('DAC Transfer Characteristics')
    # ax.legend(ncol=2)
    ax.grid()

for ax in axs_list2:
    ax.set_xlabel('DAC Input Code')
    ax.set_ylabel('Error (Vout/VDD)')
    ax.set_title('INL Plots')
    # ax.legend()
    ax.grid()

fig.tight_layout()

image_path = f"./figures/linearity_plot_{view}_{'_'.join(args)}_tb_dac"
fig.savefig(image_path + ".png")
print("Figure saved to " + image_path + ".png")

# with open(f"{image_path}.fig.pickle", 'wb') as file:
#     pickle.dump(fig, file)
# print("Figure pickled to " + image_path + ".fig.pickle")

plt.show()