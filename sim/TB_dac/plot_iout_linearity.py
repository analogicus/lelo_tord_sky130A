import pandas as pd
import yaml
import matplotlib.pyplot as plt
import sys
import pickle
import numpy as np
import matplotlib.lines as mlines

freq = 1  # MHz
duty = 65  # %


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

fig, axs = plt.subplots(2, 1, figsize=(5, 4))
fig.suptitle('DAC Output Current')

number_of_linearity_points = 9
tstart = 8000-100 # in ns
tstep = 2000  # in ns

target_times = [tstart + i*tstep for i in range(number_of_linearity_points)] # 62 ns is Tclk and should have been 62.5 ns, but with rise and fall times it might be better to add a bit more
print(f'x = {target_times}')

colors = [
    'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 
    'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan',
    'blue', 'green', 'red', 'gold', 'purple', 
    'navy', 'deeppink', 'yellowgreen', 'peru', 'darkslateblue', 
    'brown', 'maroon', 'olive', 'salmon', 'pink', 
    'dodgerblue', 'indigo', 'aquamarine', 'cadetblue', 'sienna'
]

solid_lines = []

i=0

for file in files:
    fname = file + fend
    print(f"Processing file: {fname}")
    df = pd.read_csv(fname, sep='\s+')

    df['time'] = df['time'] * 1e9 # in ns

    # print(df.columns)
    # print(df.head())
    # print(df.tail())

    name = fname.split('/')[-1].replace(fend, '')

    target_times_idx = []
    for t in target_times:
      print(f'Finding closest time to {t} ns...')
      target_times_idx.append((df['time'] - t).abs().idxmin())
      print(f'Closest time to {t} ns is {df["time"][target_times_idx[-1]]} ns at index {target_times_idx[-1]}')

    labelname = fname.split('_')[-1].replace(fend, '')

    x = np.array(range(number_of_linearity_points))

    y = df.loc[target_times_idx]['i(v.xdut.v1)']*1e6 # in uA

    line_color = colors[i]
    i += 1
    if i >= len(colors):
        i = 0

    axs[0].plot(x, y, marker='o', linestyle='solid', label=f'{labelname}', color=line_color)
    last_color = axs[0].lines[-1].get_color()

    solid_line_iout = mlines.Line2D([], [], color=last_color, linestyle='solid', marker='o', label=labelname)
    solid_lines.append(solid_line_iout)

    coeffs = np.polyfit(x, y, 1)
    a, b = coeffs
    y_fit = a*x + b

    axs[0].plot(x, y_fit, linestyle='dotted', color=last_color)

    inl_fit = y - y_fit

    axs[1].plot(x, inl_fit, marker='v', linestyle='dotted', color=last_color, label='INL (best-fit)')
    
    max_inl_fit = np.max(np.abs(inl_fit))

    rms_inl_fit = np.sqrt(np.mean(inl_fit**2))

    y_mean = np.mean(y)
    ss_tot = np.sum((y - y_mean)**2)
    ss_res = np.sum((y - y_fit)**2)
    r_squared = 1 - ss_res/ss_tot

    if labelname.endswith("GtKttTtVt"): # If file is typical case, print the results
        print(f"File: {labelname}")
        print(f"Max INL (best-fit):  {max_inl_fit}")
        print(f"RMS INL (best-fit):  {rms_inl_fit}")
        print(f"R^2 (fit) = {r_squared:.6f}")

        axs[0].text(x=0.5, y=0.01, s=f'R^2 of best fit line: {r_squared:.6f}\n(when in typical corner)', transform=axs[0].transAxes, fontsize=8, verticalalignment='bottom', horizontalalignment='center')
        axs[1].text(x=0.5, y=0.01, s=f'Max err.: {max_inl_fit:.6f}\nRMS err.: {rms_inl_fit:.6f}\n(when in typical corner)', transform=axs[1].transAxes, fontsize=8, verticalalignment='bottom', horizontalalignment='center')
    
black_dotted_line = mlines.Line2D([], [], color='black', linestyle='dotted', label='best fit')
handles = solid_lines
handles.append(black_dotted_line)
labels = [h.get_label() for h in handles]
axs[0].legend(handles, labels, ncol=3)

handles = []
black_dotted_line = mlines.Line2D([], [], color='black', linestyle='dotted', marker='v', label='best fit')
handles.append(black_dotted_line)
labels = [h.get_label() for h in handles]

axs[1].legend(handles, labels)

axs[0].set_xlabel('DAC Input Code')
axs[0].set_ylabel('Current [uA]')
axs[0].set_title(f'Output Current {freq} MHz, {duty} % Duty Cycle')
 
# axs[0].legend(ncol=2)
axs[0].grid()
axs[1].set_xlabel('DAC Input Code')
axs[1].set_ylabel('Error [uA]')
axs[1].set_title('Error from Best-Fit Line')
# axs[1].legend()
axs[1].grid()

fig.tight_layout()

image_path = f"./figures/tb_dac_plot_iout_linearity_{view}_{'_'.join(args)}"
fig.savefig(image_path + ".png")
print("Figure saved to " + image_path + ".png")

# with open(f"{image_path}.fig.pickle", 'wb') as file:
#     pickle.dump(fig, file)
# print("Figure pickled to " + image_path + ".fig.pickle")

plt.show()