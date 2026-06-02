import numpy as np
import pandas as pd    
import matplotlib.pyplot as plt
import sys

from scipy import stats


args = sys.argv[1:]
temperatures = [-40, 0, 40, 80, 125]


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


if args[-1] == "etc":

    fig_v_0p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_0p = fig_v_0p.add_subplot(1, 1, 1)

    fig_v_1p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_1p = fig_v_1p.add_subplot(1, 1, 1)

    fig_v_2p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_2p = fig_v_2p.add_subplot(1, 1, 1)

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

    ts_ttVt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Temperature (°C)"])
    vs_ttVt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Output voltage (V)"])

    coarse_code_ttVt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Coarse code"])
    fine_code_ttVt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Fine code"])
    coarse_code_ttVt = coarse_code_ttVt * 1e3 # in whole numbers
    fine_code_ttVt = fine_code_ttVt * 1e3 # in whole numbers
    dac_code_ttVt = coarse_code_ttVt * 10 + fine_code_ttVt

    mean_v_ttVt = np.mean(vs_ttVt)
    tc_ttVt = (np.max(vs_ttVt) - np.min(vs_ttVt)) / (np.max(ts_ttVt) - np.min(ts_ttVt)) # in V/°C
    tc_ttVt_in_mV_per_C = tc_ttVt * 1e3 # in mV/°C
    tc_ttVt_in_ppm = (tc_ttVt / mean_v_ttVt) * 1e6 # in ppm/°C relative to average voltage
    print(f"Typical  Vt 0pc: Mean voltage: {mean_v_ttVt:.4f} V, TC: {tc_ttVt:.4f} V/°C, TC in mV/°C {tc_ttVt_in_mV_per_C:.2f}, TC in ppm/°C: {tc_ttVt_in_ppm:.2f}")


    for corner in ["ss", "ff", "sf", "fs"]:

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

        for voltage in [1.7, 1.9]: # Volt (V)
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
            # 1 point calibrate the voltages in the calibration_t degrees Celsius voltage as the single point
            # 

            calibration_t = 40 # in degrees Celsius
            target_v = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t), "Output voltage (V)"])
            actual_v = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_t), "Output voltage (V)"])
            onepointcalibrated_vs = [v + (target_v - actual_v) for v in vs]

            mean_v_onepointcalibrated = np.mean(onepointcalibrated_vs)
            tc_onepointcalibrated = (np.max(onepointcalibrated_vs) - np.min(onepointcalibrated_vs)) / (np.max(ts) - np.min(ts)) # in V/°C
            tc_in_mV_per_C = tc_onepointcalibrated * 1e3 # in mV/°C
            tc_in_ppm = (tc_onepointcalibrated / mean_v_onepointcalibrated) * 1e6 # in ppm/°C relative to average voltage
            print(f"{process_corner}{Vx} 1pc: Mean voltage: {mean_v_onepointcalibrated:.4f} V, TC: {tc_onepointcalibrated:.4f} V/°C, TC in mV/°C {tc_in_mV_per_C:.2f}, TC in ppm/°C: {tc_in_ppm:.2f}")

            axs_v_1p.plot(ts, onepointcalibrated_vs, marker="o", label=f"{corner}{Vx}")

            # # 
            # # 2 point calibrate the voltages at the calibration_t1 and calibration_t2 degrees Celsius voltage as the single point
            # # 

            # calibration_t1 = 0
            # calibration_t2 = 80
            # calibration_v1 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
            # calibration_v2 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])
            # twopointcalibrated_vs = [v + (calibration_v2 - calibration_v1) / (calibration_t2 - calibration_t1) * (t - calibration_t1) for v, t in zip(vs, ts)]

            # axs_v_2p.plot(ts, twopointcalibrated_vs, marker="o", label=f"{corner}{Vx}")

            # 
            # 2 point calibrate the voltages at calibration_t1 and calibration_t2
            # 

            calibration_t1 = 0
            calibration_t2 = 80

            # Target values: what the tt/1.8V curve reads at each calibration temperature
            target_v1 = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
            target_v2 = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])

            twopointcalibrated_vs = []
            for v, t in zip(vs, ts):
                # Actual value of this curve at calibration temperatures (interpolated if needed)
                actual_v1 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
                actual_v2 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])

                # Offset at each calibration point
                offset1 = target_v1 - actual_v1
                offset2 = target_v2 - actual_v2

                # Linearly interpolate offset across temperature
                offset = offset1 + (offset2 - offset1) * (t - calibration_t1) / (calibration_t2 - calibration_t1)
                twopointcalibrated_vs.append(v + offset)

            mean_v_twopointcalibrated = np.mean(twopointcalibrated_vs)
            tc_twopointcalibrated = (np.max(twopointcalibrated_vs) - np.min(twopointcalibrated_vs)) / (np.max(ts) - np.min(ts)) # in V/°C
            tc_in_mV_per_C = tc_twopointcalibrated * 1e3 # in mV/°C
            tc_in_ppm = (tc_twopointcalibrated / mean_v_twopointcalibrated) * 1e6 # in ppm/°C relative to average voltage
            print(f"{process_corner}{Vx} 2pc: Mean voltage: {mean_v_twopointcalibrated:.4f} V, TC: {tc_twopointcalibrated:.4f} V/°C, TC in mV/°C {tc_in_mV_per_C:.2f}, TC in ppm/°C: {tc_in_ppm:.2f}")

            axs_v_2p.plot(ts, twopointcalibrated_vs, marker="o", label=f"{corner}{Vx}")

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

            axs_on_pwr.plot(temperatures, mean_on_pwr, linestyle="solid", marker="o", markersize=5, label=f"{corner}{Vx}")
            last_color = axs_on_pwr.get_lines()[-1].get_color()
            # axs_on_pwr.plot(temperatures, min_on_pwr, linestyle="dashed", marker="s", markersize=5, color=last_color, label=f"{corner}{Vx}, minimum")
            # axs_on_pwr.plot(temperatures, max_on_pwr, linestyle="dotted", marker="v", markersize=5, color=last_color, label=f"{corner}{Vx}, maximum")

            #
            # power while in sleep mode
            #

            off_pwr = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage), "Sleep power (uW)"])
            
            axs_off_pwr.plot(temperatures, off_pwr, marker="o", label=f"{corner}{Vx}")

            #
            # start up time
            #

            start_up_times = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage), "Start-up time (us)"])

            axs_start_up.plot(temperatures, start_up_times, marker="o", label=f"{corner}{Vx}")

            print("")

    mean_on_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Mean active power (uW)"])
    min_on_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Minimum active power (uW)"])
    max_on_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Maximum active power (uW)"])
    axs_on_pwr.plot(temperatures, mean_on_pwr, linestyle="solid", marker="o", markersize=5, label=f"ttVt")
    off_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Sleep power (uW)"])
    axs_off_pwr.plot(temperatures, off_pwr, marker="o", label=f"ttVt")

    axs_v_0p.plot(ts_ttVt, vs_ttVt, marker="o", label=f"ttVt")
    axs_v_1p.plot(ts_ttVt, vs_ttVt, marker="o", label=f"ttVt")

    calibration_t1 = 0
    calibration_t2 = 80

    # Target values: what the tt/1.8V curve reads at each calibration temperature
    target_v1 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
    target_v2 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])


    twopointcalibrated_vs = []
    for v, t in zip(vs_ttVt, ts_ttVt):
        # Actual value of this curve at calibration temperatures (interpolated if needed)
        actual_v1 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
        actual_v2 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])

        # Offset at each calibration point
        offset1 = target_v1 - actual_v1
        offset2 = target_v2 - actual_v2

        # Linearly interpolate offset across temperature
        offset = offset1 + (offset2 - offset1) * (t - calibration_t1) / (calibration_t2 - calibration_t1)
        twopointcalibrated_vs.append(v + offset)

    mean_v_twopointcalibrated = np.mean(twopointcalibrated_vs)
    tc_twopointcalibrated = (np.max(twopointcalibrated_vs) - np.min(twopointcalibrated_vs)) / (np.max(ts) - np.min(ts)) # in V/°C
    tc_in_mV_per_C = tc_twopointcalibrated * 1e3 # in mV/°C
    tc_in_ppm = (tc_twopointcalibrated / mean_v_twopointcalibrated) * 1e6 # in ppm/°C relative to average voltage
    print(f"Typical   Vt 2pc: Mean voltage: {mean_v_twopointcalibrated:.4f} V, TC: {tc_twopointcalibrated:.4f} V/°C, TC in mV/°C {tc_in_mV_per_C:.2f}, TC in ppm/°C: {tc_in_ppm:.2f}")

    axs_v_2p.plot(ts_ttVt, twopointcalibrated_vs, marker="o", label=f"ttVt")


    axs_dac.plot(ts_ttVt, dac_code_ttVt, marker="o", label=f"ttVt")
    # axs_dac_0p.plot(ts_ttVt, coarse_code_ttVt, linestyle="dashed", marker="s")
    # axs_dac_0p.plot(ts_ttVt, fine_code_ttVt, linestyle="dotted", marker="v")

    start_up_times_tt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Start-up time (us)"])

    axs_start_up.plot(temperatures, start_up_times_tt, marker="o", label=f"ttVt")


    axs_v_0p.set_title(f"Reference voltage", fontsize=title_font_size, fontweight='bold')
    axs_v_0p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_0p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_0p.legend(loc="best", fontsize=legend_font_size)
    axs_v_0p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_0p.grid()

    fig_v_0p.tight_layout()
    fig_v_0p.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_uncalibrated_temperature_vs_reference_voltage.png", dpi=300, bbox_inches="tight")


    axs_dac.set_title(f"DAC input", fontsize=title_font_size, fontweight='bold')
    axs_dac.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_dac.set_ylabel("DAC code", fontsize=label_font_size)
    axs_dac.legend(loc="best", fontsize=legend_font_size)
    axs_dac.tick_params(axis='both', labelsize=ticks_font_size)
    axs_dac.grid()

    fig_dac.tight_layout()
    fig_dac.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_uncalibrated_temperature_vs_dac_code.png", dpi=300, bbox_inches="tight")


    axs_v_1p.set_title(f"Reference voltage 1 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_1p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_1p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_1p.legend(loc="best", fontsize=legend_font_size)
    axs_v_1p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_1p.grid()

    fig_v_1p.tight_layout()
    fig_v_1p.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_onepointcalibrated_temperature_vs_reference_voltage.png", dpi=300, bbox_inches="tight")

    
    axs_v_2p.set_title(f"Reference voltage 2 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_2p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_2p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_2p.legend(loc="best", fontsize=legend_font_size)
    axs_v_2p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_2p.grid()

    fig_v_2p.tight_layout()
    fig_v_2p.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_twopointcalibrated_temperature_vs_reference_voltage.png", dpi=300, bbox_inches="tight")


    axs_on_pwr.set_title(f"Active power consumption", fontsize=title_font_size, fontweight='bold')
    axs_on_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_on_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_on_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_on_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_on_pwr.grid()

    fig_on_pwr.tight_layout()
    fig_on_pwr.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_temperature_vs_active_power.png", dpi=300, bbox_inches="tight")

    axs_off_pwr.set_title(f"Sleep power consumption", fontsize=title_font_size, fontweight='bold')
    axs_off_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_off_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_off_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_off_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_off_pwr.grid()

    fig_off_pwr.tight_layout()
    fig_off_pwr.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_temperature_vs_sleep_power.png", dpi=300, bbox_inches="tight")



if args[-1] == "ttVt":

    fig_v_0p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_0p = fig_v_0p.add_subplot(1, 1, 1)

    fig_v_1p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_1p = fig_v_1p.add_subplot(1, 1, 1)

    fig_v_2p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_2p = fig_v_2p.add_subplot(1, 1, 1)

    fig_dac = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_dac = fig_dac.add_subplot(1, 1, 1)

    fig_on_pwr = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_on_pwr = fig_on_pwr.add_subplot(1, 1, 1)

    fig_off_pwr = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_off_pwr = fig_off_pwr.add_subplot(1, 1, 1)

    fig_start_up = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_start_up = fig_start_up.add_subplot(1, 1, 1)


    df = pd.read_csv(f"plotdata/{'_'.join(args)}_stepping_{stepping_direction}.csv")
    print(f"plotdata/{'_'.join(args)}_stepping_{stepping_direction}.csv")

    ts_ttVt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Temperature (°C)"])
    vs_ttVt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Output voltage (V)"])

    coarse_code_ttVt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Coarse code"])
    fine_code_ttVt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Fine code"])
    coarse_code_ttVt = coarse_code_ttVt * 1e3 # in whole numbers
    fine_code_ttVt = fine_code_ttVt * 1e3 # in whole numbers
    dac_code_ttVt = coarse_code_ttVt * 10 + fine_code_ttVt

    mean_v_ttVt = np.mean(vs_ttVt)
    tc_ttVt = (np.max(vs_ttVt) - np.min(vs_ttVt)) / (np.max(ts_ttVt) - np.min(ts_ttVt)) # in V/°C
    tc_ttVt_in_mV_per_C = tc_ttVt * 1e3 # in mV/°C
    tc_ttVt_in_ppm = (tc_ttVt / mean_v_ttVt) * 1e6 # in ppm/°C relative to average voltage
    print(f"Typical  Vt 0pc: Mean voltage: {mean_v_ttVt:.4f} V, TC: {tc_ttVt:.4f} V/°C, TC in mV/°C {tc_ttVt_in_mV_per_C:.2f}, TC in ppm/°C: {tc_ttVt_in_ppm:.2f}")
    axs_v_0p.plot(ts_ttVt, vs_ttVt, marker="o", label=f"ttVt")
    

    axs_v_1p.plot(ts_ttVt, vs_ttVt, marker="o", label=f"ttVt")

    calibration_t1 = 0
    calibration_t2 = 80

    # Target values: what the tt/1.8V curve reads at each calibration temperature
    target_v1 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
    target_v2 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])


    twopointcalibrated_vs = []
    for v, t in zip(vs_ttVt, ts_ttVt):
        # Actual value of this curve at calibration temperatures (interpolated if needed)
        actual_v1 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
        actual_v2 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])

        # Offset at each calibration point
        offset1 = target_v1 - actual_v1
        offset2 = target_v2 - actual_v2

        # Linearly interpolate offset across temperature
        offset = offset1 + (offset2 - offset1) * (t - calibration_t1) / (calibration_t2 - calibration_t1)
        twopointcalibrated_vs.append(v + offset)

    mean_v_twopointcalibrated = np.mean(twopointcalibrated_vs)
    tc_twopointcalibrated = (np.max(twopointcalibrated_vs) - np.min(twopointcalibrated_vs)) / (np.max(ts_ttVt) - np.min(ts_ttVt)) # in V/°C
    tc_in_mV_per_C = tc_twopointcalibrated * 1e3 # in mV/°C
    tc_in_ppm = (tc_twopointcalibrated / mean_v_twopointcalibrated) * 1e6 # in ppm/°C relative to average voltage
    print(f"Typical   Vt 2pc: Mean voltage: {mean_v_twopointcalibrated:.4f} V, TC: {tc_twopointcalibrated:.4f} V/°C, TC in mV/°C {tc_in_mV_per_C:.2f}, TC in ppm/°C: {tc_in_ppm:.2f}")

    axs_v_2p.plot(ts_ttVt, twopointcalibrated_vs, marker="o", label=f"ttVt")


    mean_on_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Mean active power (uW)"])
    min_on_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Minimum active power (uW)"])
    max_on_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Maximum active power (uW)"])
    axs_on_pwr.plot(temperatures, mean_on_pwr, linestyle="solid", marker="o", markersize=5, label=f"ttVt")
    
    off_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Sleep power (uW)"])
    axs_off_pwr.plot(temperatures, off_pwr, marker="o", label=f"ttVt")

    axs_dac.plot(ts_ttVt, dac_code_ttVt, marker="o", label=f"ttVt")
    # axs_dac_0p.plot(ts_ttVt, coarse_code_ttVt, linestyle="dashed", marker="s")
    # axs_dac_0p.plot(ts_ttVt, fine_code_ttVt, linestyle="dotted", marker="v")

    start_up_times_tt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Start-up time (us)"])

    axs_start_up.plot(temperatures, start_up_times_tt, marker="o", label=f"ttVt")


    axs_v_0p.set_title(f"Reference voltage", fontsize=title_font_size, fontweight='bold')
    axs_v_0p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_0p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_0p.legend(loc="best", fontsize=legend_font_size)
    axs_v_0p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_0p.grid()

    fig_v_0p.tight_layout()
    fig_v_0p.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_uncalibrated_temperature_vs_reference_voltage.png", dpi=300, bbox_inches="tight")


    axs_dac.set_title(f"DAC input", fontsize=title_font_size, fontweight='bold')
    axs_dac.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_dac.set_ylabel("DAC code", fontsize=label_font_size)
    axs_dac.legend(loc="best", fontsize=legend_font_size)
    axs_dac.tick_params(axis='both', labelsize=ticks_font_size)
    axs_dac.grid()

    fig_dac.tight_layout()
    fig_dac.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_uncalibrated_temperature_vs_dac_code.png", dpi=300, bbox_inches="tight")


    axs_v_1p.set_title(f"Reference voltage 1 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_1p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_1p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_1p.legend(loc="best", fontsize=legend_font_size)
    axs_v_1p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_1p.grid()

    fig_v_1p.tight_layout()
    fig_v_1p.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_onepointcalibrated_temperature_vs_reference_voltage.png", dpi=300, bbox_inches="tight")

    
    axs_v_2p.set_title(f"Reference voltage 2 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_2p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_2p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_2p.legend(loc="best", fontsize=legend_font_size)
    axs_v_2p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_2p.grid()

    fig_v_2p.tight_layout()
    fig_v_2p.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_twopointcalibrated_temperature_vs_reference_voltage.png", dpi=300, bbox_inches="tight")


    axs_on_pwr.set_title(f"Active power consumption", fontsize=title_font_size, fontweight='bold')
    axs_on_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_on_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_on_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_on_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_on_pwr.grid()

    fig_on_pwr.tight_layout()
    fig_on_pwr.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_temperature_vs_active_power.png", dpi=300, bbox_inches="tight")

    axs_off_pwr.set_title(f"Sleep power consumption", fontsize=title_font_size, fontweight='bold')
    axs_off_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_off_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_off_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_off_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_off_pwr.grid()

    fig_off_pwr.tight_layout()
    fig_off_pwr.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_temperature_vs_sleep_power.png", dpi=300, bbox_inches="tight")

    axs_start_up.set_title(f"Start up time", fontsize=title_font_size, fontweight='bold')
    axs_start_up.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_start_up.set_ylabel("Time (us)", fontsize=label_font_size)
    axs_start_up.legend(loc="best", fontsize=legend_font_size)
    axs_start_up.tick_params(axis='both', labelsize=ticks_font_size)
    axs_start_up.grid()

    fig_start_up.tight_layout()
    fig_start_up.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_temperature_vs_start_up_time.png", dpi=300, bbox_inches="tight")


if args[-1] == "tfs":

    fig_v_0p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_0p = fig_v_0p.add_subplot(1, 1, 1)

    fig_v_1p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_1p = fig_v_1p.add_subplot(1, 1, 1)

    fig_v_2p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_2p = fig_v_2p.add_subplot(1, 1, 1)

    fig_dac = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_dac = fig_dac.add_subplot(1, 1, 1)

    fig_on_pwr = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_on_pwr = fig_on_pwr.add_subplot(1, 1, 1)

    fig_off_pwr = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_off_pwr = fig_off_pwr.add_subplot(1, 1, 1)

    fig_start_up = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_start_up = fig_start_up.add_subplot(1, 1, 1)


    df = pd.read_csv(f"plotdata/{'_'.join(args)}_stepping_{stepping_direction}.csv")
    print(f"plotdata/{'_'.join(args)}_stepping_{stepping_direction}.csv")

    #
    # ttVt
    #

    ts_ttVt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Temperature (°C)"])
    vs_ttVt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Output voltage (V)"])

    coarse_code_ttVt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Coarse code"])
    fine_code_ttVt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Fine code"])
    coarse_code_ttVt = coarse_code_ttVt * 1e3 # in whole numbers
    fine_code_ttVt = fine_code_ttVt * 1e3 # in whole numbers
    dac_code_ttVt = coarse_code_ttVt * 10 + fine_code_ttVt

    mean_v_ttVt = np.mean(vs_ttVt)
    tc_ttVt = (np.max(vs_ttVt) - np.min(vs_ttVt)) / (np.max(ts_ttVt) - np.min(ts_ttVt)) # in V/°C
    tc_ttVt_in_mV_per_C = tc_ttVt * 1e3 # in mV/°C
    tc_ttVt_in_ppm = (tc_ttVt / mean_v_ttVt) * 1e6 # in ppm/°C relative to average voltage
    print(f"Typical  Vt 0pc: Mean voltage: {mean_v_ttVt:.4f} V, TC: {tc_ttVt:.4f} V/°C, TC in mV/°C {tc_ttVt_in_mV_per_C:.2f}, TC in ppm/°C: {tc_ttVt_in_ppm:.2f}")
    
    
    axs_v_0p.plot(ts_ttVt, vs_ttVt, marker="o", label=f"ttVt")

    axs_v_1p.plot(ts_ttVt, vs_ttVt, marker="o", label=f"ttVt")

    calibration_t1 = 0
    calibration_t2 = 80

    # Target values: what the tt/1.8V curve reads at each calibration temperature
    target_v1 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
    target_v2 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])


    twopointcalibrated_vs = []
    for v, t in zip(vs_ttVt, ts_ttVt):
        # Actual value of this curve at calibration temperatures (interpolated if needed)
        actual_v1 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
        actual_v2 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])

        # Offset at each calibration point
        offset1 = target_v1 - actual_v1
        offset2 = target_v2 - actual_v2

        # Linearly interpolate offset across temperature
        offset = offset1 + (offset2 - offset1) * (t - calibration_t1) / (calibration_t2 - calibration_t1)
        twopointcalibrated_vs.append(v + offset)

    mean_v_twopointcalibrated = np.mean(twopointcalibrated_vs)
    tc_twopointcalibrated = (np.max(twopointcalibrated_vs) - np.min(twopointcalibrated_vs)) / (np.max(ts_ttVt) - np.min(ts_ttVt)) # in V/°C
    tc_in_mV_per_C = tc_twopointcalibrated * 1e3 # in mV/°C
    tc_in_ppm = (tc_twopointcalibrated / mean_v_twopointcalibrated) * 1e6 # in ppm/°C relative to average voltage
    print(f"Typical   Vt 2pc: Mean voltage: {mean_v_twopointcalibrated:.4f} V, TC: {tc_twopointcalibrated:.4f} V/°C, TC in mV/°C {tc_in_mV_per_C:.2f}, TC in ppm/°C: {tc_in_ppm:.2f}")

    axs_v_2p.plot(ts_ttVt, twopointcalibrated_vs, marker="o", label=f"ttVt")


    mean_on_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Mean active power (uW)"])
    min_on_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Minimum active power (uW)"])
    max_on_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Maximum active power (uW)"])
    axs_on_pwr.plot(temperatures, mean_on_pwr, linestyle="solid", marker="o", markersize=5, label=f"ttVt")
    
    off_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Sleep power (uW)"])
    axs_off_pwr.plot(temperatures, off_pwr, marker="o", label=f"ttVt")

    axs_dac.plot(ts_ttVt, dac_code_ttVt, marker="o", label=f"ttVt")
    # axs_dac_0p.plot(ts_ttVt, coarse_code_ttVt, linestyle="dashed", marker="s")
    # axs_dac_0p.plot(ts_ttVt, fine_code_ttVt, linestyle="dotted", marker="v")

    start_up_times_tt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Start-up time (us)"])

    axs_start_up.plot(temperatures, start_up_times_tt, marker="o", label=f"ttVt")


    
    #
    # ffVh
    #

    ts_ffVh = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.9), "Temperature (°C)"])
    vs_ffVh = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.9), "Output voltage (V)"])

    coarse_code_ffVh = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.9), "Coarse code"])
    fine_code_ffVh = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.9), "Fine code"])
    coarse_code_ffVh = coarse_code_ffVh * 1e3 # in whole numbers
    fine_code_ffVh = fine_code_ffVh * 1e3 # in whole numbers
    dac_code_ffVh = coarse_code_ffVh * 10 + fine_code_ffVh

    mean_v_ffVh = np.mean(vs_ffVh)
    tc_ffVh = (np.max(vs_ffVh) - np.min(vs_ffVh)) / (np.max(ts_ffVh) - np.min(ts_ffVh)) # in V/°C
    tc_ffVh_in_mV_per_C = tc_ffVh * 1e3 # in mV/°C
    tc_ffVh_in_ppm = (tc_ffVh / mean_v_ffVh) * 1e6 # in ppm/°C relative to average voltage
    print(f"Fast-Fast Vt 0pc: Mean voltage: {mean_v_ffVh:.4f} V, TC: {tc_ffVh:.4f} V/°C, TC in mV/°C {tc_ffVh_in_mV_per_C:.2f}, TC in ppm/°C: {tc_ffVh_in_ppm:.2f}")
    axs_v_0p.plot(ts_ffVh, vs_ffVh, marker="o", label=f"ffVh")
    
    calibration_t = 40 # in degrees Celsius
    target_v = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t), "Output voltage (V)"])
    actual_v = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_t), "Output voltage (V)"])
    onepointcalibrated_vs = [v + (target_v - actual_v) for v in vs_ffVh]

    mean_v_onepointcalibrated = np.mean(onepointcalibrated_vs)
    tc_onepointcalibrated = (np.max(onepointcalibrated_vs) - np.min(onepointcalibrated_vs)) / (np.max(ts_ffVh) - np.min(ts_ffVh)) # in V/°C
    tc_in_mV_per_C = tc_onepointcalibrated * 1e3 # in mV/°C
    tc_in_ppm = (tc_onepointcalibrated / mean_v_onepointcalibrated) * 1e6 # in ppm/°C relative to average voltage
    print(f"Fast-Fast Vt 1pc: Mean voltage: {mean_v_onepointcalibrated:.4f} V, TC: {tc_onepointcalibrated:.4f} V/°C, TC in mV/°C {tc_in_mV_per_C:.2f}, TC in ppm/°C: {tc_in_ppm:.2f}")

    axs_v_1p.plot(ts_ffVh, onepointcalibrated_vs, marker="o", label=f"ffVh")

    calibration_t1 = 0
    calibration_t2 = 80

    # Target values: what the ffVh/1.9V curve reads at each calibration temperature
    target_v1 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
    target_v2 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])


    twopointcalibrated_vs = []
    for v, t in zip(vs_ffVh, ts_ffVh):
        # Actual value of this curve at calibration temperatures (interpolated if needed)
        actual_v1 = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
        actual_v2 = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])

        # Offset at each calibration point
        offset1 = target_v1 - actual_v1
        offset2 = target_v2 - actual_v2

        # Linearly interpolate offset across temperature
        offset = offset1 + (offset2 - offset1) * (t - calibration_t1) / (calibration_t2 - calibration_t1)
        twopointcalibrated_vs.append(v + offset)

    mean_v_twopointcalibrated = np.mean(twopointcalibrated_vs)
    tc_twopointcalibrated = (np.max(twopointcalibrated_vs) - np.min(twopointcalibrated_vs)) / (np.max(ts_ffVh) - np.min(ts_ffVh)) # in V/°C
    tc_in_mV_per_C = tc_twopointcalibrated * 1e3 # in mV/°C
    tc_in_ppm = (tc_twopointcalibrated / mean_v_twopointcalibrated) * 1e6 # in ppm/°C relative to average voltage
    print(f"Fast-Fast Vt 2pc: Mean voltage: {mean_v_twopointcalibrated:.4f} V, TC: {tc_twopointcalibrated:.4f} V/°C, TC in mV/°C {tc_in_mV_per_C:.2f}, TC in ppm/°C: {tc_in_ppm:.2f}")

    axs_v_2p.plot(ts_ffVh, twopointcalibrated_vs, marker="o", label=f"ffVh")


    mean_on_pwr = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.9), "Mean active power (uW)"])
    min_on_pwr = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.9), "Minimum active power (uW)"])
    max_on_pwr = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.9), "Maximum active power (uW)"])
    axs_on_pwr.plot(temperatures, mean_on_pwr, linestyle="solid", marker="o", markersize=5, label=f"ffVh")
    
    off_pwr = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.9), "Sleep power (uW)"])
    axs_off_pwr.plot(temperatures, off_pwr, marker="o", label=f"ffVh")

    axs_dac.plot(ts_ffVh, dac_code_ffVh, marker="o", label=f"ffVh")
    # axs_dac_0p.plot(ts_ffVh, coarse_code_ffVh, linestyle="dashed", marker="s")
    # axs_dac_0p.plot(ts_ffVh, fine_code_ffVh, linestyle="dotted", marker="v")

    start_up_times_ffVh = np.array(df.loc[(df['Process corner'] == "Fast-Fast") & (df["Voltage supply (V)"] == 1.9), "Start-up time (us)"])

    axs_start_up.plot(temperatures, start_up_times_ffVh, marker="o", label=f"ffVh")

    
    #
    # ssVl
    #

    ts_ssVl = np.array(df.loc[(df['Process corner'] == "Slow-Slow") & (df["Voltage supply (V)"] == 1.7), "Temperature (°C)"])
    vs_ssVl = np.array(df.loc[(df['Process corner'] == "Slow-Slow") & (df["Voltage supply (V)"] == 1.7), "Output voltage (V)"])

    coarse_code_ssVl = np.array(df.loc[(df['Process corner'] == "Slow-Slow") & (df["Voltage supply (V)"] == 1.7), "Coarse code"])
    fine_code_ssVl = np.array(df.loc[(df['Process corner'] == "Slow-Slow") & (df["Voltage supply (V)"] == 1.7), "Fine code"])
    coarse_code_ssVl = coarse_code_ssVl * 1e3 # in whole numbers
    fine_code_ssVl = fine_code_ssVl * 1e3 # in whole numbers
    dac_code_ssVl = coarse_code_ssVl * 10 + fine_code_ssVl

    mean_v_ssVl = np.mean(vs_ssVl)
    tc_ssVl = (np.max(vs_ssVl) - np.min(vs_ssVl)) / (np.max(ts_ssVl) - np.min(ts_ssVl)) # in V/°C
    tc_ssVl_in_mV_per_C = tc_ssVl * 1e3 # in mV/°C
    tc_ssVl_in_ppm = (tc_ssVl / mean_v_ssVl) * 1e6 # in ppm/°C relative to average voltage
    print(f"Slow-Slow Vt 0pc: Mean voltage: {mean_v_ssVl:.4f} V, TC: {tc_ssVl:.4f} V/°C, TC in mV/°C {tc_ssVl_in_mV_per_C:.2f}, TC in ppm/°C: {tc_ssVl_in_ppm:.2f}")
    axs_v_0p.plot(ts_ssVl, vs_ssVl, marker="o", label=f"ssVl")
    

    calibration_t = 40 # in degrees Celsius
    target_v = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t), "Output voltage (V)"])
    actual_v = np.array(df.loc[(df['Process corner'] == "Slow-Slow") & (df["Voltage supply (V)"] == 1.7) & (df["Temperature (°C)"] == calibration_t), "Output voltage (V)"])
    onepointcalibrated_vs = [v + (target_v - actual_v) for v in vs_ssVl]

    mean_v_onepointcalibrated = np.mean(onepointcalibrated_vs)
    tc_onepointcalibrated = (np.max(onepointcalibrated_vs) - np.min(onepointcalibrated_vs)) / (np.max(ts_ssVl) - np.min(ts_ssVl)) # in V/°C
    tc_in_mV_per_C = tc_onepointcalibrated * 1e3 # in mV/°C
    tc_in_ppm = (tc_onepointcalibrated / mean_v_onepointcalibrated) * 1e6 # in ppm/°C relative to average voltage
    print(f"Slow-Slow Vt 1pc: Mean voltage: {mean_v_onepointcalibrated:.4f} V, TC: {tc_onepointcalibrated:.4f} V/°C, TC in mV/°C {tc_in_mV_per_C:.2f}, TC in ppm/°C: {tc_in_ppm:.2f}")

    axs_v_1p.plot(ts_ssVl, onepointcalibrated_vs, marker="o", label=f"ssVl")

    calibration_t1 = 0
    calibration_t2 = 80

    # Target values: what the tt/1.8V curve reads at each calibration temperature
    target_v1 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
    target_v2 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])


    twopointcalibrated_vs = []
    for v, t in zip(vs_ssVl, ts_ssVl):
        # Actual value of this curve at calibration temperatures (interpolated if needed)
        actual_v1 = np.array(df.loc[(df['Process corner'] == "Slow-Slow") & (df["Voltage supply (V)"] == 1.7) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
        actual_v2 = np.array(df.loc[(df['Process corner'] == "Slow-Slow") & (df["Voltage supply (V)"] == 1.7) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])

        # Offset at each calibration point
        offset1 = target_v1 - actual_v1
        offset2 = target_v2 - actual_v2

        # Linearly interpolate offset across temperature
        offset = offset1 + (offset2 - offset1) * (t - calibration_t1) / (calibration_t2 - calibration_t1)
        twopointcalibrated_vs.append(v + offset)

    mean_v_twopointcalibrated = np.mean(twopointcalibrated_vs)
    tc_twopointcalibrated = (np.max(twopointcalibrated_vs) - np.min(twopointcalibrated_vs)) / (np.max(ts_ssVl) - np.min(ts_ssVl)) # in V/°C
    tc_in_mV_per_C = tc_twopointcalibrated * 1e3 # in mV/°C
    tc_in_ppm = (tc_twopointcalibrated / mean_v_twopointcalibrated) * 1e6 # in ppm/°C relative to average voltage
    print(f"Slow-Slow Vt 2pc: Mean voltage: {mean_v_twopointcalibrated:.4f} V, TC: {tc_twopointcalibrated:.4f} V/°C, TC in mV/°C {tc_in_mV_per_C:.2f}, TC in ppm/°C: {tc_in_ppm:.2f}")

    axs_v_2p.plot(ts_ssVl, twopointcalibrated_vs, marker="o", label=f"ssVl")


    mean_on_pwr = np.array(df.loc[(df['Process corner'] == "Slow-Slow") & (df["Voltage supply (V)"] == 1.7), "Mean active power (uW)"])
    min_on_pwr = np.array(df.loc[(df['Process corner'] == "Slow-Slow") & (df["Voltage supply (V)"] == 1.7), "Minimum active power (uW)"])
    max_on_pwr = np.array(df.loc[(df['Process corner'] == "Slow-Slow") & (df["Voltage supply (V)"] == 1.7), "Maximum active power (uW)"])
    axs_on_pwr.plot(temperatures, mean_on_pwr, linestyle="solid", marker="o", markersize=5, label=f"ssVl")
    
    off_pwr = np.array(df.loc[(df['Process corner'] == "Slow-Slow") & (df["Voltage supply (V)"] == 1.7), "Sleep power (uW)"])
    axs_off_pwr.plot(temperatures, off_pwr, marker="o", label=f"ssVl")

    axs_dac.plot(ts_ssVl, dac_code_ssVl, marker="o", label=f"ssVl")
    # axs_dac_0p.plot(ts_ssVl, coarse_code_ssVl, linestyle="dashed", marker="s")
    # axs_dac_0p.plot(ts_ssVl, fine_code_ssVl, linestyle="dotted", marker="v")

    start_up_times_ss = np.array(df.loc[(df['Process corner'] == "Slow-Slow") & (df["Voltage supply (V)"] == 1.7), "Start-up time (us)"])

    axs_start_up.plot(temperatures, start_up_times_ss, marker="o", label=f"ssVl")


    axs_v_0p.set_title(f"Reference voltage", fontsize=title_font_size, fontweight='bold')
    axs_v_0p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_0p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_0p.legend(loc="best", fontsize=legend_font_size)
    axs_v_0p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_0p.grid()

    fig_v_0p.tight_layout()
    fig_v_0p.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_uncalibrated_temperature_vs_reference_voltage.png", dpi=300, bbox_inches="tight")


    axs_dac.set_title(f"DAC input", fontsize=title_font_size, fontweight='bold')
    axs_dac.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_dac.set_ylabel("DAC code", fontsize=label_font_size)
    axs_dac.legend(loc="best", fontsize=legend_font_size)
    axs_dac.tick_params(axis='both', labelsize=ticks_font_size)
    axs_dac.grid()

    fig_dac.tight_layout()
    fig_dac.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_uncalibrated_temperature_vs_dac_code.png", dpi=300, bbox_inches="tight")


    axs_v_1p.set_title(f"Reference voltage 1 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_1p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_1p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_1p.legend(loc="best", fontsize=legend_font_size)
    axs_v_1p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_1p.grid()

    fig_v_1p.tight_layout()
    fig_v_1p.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_onepointcalibrated_temperature_vs_reference_voltage.png", dpi=300, bbox_inches="tight")

    
    axs_v_2p.set_title(f"Reference voltage 2 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_2p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_2p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_2p.legend(loc="best", fontsize=legend_font_size)
    axs_v_2p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_2p.grid()

    fig_v_2p.tight_layout()
    fig_v_2p.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_twopointcalibrated_temperature_vs_reference_voltage.png", dpi=300, bbox_inches="tight")


    axs_on_pwr.set_title(f"Active power consumption", fontsize=title_font_size, fontweight='bold')
    axs_on_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_on_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_on_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_on_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_on_pwr.grid()

    fig_on_pwr.tight_layout()
    fig_on_pwr.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_temperature_vs_active_power.png", dpi=300, bbox_inches="tight")

    axs_off_pwr.set_title(f"Sleep power consumption", fontsize=title_font_size, fontweight='bold')
    axs_off_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_off_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_off_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_off_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_off_pwr.grid()

    fig_off_pwr.tight_layout()
    fig_off_pwr.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_temperature_vs_sleep_power.png", dpi=300, bbox_inches="tight")

    axs_start_up.set_title(f"Start up time", fontsize=title_font_size, fontweight='bold')
    axs_start_up.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_start_up.set_ylabel("Time (us)", fontsize=label_font_size)
    axs_start_up.legend(loc="best", fontsize=legend_font_size)
    axs_start_up.tick_params(axis='both', labelsize=ticks_font_size)
    axs_start_up.grid()

    fig_start_up.tight_layout()
    fig_start_up.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_temperature_vs_start_up_time.png", dpi=300, bbox_inches="tight")
