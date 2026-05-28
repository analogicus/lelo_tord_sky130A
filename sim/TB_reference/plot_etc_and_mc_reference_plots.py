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
                
                t = temperature
                v = df.loc[idx, "v(vout)"] if idx is not None else None
                
                ts.append(t)
                vs.append(v)

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
    figvhl.savefig(f"figures/etc_vhl_{stepping_direction}.png")
    figvh.tight_layout()
    figvh.savefig(f"figures/etc_vh_{stepping_direction}.png")
    figvl.tight_layout()
    figvl.savefig(f"figures/etc_vl_{stepping_direction}.png")

    plt.show()



if "mc" in args:

    runs = 300
    bin_count = 7
    distribution_temperature = 0


    #
    # Plot mean resistance and standard deviation across temperatures
    #

    fig_tran = plt.figure(dpi=300)
    ax_tran = fig_tran.add_subplot(1, 1, 1)
    ax_tran.set_title(f"Mean reference voltage and standard deviation after {runs} runs")

    tss = list()
    vss = list()

    for run in range(0, runs):
        ts = []
        vs = []

        for temperature in [-40, 0, 40, 80, 125]:

            if run == 0:
                file = f"output_tran/tran_{view}GtKttmmTtVt_stepping_{stepping_direction}_{temperature}celsius_1.8volt.out"
            else:
                file = f"output_tran/tran_{view}GtK{process_corner}Tt{voltage_corner}_{run}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out"
            
            print(f"Now processing {file}")

            df = pd.read_csv(file, sep="\s+")
            idx = df[df["v(correct_output_found)"] >= 0.99 * 1.8].index[-1] if not df[df["v(correct_output_found)"] >= 0.99 * 1.8].empty else None
            
            t = temperature
            v = df.loc[idx, "v(vout)"] if idx is not None else None
            
            ts.append(t)
            vs.append(v)

        # ax_tran.plot(ts, vs, marker="o", label=f"run no. {run}")

    tss.append(ts)
    vss.append(vs)

    vss_array = np.array(vss)  # shape: (runs, len(temperatures))
    mean_v = np.mean(vss_array, axis=0)
    std_v  = np.std(vss_array, axis=0)

    ax_tran.plot(ts, mean_v, color="steelblue", label="Mean resistance")
    ax_tran.fill_between(ts, mean_v - std_v, mean_v + std_v, alpha=0.15, color="steelblue", label="±1σ band")
    
    ax_tran.grid(True)
    ax_tran.legend(loc="best")
    ax_tran.set_xlabel("Voltage (V)")
    fig_tran.tight_layout()
    fig_tran.savefig(f"figures/mc_tran_{stepping_direction}.png")


    #
    # Find the distribution of resistances at x degrees Celsius
    # 

    for run in range(0, runs):

        ts = []
        vs = []

        if run == 0:
            file = f"output_tran/tran_{view}GtKttmmTtVt_{distribution_temperature}celsius"
        else:
            file = f"output_tran/tran_{view}GtKttmmTtVt_{run}_{distribution_temperature}celsius"
    
        print(f"Now processing {file}")

        df = pd.read_csv(file, sep="\s+")
        idx = df[df["v(correct_output_found)"] >= 0.99 * 1.8].index[-1] if not df[df["v(correct_output_found)"] >= 0.99 * 1.8].empty else None
        
        t = temperature
        v = df.loc[idx, "v(vout)"] if idx is not None else None
        
        ts.append(t)
        vs.append(v)

    vs_array = np.array(vs)
    
    mean_v = np.mean(vs_array)
    std_v  = np.std(vs_array)

    within_1sigma = np.sum(np.abs(vs_array - mean_v) <= std_v)
    pct_1sigma = within_1sigma / len(vs_array) * 100
    
    print(f"mean resistance at {temperature} °C after {runs} runs: {mean_v} Ω")
    print(f"standard error at {temperature} °C after {runs} runs: {std_v}")    
    print(f"Values within ±1σ: {within_1sigma} of {len(vs_array)} ({pct_1sigma:.1f}%) — normal distribution expects 68.3%")

    fig_dist = plt.figure(dpi=300)
    ax_dist = fig_dist.add_subplot(1, 1, 1)
    ax_dist.set_title(f"MC distribution at {distribution_temperature}°C after {runs} runs")

    sns.histplot(vs, bins=bin_count, kde=True, color="steelblue", edgecolor="black", ax=ax_dist)
    sns.rugplot(vs, height=0.1, color="blue", ax=ax_dist)

    ax_dist.axvline(mean_v, linestyle="dashed", color="black", label=f"μ = {mean_v:.2f} Ω")

    ax_dist.grid(True)
    fig_dist.gca().set_axisbelow(True)
        
    # Fill after seaborn has set the y-limits
    ymin, ymax = ax_dist.get_ylim()
    ax_dist.fill_between(
        [mean_v - std_v, mean_v + std_v],
        ymin, ymax,
        alpha=0.2,
        color="black",
        label=f"μ ± σ = μ ± {std_v:.2f} Ω\nValues within ±1σ:\n{within_1sigma} of {len(vs_array)} ({pct_1sigma:.1f}%) "
    )
    ax_dist.set_ylim(ymin, ymax)  # re-apply so fill_between doesn't expand the axis

    ax_dist.legend(loc="best")
    ax_dist.set_xlabel("Voltage (V)")
    fig_dist.tight_layout()
    fig_dist.savefig(f"figures/mc_dist_{stepping_direction}.png")

    plt.show()
