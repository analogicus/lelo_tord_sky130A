import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

fig_width = 4
fig_height = 3
font_size = 8
title_fontsize = font_size + 2
label_fontsize = font_size
legend_fontsize = 3
ticks_fontsize = font_size

fend = ".out" # File extension for output files, can be changed to ".yaml", ".csv" or others if needed
# view = "Sch" # Sets schematic as default view if noen is specified
view = "Lay" # Sets layout as default view if noen is specified

mc_runs = 30
num_of_bins = 5

args = [arg.lower() for arg in sys.argv[1:]]

if len(args) == 0 or all(arg not in ["typical", "etc", "mc"] for arg in args):
    print("Wrong/No arguments provided. Please specify a combination of 'typical', 'etc', and 'mc' to be plotted and/or specify circuit view.")
    sys.exit(1)

for arg in args:
    if arg in ["sch"]:
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
    for n in range(1, mc_runs + 1):
        files.append(f"output_tran/tran_{view}GtKttmmTtVt_{n}")

fig, axs = plt.subplot_mosaic([["gain_vv"], ["gain_db"]], figsize=(fig_width, fig_height), dpi=300)
fig.suptitle(f"Gain - AC sims: {', '.join(args)}", fontsize=title_fontsize)

gains_vv = dict()
gains_db = dict()

for file in files:

    fname = file + "_ac" + fend
    print(f"Processing file: {fname}")
    df = pd.read_csv(fname, sep='\s+')

    df["frequency"] = df["frequency"] * 1e-3 # in kHz
    df["gain_vv"] = df["vm(vout)"] / df["vm(vip)"] # AC Gain ≈ V(out) / V(in)
    df["gain_db"] = 20 * np.log10(df["gain_vv"])
    df["gain_db_alt"] = df["vdb(vout)"] - df["vdb(vip)"]

    print(df.columns)
    print(df.head())

    labelname = file.split('/')[-1]

    axs["gain_vv"].plot(df["frequency"], df["gain_vv"], label=f"{labelname}")
    line_color = axs["gain_vv"].lines[-1].get_color()
    
    axs["gain_db"].plot(df["frequency"], df["gain_db"], label=f"{labelname}", color=line_color, linestyle="solid")

    gains_vv[labelname] = np.max(df["gain_vv"])
    gains_db[labelname] = np.max(df["gain_db"])

print(f"-----------------------------------------------------------")
print(f"Maximum gains across PVT variations: {gains_vv} V/V")
print(f"Highest maximum gain: {np.max(list(gains_vv.values()))} V/V")
print(f"Minimum maximum gain: {np.min(list(gains_vv.values()))} V/V")
print(f"Mean of the maximum gains: {np.mean(list(gains_vv.values()))} V/V")  
print(f"-----------------------------------------------------------")
print(f"Mean gains across PVT variations: {gains_db} dB")
print(f"Highest maximum gain: {np.max(list(gains_db.values()))} dB")
print(f"Lowest maximum gain: {np.min(list(gains_db.values()))} dB")
print(f"Mean of the maximum gains: {np.mean(list(gains_db.values()))} dB")  
print(f"-----------------------------------------------------------")


for ax in axs.values():
    ax.tick_params(axis="both", labelsize=ticks_fontsize)
    ax.grid()
    ax.set_xscale('log')

    if ax is axs["gain_vv"]:
        ax.legend(loc="best", fontsize=legend_fontsize, bbox_to_anchor=(1.05, 1.05), ncol=2)
    elif ax is not axs["gain_db"]:
        ax.legend(loc="best", fontsize=legend_fontsize)

axs["gain_vv"].set_ylabel("Gain (V/V)", fontsize=label_fontsize)
axs["gain_db"].set_ylabel("Gain (dB)", fontsize=label_fontsize)
axs["gain_db"].set_xlabel("Frequency (kHz)", fontsize=label_fontsize)


fig_hist, ax_hist= plt.subplots(1, 1, figsize=(fig_width, fig_height), dpi=300)
ax_hist.set_title(f"Gain histogram: {', '.join(args)}")

if "mm" in fname:
    label_add_on =  f"MC runs={mc_runs}, bins={num_of_bins}"
else: 
    label_add_on = ""

sns.histplot(gains_db, bins=5, kde=True, color="red", edgecolor="black", label=f"{label_add_on}")
sns.rugplot(gains_db, height=0.1, color="red")
plt.grid(True)
plt.gca().set_axisbelow(True)

if "mm" in fname:
    ax_hist.legend()

ax_hist.tick_params(axis="both", which="major", labelsize=ticks_fontsize)


image_path = f"./figures/plot_gains_{view}_{'_'.join(args)}"

fig.tight_layout()
fig.savefig(image_path + ".png", bbox_inches="tight", dpi=300)

fig_hist.tight_layout()
fig_hist.savefig(image_path + "_histogram.png", bbox_inches="tight", dpi=300)

print("Figures saved to " + image_path + "...")

plt.show()

plt.close("all")