import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats   


args = sys.argv[1:]
view = "Sch" # Sets schematic as default view if noen is specified
files = list()


if len(args) == 0:
    print("No arguments provided.")

stepping_direction = ""
if "up" in args:
    args.remove("up")
    stepping_direction = "up"
    print("Setting step direction upwards")
else: 
    stepping_direction = "down"
    print("Setting step direction downwards")


figure_width = 4
figure_height = 4
font_size = 6
title_font_size = font_size
label_font_size = font_size
legend_font_size = font_size
ticks_font_size = font_size


if "etc" in args:

    figvhl = plt.figure(dpi=300, figsize=(figure_width, figure_height))
    axvhl = figvhl.add_subplot(1, 1, 1)
    axvhl.set_title("Corner lot")

    figvl = plt.figure(dpi=300, figsize=(figure_width, figure_height))
    axvl = figvl.add_subplot(1, 1, 1)
    axvl.set_title("Corner lot, low voltage supply (Vl)")

    figvh = plt.figure(dpi=300, figsize=(figure_width, figure_height))
    axvh = figvh.add_subplot(1, 1, 1)
    axvh.set_title("Corner lot, high voltage supply (Vl)")

    for process_corner in ["ff", "ss", "sf", "fs"]:

        for voltage in [1.7, 1.9]: # Volt (V)

            voltage_corner = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"

            ts = []
            vs = []

            for temperature in [-40, 0, 40, 80, 125]:
                file = f"output_tran/tran_{view}GtK{process_corner}Tt{voltage_corner}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out"
                print(f"Now processing {file}")

                df = pd.read_csv(file, sep="\s+")
                idx = df[df["v(correct_output_found)"] >= 0.99 * 1.8].index[-1] if not df[df["v(correct_output_found)"] >= 0.99 * 1.8].empty else None

                df["pwr"] = df["v(vdd)"] * -(df["i(vdd)"]) * 1e6 # in uW
                df["moving_avg_pwr"] = df["pwr"].rolling(window=100).mean() # moving average filter with window size of 100 applied to the power plot
                df["filtered_pwr"] = df.loc[df['moving_avg_pwr'] < 0.050, 'moving_avg_pwr'] # moving average filter with window size of 100 applied to the power plot, but only for the datapoints where v(slp) is above 0.99 * VDD
                
                t = temperature

                min_pwr = ((df["moving_avg_pwr"]).min())
                avg_pwr = ((df["moving_avg_pwr"]).mean())
                max_pwr = ((df["moving_avg_pwr"]).max())
                min_slp_pwr = ((df["filtered_pwr"]).min())
                avg_slp_pwr = ((df["filtered_pwr"]).mean())
                max_slp_pwr = ((df["filtered_pwr"]).max())
                
                ts.append(t)

                vs.append(min)

            axvhl.plot(ts, vs, marker="o", label=f"{process_corner}, {voltage_corner}")

            if voltage_corner == "Vh":
                axvh.plot(ts, vs, marker="o", label=f"{process_corner}")
            elif voltage_corner == "Vl":
                axvl.plot(ts, vs, marker="o", label=f"{process_corner}")
    
    for ax in {axvh, axvl, axvhl}:
        ax.set_xlabel("Temperature (°C)")
        ax.set_ylabel("Voltage (V)")
        ax.legend(loc="best")
        ax.grid(True)

    figvhl.tight_layout()
    figvhl.savefig("figures/etc_vhl.png")
    figvh.tight_layout()
    figvh.savefig("figures/etc_vh.png")
    figvl.tight_layout()
    figvl.savefig("figures/etc_vl.png")

    plt.show()