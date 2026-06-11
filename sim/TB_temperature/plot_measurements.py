import numpy as np
import pandas as pd    
import matplotlib.pyplot as plt
import sys
import seaborn as sns

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
font_size = 10
title_font_size = font_size
label_font_size = font_size
legend_font_size = font_size - 1
ticks_font_size = font_size


if args[-1] == "ttvtetc":

    fig_v_0p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_0p = fig_v_0p.add_subplot(1, 1, 1)

    fig_v_1p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_1p = fig_v_1p.add_subplot(1, 1, 1)

    fig_v_2p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_2p = fig_v_2p.add_subplot(1, 1, 1)

    fig_dac = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_dac = fig_dac.add_subplot(1, 1, 1)

    fig_d_1p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_d_1p = fig_d_1p.add_subplot(1, 1, 1)

    fig_d_2p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_d_2p = fig_d_2p.add_subplot(1, 1, 1)

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

    nocalibrationlist = []
    onepointcalibrationlist = []
    twopointcalibrationlist = []

    dac_nocalibrationlist = []
    dac_onepointcalibrationlist = []
    dac_twopointcalibrationlist = []

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
            # temperature sensitive voltage on the output
            #

            ts = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage), "Temperature (°C)"])
            vs = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage), "Output voltage (V)"])
            print(ts)
            print(vs)

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

            nocalibrationlist.append(vs)

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

            onepointcalibrationlist.append(onepointcalibrated_vs)

            # 
            # 2 point calibrate the voltages at calibration_t1 and calibration_t2
            # 

            calibration_t1 = 0
            calibration_t2 = 80

            # Target values: what the tt/1.8V curve reads at each calibration temperature
            target_v1 = np.array(df.loc[(df['Process corner'] == "Fast-Slow") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
            target_v2 = np.array(df.loc[(df['Process corner'] == "Fast-Slow") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])

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

            twopointcalibrationlist.append(twopointcalibrated_vs)

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

            dac_nocalibrationlist.append(dac_code)

            # 
            # 1 point calibrate the dac codes at the calibration_dac_t degrees Celsius
            # 

            calibration_dac_t = 40 # in degrees Celsius

            # target_coarse_code = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t), "Coarse code"])
            # target_fine_code = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t), "Fine code"])
            # target_coarse_code = target_coarse_code * 1e3 # in whole numbers
            # target_fine_code = target_fine_code * 1e3 # in whole numbers
            # target_d = target_coarse_code * 10 + target_fine_code
            target_d = 50

            actual_coarse_code = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_dac_t), "Coarse code"])
            actual_fine_code = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_dac_t), "Fine code"])
            actual_coarse_code = actual_coarse_code * 1e3 # in whole numbers
            actual_fine_code = actual_fine_code * 1e3 # in whole numbers
            actual_d = actual_coarse_code * 10 + actual_fine_code

            onepointcalibrated_ds = [d + (target_d - actual_d) for d in dac_code]

            mean_v_onepointcalibrated = np.mean(onepointcalibrated_ds)
            tc_onepointcalibrated = (np.max(onepointcalibrated_ds) - np.min(onepointcalibrated_ds)) / (np.max(ts) - np.min(ts)) # in V/°C
            print(f"{process_corner}{Vx} 1pc TC: {tc_onepointcalibrated:.4f} -/°C")

            axs_d_1p.plot(ts, onepointcalibrated_ds, marker="o", label=f"{corner}{Vx}")

            dac_onepointcalibrationlist.append(onepointcalibrated_ds)

            # 
            # 2 point calibrate the dac codes at calibration_dac_t1 and calibration_dac_t2 degrees Celsius
            # 

            calibration_dac_t1 = 0
            calibration_dac_t2 = 80

            target_coarse_code1 = np.array(df.loc[(df['Process corner'] == "Fast-Slow") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_dac_t1), "Coarse code"])
            target_fine_code1 = np.array(df.loc[(df['Process corner'] == "Fast-Slow") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_dac_t1), "Fine code"])
            target_coarse_code1 = target_coarse_code1 * 1e3 # in whole numbers
            target_fine_code1 = target_fine_code1 * 1e3 # in whole numbers
            target_d1 = target_coarse_code1 * 10 + target_fine_code1

            target_coarse_code2 = np.array(df.loc[(df['Process corner'] == "Fast-Slow") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_dac_t2), "Coarse code"])
            target_fine_code2 = np.array(df.loc[(df['Process corner'] == "Fast-Slow") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_dac_t2), "Fine code"])
            target_coarse_code2 = target_coarse_code2 * 1e3 # in whole numbers
            target_fine_code2 = target_fine_code2 * 1e3 # in whole numbers
            target_d2 = target_coarse_code2 * 10 + target_fine_code2

            
            
            twopointcalibrated_ds = []
            for d, t in zip(dac_code, ts):

                actual_coarse_code1 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_dac_t1), "Coarse code"])    
                actual_fine_code1 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_dac_t1), "Fine code"])
                actual_coarse_code1 = actual_coarse_code1 * 1e3 # in whole numbers
                actual_fine_code1 = actual_fine_code1 * 1e3 # in whole numbers
                actual_d1 = actual_coarse_code1 * 10 + actual_fine_code1

                actual_coarse_code2 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_dac_t2), "Coarse code"])
                actual_fine_code2 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_dac_t2), "Fine code"])
                actual_coarse_code2 = actual_coarse_code2 * 1e3 # in whole numbers
                actual_fine_code2 = actual_fine_code2 * 1e3 # in whole numbers
                actual_d2 = actual_coarse_code2 * 10 + actual_fine_code2

                offset1 = target_d1 - actual_d1
                offset2 = target_d2 - actual_d2

                offset = offset1 + (offset2 - offset1) * (t - calibration_dac_t1) / (calibration_dac_t2 - calibration_dac_t1)
                twopointcalibrated_d = d + offset
                twopointcalibrated_ds.append(twopointcalibrated_d)

            axs_d_2p.plot(ts, twopointcalibrated_ds, marker="o", label=f"{corner}{Vx}")

            dac_twopointcalibrationlist.append(twopointcalibrated_ds)

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

    print(f"Typical  Vt 0pc: Mean voltage: {mean_v_ttVt:.4f} V, TC: {tc_ttVt:.4f} V/°C, TC in mV/°C {tc_ttVt_in_mV_per_C:.2f}, TC in ppm/°C: {tc_ttVt_in_ppm:.2f}")

    mean_on_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Mean active power (uW)"])
    min_on_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Minimum active power (uW)"])
    max_on_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Maximum active power (uW)"])
    axs_on_pwr.plot(temperatures, mean_on_pwr, linestyle="solid", marker="o", markersize=5, label=f"ttVt")
    off_pwr = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Sleep power (uW)"])
    axs_off_pwr.plot(temperatures, off_pwr, marker="o", label=f"ttVt")

    axs_v_0p.plot(ts_ttVt, vs_ttVt, marker="o", label=f"ttVt")

    nocalibrationlist.append(vs_ttVt)

    ts_fit = np.array(temperatures)
    vs2p = nocalibrationlist

    vs = np.array(vs2p)
    vs = vs.squeeze()  
    means = vs.mean(axis=0)

    slope, intercept, r_value, _, _ = stats.linregress(ts_fit, means)
    linear_fit = slope * ts_fit + intercept

    print(f"means: {means}")
    print(f"V 0p mean linear fit: slope={slope:.4f} /°C, intercept={intercept:.2f}, R²={r_value**2:.6f}")

    axs_v_0p.plot(ts_fit, means,       marker="o", linestyle="none", label="Mean")
    axs_v_0p.plot(ts_fit, linear_fit,  linestyle="--",               label=f"Lin. fit")

    residuals = means - linear_fit            # deviation at each x-point
    max_dev = np.max(np.abs(residuals))       # largest deviation (magnitude)
    idx = np.argmax(np.abs(residuals))        # which x-point it occurs at
    print(f"residuals: {residuals}")
    print(f"Max deviation: {max_dev:.4f} at temp = {ts_fit[idx]} (residual = {residuals[idx]:+.4f})")
    
    all_residuals = vs - linear_fit                     # shape (n_curves, 5)

    flat_idx = np.argmax(np.abs(all_residuals))         # index into the flattened array
    curve_idx, t_idx = np.unravel_index(flat_idx, all_residuals.shape)

    max_dev_v = vs[curve_idx, t_idx]                    # the voltage itself
    max_dev_t = ts_fit[t_idx]                           # temperature where it happens
    max_dev = all_residuals[curve_idx, t_idx]           # signed deviation

    print(f"Max deviation from fit: {np.abs(max_dev)*1e3:.2f} mV "
        f"(voltage = {max_dev_v:.4f} V, curve #{curve_idx}, at {max_dev_t} °C, residual = {max_dev:+.4f})")
    print()

    # vs = []
    # for temperature in temperatures:
    #     v = np.array(df.loc[(df["Temperature (°C)"] == temperature), "Output voltage (V)"])
    #     v = [x for x in v if x == x]
    #     vs.append(np.mean(v))

    # means = np.array(vs)
    # ts_fit = np.array(temperatures)

    # slope, intercept, r_value, _, _ = stats.linregress(ts_fit, vs)
    # linear_fit = slope * ts_fit + intercept


    # print(f"means: {means}")
    # print(f"V 0p mean linear fit: slope={slope:.4f} /°C, intercept={intercept:.2f}, R²={r_value**2:.6f}")

    # axs_v_0p.plot(ts_fit, means,       marker="o", linestyle="none", label="Mean")
    # axs_v_0p.plot(ts_fit, linear_fit,  linestyle="--",               label=f"Lin. fit")

    # residuals = means - linear_fit            # deviation at each x-point
    # max_dev = np.max(np.abs(residuals))       # largest deviation (magnitude)
    # idx = np.argmax(np.abs(residuals))        # which x-point it occurs at

    # print(f"Max deviation: {max_dev:.4f} at temp = {ts_fit[idx]} (residual = {residuals[idx]:+.4f})")

    axs_v_1p.plot(ts_ttVt, vs_ttVt, marker="o", label=f"ttVt")

    onepointcalibrationlist.append(vs_ttVt)

    ts_fit = np.array(temperatures)
    vs1p = onepointcalibrationlist

    vs = np.array([np.asarray(curve, dtype=float).ravel() for curve in vs1p])
    means = vs.mean(axis=0)

    slope, intercept, r_value, _, _ = stats.linregress(ts_fit, means)
    linear_fit = slope * ts_fit + intercept

    print(f"means: {means}")
    print(f"V 1p mean linear fit: slope={slope:.4f} /°C, intercept={intercept:.2f}, R²={r_value**2:.6f}")

    axs_v_1p.plot(ts_fit, means,       marker="o", linestyle="none", label="Mean")
    axs_v_1p.plot(ts_fit, linear_fit,  linestyle="--",               label=f"Lin. fit")

    residuals = means - linear_fit            # deviation at each x-point
    max_dev = np.max(np.abs(residuals))       # largest deviation (magnitude)
    idx = np.argmax(np.abs(residuals))        # which x-point it occurs at

    print(f"Max deviation: {max_dev:.4f} at temp = {ts_fit[idx]} (residual = {residuals[idx]:+.4f})")
    all_residuals = vs - linear_fit                     # shape (n_curves, 5)

    flat_idx = np.argmax(np.abs(all_residuals))         # index into the flattened array
    curve_idx, t_idx = np.unravel_index(flat_idx, all_residuals.shape)

    max_dev_v = vs[curve_idx, t_idx]                    # the voltage itself
    max_dev_t = ts_fit[t_idx]                           # temperature where it happens
    max_dev = all_residuals[curve_idx, t_idx]           # signed deviation

    print(f"Max deviation from fit: {np.abs(max_dev)*1e3:.2f} mV "
        f"(voltage = {max_dev_v:.4f} V, curve #{curve_idx}, at {max_dev_t} °C, residual = {max_dev:+.4f})")
    print()

    calibration_t1 = 0
    calibration_t2 = 80

    # Target values: what the tt/1.8V curve reads at each calibration temperature
    target_v1 = np.array(df.loc[(df['Process corner'] == "Fast-Slow") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_t1), "Output voltage (V)"])
    target_v2 = np.array(df.loc[(df['Process corner'] == "Fast-Slow") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_t2), "Output voltage (V)"])


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

    twopointcalibrationlist.append(twopointcalibrated_vs)

    ts_fit = np.array(temperatures)
    vs2p = twopointcalibrationlist

    vs = np.array(vs2p)
    vs = vs.squeeze()  
    means = vs.mean(axis=0)

    slope, intercept, r_value, _, _ = stats.linregress(ts_fit, means)
    linear_fit = slope * ts_fit + intercept

    print(f"means: {means}")
    print(f"V 2p mean linear fit: slope={slope:.4f} /°C, intercept={intercept:.2f}, R²={r_value**2:.6f}")

    axs_v_2p.plot(ts_fit, means,       marker="o", linestyle="none", label="Mean")
    axs_v_2p.plot(ts_fit, linear_fit,  linestyle="--",               label=f"Lin. fit")

    residuals = means - linear_fit            # deviation at each x-point
    max_dev = np.max(np.abs(residuals))       # largest deviation (magnitude)
    idx = np.argmax(np.abs(residuals))        # which x-point it occurs at

    print(f"Max deviation: {max_dev:.4f} at temp = {ts_fit[idx]} (residual = {residuals[idx]:+.4f})")
    all_residuals = vs - linear_fit                     # shape (n_curves, 5)

    flat_idx = np.argmax(np.abs(all_residuals))         # index into the flattened array
    curve_idx, t_idx = np.unravel_index(flat_idx, all_residuals.shape)

    max_dev_v = vs[curve_idx, t_idx]                    # the voltage itself
    max_dev_t = ts_fit[t_idx]                           # temperature where it happens
    max_dev = all_residuals[curve_idx, t_idx]           # signed deviation

    print(f"Max deviation from fit: {np.abs(max_dev)*1e3:.2f} mV "
        f"(voltage = {max_dev_v:.4f} V, curve #{curve_idx}, at {max_dev_t} °C, residual = {max_dev:+.4f})")
    print()


    axs_dac.plot(ts_ttVt, dac_code_ttVt, marker="o", label=f"ttVt")

    dac_nocalibrationlist.append(dac_code_ttVt)   # add the ttVt curve like you do for voltages

    ds = []
    for temperature in temperatures:
        c = np.array(df.loc[(df["Temperature (°C)"] == temperature), "Coarse code"])
        f = np.array(df.loc[(df["Temperature (°C)"] == temperature), "Fine code"])
        c = c * 1e3
        f = f * 1e3
        d = c * 10 + f
        d = [x for x in d if x == x]
        ds.append(np.mean(d))

    ds = np.array(ds)
    ts_fit = np.array(temperatures)
    means = ds

    slope, intercept, r_value, _, _ = stats.linregress(ts_fit, ds)
    linear_fit = slope * ts_fit + intercept

    print(f"DAC 0p mean linear fit: slope={slope:.4f} /°C, intercept={intercept:.2f}, R²={r_value**2:.6f}")

    axs_dac.plot(ts_fit, ds,          marker="o", linestyle="none", label="Mean")
    axs_dac.plot(ts_fit, linear_fit,  linestyle="--",               label=f"Lin. fit")

    residuals = means - linear_fit            # deviation at each x-point
    max_dev = np.max(np.abs(residuals))       # largest deviation (magnitude)
    idx = np.argmax(np.abs(residuals))        # which x-point it occurs at

    print(f"Max deviation: {max_dev:.4f} at temp = {ts_fit[idx]} (residual = {residuals[idx]:+.4f})")
    ds_all = np.array([np.asarray(c, dtype=float).ravel() for c in dac_nocalibrationlist])

    all_residuals = ds_all - linear_fit           # (n_curves, 5) - (5,) → 2D                     # shape (n_curves, 5)

    flat_idx = np.argmax(np.abs(all_residuals))         # index into the flattened array
    curve_idx, t_idx = np.unravel_index(flat_idx, all_residuals.shape)

    max_dev_v = ds_all[curve_idx, t_idx]
    max_dev_t = ts_fit[t_idx]                           # temperature where it happens
    max_dev = all_residuals[curve_idx, t_idx]           # signed deviation

    print(f"Max deviation from fit: {np.abs(max_dev):.2f} codes "
      f"(dac code = {max_dev_v:.1f}, curve #{curve_idx}, at {max_dev_t} °C, residual = {max_dev:+.2f})")
    print()


    # axs_dac_0p.plot(ts_ttVt, coarse_code_ttVt, linestyle="dashed", marker="s")
    # axs_dac_0p.plot(ts_ttVt, fine_code_ttVt, linestyle="dotted", marker="v")
    # axs_d_1p.plot(ts_ttVt, dac_code_ttVt, marker="o", label=f"ttVt")

    calibration_dac_t = 40 # in degrees Celsius

    # target_coarse_code = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t), "Coarse code"])
    # target_fine_code = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t), "Fine code"])
    # target_coarse_code = target_coarse_code * 1e3 # in whole numbers
    # target_fine_code = target_fine_code * 1e3 # in whole numbers
    # target_d = target_coarse_code * 10 + target_fine_code
    target_d = 50

    actual_coarse_code = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t), "Coarse code"])
    actual_fine_code = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t), "Fine code"])
    actual_coarse_code = actual_coarse_code * 1e3 # in whole numbers
    actual_fine_code = actual_fine_code * 1e3 # in whole numbers
    actual_d = actual_coarse_code * 10 + actual_fine_code

    onepointcalibrated_ds = [d + (target_d - actual_d) for d in dac_code_ttVt]

    mean_v_onepointcalibrated = np.mean(onepointcalibrated_ds)
    tc_onepointcalibrated = (np.max(onepointcalibrated_ds) - np.min(onepointcalibrated_ds)) / (np.max(ts) - np.min(ts)) # in V/°C
    print(f"{process_corner}{Vx} 1pc TC: {tc_onepointcalibrated:.4f} -/°C")

    axs_d_1p.plot(ts, onepointcalibrated_ds, marker="o", label=f"ttVt")
    # axs_d_1p.plot(ts_fit, ds,          marker="o", linestyle="none", label="Mean")
    # axs_d_1p.plot(ts_fit, linear_fit,  linestyle="--",               label=f"Lin. fit")

    dac_onepointcalibrationlist.append(onepointcalibrated_ds)

    ts_fit = np.array(temperatures)
    ds = dac_onepointcalibrationlist

    ds = np.array(ds)
    ds = ds.squeeze()  
    means = ds.mean(axis=0)

    slope, intercept, r_value, _, _ = stats.linregress(ts_fit, means)
    linear_fit = slope * ts_fit + intercept

    print(f"means: {means}")
    print(f"DAC 1p mean linear fit: slope={slope:.4f} /°C, intercept={intercept:.2f}, R²={r_value**2:.6f}")

    axs_d_1p.plot(ts_fit, means,       marker="o", linestyle="none", label="Mean")
    axs_d_1p.plot(ts_fit, linear_fit,  linestyle="--",               label=f"Lin. fit")

    residuals = means - linear_fit            # deviation at each x-point
    max_dev = np.max(np.abs(residuals))       # largest deviation (magnitude)
    idx = np.argmax(np.abs(residuals))        # which x-point it occurs at

    print(f"Max deviation: {max_dev:.4f} at temp = {ts_fit[idx]} (residual = {residuals[idx]:+.4f})")
    all_residuals = ds - linear_fit                     # shape (n_curves, 5)

    flat_idx = np.argmax(np.abs(all_residuals))         # index into the flattened array
    curve_idx, t_idx = np.unravel_index(flat_idx, all_residuals.shape)

    max_dev_v = ds[curve_idx, t_idx]                    # the voltage itself
    max_dev_t = ts_fit[t_idx]                           # temperature where it happens
    max_dev = all_residuals[curve_idx, t_idx]           # signed deviation

    print(f"Max deviation from fit: {np.abs(max_dev):.2f} codes "
      f"(dac code = {max_dev_v:.1f}, curve #{curve_idx}, at {max_dev_t} °C, residual = {max_dev:+.2f})")
    print()


    # axs_d_2p.plot(ts_ttVt, dac_code_ttVt_two_point_calibrated, marker="o", label=f"ttVt")

    coarse_code = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Coarse code"])
    fine_code = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Fine code"])
    coarse_code = coarse_code * 1e3 # in whole numbers
    fine_code = fine_code * 1e3 # in whole numbers
    dac_code = coarse_code * 10 + fine_code

    calibration_dac_t1 = 0
    calibration_dac_t2 = 80

    target_coarse_code1 = np.array(df.loc[(df['Process corner'] == "Fast-Slow") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_dac_t1), "Coarse code"])
    target_fine_code1 = np.array(df.loc[(df['Process corner'] == "Fast-Slow") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_dac_t1), "Fine code"])
    target_coarse_code1 = target_coarse_code1 * 1e3 # in whole numbers
    target_fine_code1 = target_fine_code1 * 1e3 # in whole numbers
    target_d1 = target_coarse_code1 * 10 + target_fine_code1

    target_coarse_code2 = np.array(df.loc[(df['Process corner'] == "Fast-Slow") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_dac_t2), "Coarse code"])
    target_fine_code2 = np.array(df.loc[(df['Process corner'] == "Fast-Slow") & (df["Voltage supply (V)"] == 1.9) & (df["Temperature (°C)"] == calibration_dac_t2), "Fine code"])
    target_coarse_code2 = target_coarse_code2 * 1e3 # in whole numbers
    target_fine_code2 = target_fine_code2 * 1e3 # in whole numbers
    target_d2 = target_coarse_code2 * 10 + target_fine_code2


    twopointcalibrated_ds = []
    for d, t in zip(dac_code, ts):

        actual_coarse_code1 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t1), "Coarse code"])    
        actual_fine_code1 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t1), "Fine code"])
        actual_coarse_code1 = actual_coarse_code1 * 1e3 # in whole numbers
        actual_fine_code1 = actual_fine_code1 * 1e3 # in whole numbers
        actual_d1 = actual_coarse_code1 * 10 + actual_fine_code1

        actual_coarse_code2 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t2), "Coarse code"])
        actual_fine_code2 = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t2), "Fine code"])
        actual_coarse_code2 = actual_coarse_code2 * 1e3 # in whole numbers
        actual_fine_code2 = actual_fine_code2 * 1e3 # in whole numbers
        actual_d2 = actual_coarse_code2 * 10 + actual_fine_code2

        offset1 = target_d1 - actual_d1
        offset2 = target_d2 - actual_d2

        offset = offset1 + (offset2 - offset1) * (t - calibration_dac_t1) / (calibration_dac_t2 - calibration_dac_t1)
        twopointcalibrated_d = d + offset
        twopointcalibrated_ds.append(twopointcalibrated_d)

    
    axs_d_2p.plot(ts, twopointcalibrated_ds, marker="o", label=f"ttVt")

    dac_twopointcalibrationlist.append(twopointcalibrated_ds)

    ts_fit = np.array(temperatures)
    ds = dac_twopointcalibrationlist

    ds = np.array(ds)
    ds = ds.squeeze()  
    means = ds.mean(axis=0)

    slope, intercept, r_value, _, _ = stats.linregress(ts_fit, means)
    linear_fit = slope * ts_fit + intercept

    print(f"means: {means}")
    print(f"DAC 2p mean linear fit: slope={slope:.4f} /°C, intercept={intercept:.2f}, R²={r_value**2:.6f}")

    axs_d_2p.plot(ts_fit, means,       marker="o", linestyle="none", label="Mean")
    axs_d_2p.plot(ts_fit, linear_fit,  linestyle="--",               label=f"Lin. fit")

    residuals = means - linear_fit            # deviation at each x-point
    max_dev = np.max(np.abs(residuals))       # largest deviation (magnitude)
    idx = np.argmax(np.abs(residuals))        # which x-point it occurs at

    print(f"Max deviation: {max_dev:.4f} at temp = {ts_fit[idx]} (residual = {residuals[idx]:+.4f})")
    all_residuals = ds - linear_fit                     # shape (n_curves, 5)

    flat_idx = np.argmax(np.abs(all_residuals))         # index into the flattened array
    curve_idx, t_idx = np.unravel_index(flat_idx, all_residuals.shape)

    max_dev_v = ds[curve_idx, t_idx]                    # the voltage itself
    max_dev_t = ts_fit[t_idx]                           # temperature where it happens
    max_dev = all_residuals[curve_idx, t_idx]           # signed deviation

    print(f"Max deviation from fit: {np.abs(max_dev):.2f} codes "
      f"(dac code = {max_dev_v:.1f}, curve #{curve_idx}, at {max_dev_t} °C, residual = {max_dev:+.2f})")
    print()



    start_up_times_tt = np.array(df.loc[(df['Process corner'] == "Typical") & (df["Voltage supply (V)"] == 1.8), "Start-up time (us)"])
    axs_start_up.plot(temperatures, start_up_times_tt, marker="o", label=f"ttVt")


    axs_v_0p.set_title(f"Temperature sensitivity", fontsize=title_font_size, fontweight='bold')
    axs_v_0p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_0p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_0p.legend(loc="best", ncol=2, fontsize=legend_font_size)
    axs_v_0p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_0p.grid()

    fig_v_0p.tight_layout()
    fig_v_0p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_uncalibrated_temperature_vs_temperature_sensitive_voltage.png", dpi=300, bbox_inches="tight")

    axs_v_1p.set_title(f"Temperature sensitivity 1 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_1p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_1p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_1p.legend(loc="best", ncol=2, fontsize=legend_font_size)
    axs_v_1p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_1p.grid()

    fig_v_1p.tight_layout()
    fig_v_1p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_onepointcalibrated_temperature_vs_temperature_sensitive_voltage.png", dpi=300, bbox_inches="tight")
    
    axs_v_2p.set_title(f"Temperature sensitivity 2 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_2p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_2p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_2p.legend(loc="best", ncol=2, fontsize=legend_font_size)
    axs_v_2p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_2p.grid()

    fig_v_2p.tight_layout()
    fig_v_2p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_twopointcalibrated_temperature_vs_temperature_sensitive_voltage.png", dpi=300, bbox_inches="tight")


    axs_dac.set_title(f"DAC input", fontsize=title_font_size, fontweight='bold')
    axs_dac.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_dac.set_ylabel("DAC code", fontsize=label_font_size)
    axs_dac.legend(loc="best", ncol=2, fontsize=legend_font_size)
    axs_dac.tick_params(axis='both', labelsize=ticks_font_size)
    axs_dac.grid()

    fig_dac.tight_layout()
    fig_dac.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_uncalibrated_temperature_vs_dac_code.png", dpi=300, bbox_inches="tight")

    axs_d_1p.set_title(f"DAC input 1 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_d_1p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_d_1p.set_ylabel("DAC code", fontsize=label_font_size)
    axs_d_1p.legend(loc="best", ncol=2, fontsize=legend_font_size)
    axs_d_1p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_d_1p.grid()

    fig_d_1p.tight_layout()
    fig_d_1p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_onepointcalibrated_temperature_vs_dac_code.png", dpi=300, bbox_inches="tight")
    
    axs_d_2p.set_title(f"DAC input 2 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_d_2p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_d_2p.set_ylabel("DAC code", fontsize=label_font_size)
    axs_d_2p.legend(loc="best", ncol=2, fontsize=legend_font_size)
    axs_d_2p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_d_2p.grid()

    fig_d_2p.tight_layout()
    fig_d_2p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_twopointcalibrated_temperature_vs_dac_code.png", dpi=300, bbox_inches="tight")

    axs_on_pwr.set_title(f"Active power consumption", fontsize=title_font_size, fontweight='bold')
    axs_on_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_on_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_on_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_on_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_on_pwr.grid()

    fig_on_pwr.tight_layout()
    fig_on_pwr.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_temperature_vs_active_power.png", dpi=300, bbox_inches="tight")

    axs_off_pwr.set_yscale("log")
    axs_off_pwr.set_title(f"Sleep power consumption", fontsize=title_font_size, fontweight='bold')
    axs_off_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_off_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_off_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_off_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_off_pwr.grid()

    fig_off_pwr.tight_layout()
    fig_off_pwr.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_temperature_vs_sleep_power.png", dpi=300, bbox_inches="tight")

    axs_start_up.set_title(f"Start up time", fontsize=title_font_size, fontweight='bold')
    axs_start_up.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_start_up.set_ylabel("Time (us)", fontsize=label_font_size)
    axs_start_up.legend(loc="best", fontsize=legend_font_size)
    axs_start_up.tick_params(axis='both', labelsize=ticks_font_size)
    axs_start_up.grid()

    fig_start_up.tight_layout()
    fig_start_up.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_temperature_vs_start_up_time.png", dpi=300, bbox_inches="tight")



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


    axs_v_0p.set_title(f"Temperature sensitivity", fontsize=title_font_size, fontweight='bold')
    axs_v_0p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_0p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_0p.legend(loc="best", fontsize=legend_font_size)
    axs_v_0p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_0p.grid()

    fig_v_0p.tight_layout()
    fig_v_0p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_uncalibrated_temperature_vs_temperature_sensitive_voltage.png", dpi=300, bbox_inches="tight")


    axs_dac.set_title(f"DAC input", fontsize=title_font_size, fontweight='bold')
    axs_dac.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_dac.set_ylabel("DAC code", fontsize=label_font_size)
    axs_dac.legend(loc="best", fontsize=legend_font_size)
    axs_dac.tick_params(axis='both', labelsize=ticks_font_size)
    axs_dac.grid()

    fig_dac.tight_layout()
    fig_dac.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_uncalibrated_temperature_vs_dac_code.png", dpi=300, bbox_inches="tight")


    axs_v_1p.set_title(f"Temperature sensitivity 1 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_1p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_1p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_1p.legend(loc="best", fontsize=legend_font_size)
    axs_v_1p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_1p.grid()

    fig_v_1p.tight_layout()
    fig_v_1p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_onepointcalibrated_temperature_vs_temperature_sensitive_voltage.png", dpi=300, bbox_inches="tight")

    
    axs_v_2p.set_title(f"Temperature sensitivity 2 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_2p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_2p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_2p.legend(loc="best", fontsize=legend_font_size)
    axs_v_2p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_2p.grid()

    fig_v_2p.tight_layout()
    fig_v_2p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_twopointcalibrated_temperature_vs_temperature_sensitive_voltage.png", dpi=300, bbox_inches="tight")


    axs_on_pwr.set_title(f"Active power consumption", fontsize=title_font_size, fontweight='bold')
    axs_on_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_on_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_on_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_on_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_on_pwr.grid()

    fig_on_pwr.tight_layout()
    fig_on_pwr.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_temperature_vs_active_power.png", dpi=300, bbox_inches="tight")

    axs_off_pwr.set_yscale("log")
    axs_off_pwr.set_title(f"Sleep power consumption", fontsize=title_font_size, fontweight='bold')
    axs_off_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_off_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_off_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_off_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_off_pwr.grid()

    fig_off_pwr.tight_layout()
    fig_off_pwr.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_temperature_vs_sleep_power.png", dpi=300, bbox_inches="tight")

    axs_start_up.set_title(f"Start up time", fontsize=title_font_size, fontweight='bold')
    axs_start_up.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_start_up.set_ylabel("Time (us)", fontsize=label_font_size)
    axs_start_up.legend(loc="best", fontsize=legend_font_size)
    axs_start_up.tick_params(axis='both', labelsize=ticks_font_size)
    axs_start_up.grid()

    fig_start_up.tight_layout()
    fig_start_up.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_temperature_vs_start_up_time.png", dpi=300, bbox_inches="tight")


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


    axs_v_0p.set_title(f"Temperature sensitivity", fontsize=title_font_size, fontweight='bold')
    axs_v_0p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_0p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_0p.legend(loc="best", fontsize=legend_font_size)
    axs_v_0p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_0p.grid()

    fig_v_0p.tight_layout()
    fig_v_0p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_uncalibrated_temperature_vs_temperature_sensitive_voltage.png", dpi=300, bbox_inches="tight")


    axs_dac.set_title(f"DAC input", fontsize=title_font_size, fontweight='bold')
    axs_dac.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_dac.set_ylabel("DAC code", fontsize=label_font_size)
    axs_dac.legend(loc="best", fontsize=legend_font_size)
    axs_dac.tick_params(axis='both', labelsize=ticks_font_size)
    axs_dac.grid()

    fig_dac.tight_layout()
    fig_dac.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_uncalibrated_temperature_vs_dac_code.png", dpi=300, bbox_inches="tight")


    axs_v_1p.set_title(f"Temperature sensitivity 1 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_1p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_1p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_1p.legend(loc="best", fontsize=legend_font_size)
    axs_v_1p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_1p.grid()

    fig_v_1p.tight_layout()
    fig_v_1p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_onepointcalibrated_temperature_vs_temperature_sensitive_voltage.png", dpi=300, bbox_inches="tight")

    
    axs_v_2p.set_title(f"Temperature sensitivity 2 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_2p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_2p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_2p.legend(loc="best", fontsize=legend_font_size)
    axs_v_2p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_2p.grid()

    fig_v_2p.tight_layout()
    fig_v_2p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_twopointcalibrated_temperature_vs_temperature_sensitive_voltage.png", dpi=300, bbox_inches="tight")


    axs_on_pwr.set_title(f"Active power consumption", fontsize=title_font_size, fontweight='bold')
    axs_on_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_on_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_on_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_on_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_on_pwr.grid()

    fig_on_pwr.tight_layout()
    fig_on_pwr.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_temperature_vs_active_power.png", dpi=300, bbox_inches="tight")

    axs_off_pwr.set_yscale("log")
    axs_off_pwr.set_title(f"Sleep power consumption", fontsize=title_font_size, fontweight='bold')
    axs_off_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_off_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_off_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_off_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_off_pwr.grid()

    fig_off_pwr.tight_layout()
    fig_off_pwr.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_temperature_vs_sleep_power.png", dpi=300, bbox_inches="tight")

    axs_start_up.set_title(f"Start up time", fontsize=title_font_size, fontweight='bold')
    axs_start_up.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_start_up.set_ylabel("Time (us)", fontsize=label_font_size)
    axs_start_up.legend(loc="best", fontsize=legend_font_size)
    axs_start_up.tick_params(axis='both', labelsize=ticks_font_size)
    axs_start_up.grid()

    fig_start_up.tight_layout()
    fig_start_up.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_temperature_vs_start_up_time.png", dpi=300, bbox_inches="tight")


mc_runs = 30
if args[-1] == "mc":

    fig_v_0p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_0p = fig_v_0p.add_subplot(1, 1, 1)

    fig_v_1p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_1p = fig_v_1p.add_subplot(1, 1, 1)

    fig_v_2p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_v_2p = fig_v_2p.add_subplot(1, 1, 1)

    fig_dac = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_dac = fig_dac.add_subplot(1, 1, 1)

    fig_d_1p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_d_1p = fig_d_1p.add_subplot(1, 1, 1)

    fig_d_2p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_d_2p = fig_d_2p.add_subplot(1, 1, 1)

    fig_on_pwr = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_on_pwr = fig_on_pwr.add_subplot(1, 1, 1)

    fig_off_pwr = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_off_pwr = fig_off_pwr.add_subplot(1, 1, 1)

    fig_start_up = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_start_up = fig_start_up.add_subplot(1, 1, 1)

    fig_mc_errorbar = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_mc_errorbar = fig_mc_errorbar.add_subplot(1, 1, 1)

    fig_mc_dac_errorbar = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_mc_dac_errorbar = fig_mc_dac_errorbar.add_subplot(1, 1, 1)

    fig_mc_errorbar_1p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_mc_errorbar_1p = fig_mc_errorbar_1p.add_subplot(1, 1, 1)

    fig_mc_dac_errorbar_1p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_mc_dac_errorbar_1p = fig_mc_dac_errorbar_1p.add_subplot(1, 1, 1)



    df = pd.read_csv(f"plotdata/{'_'.join(args)}_stepping_{stepping_direction}.csv")
    print(f"plotdata/{'_'.join(args)}_stepping_{stepping_direction}.csv")


    corner = "ttmm"
    for run in range(0, mc_runs):

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
        elif corner == "ttmm":
            process_corner = "ttmm"
        else:
            process_corner = "Oops, something is wrong!"

        for voltage in [1.8]: # Volt (V)
            Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"

            #
            # Temperature voltage on the output
            #

            ts = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == run), "Temperature (°C)"])
            vs = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == run), "Output voltage (V)"])

            if vs.size == 0:
                continue

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

            axs_v_0p.plot(ts, vs, marker="o", label=f"{run}")
            last_color = axs_v_0p.get_lines()[-1].get_color()
            # axs_v_0p.plot(ts, [avg_v]*len(ts), linestyle="dashed", color=last_color, label=f"mean: {avg_v:.4f} V")
            # axs_v_0p.plot(ts, linear_fit, linestyle="dashed", color=last_color, label=f"Linear fit v={slope*1e3:.2f}t mV/°C + {intercept*1e3:.1f} mV, R²={r_value**2:.4f}")
            # axs_v_0p.plot(avg_v_max_dev_t, avg_v_max_dev_v, linestyle="none", color=last_color, marker="x", markeredgewidth=2, label=f"Max deviation: {avg_v_max_dev_v*1e3:.2f} mV at {avg_v_max_dev_t} °C")

            # 
            # 1 point calibrate the voltages in the calibration_t degrees Celsius voltage as the single point
            # 

            calibration_t = 40 # in degrees Celsius
            target_v = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t) & (df["monte carlo run"] == 1), "Output voltage (V)"])
            actual_v = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_t) & (df["monte carlo run"] == run), "Output voltage (V)"])
            onepointcalibrated_vs = [v + (target_v - actual_v) for v in vs]

            mean_v_onepointcalibrated = np.mean(onepointcalibrated_vs)
            tc_onepointcalibrated = (np.max(onepointcalibrated_vs) - np.min(onepointcalibrated_vs)) / (np.max(ts) - np.min(ts)) # in V/°C
            tc_in_mV_per_C = tc_onepointcalibrated * 1e3 # in mV/°C
            tc_in_ppm = (tc_onepointcalibrated / mean_v_onepointcalibrated) * 1e6 # in ppm/°C relative to average voltage
            print(f"{process_corner}{Vx} 1pc: Mean voltage: {mean_v_onepointcalibrated:.4f} V, TC: {tc_onepointcalibrated:.4f} V/°C, TC in mV/°C {tc_in_mV_per_C:.2f}, TC in ppm/°C: {tc_in_ppm:.2f}")

            axs_v_1p.plot(ts, onepointcalibrated_vs, marker="o", label=f"{run}")

            # 
            # 2 point calibrate the voltages at calibration_t1 and calibration_t2
            # 

            calibration_t1 = 0
            calibration_t2 = 80

            # Target values: what the tt/1.8V curve reads at each calibration temperature
            target_v1 = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t1) & (df["monte carlo run"] == 1), "Output voltage (V)"])
            target_v2 = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_t2) & (df["monte carlo run"] == 1), "Output voltage (V)"])

            twopointcalibrated_vs = []
            for v, t in zip(vs, ts):
                # Actual value of this curve at calibration temperatures (interpolated if needed)
                actual_v1 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_t1) & (df["monte carlo run"] == run), "Output voltage (V)"])
                actual_v2 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_t2) & (df["monte carlo run"] == run), "Output voltage (V)"])

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

            axs_v_2p.plot(ts, twopointcalibrated_vs, marker="o", label=f"{run}")

            #
            # DAC input settings
            #

            coarse_code = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == run), "Coarse code"])
            fine_code = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == run), "Fine code"])
            coarse_code = coarse_code * 1e3 # in whole numbers
            fine_code = fine_code * 1e3 # in whole numbers
            dac_code = coarse_code * 10 + fine_code

            axs_dac.plot(ts, dac_code, marker="o", label=f"{run}")
            last_color = axs_dac.get_lines()[-1].get_color()
            # axs_dac.plot(ts, coarse_code, linestyle="dashed", marker="s", color=last_color)
            # axs_dac.plot(ts, fine_code, linestyle="dotted", marker="v", color=last_color)

            
            # 
            # 1 point calibrate the dac codes at the calibration_dac_t degrees Celsius
            # 

            calibration_dac_t = 40 # in degrees Celsius

            target_coarse_code = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t) & (df["monte carlo run"] == 1), "Coarse code"])
            target_fine_code = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t) & (df["monte carlo run"] == 1), "Fine code"])
            target_coarse_code = target_coarse_code * 1e3 # in whole numbers
            target_fine_code = target_fine_code * 1e3 # in whole numbers
            target_d = target_coarse_code * 10 + target_fine_code

            actual_coarse_code = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_dac_t) & (df["monte carlo run"] == run), "Coarse code"])
            actual_fine_code = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_dac_t) & (df["monte carlo run"] == run), "Fine code"])
            actual_coarse_code = actual_coarse_code * 1e3 # in whole numbers
            actual_fine_code = actual_fine_code * 1e3 # in whole numbers
            actual_d = actual_coarse_code * 10 + actual_fine_code

            onepointcalibrated_ds = [d + (target_d - actual_d) for d in dac_code]

            mean_v_onepointcalibrated = np.mean(onepointcalibrated_ds)
            tc_onepointcalibrated = (np.max(onepointcalibrated_ds) - np.min(onepointcalibrated_ds)) / (np.max(ts) - np.min(ts)) # in V/°C
            print(f"{process_corner}{Vx} 1pc TC: {tc_onepointcalibrated:.4f} -/°C")

            axs_d_1p.plot(ts, onepointcalibrated_ds, marker="o", label=f"{run}")

            # 
            # 2 point calibrate the dac codes at calibration_dac_t1 and calibration_dac_t2 degrees Celsius
            # 

            calibration_dac_t1 = 0
            calibration_dac_t2 = 80

            target_coarse_code_1 = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t1)  & (df["monte carlo run"] == 1), "Coarse code"])
            target_fine_code_1 = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t1) & (df["monte carlo run"] == 1), "Fine code"])
            target_coarse_code_1 = target_coarse_code_1 * 1e3 # in whole numbers
            target_fine_code_1 = target_fine_code_1 * 1e3 # in whole numbers
            target_d1 = target_coarse_code_1 * 10 + target_fine_code_1
            
            target_coarse_code_2 = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t2) & (df["monte carlo run"] == 1), "Coarse code"])
            target_fine_code_2 = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == calibration_dac_t2) & (df["monte carlo run"] == 1), "Fine code"])
            target_coarse_code_2 = target_coarse_code_2 * 1e3 # in whole numbers
            target_fine_code_2 = target_fine_code_2 * 1e3 # in whole numbers
            target_d2 = target_coarse_code_2 * 10 + target_fine_code_2

            twopointcalibrated_ds = []
            for d, t in zip(dac_code, ts):
                # Actual value of this curve at calibration temperatures (interpolated if needed)
                actual_coarse_code_1 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_dac_t1) & (df["monte carlo run"] == run), "Coarse code"])
                actual_fine_code_1 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_dac_t1) & (df["monte carlo run"] == run), "Fine code"])
                actual_coarse_code_1 = actual_coarse_code_1 * 1e3 # in whole numbers
                actual_fine_code_1 = actual_fine_code_1 * 1e3 # in whole numbers
                actual_d1 = actual_coarse_code_1 * 10 + actual_fine_code_1
                
                actual_coarse_code_2 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_dac_t2) & (df["monte carlo run"] == run), "Coarse code"])
                actual_fine_code_2 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["Temperature (°C)"] == calibration_dac_t2) & (df["monte carlo run"] == run), "Fine code"])
                actual_coarse_code_2 = actual_coarse_code_2 * 1e3 # in whole numbers
                actual_fine_code_2 = actual_fine_code_2 * 1e3 # in whole numbers
                actual_d2 = actual_coarse_code_2 * 10 + actual_fine_code_2

                # Offset at each calibration point
                offset1 = target_d1 - actual_d1
                offset2 = target_d2 - actual_d2

                # Linearly interpolate offset across temperature
                offset = offset1 + (offset2 - offset1) * (t - calibration_dac_t1) / (calibration_dac_t2 - calibration_dac_t1)
                twopointcalibrated_ds.append(d + offset)

            mean_v_twopointcalibrated = np.mean(twopointcalibrated_ds)
            tc_twopointcalibrated = (np.max(twopointcalibrated_ds) - np.min(twopointcalibrated_ds)) / (np.max(ts) - np.min(ts)) # in V/°C
            tc_in_mV_per_C = tc_twopointcalibrated * 1e3 # in mV/°C
            tc_in_ppm = (tc_twopointcalibrated / mean_v_twopointcalibrated) * 1e6 # in ppm/°C relative to average voltage
            print(f"{process_corner}{Vx} 2pc: Mean voltage: {mean_v_twopointcalibrated:.4f} V, TC: {tc_twopointcalibrated:.4f} V/°C, TC in mV/°C {tc_in_mV_per_C:.2f}, TC in ppm/°C: {tc_in_ppm:.2f}")

            axs_d_2p.plot(ts, twopointcalibrated_ds, marker="o", label=f"{run}")


            #
            # power while in active mode
            #

            mean_on_pwr = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == run), "Mean active power (uW)"])
            min_on_pwr = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == run), "Minimum active power (uW)"])
            max_on_pwr = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == run), "Maximum active power (uW)"])

            axs_on_pwr.plot(temperatures, mean_on_pwr, linestyle="solid", marker="o", markersize=5, label=f"{run}")
            last_color = axs_on_pwr.get_lines()[-1].get_color()
            # axs_on_pwr.plot(temperatures, min_on_pwr, linestyle="dashed", marker="s", markersize=5, color=last_color, label=f"{corner}{Vx}, minimum")
            # axs_on_pwr.plot(temperatures, max_on_pwr, linestyle="dotted", marker="v", markersize=5, color=last_color, label=f"{corner}{Vx}, maximum")

            #
            # power while in sleep mode
            #

            off_pwr = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == run), "Sleep power (uW)"])
            
            if run == 15: 
                print()
            else:
                axs_off_pwr.plot(temperatures, off_pwr, marker="o", label=f"{run}")

            #
            # start up time
            #


            start_up_times = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == run), "Start-up time (us)"])
            if start_up_times.size == 0:
                continue
            axs_start_up.plot(temperatures, start_up_times, marker="o", label=f"{run}")

            print("")

    # Plot the mean voltage, active power, sleep power, and start-up time across the runs for each temperature in the monte carlo simulation and the pluss minus one standard deviation as error bars

    # dac_twopointcalibrationlist.append(twopointcalibrated_ds)

    # ts_fit = np.array(temperatures)
    # ds = dac_twopointcalibrationlist

    # ds = np.array(ds)
    # ds = ds.squeeze()  
    # means = ds.mean(axis=0)

    # slope, intercept, r_value, _, _ = stats.linregress(ts_fit, means)
    # linear_fit = slope * ts_fit + intercept

    # print(f"means: {means}")
    # print(f"DAC 2p mean linear fit: slope={slope:.4f} /°C, intercept={intercept:.2f}, R²={r_value**2:.6f}")

    # axs_d_2p.plot(ts_fit, means,       marker="o", linestyle="none", label="Mean")
    # axs_d_2p.plot(ts_fit, linear_fit,  linestyle="--",               label=f"Lin. fit")

    # residuals = means - linear_fit            # deviation at each x-point
    # max_dev = np.max(np.abs(residuals))       # largest deviation (magnitude)
    # idx = np.argmax(np.abs(residuals))        # which x-point it occurs at

    # print(f"Max deviation: {max_dev:.4f} at temp = {ts_fit[idx]} (residual = {residuals[idx]:+.4f})")
    # all_residuals = ds - linear_fit                     # shape (n_curves, 5)

    # flat_idx = np.argmax(np.abs(all_residuals))         # index into the flattened array
    # curve_idx, t_idx = np.unravel_index(flat_idx, all_residuals.shape)

    # max_dev_v = ds[curve_idx, t_idx]                    # the voltage itself
    # max_dev_t = ts_fit[t_idx]                           # temperature where it happens
    # max_dev = all_residuals[curve_idx, t_idx]           # signed deviation

    # print(f"Max deviation from fit: {np.abs(max_dev):.2f} codes "
    #   f"(dac code = {max_dev_v:.1f}, curve #{curve_idx}, at {max_dev_t} °C, residual = {max_dev:+.2f})")
    # print()

    mean_v_list = []
    std_v_list = []
    for temperature in temperatures:
        v = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == temperature), "Output voltage (V)"])
        v = [x for x in v if x == x]
        mean_v_list.append(np.mean(v))
        std_v_list.append(np.std(v))
        print(f"Temperature: {temperature} °C, Mean voltage: {mean_v_list[-1]:.4f} V, Std voltage: {std_v_list[-1]*1e3:.2f} mV")

    nruns = len(v)

    axs_mc_errorbar.plot(temperatures, mean_v_list, marker="o", label=f"Mean voltage (μ)")
    axs_mc_errorbar.fill_between(temperatures, np.array(mean_v_list) - np.array(std_v_list), np.array(mean_v_list) + np.array(std_v_list), alpha=0.2, label=f"standard deviation (±σ)")

    axs_mc_errorbar.set_title(f"Temperature voltage", fontsize=title_font_size+2, fontweight='bold')
    axs_mc_errorbar.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_mc_errorbar.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_mc_errorbar.legend(loc="best", fontsize=legend_font_size+2)
    axs_mc_errorbar.tick_params(axis='both', labelsize=ticks_font_size+2)
    axs_mc_errorbar.grid()

    fig_mc_errorbar.tight_layout()
    fig_mc_errorbar.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_mean_v_w_erorr_bars.png", dpi=300, bbox_inches="tight")


    # Plot the distribution of monte carlo runs at each temperature as  
    distribution_temperature = 125
    bin_count = 7

    v = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == distribution_temperature), "Output voltage (V)"])
    v = [x for x in v if x == x]
    mean_v = np.mean(v)
    std_v = np.std(v)

    nruns = len(v)

    within_1sigma = np.sum([np.abs(x - mean_v) <= std_v for x in v])
    pct_1sigma = within_1sigma / len(v) * 100

    print(f"mean voltage at {distribution_temperature} °C after {nruns} runs: {mean_v} V")
    print(f"standard error at {distribution_temperature} °C after {nruns} runs: {std_v}")
    print(f"Values within ±1σ: {within_1sigma} of {len(v)} ({pct_1sigma:.1f}%) — normal distribution expects 68.3%")

    fig_dist = plt.figure(dpi=300, figsize=(figure_width, figure_height))
    ax_dist = fig_dist.add_subplot(1, 1, 1)
    ax_dist.set_title(f"MC distribution at {distribution_temperature}°C")

    sns.histplot(v, bins=bin_count, kde=True, color="steelblue", edgecolor="black", ax=ax_dist)
    sns.rugplot(v, height=0.1, color="blue", ax=ax_dist)

    ax_dist.axvline(mean_v, linestyle="dashed", color="black", label=f"μ = {mean_v*1e3:.2f} mV")
    ax_dist.grid(True)
    fig_dist.gca().set_axisbelow(True)
        
    # Fill after seaborn has set the y-limits
    ymin, ymax = ax_dist.get_ylim()
    ax_dist.fill_between(
        [mean_v - std_v, mean_v + std_v],
        ymin, ymax,
        alpha=0.2,
        color="black",
        label=f"±σ = ±{np.abs(std_v)*1e3:.2f} mV",
    )
    ax_dist.set_ylim(ymin, ymax)  # re-apply so fill_between doesn't expand the axis

    ax_dist.legend(loc="best")
    ax_dist.set_xlabel("Voltage (V)")
    fig_dist.tight_layout()
    fig_dist.savefig(f"plots/mc_tsens_dist_{stepping_direction}_at_{distribution_temperature}C.png")



    # Plot the mean dac code mean and standard deviation across the runs for each temperature in the monte carlo simulation and the pluss minus one standard deviation as error bars

    mean_d_list = []
    std_d_list = []
    for temperature in temperatures:
        dcoarse = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == temperature), "Coarse code"])
        dfine = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == temperature), "Fine code"])
        dcoarse = dcoarse * 1e3 # in whole numbers
        dfine = dfine * 1e3 # in whole numbers
        d = dcoarse * 10 + dfine
        d = [x for x in d if x == x]
        mean_d_list.append(np.mean(d))
        std_d_list.append(np.std(d))
        print(f"Temperature: {temperature} °C, Mean DAC code: {mean_d_list[-1]:.4f}, Std DAC code: {std_d_list[-1]:.4f}")

    nruns = len(d)

    axs_mc_dac_errorbar.plot(temperatures, mean_d_list, marker="o", label=f"Mean DAC code (μ)")
    axs_mc_dac_errorbar.fill_between(temperatures, np.array(mean_d_list) - np.array(std_d_list), np.array(mean_d_list) + np.array(std_d_list), alpha=0.2, label=f"standard deviation (±σ)")

    axs_mc_dac_errorbar.set_title(f"DAC code on the input", fontsize=title_font_size+2, fontweight='bold')
    axs_mc_dac_errorbar.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_mc_dac_errorbar.set_ylabel("DAC code", fontsize=label_font_size)
    axs_mc_dac_errorbar.legend(loc="best", fontsize=legend_font_size+2)
    axs_mc_dac_errorbar.tick_params(axis='both', labelsize=ticks_font_size+2)
    axs_mc_dac_errorbar.grid()

    fig_mc_dac_errorbar.tight_layout()
    fig_mc_dac_errorbar.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_mean_dac_code_w_error_bars.png", dpi=300, bbox_inches="tight")


    mean_d_list = []
    std_d_list = []
    for temperature in temperatures:
        dcoarse = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == temperature), "Coarse code"])
        dfine = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == temperature), "Fine code"])
        dcoarse = dcoarse * 1e3 # in whole numbers
        dfine = dfine * 1e3 # in whole numbers
        d = dcoarse * 10 + dfine
        d = [x for x in d if x == x]
        mean_d_list.append(np.mean(d))
        std_d_list.append(np.std(d))
        print(f"Temperature: {temperature} °C, Mean DAC code: {mean_d_list[-1]:.4f}, Std DAC code: {std_d_list[-1]:.4f}")

    nruns = len(d)

    axs_mc_errorbar_1p.plot(temperatures, mean_d_list, marker="o", label=f"Mean DAC code (μ)")
    axs_mc_errorbar_1p.fill_between(temperatures, np.array(mean_d_list) - np.array(std_d_list), np.array(mean_d_list) + np.array(std_d_list), alpha=0.2, label=f"standard deviation (±σ)")

    axs_mc_errorbar_1p.set_title(f"Temperature voltage", fontsize=title_font_size+2, fontweight='bold')
    axs_mc_errorbar_1p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_mc_errorbar_1p.set_ylabel("DAC code", fontsize=label_font_size)
    axs_mc_errorbar_1p.legend(loc="best", fontsize=legend_font_size+2)
    axs_mc_errorbar_1p.tick_params(axis='both', labelsize=ticks_font_size+2)
    axs_mc_errorbar_1p.grid()

    fig_mc_errorbar_1p.tight_layout()
    fig_mc_errorbar_1p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_mean_dac_code_w_error_bars_colt_1p.png", dpi=300, bbox_inches="tight")


    mean_d_list = []
    std_d_list = []
    for temperature in temperatures:
        dcoarse = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == temperature), "Coarse code"])
        dfine = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == temperature), "Fine code"])
        dcoarse = dcoarse * 1e3 # in whole numbers
        dfine = dfine * 1e3 # in whole numbers
        d = dcoarse * 10 + dfine
        d = [x for x in d if x == x]
        mean_d_list.append(np.mean(d))
        std_d_list.append(np.std(d))
        print(f"Temperature: {temperature} °C, Mean DAC code: {mean_d_list[-1]:.4f}, Std DAC code: {std_d_list[-1]:.4f}")

    nruns = len(d)

    axs_mc_dac_errorbar_1p.plot(temperatures, mean_d_list, marker="o", label=f"Mean DAC code (μ)")
    axs_mc_dac_errorbar_1p.fill_between(temperatures, np.array(mean_d_list) - np.array(std_d_list), np.array(mean_d_list) + np.array(std_d_list), alpha=0.2, label=f"standard deviation (±σ)")

    axs_mc_dac_errorbar_1p.set_title(f"DAC code", fontsize=title_font_size+2, fontweight='bold')
    axs_mc_dac_errorbar_1p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_mc_dac_errorbar_1p.set_ylabel("DAC code", fontsize=label_font_size)
    axs_mc_dac_errorbar_1p.legend(loc="best", fontsize=legend_font_size+2)
    axs_mc_dac_errorbar_1p.tick_params(axis='both', labelsize=ticks_font_size+2)
    axs_mc_dac_errorbar_1p.grid()

    fig_mc_dac_errorbar_1p.tight_layout()
    fig_mc_dac_errorbar_1p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_mean_dac_code_w_error_bars_dac_1p.png", dpi=300, bbox_inches="tight")




    # Plot the distribution of monte carlo runs at each temperature as  

    d_coarse = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == distribution_temperature), "Coarse code"])
    d_fine = np.array(df.loc[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8) & (df["Temperature (°C)"] == distribution_temperature), "Fine code"])
    d = d_coarse * 1e3 * 10 + d_fine * 1e3
    d = [x for x in d if x == x]
    mean_d = np.mean(d)
    std_d = np.std(d)

    nruns = len(d)

    within_1sigma = np.sum([np.abs(x - mean_d) <= std_d for x in d])
    pct_1sigma = within_1sigma / len(d) * 100

    print(f"mean DAC code at {distribution_temperature} °C after {nruns} runs: {mean_d} ")
    print(f"standard error at {distribution_temperature} °C after {nruns} runs: {std_d}")
    print(f"Values within ±1σ: {within_1sigma} of {len(d)} ({pct_1sigma:.1f}%) — normal distribution expects 68.3%")

    fig_d_dist = plt.figure(dpi=300, figsize=(figure_width, figure_height))
    ax_d_dist = fig_d_dist.add_subplot(1, 1, 1)
    ax_d_dist.set_title(f"MC distribution at {distribution_temperature}°C\nafter {nruns} runs")

    sns.histplot(d, bins=bin_count, kde=True, color="steelblue", edgecolor="black", ax=ax_d_dist)
    sns.rugplot(d, height=0.1, color="blue", ax=ax_d_dist)

    ax_d_dist.axvline(mean_d, linestyle="dashed", color="black", label=f"μ = {mean_d:.0f}")
    ax_d_dist.grid(True)
    fig_d_dist.gca().set_axisbelow(True)
        
    # Fill after seaborn has set the y-limits
    ymin, ymax = ax_d_dist.get_ylim()
    ax_d_dist.fill_between(
        [mean_d - std_d, mean_d + std_d],
        ymin, ymax,
        alpha=0.2,
        color="black",
        label=f"±σ = ±{np.abs(std_d):.0f}",
    )

    ax_d_dist.set_ylim(ymin, ymax)  # re-apply so fill_between doesn't expand the axis

    ax_d_dist.legend(loc="best")
    ax_d_dist.set_xlabel("DAC code")
    fig_d_dist.tight_layout()
    fig_d_dist.savefig(f"plots/mc_tsens_dist_dac_{stepping_direction}_at_{distribution_temperature}C.png")



    axs_v_0p.set_title(f"Temperature voltage", fontsize=title_font_size, fontweight='bold')
    axs_v_0p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_0p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_0p.legend(loc="best", fontsize=legend_font_size, ncol=3)
    axs_v_0p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_0p.grid()

    fig_v_0p.tight_layout()
    fig_v_0p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_uncalibrated_temperature_vs_temperature_voltage_new_resistance_v2.png", dpi=300, bbox_inches="tight")

    axs_v_1p.set_title(f"Temperature voltage 1 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_1p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_1p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_1p.legend(loc="best", fontsize=legend_font_size, ncol=3)
    axs_v_1p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_1p.grid()

    fig_v_1p.tight_layout()
    fig_v_1p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_onepointcalibrated_temperature_vs_temperature_voltage_new_resistance_v2.png", dpi=300, bbox_inches="tight")

    axs_v_2p.set_title(f"Temperature voltage 2 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_v_2p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_v_2p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_v_2p.legend(loc="best", fontsize=legend_font_size, ncol=3)
    axs_v_2p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_v_2p.grid()

    fig_v_2p.tight_layout()
    fig_v_2p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_twopointcalibrated_temperature_vs_temperature_voltage_new_resistance_v2.png", dpi=300, bbox_inches="tight")


    axs_dac.set_title(f"DAC input", fontsize=title_font_size, fontweight='bold')
    axs_dac.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_dac.set_ylabel("DAC code", fontsize=label_font_size)
    axs_dac.legend(loc="best", fontsize=legend_font_size, ncol=3)
    axs_dac.tick_params(axis='both', labelsize=ticks_font_size)
    axs_dac.grid()

    fig_dac.tight_layout()
    fig_dac.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_uncalibrated_temperature_vs_dac_code_new_resistance_v2.png", dpi=300, bbox_inches="tight")

    axs_d_1p.set_title(f"DAC input 1 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_d_1p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_d_1p.set_ylabel("DAC code", fontsize=label_font_size)
    axs_d_1p.legend(loc="best", fontsize=legend_font_size, ncol=3)
    axs_d_1p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_d_1p.grid()

    fig_d_1p.tight_layout()
    fig_d_1p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_onepointcalibrated_temperature_vs_dac_code.png", dpi=300, bbox_inches="tight")
    
    axs_d_2p.set_title(f"DAC input 2 point calibrated", fontsize=title_font_size, fontweight='bold')
    axs_d_2p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_d_2p.set_ylabel("DAC code", fontsize=label_font_size)
    axs_d_2p.legend(loc="best", fontsize=legend_font_size, ncol=3)
    axs_d_2p.tick_params(axis='both', labelsize=ticks_font_size)
    axs_d_2p.grid()

    fig_d_2p.tight_layout()
    fig_d_2p.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_twopointcalibrated_temperature_vs_dac_code.png", dpi=300, bbox_inches="tight")


    axs_on_pwr.set_title(f"Active power consumption", fontsize=title_font_size, fontweight='bold')
    axs_on_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_on_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    # axs_on_pwr.legend(loc="best", fontsize=legend_font_size, ncol=3)
    axs_on_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_on_pwr.grid()

    fig_on_pwr.tight_layout()
    fig_on_pwr.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_temperature_vs_active_power_new_resistance_v2.png", dpi=300, bbox_inches="tight")

    # axs_off_pwr.set_yscale("log")
    axs_off_pwr.set_title(f"Sleep power consumption", fontsize=title_font_size, fontweight='bold')
    axs_off_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_off_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    # axs_off_pwr.legend(loc="best", fontsize=legend_font_size, ncol=3)
    axs_off_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_off_pwr.grid()

    fig_off_pwr.tight_layout()
    fig_off_pwr.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_temperature_vs_sleep_power_new_resistance_v2.png", dpi=300, bbox_inches="tight")

    axs_start_up.set_title(f"Start-up time", fontsize=title_font_size, fontweight='bold')
    axs_start_up.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_start_up.set_ylabel("Time (us)", fontsize=label_font_size)
    axs_start_up.legend(loc="best", fontsize=legend_font_size, ncol=3)
    axs_start_up.tick_params(axis='both', labelsize=ticks_font_size)
    axs_start_up.grid()

    fig_start_up.tight_layout()
    fig_start_up.savefig(f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_temperature_vs_start_up_time_new_resistance_v2.png", dpi=300, bbox_inches="tight")

if "fail" in args:

    df = pd.read_csv(f"plotdata/mc_stepping_{stepping_direction}.csv")
    print(f"plotdata/mc_stepping_{stepping_direction}.csv")

    process_corner = "ttmm"
    voltage = 1.8

    fig_count = plt.figure(dpi=300, figsize=(3, 3))
    ax_count = fig_count.add_subplot(1, 1, 1)
    ax_count.set_title(f"Problematic runs with mismatch", fontsize=8, fontweight='bold')

    mc2 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 2), "Output voltage (V)"])
    mc3 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 3), "Output voltage (V)"])
    mc5 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 5), "Output voltage (V)"])
    mc12 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 12), "Output voltage (V)"])
    mc15 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 15), "Output voltage (V)"])
    mc22 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 22), "Output voltage (V)"])
    mc25 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 25), "Output voltage (V)"])

    ax_count.plot(temperatures, mc2, linestyle="solid", marker="o", markersize=5, label=f"2")
    ax_count.plot(temperatures, mc3, linestyle="solid", marker="o", markersize=5, label=f"3")
    # ax_count.plot(temperatures, mc5, linestyle="solid", marker="o", markersize=5, label=f"5")
    # ax_count.plot(temperatures, mc12, linestyle="solid", marker="o", markersize=5, label=f"12")
    ax_count.plot(temperatures, mc15, linestyle="solid", marker="o", markersize=5, label=f"15")
    ax_count.plot(temperatures, mc22, linestyle="solid", marker="o", markersize=5, label=f"22")
    # ax_count.plot(temperatures, mc25, linestyle="solid", marker="o", markersize=5, label=f"25")

    # ax_count.set_xlim(45, 82.5)
    ax_count.set_xlabel("Time (us)", fontsize=8)
    ax_count.set_ylabel("Voltage (V)", fontsize=8)
    ax_count.legend(loc="best", fontsize=8)
    ax_count.tick_params(axis='both', labelsize=8)
    ax_count.grid(True)

    fig_count.tight_layout()
    fig_count.savefig(f"plots/mc_failures_volt.png")

    fig_dac = plt.figure(dpi=300, figsize=(3, 3))
    ax_dac = fig_dac.add_subplot(1, 1, 1)
    ax_dac.set_title(f"Problematic runs with mismatch", fontsize=8, fontweight='bold')

    c2 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 2), "Coarse code"])
    c3 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 3), "Coarse code"])
    c15 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 15), "Coarse code"])
    c22 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 22), "Coarse code"])
    f2 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 2), "Fine code"])
    f3 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 3), "Fine code"])
    f15 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 15), "Fine code"])
    f22 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 22), "Fine code"])

    d2 = 10 * c2 + f2
    d3 = 10 * c3 + f3
    d15 = 10 * c15 + f15
    d22 = 10 * c22 + f22

    ax_dac.plot(temperatures, d2, linestyle="solid", marker="o", markersize=5, label=f"2")
    ax_dac.plot(temperatures, d3, linestyle="solid", marker="o", markersize=5, label=f"2")
    ax_dac.plot(temperatures, d15, linestyle="solid", marker="o", markersize=5, label=f"15")
    ax_dac.plot(temperatures, d22, linestyle="solid", marker="o", markersize=5, label=f"22")
    
    # ax_count.set_xlim(45, 82.5)
    ax_dac.set_xlabel("Time (us)", fontsize=8)
    ax_dac.set_ylabel("DAC code", fontsize=8)
    ax_dac.legend(loc="best", fontsize=8)
    ax_dac.tick_params(axis='both', labelsize=8)
    ax_dac.grid(True)

    fig_dac.tight_layout()
    fig_dac.savefig(f"plots/mc_failures_dac.png")


    fig_mc_errorbar_1p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_mc_errorbar_1p = fig_mc_errorbar_1p.add_subplot(1, 1, 1)

    fig_mc_dac_errorbar_1p = plt.figure(figsize=(figure_width, figure_height), dpi=300)
    axs_mc_dac_errorbar_1p = fig_mc_dac_errorbar_1p.add_subplot(1, 1, 1)

    T_cal = 40 # calibration temperature, pick one that exists in `temperatures`

    # --- Build a (nruns x ntemps) matrix, keeping run identity ---
    d_matrix = []
    for temperature in temperatures:
        sel = (df['Process corner'] == "ttmm") & \
            (df["Voltage supply (V)"] == 1.8) & \
            (df["Temperature (°C)"] == temperature)
        dcoarse = np.array(df.loc[sel, "Coarse code"]) * 1e3
        dfine   = np.array(df.loc[sel, "Fine code"])   * 1e3
        d_matrix.append(dcoarse * 10 + dfine)

    d_matrix = np.array(d_matrix).T   # shape: (nruns, ntemps)

    # Drop runs that contain any NaN (so every run has a value at T_cal)
    valid = ~np.isnan(d_matrix).any(axis=1)
    d_matrix = d_matrix[valid]
    nruns = d_matrix.shape[0]

    # --- One-point calibration ---
    i_cal = list(temperatures).index(T_cal)

    # Per-run offset relative to the mean code at the calibration point
    offset = d_matrix[:, i_cal] - np.mean(d_matrix[:, i_cal])   # shape: (nruns,)

    d_cal = d_matrix - offset[:, None]   # subtract each run's own offset

    mean_d_list = np.mean(d_cal, axis=0)
    std_d_list  = np.std(d_cal, axis=0)

    for t, m, s in zip(temperatures, mean_d_list, std_d_list):
        print(f"Temperature: {t} °C, Mean DAC code: {m:.4f}, Std DAC code: {s:.4f}")

    # --- Plot ---
    axs_mc_dac_errorbar_1p.plot(temperatures, mean_d_list, marker="o",
                                label="Mean DAC code (μ)")
    axs_mc_dac_errorbar_1p.fill_between(temperatures,
                                        mean_d_list - std_d_list,
                                        mean_d_list + std_d_list,
                                        alpha=0.2,
                                        label="standard deviation (±σ)")
    axs_mc_dac_errorbar_1p.axvline(T_cal, color="gray", linestyle="--", alpha=0.7,
                                label=f"Calibration point ({T_cal} °C)")

    axs_mc_dac_errorbar_1p.set_title(f"DAC code after {nruns} runs",
                                    fontsize=title_font_size+2, fontweight='bold')
    axs_mc_dac_errorbar_1p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_mc_dac_errorbar_1p.set_ylabel("DAC code", fontsize=label_font_size)
    axs_mc_dac_errorbar_1p.legend(loc="best", fontsize=legend_font_size+2)
    axs_mc_dac_errorbar_1p.tick_params(axis='both', labelsize=ticks_font_size+2)
    axs_mc_dac_errorbar_1p.grid()

    fig_mc_dac_errorbar_1p.tight_layout()
    fig_mc_dac_errorbar_1p.savefig(
        f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_mean_dac_code_w_error_bars_dac_1p.png",
        dpi=300, bbox_inches="tight")
    
    # --- Build a (nruns x ntemps) matrix for output voltage, keeping run identity ---
    v_matrix = []
    for temperature in temperatures:
        sel = (df['Process corner'] == "ttmm") & \
            (df["Voltage supply (V)"] == 1.8) & \
            (df["Temperature (°C)"] == temperature)
        v_matrix.append(np.array(df.loc[sel, "Output voltage (V)"]))

    v_matrix = np.array(v_matrix).T   # shape: (nruns, ntemps)

    # Drop runs that contain any NaN (so every run has a value at T_cal)
    valid_v = ~np.isnan(v_matrix).any(axis=1)
    v_matrix = v_matrix[valid_v]
    nruns_v = v_matrix.shape[0]

    # --- One-point calibration ---
    i_cal = list(temperatures).index(T_cal)

    # Per-run offset relative to the mean voltage at the calibration point
    offset_v = v_matrix[:, i_cal] - np.mean(v_matrix[:, i_cal])   # shape: (nruns,)

    v_cal = v_matrix - offset_v[:, None]   # subtract each run's own offset

    mean_v_list = np.mean(v_cal, axis=0)
    std_v_list  = np.std(v_cal, axis=0)

    for t, m, s in zip(temperatures, mean_v_list, std_v_list):
        print(f"Temperature: {t} °C, Mean output voltage: {m:.6f} V, Std: {s*1e3:.4f} mV")

    # --- Plot ---
    axs_mc_errorbar_1p.plot(temperatures, mean_v_list, marker="o",
                            label="Mean output voltage (μ)")
    axs_mc_errorbar_1p.fill_between(temperatures,
                                    mean_v_list - std_v_list,
                                    mean_v_list + std_v_list,
                                    alpha=0.2,
                                    label="standard deviation (±σ)")
    axs_mc_errorbar_1p.axvline(T_cal, color="gray", linestyle="--", alpha=0.7,
                            label=f"Calibration point ({T_cal} °C)")

    axs_mc_errorbar_1p.set_title(f"Output voltage after {nruns_v} runs",
                                fontsize=title_font_size+2, fontweight='bold')
    axs_mc_errorbar_1p.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_mc_errorbar_1p.set_ylabel("Output voltage (V)", fontsize=label_font_size)
    axs_mc_errorbar_1p.legend(loc="best", fontsize=legend_font_size+2)
    axs_mc_errorbar_1p.tick_params(axis='both', labelsize=ticks_font_size+2)
    axs_mc_errorbar_1p.grid()

    fig_mc_errorbar_1p.tight_layout()
    fig_mc_errorbar_1p.savefig(
        f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_mean_volt_w_error_bars_volt_1p.png",
        dpi=300, bbox_inches="tight")
    
    # Uncalibrated stats (from the raw matrices, before offset removal)
    mean_d_raw = np.mean(d_matrix, axis=0)
    std_d_raw  = np.std(d_matrix, axis=0)
    mean_v_raw = np.mean(v_matrix, axis=0)
    std_v_raw  = np.std(v_matrix, axis=0)

    print("=" * 78)
    print(f"DAC code — uncalibrated vs 1-point cal @ {T_cal} °C ({nruns} runs)")
    print("-" * 78)
    print(f"{'T (°C)':>8} | {'mean raw':>10} | {'std raw':>9} | {'mean cal':>10} | {'std cal':>9}")
    print("-" * 78)
    for t, mr, sr, mc, sc in zip(temperatures, mean_d_raw, std_d_raw, mean_d_list, std_d_list):
        print(f"{t:8.1f} | {mr:10.4f} | {sr:9.4f} | {mc:10.4f} | {sc:9.4f}")

    print("=" * 78)
    print(f"Output voltage — uncalibrated vs 1-point cal @ {T_cal} °C ({nruns_v} runs)")
    print("-" * 78)
    print(f"{'T (°C)':>8} | {'mean raw (V)':>12} | {'std raw (mV)':>12} | {'mean cal (V)':>12} | {'std cal (mV)':>12}")
    print("-" * 78)
    for t, mr, sr, mc, sc in zip(temperatures, mean_v_raw, std_v_raw, mean_v_list, std_v_list):
        print(f"{t:8.1f} | {mr:12.6f} | {sr*1e3:12.4f} | {mc:12.6f} | {sc*1e3:12.4f}")
    print("=" * 78)

    fig_mc_on_pwr = plt.figure(figsize=(3, 3), dpi=300)
    axs_mc_on_pwr = fig_mc_on_pwr.add_subplot(1, 1, 1)

    fig_mc_off_pwr = plt.figure(figsize=(3, 3), dpi=300)
    axs_mc_off_pwr = fig_mc_off_pwr.add_subplot(1, 1, 1)

    # --- Build (nruns x ntemps) matrices for active and sleep power ---
    on_pwr_matrix = []
    off_pwr_matrix = []
    for temperature in temperatures:
        sel = (df['Process corner'] == "ttmm") & \
            (df["Voltage supply (V)"] == 1.8) & \
            (df["Temperature (°C)"] == temperature)
        on_pwr_matrix.append(np.array(df.loc[sel, "Mean active power (uW)"]))
        off_pwr_matrix.append(np.array(df.loc[sel, "Sleep power (uW)"]))

    on_pwr_matrix  = np.array(on_pwr_matrix).T    # shape: (nruns, ntemps)
    off_pwr_matrix = np.array(off_pwr_matrix).T

    valid_on  = ~np.isnan(on_pwr_matrix).any(axis=1)
    valid_off = ~np.isnan(off_pwr_matrix).any(axis=1)
    on_pwr_matrix  = on_pwr_matrix[valid_on]
    off_pwr_matrix = off_pwr_matrix[valid_off]
    nruns_on  = on_pwr_matrix.shape[0]
    nruns_off = off_pwr_matrix.shape[0]

    mean_on_list = np.mean(on_pwr_matrix, axis=0)
    std_on_list  = np.std(on_pwr_matrix, axis=0)
    mean_off_list = np.mean(off_pwr_matrix, axis=0)
    std_off_list  = np.std(off_pwr_matrix, axis=0)

    print("=" * 70)
    print(f"Active power")
    for t, m, s in zip(temperatures, mean_on_list, std_on_list):
        print(f"Temperature: {t} °C, Mean: {m:.4f} uW, Std: {s:.4f} uW")
    print("-" * 70)
    print(f"Sleep power")
    for t, m, s in zip(temperatures, mean_off_list, std_off_list):
        print(f"Temperature: {t} °C, Mean: {m:.6f} uW, Std: {s:.6f} uW")
    print("=" * 70)

    # --- Active power plot ---
    axs_mc_on_pwr.plot(temperatures, mean_on_list, marker="o",
                    label="Mean active power (μ)")
    axs_mc_on_pwr.fill_between(temperatures,
                            mean_on_list - std_on_list,
                            mean_on_list + std_on_list,
                            alpha=0.2,
                            label="standard deviation (±σ)")

    axs_mc_on_pwr.set_title(f"Active power after {nruns_on} runs",
                            fontsize=title_font_size+2, fontweight='bold')
    axs_mc_on_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_mc_on_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_mc_on_pwr.legend(loc="best", fontsize=legend_font_size+2)
    axs_mc_on_pwr.tick_params(axis='both', labelsize=ticks_font_size+2)
    axs_mc_on_pwr.grid()

    fig_mc_on_pwr.tight_layout()
    fig_mc_on_pwr.savefig(
        f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_mean_active_power_w_error_bars.png",
        dpi=300, bbox_inches="tight")

    # --- Sleep power plot ---
    axs_mc_off_pwr.plot(temperatures, mean_off_list, marker="o",
                        label="Mean sleep power (μ)")
    axs_mc_off_pwr.fill_between(temperatures,
                                mean_off_list - std_off_list,
                                mean_off_list + std_off_list,
                                alpha=0.2,
                                label="standard deviation (±σ)")

    axs_mc_off_pwr.set_title(f"Sleep power after {nruns_off} runs",
                            fontsize=title_font_size+2, fontweight='bold')
    axs_mc_off_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_mc_off_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_mc_off_pwr.legend(loc="best", fontsize=legend_font_size+2)
    axs_mc_off_pwr.tick_params(axis='both', labelsize=ticks_font_size+2)
    axs_mc_off_pwr.grid()

    fig_mc_off_pwr.tight_layout()
    fig_mc_off_pwr.savefig(
        f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_mean_sleep_power_w_error_bars.png",
        dpi=300, bbox_inches="tight")
    
    fig_test= plt.figure(dpi=300, figsize=(3, 3))
    ax_test = fig_test.add_subplot(1, 1, 1)
    ax_test.set_title(f"Problematic runs with mismatch", fontsize=8, fontweight='bold')

    mc5 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 5), "Sleep power (uW)"])
    mc15 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 15), "Sleep power (uW)"])
    mc25 = np.array(df.loc[(df['Process corner'] == process_corner) & (df["Voltage supply (V)"] == voltage) & (df["monte carlo run"] == 25), "Sleep power (uW)"])

    ax_test.plot(temperatures, mc5, linestyle="solid", marker="o", markersize=5, label=f"5")
    ax_test.plot(temperatures, mc15, linestyle="solid", marker="o", markersize=5, label=f"15")
    ax_test.plot(temperatures, mc25, linestyle="solid", marker="o", markersize=5, label=f"25")

    # ax_test.set_xlim(45, 82.5)
    ax_test.set_xlabel("Time (us)", fontsize=8)
    ax_test.set_ylabel("Voltage (V)", fontsize=8)
    ax_test.legend(loc="best", fontsize=8)
    ax_test.tick_params(axis='both', labelsize=8)
    ax_test.grid(True)

    fig_test.tight_layout()
    fig_test.savefig(f"plots/mc_failures_sleep_power_test.png")

if "mc_pwr" in args:

    df = pd.read_csv(f"plotdata/mc_stepping_{stepping_direction}.csv")
    print(f"plotdata/mc_stepping_{stepping_direction}.csv")

    process_corner = "ttmm"
    voltage = 1.8

    fig_mc_on_pwr = plt.figure(figsize=(3, 3), dpi=300)
    axs_mc_on_pwr = fig_mc_on_pwr.add_subplot(1, 1, 1)

    fig_mc_off_pwr = plt.figure(figsize=(3, 3), dpi=300)
    axs_mc_off_pwr = fig_mc_off_pwr.add_subplot(1, 1, 1)

    # --- Build (nruns x ntemps) matrices with run identity via pivot ---
    sub = df[(df['Process corner'] == "ttmm") & (df["Voltage supply (V)"] == 1.8)]

    on_pwr_piv  = sub.pivot(index="monte carlo run", columns="Temperature (°C)",
                            values="Mean active power (uW)")[list(temperatures)]
    off_pwr_piv = sub.pivot(index="monte carlo run", columns="Temperature (°C)",
                            values="Sleep power (uW)")[list(temperatures)]

    # --- Mask outlier: run 15 at 125 °C ---
    outlier_run, outlier_t = 15, 125
    on_pwr_piv.loc[outlier_run, outlier_t]  = np.nan
    off_pwr_piv.loc[outlier_run, outlier_t] = np.nan

    on_pwr_matrix  = on_pwr_piv.to_numpy()
    off_pwr_matrix = off_pwr_piv.to_numpy()

    # Per-temperature stats, ignoring NaNs (keeps the rest of run 15)
    mean_on_list  = np.nanmean(on_pwr_matrix, axis=0)
    std_on_list   = np.nanstd(on_pwr_matrix, axis=0)
    mean_off_list = np.nanmean(off_pwr_matrix, axis=0)
    std_off_list  = np.nanstd(off_pwr_matrix, axis=0)

    # Number of runs contributing at each temperature (varies where NaNs are)
    n_on  = np.sum(~np.isnan(on_pwr_matrix), axis=0)
    n_off = np.sum(~np.isnan(off_pwr_matrix), axis=0)
    nruns_on, nruns_off = int(np.max(n_on)), int(np.max(n_off))

    print("=" * 70)
    print(f"Active power ({nruns_on} runs, run {outlier_run} excluded at {outlier_t} °C)")
    for t, m, s, n in zip(temperatures, mean_on_list, std_on_list, n_on):
        print(f"Temperature: {t} °C, Mean: {m:.4f} uW, Std: {s:.4f} uW, n={n}")
    print("-" * 70)
    print(f"Sleep power ({nruns_off} runs, run {outlier_run} excluded at {outlier_t} °C)")
    for t, m, s, n in zip(temperatures, mean_off_list, std_off_list, n_off):
        print(f"Temperature: {t} °C, Mean: {m:.6f} uW, Std: {s:.6f} uW, n={n}")
    print("=" * 70)

    # --- Active power plot ---
    axs_mc_on_pwr.plot(temperatures, mean_on_list, marker="o",
                    label="Mean active power (μ)")
    axs_mc_on_pwr.fill_between(temperatures,
                            mean_on_list - std_on_list,
                            mean_on_list + std_on_list,
                            alpha=0.2,
                            label="standard deviation (±σ)")

    axs_mc_on_pwr.set_title(f"Active power",
                            fontsize=title_font_size+2, fontweight='bold')
    axs_mc_on_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_mc_on_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_mc_on_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_mc_on_pwr.tick_params(axis='both', labelsize=ticks_font_size+2)
    axs_mc_on_pwr.grid()

    fig_mc_on_pwr.tight_layout()
    fig_mc_on_pwr.savefig(
        f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_mean_active_power_w_error_bars_v2.png",
        dpi=300, bbox_inches="tight")

    # --- Sleep power plot ---
    axs_mc_off_pwr.plot(temperatures, mean_off_list, marker="o",
                        label="Mean sleep power (μ)")
    axs_mc_off_pwr.fill_between(temperatures,
                                mean_off_list - std_off_list,
                                mean_off_list + std_off_list,
                                alpha=0.2,
                                label="standard deviation (±σ)")

    axs_mc_off_pwr.set_title(f"Sleep power",
                            fontsize=title_font_size, fontweight='bold')
    axs_mc_off_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
    axs_mc_off_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
    axs_mc_off_pwr.legend(loc="best", fontsize=legend_font_size)
    axs_mc_off_pwr.tick_params(axis='both', labelsize=ticks_font_size)
    axs_mc_off_pwr.grid()

    fig_mc_off_pwr.tight_layout()
    fig_mc_off_pwr.savefig(
        f"plots/{'_'.join(args)}_tsens_stepping_{stepping_direction}_mean_sleep_power_w_error_bars_v2.png",
        dpi=300, bbox_inches="tight")
