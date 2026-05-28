import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats   
from spicelib import RawRead


def extract_temeratures_and_resistances(files=["output_tran/tran_SchGtKttTtVt"]):

    ts = list()
    rs  = list()

    for file in files:
        print(f"Now processing file: {file}.raw")

        rawfile = RawRead(file + ".raw")
        
        vdd = rawfile.get_trace("v(vdd)").get_wave()[-1]
        idd = rawfile.get_trace("i(vdd)").get_wave()[-1]

        idd = -idd # flips the sign of the current from negative to positive

        ts.append(float(file.split("_")[-1].replace("celsius", "")))
        rs.append(vdd / idd)

    return ts, rs


args = sys.argv[1:]
view = "Sch" # Sets schematic as default view if noen is specified

resistance_specified = 7535 # in Ohm
temperatures = [-40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]

if "tt" in args:
    fig_r = plt.figure(dpi=300, figsize=(4,4))
    ax_r = fig_r.add_subplot(1, 1, 1)
    ax_r.set_title('_'.join(args), fontsize=10, fontweight="bold")

    files = []
    for temperature in temperatures:
        files.append(f"output_tran/tran_{view}GtKttTtVt_{temperature}celsius")
    ts, rs = extract_temeratures_and_resistances(files)

    slope, intercept, r_value, p_value, standard_error = stats.linregress(ts, rs)
    linear_fit = slope * np.array(ts) + intercept

    ax_r.plot(ts, rs, label=f"tran_{view}GtKffTtVt")
    last_color = ax_r.get_lines()[-1].get_color()
    ax_r.plot(ts, linear_fit, linestyle="dashed", color=last_color, label=f"Lin. fit: {slope:.2f} Ω/°C + {intercept:.1f} Ω,\nR²={r_value**2:.4f}")
    
    ax_r.plot(ts, [resistance_specified] * len(ts), linestyle="dotted", color="black", label=f"Spec. res.: {resistance_specified} Ω")

    ax_r.set_xlabel("Temperature (°C)")
    ax_r.set_ylabel("Resistance (Ω)")
    ax_r.legend(loc="best", fontsize=9)
    ax_r.grid(True)

    fig_r.tight_layout()
    fig_r.savefig(f"figures/{'_'.join(args)}_r_vs_t.png", dpi=300)

    plt.close("all")

if "ss" in args:
    fig_r = plt.figure(dpi=300, figsize=(4,4))
    ax_r = fig_r.add_subplot(1, 1, 1)
    ax_r.set_title('_'.join(args), fontsize=10, fontweight="bold")

    files = []
    for temperature in temperatures:
        files.append(f"output_tran/tran_{view}GtKttTtVt_{temperature}celsius")
    ts, rs = extract_temeratures_and_resistances(files)

    for voltage in ["Vl", "Vt", "Vh"]:
        files = []
        for temperature in temperatures:
            files.append(f"output_tran/tran_{view}GtKssTt{voltage}_{temperature}celsius")
        ts, rs = extract_temeratures_and_resistances(files)

        slope, intercept, r_value, p_value, standard_error = stats.linregress(ts, rs)
        linear_fit = slope * np.array(ts) + intercept

        ax_r.plot(ts, rs, label=f"tran_{view}GtKssTt{voltage}")
        last_color = ax_r.get_lines()[-1].get_color()
        ax_r.plot(ts, linear_fit, linestyle="dashed", color=last_color, label=f"Lin. fit: {slope:.2f} Ω/°C + {intercept:.1f} Ω,\nR²={r_value**2:.4f}")
    
    ax_r.plot(ts, [resistance_specified] * len(ts), linestyle="dotted", color="black", label=f"Spec. res.: {resistance_specified} Ω")

    ax_r.set_xlabel("Temperature (°C)")
    ax_r.set_ylabel("Resistance (Ω)")
    ax_r.legend(loc="best", fontsize=9)
    ax_r.grid(True)

    fig_r.tight_layout()
    fig_r.savefig(f"figures/{'_'.join(args)}_r_vs_t.png", dpi=300)

    plt.close("all")

if "ff" in args:
    fig_r = plt.figure(dpi=300, figsize=(4,4))
    ax_r = fig_r.add_subplot(1, 1, 1)
    ax_r.set_title('_'.join(args), fontsize=10, fontweight="bold")

    for voltage in ["Vl", "Vt","Vh"]:
        files = []
        for temperature in temperatures:
            files.append(f"output_tran/tran_{view}GtKffTt{voltage}_{temperature}celsius")
        ts, rs = extract_temeratures_and_resistances(files)

        slope, intercept, r_value, p_value, standard_error = stats.linregress(ts, rs)
        linear_fit = slope * np.array(ts) + intercept

        ax_r.plot(ts, rs, label=f"tran_{view}GtKffTt{voltage}")
        last_color = ax_r.get_lines()[-1].get_color()
        ax_r.plot(ts, linear_fit, linestyle="dashed", color=last_color, label=f"Lin. fit: {slope:.2f} Ω/°C + {intercept:.1f} Ω,\nR²={r_value**2:.4f}")
    
    ax_r.plot(ts, [resistance_specified] * len(ts), linestyle="dotted", color="black", label=f"Spec. res.: {resistance_specified} Ω")

    ax_r.set_xlabel("Temperature (°C)")
    ax_r.set_ylabel("Resistance (Ω)")
    ax_r.legend(loc="best", fontsize=9)
    ax_r.grid(True)

    fig_r.tight_layout()
    fig_r.savefig(f"figures/{'_'.join(args)}_r_vs_t.png", dpi=300)

    plt.close("all")

if "sf" in args:
    fig_r = plt.figure(dpi=300, figsize=(4,4))
    ax_r = fig_r.add_subplot(1, 1, 1)
    ax_r.set_title('_'.join(args), fontsize=10, fontweight="bold")

    for voltage in ["Vl", "Vt", "Vh"]:
        files = []
        for temperature in temperatures:
            files.append(f"output_tran/tran_{view}GtKsfTt{voltage}_{temperature}celsius")
        ts, rs = extract_temeratures_and_resistances(files)

        slope, intercept, r_value, p_value, standard_error = stats.linregress(ts, rs)
        linear_fit = slope * np.array(ts) + intercept

        ax_r.plot(ts, rs, label=f"tran_{view}GtKsfTt{voltage}")
        last_color = ax_r.get_lines()[-1].get_color()
        ax_r.plot(ts, linear_fit, linestyle="dashed", color=last_color, label=f"Lin. fit: {slope:.2f} Ω/°C + {intercept:.1f} Ω,\nR²={r_value**2:.4f}")
    
    ax_r.plot(ts, [resistance_specified] * len(ts), linestyle="dotted", color="black", label=f"Spec res.: {resistance_specified} Ω")

    ax_r.set_xlabel("Temperature (°C)")
    ax_r.set_ylabel("Resistance (Ω)")
    ax_r.legend(loc="best", fontsize=9)
    ax_r.grid(True)

    fig_r.tight_layout()
    fig_r.savefig(f"figures/{'_'.join(args)}_r_vs_t.png", dpi=300)

    plt.close("all")

if "fs" in args:
    fig_r = plt.figure(dpi=300, figsize=(4,4))
    ax_r = fig_r.add_subplot(1, 1, 1)
    ax_r.set_title('_'.join(args), fontsize=10, fontweight="bold")

    for voltage in ["Vl", "Vt", "Vh"]:
        files = []
        for temperature in temperatures:
            files.append(f"output_tran/tran_{view}GtKsfTt{voltage}_{temperature}celsius")
        ts, rs = extract_temeratures_and_resistances(files)

        slope, intercept, r_value, p_value, standard_error = stats.linregress(ts, rs)
        linear_fit = slope * np.array(ts) + intercept

        ax_r.plot(ts, rs, label=f"tran_{view}GtKsfTt{voltage}")
        last_color = ax_r.get_lines()[-1].get_color()
        ax_r.plot(ts, linear_fit, linestyle="dashed", color=last_color, label=f"Lin. fit: {slope:.2f} Ω/°C + {intercept:.1f} Ω,\nR²={r_value**2:.4f}")

    slope, intercept, r_value, p_value, standard_error = stats.linregress(ts, rs)
    linear_fit = slope * np.array(ts) + intercept
    
    ax_r.plot(ts, [resistance_specified] * len(ts), linestyle="dotted", color="black", label=f"Spec res.: {resistance_specified} Ω")

    ax_r.set_xlabel("Temperature (°C)")
    ax_r.set_ylabel("Resistance (Ω)")
    ax_r.legend(loc="best", fontsize=9)
    ax_r.grid(True)

    fig_r.tight_layout()
    fig_r.savefig(f"figures/{'_'.join(args)}_r_vs_t.png", dpi=300)

    plt.close("all")

if "Vt" in args:
    fig_r = plt.figure(dpi=300, figsize=(4,4))
    ax_r = fig_r.add_subplot(1, 1, 1)
    ax_r.set_title('_'.join(args), fontsize=10, fontweight="bold")

    for process in ["tt", "ff", "ss", "sf", "fs"]:
        files = []
        for temperature in temperatures:
            files.append(f"output_tran/tran_{view}GtK{process}TtVt_{temperature}celsius")
        ts, rs = extract_temeratures_and_resistances(files)

        slope, intercept, r_value, p_value, standard_error = stats.linregress(ts, rs)
        linear_fit = slope * np.array(ts) + intercept

        ax_r.plot(ts, rs, label=f"tran_{view}GtK{process}TtVt")
        last_color = ax_r.get_lines()[-1].get_color()
        ax_r.plot(ts, linear_fit, linestyle="dashed", color=last_color, label=f"Lin. fit: {slope:.2f} Ω/°C + {intercept:.1f} Ω,\nR²={r_value**2:.4f}")
    
    ax_r.plot(ts, [resistance_specified] * len(ts), linestyle="dotted", color="black", label=f"Spec. res.: {resistance_specified} Ω")

    ax_r.set_xlabel("Temperature (°C)")
    ax_r.set_ylabel("Resistance (Ω)")
    ax_r.legend(loc="best", fontsize=9)
    ax_r.grid(True)

    fig_r.tight_layout()
    fig_r.savefig(f"figures/{'_'.join(args)}_r_vs_t.png", dpi=300)

    plt.close("all")

if "Vl" in args:
    fig_r = plt.figure(dpi=300, figsize=(4,4))
    ax_r = fig_r.add_subplot(1, 1, 1)
    ax_r.set_title('_'.join(args), fontsize=10, fontweight="bold")

    for process in ["tt", "ff", "ss", "sf", "fs"]:
        files = []
        for temperature in temperatures:
            files.append(f"output_tran/tran_{view}GtK{process}TtVl_{temperature}celsius")
        ts, rs = extract_temeratures_and_resistances(files)

        slope, intercept, r_value, p_value, standard_error = stats.linregress(ts, rs)
        linear_fit = slope * np.array(ts) + intercept

        ax_r.plot(ts, rs, label=f"tran_{view}GtK{process}TtVl")
        last_color = ax_r.get_lines()[-1].get_color()
        ax_r.plot(ts, linear_fit, linestyle="dashed", color=last_color, label=f"Lin. fit: {slope:.2f} Ω/°C + {intercept:.1f} Ω,\nR²={r_value**2:.4f}")
    
    ax_r.plot(ts, [resistance_specified] * len(ts), linestyle="dotted", color="black", label=f"Spec. res.: {resistance_specified} Ω")

    ax_r.set_xlabel("Temperature (°C)")
    ax_r.set_ylabel("Resistance (Ω)")
    ax_r.legend(loc="best", fontsize=9)
    ax_r.grid(True)

    fig_r.tight_layout()
    fig_r.savefig(f"figures/{'_'.join(args)}_r_vs_t.png", dpi=300)

    plt.close("all")

if "Vh" in args:
    fig_r = plt.figure(dpi=300, figsize=(4,4))
    ax_r = fig_r.add_subplot(1, 1, 1)
    ax_r.set_title('_'.join(args), fontsize=10, fontweight="bold")

    for process in ["tt", "ff", "ss", "sf", "fs"]:
        files = []
        for temperature in temperatures:
            files.append(f"output_tran/tran_{view}GtK{process}TtVh_{temperature}celsius")
        ts, rs = extract_temeratures_and_resistances(files)

        slope, intercept, r_value, p_value, standard_error = stats.linregress(ts, rs)
        linear_fit = slope * np.array(ts) + intercept

        ax_r.plot(ts, rs, label=f"tran_{view}GtK{process}TtVh")
        last_color = ax_r.get_lines()[-1].get_color()
        ax_r.plot(ts, linear_fit, linestyle="dashed", color=last_color, label=f"Lin. fit: {slope:.2f} Ω/°C + {intercept:.1f} Ω,\nR²={r_value**2:.4f}")
    
    ax_r.plot(ts, [resistance_specified] * len(ts), linestyle="dotted", color="black", label=f"Spec. res.: {resistance_specified} Ω")

    ax_r.set_xlabel("Temperature (°C)")
    ax_r.set_ylabel("Resistance (Ω)")
    ax_r.legend(loc="best", fontsize=9)
    ax_r.grid(True)

    fig_r.tight_layout()
    fig_r.savefig(f"figures/{'_'.join(args)}_r_vs_t.png", dpi=300)

    plt.close("all")

if "mc" in args:
    runs = 50
    bin_count = 7
    distribution_temperature = 0


    #
    # Plot mean resistance and standard deviation across temperatures
    #

    fig_tran = plt.figure(dpi=300)
    ax_tran = fig_tran.add_subplot(1, 1, 1)
    ax_tran.set_title(f"Montecarlo mean resistance and standard deviation after {runs} runs")

    tts = list()
    rrs = list()

    for run in range(1, runs+1):

        files = []
        for temperature in temperatures:
            files.append(f"output_tran/tran_{view}GtKttmmTtVt_{run}_{temperature}celsius")
        ts, rs = extract_temeratures_and_resistances(files)

        tts.append(ts)
        rrs.append(rs)

    rrs_array = np.array(rrs)  # shape: (runs, len(temperatures))
    mean_r = np.mean(rrs_array, axis=0)
    std_r  = np.std(rrs_array, axis=0)

    ax_tran.plot(ts, mean_r, color="steelblue", label="Mean resistance")
    ax_tran.fill_between(ts, mean_r - std_r, mean_r + std_r, alpha=0.15, color="steelblue", label="±1σ band")

    ax_tran.plot(ts, [resistance_specified] * len(ts), linestyle="dotted", color="black", label=f"Spec. res.: {resistance_specified} Ω")

    ax_tran.set_xlabel("Temperature (°C)")
    ax_tran.set_ylabel("Resistance (Ω)")
    ax_tran.legend(loc="best")
    ax_tran.grid(True)

    fig_tran.tight_layout()
    fig_tran.savefig(f"figures/mc_transient_resistance_vs_temperature.png", dpi=300)


    #
    # Find the distribution of resistances at 0 degrees temperature
    # 

    files = []
    for run in range(1, runs+1):
        files.append(f"output_tran/tran_{view}GtKttmmTtVt_{run}_{distribution_temperature}celsius")
    ts, rs = extract_temeratures_and_resistances(files)

    rs_array = np.array(rs)
    
    mean_r = np.mean(rs_array)
    std_r  = np.std(rs_array)
    
    print(f"mean resistance at {distribution_temperature} °C after {runs} runs: {mean_r} Ω")
    print(f"standard error at {distribution_temperature} °C after {runs} runs: {std_r}")

    within_1sigma = np.sum(np.abs(rs_array - mean_r) <= std_r)
    pct_1sigma = within_1sigma / len(rs_array) * 100
    
    print(f"Values within ±1σ: {within_1sigma} of {len(rs_array)} ({pct_1sigma:.1f}%) — normal distribution expects 68.3%")

    fig_dist = plt.figure(dpi=300)
    ax_dist = fig_dist.add_subplot(1, 1, 1)
    ax_dist.set_title(f"Montecarlo distribution at {distribution_temperature}°C after {runs} runs")

    sns.histplot(rs, bins=bin_count, kde=True, color="steelblue", edgecolor="black", ax=ax_dist)
    sns.rugplot(rs, height=0.1, color="blue", ax=ax_dist)

    ax_dist.axvline(mean_r, linestyle="dashed", color="black", label=f"μ = {mean_r:.2f} Ω")
    ax_dist.axvline(resistance_specified, linestyle="dotted", color="black", label=f"Sch. spec.: {resistance_specified} Ω")

    fig_dist.gca().set_axisbelow(True)
        
    # Fill after seaborn has set the y-limits
    ymin, ymax = ax_dist.get_ylim()
    ax_dist.fill_between(
        [mean_r - std_r, mean_r + std_r],
        ymin, ymax,
        alpha=0.2,
        color="black",
        label=f"μ ± σ = μ ± {std_r:.2f} Ω\nValues within ±1σ:\n{within_1sigma} of {len(rs_array)} ({pct_1sigma:.1f}%) "
    )
    ax_dist.set_ylim(ymin, ymax)  # re-apply so fill_between doesn't expand the axis

    ax_dist.set_xlabel("Resistance (Ω)")
    ax_dist.legend(loc="best")
    ax_dist.grid(True)

    fig_dist.tight_layout()
    fig_dist.savefig(f"figures/mc_distribution_at_{distribution_temperature}_degrees_celsius.png")

    plt.show()
