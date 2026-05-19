import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats   
from spicelib import RawRead


arguments = sys.argv[1:]

case = arguments[0] if len(arguments) > 0 else "typical"
sleep_signal = arguments[1] if len(arguments) > 1 else "low"
view = arguments[2] if len(arguments) > 2 else "Sch"

temperatures = [-40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 
                15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 
                70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]

runs = 30
bin_count = 7

single_temperature = 25 # room temperature = 27°C ≈ 25°C Ω
target_current = 1.2 # in uA

if case == "typical":

    file = f"output_tran/tran_{view}GtKttTtVt_{single_temperature}celsius_sleep_{sleep_signal}.raw"
    name = file.split("/")[-1].replace(".raw", "")
    raw = RawRead(file)

    print(f"Now processing {file}")

    time = raw.get_axis() * 1e9 # in ns

    idd = -(raw.get_trace("i(vdd)").get_wave() * 1e6) # in uA with positive sign
    iss = -(raw.get_trace("i(vss)").get_wave() * 1e6) # in uA with positive sign
    ir5 = -(raw.get_trace("i(@r.xdut.x11.xxa1.xr1_0.rhead[i])").get_wave() * 1e6) # in uA with positive sign
    id = (raw.get_trace("i(@m.xdut.x8.xm1.msky130_fd_pr__pfet_01v8[id])").get_wave() * 1e6) # in uA with positive sign

    slp = raw.get_trace("v(slp)").get_wave()
    slp_n = raw.get_trace("v(slp_n)").get_wave()
    vbn = raw.get_trace("v(vbn)").get_wave()
    vbp = raw.get_trace("v(vbp)").get_wave()
    vdd = raw.get_trace("v(vdd)").get_wave()
    vss = raw.get_trace("v(vss)").get_wave()
    vr1 = raw.get_trace("v(xdut.vr1)").get_wave()
    vr2 = raw.get_trace("v(xdut.vr2)").get_wave()
    vr3 = raw.get_trace("v(xdut.vr3)").get_wave()
    vr4 = raw.get_trace("v(xdut.vr4)").get_wave()
    vr5 = raw.get_trace("v(xdut.vr5)").get_wave()
    vr6 = raw.get_trace("v(xdut.vr6)").get_wave()
    vr7 = raw.get_trace("v(xdut.vr7)").get_wave()

    fig, axs = plt.subplots(2, 2, sharex=True, dpi=300)
    fig.suptitle(f"Bias currents (target {target_current} uA) and voltages at {single_temperature}°C\nin the all typical corner with sleep signal set to {sleep_signal}")

    axs[0,0].plot(time, (idd/2), label=f"i(vdd)/2 = {idd[-1]/2:.2f} uA")
    axs[0,0].plot(time, ir5, label=f"ires = {ir5[-1]:.2f} uA")
    axs[0,0].plot(time, id, label=f"idrain = {id[-1]:.2f} uA")

    axs[0,1].plot(time, vbn, label=f'vbn = {vbn[-1]:.2f} V')
    axs[0,1].plot(time, vbp, label=f'vbp = {vbp[-1]:.2f} V')

    axs[1,0].plot(time, vr1, label=f'vr1 = {vr1[-1]:.2f} V')
    axs[1,0].plot(time, vr2, label=f'vr2 = {vr2[-1]:.2f} V')
    axs[1,0].plot(time, vr3, label=f'vr3 = {vr3[-1]:.2f} V')
    axs[1,0].plot(time, vr4, label=f'vr4 = {vr4[-1]:.2f} V')
    axs[1,0].plot(time, vr5, label=f'vr5 = {vr5[-1]:.2f} V')
    axs[1,0].plot(time, vr6, label=f'vr6 = {vr6[-1]:.2f} V')
    axs[1,0].plot(time, vr7, label=f'vr7 = {vr7[-1]:.2f} V')

    axs[1,1].plot(time, slp, label=f'slp = {slp[-1]:.2f} V')
    axs[1,1].plot(time, slp_n, label=f'slp_n = {slp_n[-1]:.2f} V')
    
    axs[0,0].set_xlabel("Time (ns)")
    axs[0,0].set_ylabel("Current (uA)")  
    axs[0,0].tick_params(axis='both', which='major')
    axs[0,0].legend()
    axs[0,0].grid()
    axs[0,0].set_ylim(-0.1, 2.6)

    for ax in (axs[0,1], axs[1,0], axs[1,1]):
        ax.set_xlabel("Time (ns)")
        ax.set_ylabel("Voltage (V)")
        ax.legend()
        ax.grid()
        ax.set_ylim(-0.1, 2.1)

    fig.tight_layout()
    fig.savefig(f"figures/{case}_sleep_{sleep_signal}")


if case == "etc":

    fig_etc = plt.figure(dpi=300)
    ax_etc = fig_etc.add_subplot(1,1,1)
    ax_etc.set_title(f"Bias currents (target {target_current} uA) at {single_temperature}°C\nacross extreme corners with sleep signal set to {sleep_signal}")

    for process in ["ff", "ss", "sf", "fs"]:
        for temperature in ["Th", "Tl"]:
            for voltage in ["Vh", "Vl"]:

                if temperature == "Th":
                    etc_temperature = "125"
                elif temperature == "Tl": 
                    etc_temperature = "-40"
                else:
                    etc_temperature = single_temperature
                
                file = f"output_tran/tran_{view}GtK{process}{temperature}{voltage}_{etc_temperature}celsius_sleep_{sleep_signal}.raw"
                name = file.split("/")[-1].replace(".raw", "")
                labelname = "_".join(name.split("_")[0:3])
                raw = RawRead(file)

                print(f"Now processing {file}")

                time = raw.get_axis() * 1e9 # in ns

                idd = -(raw.get_trace("i(vdd)").get_wave() * 1e6) # in uA with positive sign
                iss = -(raw.get_trace("i(vss)").get_wave() * 1e6) # in uA with positive sign
                ir5 = -(raw.get_trace("i(@r.xdut.x11.xxa1.xr1_0.rhead[i])").get_wave() * 1e6) # in uA with positive sign
                id = (raw.get_trace("i(@m.xdut.x8.xm1.msky130_fd_pr__pfet_01v8[id])").get_wave() * 1e6) # in uA with positive sign

                slp = raw.get_trace("v(slp)").get_wave()
                slp_n = raw.get_trace("v(slp_n)").get_wave()
                vbn = raw.get_trace("v(vbn)").get_wave()
                vbp = raw.get_trace("v(vbp)").get_wave()
                vdd = raw.get_trace("v(vdd)").get_wave()
                vss = raw.get_trace("v(vss)").get_wave()
                vr1 = raw.get_trace("v(xdut.vr1)").get_wave()
                vr2 = raw.get_trace("v(xdut.vr2)").get_wave()
                vr3 = raw.get_trace("v(xdut.vr3)").get_wave()
                vr4 = raw.get_trace("v(xdut.vr4)").get_wave()
                vr5 = raw.get_trace("v(xdut.vr5)").get_wave()
                vr6 = raw.get_trace("v(xdut.vr6)").get_wave()
                vr7 = raw.get_trace("v(xdut.vr7)").get_wave()

                # ax_etc.plot(time, (idd/2), label=f"i(vdd)/2 = {idd[-1]/2:.2f} uA")
                # ax_etc.plot(time, ir5, label=f"ires = {ir5[-1]:.2f} uA")
                ax_etc.plot(time, id, label=f"idrain ({labelname}) = {id[-1]:.2f} uA")

                fig, axs = plt.subplots(2, 2, sharex=True, dpi=300)
                fig.suptitle(f"Bias currents (target {target_current} uA) and voltages at {etc_temperature}°C\nin {name} corner")

                axs[0,0].plot(time, (idd/2), label=f"i(vdd)/2 = {idd[-1]/2:.2f} uA")
                axs[0,0].plot(time, ir5, label=f"ires = {ir5[-1]:.2f} uA")
                axs[0,0].plot(time, id, label=f"idrain = {id[-1]:.2f} uA")

                axs[0,1].plot(time, vbn, label=f'vbn = {vbn[-1]:.2f} V')
                axs[0,1].plot(time, vbp, label=f'vbp = {vbp[-1]:.2f} V')

                axs[1,0].plot(time, vr1, label=f'vr1 = {vr1[-1]:.2f} V')
                axs[1,0].plot(time, vr2, label=f'vr2 = {vr2[-1]:.2f} V')
                axs[1,0].plot(time, vr3, label=f'vr3 = {vr3[-1]:.2f} V')
                axs[1,0].plot(time, vr4, label=f'vr4 = {vr4[-1]:.2f} V')
                axs[1,0].plot(time, vr5, label=f'vr5 = {vr5[-1]:.2f} V')
                axs[1,0].plot(time, vr6, label=f'vr6 = {vr6[-1]:.2f} V')
                axs[1,0].plot(time, vr7, label=f'vr7 = {vr7[-1]:.2f} V')

                axs[1,1].plot(time, slp, label=f'slp = {slp[-1]:.2f} V')
                axs[1,1].plot(time, slp_n, label=f'slp_n = {slp_n[-1]:.2f} V')
                
                axs[0,0].set_xlabel("Time (ns)")
                axs[0,0].set_ylabel("Current (uA)")  
                axs[0,0].tick_params(axis='both', which='major')
                axs[0,0].legend()
                axs[0,0].grid()
                axs[0,0].set_ylim(-0.1, 2.6)

                for ax in (axs[0,1], axs[1,0], axs[1,1]):
                    ax.set_xlabel("Time (ns)")
                    ax.set_ylabel("Voltage (V)")
                    ax.legend()
                    ax.grid()
                    ax.set_ylim(-0.1, 2.1)

                fig.tight_layout()
                fig.savefig(f"figures/{case}_{name}")
    
    ax_etc.set_xlabel("Time (ns)")
    ax_etc.set_ylabel("Current (uA)")
    ax_etc.legend(loc="best")
    ax_etc.grid(True)

    fig_etc.tight_layout()
    fig_etc.savefig(f"figures/{case}_sleep_{sleep_signal}")


if case == "mc":

    fig_mc_tran = plt.figure(dpi=300)
    ax_mc_tran = fig_mc_tran.add_subplot(1,1,1)
    ax_mc_tran.set_title(f"Bias currents (target {target_current} uA) over temperatures\nacross montecarlo corners with sleep signal set to {sleep_signal}")

    #
    # Plot mean resistance and standard deviation across temperatures
    #

    tss = list()
    idss = list()

    for run in range(1, runs + 1):
        ts = list()
        ids = list()
        for temperature in temperatures:
            file = f"output_tran/tran_{view}GtKttmmTtVt_{run}_{temperature}celsius_sleep_{sleep_signal}.raw"
            name = file.split("/")[-1].replace(".raw", "")
            labelname = "_".join(name.split("_")[0:3])
            raw = RawRead(file)

            print(f"Now processing {file}")
            id = (raw.get_trace("i(@m.xdut.x8.xm1.msky130_fd_pr__pfet_01v8[id])").get_wave() * 1e6) # in uA with positive sign

            ts.append(temperature)
            ids.append(id[-1])

        tss.append(ts)
        idss.append(ids)

    idss = np.array(idss)

    mean_i = np.mean(idss, axis=0)
    std_i  = np.std(idss, axis=0)

    ax_mc_tran.plot(ts, mean_i, color="steelblue", label="Mean resistance")
    ax_mc_tran.fill_between(ts, mean_i - std_i, mean_i + std_i, alpha=0.15, color="steelblue", label="±1σ band")
 

    #
    # Calculates the confidence intervals of the mean
    #

    n = len(idss)
    sem = std_i / np.sqrt(n)
    t_crit = stats.t.ppf(0.975, df=n - 1)  # 95% confidence interval
 
    ci_lower = mean_i - t_crit * sem
    ci_upper = mean_i + t_crit * sem

    ax_mc_tran.fill_between(ts, ci_lower, ci_upper, alpha=0.3, color="steelblue", label=f"95% confidence interval of mean resistance")
 
    ax_mc_tran.plot(ts, [1.2] * len(ts), linestyle="dotted", color="black", label=f"Target current: {target_current} uA")

    ax_mc_tran.set_xlabel("Temperature (°C)")
    ax_mc_tran.set_ylabel("Current (uA)")
    ax_mc_tran.legend(loc="best")
    ax_mc_tran.grid(True)

    fig_mc_tran.tight_layout()
    fig_mc_tran.savefig(f"figures/{case}_tran_sleep_{sleep_signal}")


    #
    # Find the distribution of resistances at 0 degrees temperature
    # 

    ids = []

    for run in range(1, runs + 1):
        file = f"output_tran/tran_{view}GtKttmmTtVt_{run}_{single_temperature}celsius_sleep_{sleep_signal}.raw"
        name = file.split("/")[-1].replace(".raw", "")
        labelname = "_".join(name.split("_")[0:3])
        raw = RawRead(file)
        
        id = (raw.get_trace("i(@m.xdut.x8.xm1.msky130_fd_pr__pfet_01v8[id])").get_wave() * 1e6) # in uA with positive sign
        ids.append(id[-1])

    print(ids)

    mean_i = np.mean(ids)
    std_i  = np.std(ids)
    
    print(f"mean resistance at {single_temperature}°C after {runs} runs: {mean_i} uA")
    print(f"standard error at {single_temperature}°C after {runs} runs: {std_i} uA")

    within_1sigma = np.sum(np.abs(ids - mean_i) <= std_i)
    pct_1sigma = within_1sigma / len(ids) * 100
    
    print(f"Values within ±1σ: {within_1sigma} of {len(ids)} ({pct_1sigma:.1f}%) — normal distribution expects 68.3%")

    fig_mc_dist = plt.figure(dpi=300)
    ax_mc_dist = fig_mc_dist.add_subplot(1, 1, 1)
    ax_mc_dist.set_title(f"Distribution of bias currents (target {target_current} uA) at {single_temperature}°C\nacross montecarlo corners with sleep signal set to {sleep_signal}")

    sns.histplot(ids, bins=bin_count, kde=True, color="steelblue", edgecolor="black", ax=ax_mc_dist)
    sns.rugplot(ids, height=0.1, color="blue", ax=ax_mc_dist)

    ax_mc_dist.axvline(mean_i, linestyle="dashed", color="black", label=f"μ = {mean_i:.2f} uA")
    ax_mc_dist.axvline(1.2, linestyle="dotted", color="black", label=f"Target current = {target_current} uA")

    ax_mc_dist.grid(True)
    fig_mc_dist.gca().set_axisbelow(True)
        
    # Fill after seaborn has set the y-limits
    ymin, ymax = ax_mc_dist.get_ylim()
    ax_mc_dist.fill_between(
        [mean_i - std_i, mean_i + std_i],
        ymin, ymax,
        alpha=0.2,
        color="black",
        label=f"μ ± σ = μ ± {std_i:.2f} uA\nValues within ±1σ:\n{within_1sigma} of {len(ids)} ({pct_1sigma:.1f}%) "
    )
    ax_mc_dist.set_ylim(ymin, ymax)  # re-apply so fill_between doesn't expand the axis

    ax_mc_dist.legend(loc="best")
    ax_mc_dist.set_xlabel("Current (uA)")
    
    fig_mc_dist.tight_layout()
    fig_mc_dist.savefig(f"figures/{case}_distribution_sleep_{sleep_signal}")


if case == "typical":
    plt.show()
else:
    plt.close()