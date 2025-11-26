import pandas as pd
import yaml
import matplotlib.pyplot as plt
import sys
import pickle
import numpy as np

fend = ".out" # File extension for output files, can be changed to ".yaml", ".csv" or others if needed
view = "Sch" # Sets schematic is default view if none is specified
# view = "Lay" # Sets schematic is default view if none is specified
number_of_linearity_points = 9

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

fig, axs = plt.subplot_mosaic([['top_left', 'top_middle', 'top_right'], 
                               ['bottom_left', 'bottom_middle', 'bottom_right']],
                                sharex=True, figsize=(12, 8))
fig.suptitle('DAC Linearity')

target_times = [8500 + i*62 for i in range(number_of_linearity_points)] # 62 ns is Tclk and should have been 62.5 ns, but with rise and fall times it might be better to add a bit more
print(f'x = {target_times}')

for file in files:
    fname = file + fend
    print(f"Processing file: {fname}")
    df = pd.read_csv(fname, sep='\s+')

    df['time'] = df['time'] * 1e9 # in ns

    # print(df.columns)
    # print(df.head())
    # print(df.tail())

    target_times_idx = [df.index[df['time'] == xi][0] for xi in target_times]
    print(f'target_times_idx = {target_times_idx}')

    labelname = fname.split('/')[-1].replace(fend, '')

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

    axs['top_left'].plot(x, y1, marker='o', linestyle='solid', label='vout1 levels')
    line_color = axs['top_left'].lines[-1].get_color()
    axs['top_middle'].plot(x, y2, marker='o', linestyle='solid', color=line_color, label='vout2 levels')
    axs['top_right'].plot(x, y3, marker='o', linestyle='solid', color=line_color, label='vout3 levels')

    ys = [y1, y2, y3]
    axs_list1 = [axs['top_left'], axs['top_middle'], axs['top_right']]
    axs_list2 = [axs['bottom_left'], axs['bottom_middle'], axs['bottom_right']]

    for yi, axi1, axi2 in zip(ys, axs_list1, axs_list2):
    
        y_ep_start = yi.iloc[0]
        y_ep_end   = yi.iloc[-1]

        y_ep = y_ep_start + (y_ep_end - y_ep_start) * (x - x[0]) / (x[-1] - x[0])
        axi1.plot(x, y_ep, linestyle='dashed', color=line_color, label='end points linear trend')

        coeffs = np.polyfit(x, yi, 1)
        a, b = coeffs
        y_fit = a*x + b

        axi1.plot(x, y_fit, linestyle='dotted', color=line_color, label='best fit linear trend')

        inl_ep = yi - y_ep
        inl_fit = yi - y_fit

        axi2.plot(x, inl_ep, marker='s', linestyle='dashed', color=line_color, label='INL (end-point)')
        axi2.plot(x, inl_fit, marker='v', linestyle='dotted', color=line_color, label='INL (best-fit)')
        
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

            axi1.text(x=0.5, y=0.5, s=f'Max INL (end-point): {max_inl_ep:.4f}\nRMS INL (end-point): {rms_inl_ep:.4f}\nMax INL (best-fit): {max_inl_fit:.4f}\nRMS INL (best-fit): {rms_inl_fit:.4f}\nR² (best fit): {r_squared:.6f}\nin typical corner', transform=axi1.transAxes, fontsize=8, verticalalignment='center', horizontalalignment='center')
    
for ax in axs_list1:
    ax.set_xlabel('DAC Input Code')
    ax.set_ylabel('Voltage (Vout/VDD)')
    ax.legend()
    ax.grid()

for ax in axs_list2:
    ax.set_xlabel('DAC Input Code')
    ax.set_ylabel('INL (Vout/VDD)')
    ax.legend()
    ax.grid()

# fig.tight_layout()

image_path = f"./figures/linearity_plot_{view}_{'_'.join(args)}_tb_dac"
fig.savefig(image_path + ".png")
print("Figure saved to " + image_path + ".png")

# with open(f"{image_path}.fig.pickle", 'wb') as file:
#     pickle.dump(fig, file)
# print("Figure pickled to " + image_path + ".fig.pickle")

plt.show()