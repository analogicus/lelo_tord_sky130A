import numpy as np
import pandas as pd    
import matplotlib.pyplot as plt
import sys

from scipy import stats


args = sys.argv[1:]


stepping_direction = ""
if "up" in args:
    args.remove("up")
    stepping_direction = "up"
elif "down" in args:
    args.remove("down")
    stepping_direction = "down"
else: 
    stepping_direction = "down"
print(f"Plotting for transient signals stepping {stepping_direction}")


figure_width = 3
figure_height = 3
font_size = 7
title_font_size = font_size
label_font_size = font_size
legend_font_size = font_size - 1
ticks_font_size = font_size


if args[-1] == "highres":

    fig_v_0p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_0p = fig_v_0p.add_subplot(1, 1, 1)

    fig_dac = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_dac = fig_dac.add_subplot(1, 1, 1)

    fig_on_pwr = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_on_pwr = fig_on_pwr.add_subplot(1, 1, 1)

    fig_off_pwr = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_off_pwr = fig_off_pwr.add_subplot(1, 1, 1)

    fig_start_up = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_start_up = fig_start_up.add_subplot(1, 1, 1)


    df = pd.read_csv(f"plot_data/{'_'.join(args)}_stepping_{stepping_direction}.csv")
    print(f"plot_data/{'_'.join(args)}_stepping_{stepping_direction}.csv")

    for corner in ["tt"]:

        if corner == "tt":
            process_corner = "Typical"
        elif corner == "ss":
            process_corner = "Slow-Slow"
        elif corner == "ff":
            process_corner = "Fast-Fast"
        elif corner == "sf":
            process_corner = "Slow-Fast"
        elif corner == "fs":
            process_corner = "Fast-Slow"
        else:
            process_corner = "Oops, something is wrong!"

        for voltage in [1.8]: # Volt (V)
            Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"

            #
            # Reference voltage on the output
            #

            ts = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage), "Temperature (°C)"])
            vs = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage), "Output voltage (V)"])

            avg_v = np.mean(vs)
            avg_v_devs = np.abs(vs - avg_v)
            avg_v_max_dev = np.max(avg_v_devs)
            avg_v_max_dev_idx = np.argmax(avg_v_devs)
            avg_v_max_dev_t = ts[avg_v_max_dev_idx]
            avg_v_max_dev_v = vs[avg_v_max_dev_idx]

            slope, intercept, r_value, p_value, standard_error = stats.linregress(ts, vs)
            linear_fit = slope * np.array(ts) + intercept

            linear_fit_deviations = np.abs(vs - linear_fit)
            linear_fit_max_deviation = np.max(linear_fit_deviations)
            linear_fit_max_deviation_index = np.argmax(linear_fit_deviations)
            linear_fit_max_deviation_temperature = ts[linear_fit_max_deviation_index]
            linear_fit_max_deviation_voltage = vs[linear_fit_max_deviation_index]

            tc = (np.max(vs) - np.min(vs)) / (np.max(ts) - np.min(ts)) # in V/°C
            tc_in_mV_per_C = tc * 1e3 # in mV/°C
            tc_in_ppm = (tc / avg_v) * 1e6 # in ppm/°C relative to average voltage
            print(f"{process_corner}{Vx} 0pc: mean voltage: {avg_v:.4f} V, TC: {tc:.4f} V/°C, TC in mV/°C {tc_in_mV_per_C:.2f}, TC in ppm/°C: {tc_in_ppm:.2f}")

            axs_v_0p.plot(ts, vs, marker="o", label=f"{corner}{Vx}")
            last_color = axs_v_0p.get_lines()[-1].get_color()
            # axs_v_0p.plot(ts, [avg_v]*len(ts), linestyle="dashed", color=last_color, label=f"mean: {avg_v:.4f} V")
            # axs_v_0p.plot(ts, linear_fit, linestyle="dashed", color=last_color, label=f"Linear fit v={slope*1e3:.2f}t mV/°C + {intercept*1e3:.1f} mV, R²={r_value**2:.4f}")
            # axs_v_0p.plot(avg_v_max_dev_t, avg_v_max_dev_v, linestyle="none", color=last_color, marker="x", markeredgewidth=2, label=f"Max deviation: {avg_v_max_dev_v*1e3:.2f} mV at {avg_v_max_dev_t} °C")

            #
            # Start up time
            #

            startuptimes = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage), "Start-up time (ns)"])
            startuptimes_in_us = startuptimes * 1e-3 # in us

            axs_start_up.plot(ts, startuptimes_in_us, marker="o", label=f"{corner}{Vx}")

            #
            # DAC input settings
            #

            coarse_code = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage), "Coarse code"])
            fine_code = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage), "Fine code"])
            coarse_code = coarse_code * 1e3 # in whole numbers
            fine_code = fine_code * 1e3 # in whole numbers
            dac_code = coarse_code * 10 + fine_code

            axs_dac.plot(ts, dac_code, marker="o", label=f"{corner}{Vx}")
            last_color = axs_dac.get_lines()[-1].get_color()
            # axs_dac.plot(ts, coarse_code, linestyle="dashed", marker="s", color=last_color)
            # axs_dac.plot(ts, fine_code, linestyle="dotted", marker="v", color=last_color)

            #
            # power while in active mode
            #

            mean_on_pwr = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage), "Mean active power (uW)"])
            min_on_pwr = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage), "Minimum active power (uW)"])
            max_on_pwr = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage), "Maximum active power (uW)"])

            axs_on_pwr.plot(ts, mean_on_pwr, linestyle="solid", marker="o", markersize=5, label=f"{corner}{Vx}")
            last_color = axs_on_pwr.get_lines()[-1].get_color()
            # axs_on_pwr.plot(ts, min_on_pwr, linestyle="dashed", marker="s", markersize=5, color=last_color, label=f"{corner}{Vx}, minimum")
            # axs_on_pwr.plot(ts, max_on_pwr, linestyle="dotted", marker="v", markersize=5, color=last_color, label=f"{corner}{Vx}, maximum")

            #
            # power while in sleep mode
            #

            off_pwr = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage), "Sleep power (uW)"])
    
            axs_off_pwr.plot(ts, off_pwr, marker="o", label=f"{corner}{Vx}")

            print("")


    axs_v_0p.set_title(f"Reference voltage", fontsize=title_font_size, fontweight='bold')
    axs_v_0p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_0p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_0p.legend(loc="best", fontsize=legend_font_size)
    axs_v_0p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_0p.grid()

    fig_v_0p.tight_layout()
    fig_v_0p.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_uncalibrated_temperature_vs_reference_voltage_v2.png", dpi=300, bbox_inches="tight")


    axs_dac.set_title(f"DAC input", fontsize=title_font_size, fontweight='bold')
    axs_dac.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_dac.set_ylabel("DAC code", fontsize=label_font_size)
    axs_dac.legend(loc="best", fontsize=legend_font_size)
    axs_dac.tick_params(axis='both', labelsize=ticks_font_size)
    axs_dac.grid()

    fig_dac.tight_layout()
    fig_dac.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_uncalibrated_temperature_vs_dac_code_v2.png", dpi=300, bbox_inches="tight")


    axs_on_pwr.set_title(f"Active power consumption", fontsize=title_font_size, fontweight='bold')
    axs_on_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_on_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_on_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_on_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_on_pwr.grid()

    fig_on_pwr.tight_layout()
    fig_on_pwr.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_temperature_vs_active_power_new_resistance_v2.png", dpi=300, bbox_inches="tight")


    axs_off_pwr.set_title(f"Sleep power consumption", fontsize=title_font_size, fontweight='bold')
    axs_off_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_off_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_off_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_off_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_off_pwr.grid()

    fig_off_pwr.tight_layout()
    fig_off_pwr.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_temperature_vs_sleep_power_new_resistance_v2.png", dpi=300, bbox_inches="tight")


    axs_start_up.set_title(f"Start-up time", fontsize=title_font_size, fontweight='bold')
    axs_start_up.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_start_up.set_ylabel("Time (us)", fontsize=label_font_size)
    axs_start_up.tick_params(axis='both', labelsize=ticks_font_size)
    axs_start_up.grid()

    fig_start_up.tight_layout()
    fig_start_up.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_temperature_vs_start_up_time_new_resistance_v2.png", dpi=300, bbox_inches="tight")
