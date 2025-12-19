import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
import glob

# Example input arguments: typical -40 -20 0 20 27 40 60 80 100 125

if __name__ == "__main__":

    fig_width = 3
    fig_height = 3
    font_size = 8
    title_fontsize = font_size
    label_fontsize = font_size
    legend_fontsize = font_size
    ticks_fontsize = font_size
    view = "Sch"
    # view = "Lay"

    names = list()
    data = dict()

    args = sys.argv[1:]
    case = args[0] if len(args) > 0 else "typical"

    corners = list()
    voltages = list()
    temperatures = args[1:] if len(args) > 1 else [-40, 27, 125]

    time_start = 13000  # in ns

    print(args)

    if case == "all":
        corners = ["tt", "ff", "ss", "sf", "fs"]
        voltages = ["1.7", "1.8", "1.9"]
    elif case == "typical":
        corners = ["tt"]
        voltages = ["1.8"]
    elif case == "slow":
        corners = ["ss"]
        voltages = ["1.7"]
    elif case == "fast":
        corners = ["ff"]
        voltages = ["1.9"]
    elif case == "etc":
        corners = ["ff", "ss", "sf", "fs"]
        voltages = ["1.7", "1.9"]
    elif case == "test":
        corners = ["tt"]
        voltages = ["1.7", "1.8", "1.9"]
    elif case == "mc":
        corners = ["ttmm"]
        voltages = ["1.8"]
    elif case == "custom":
        corners = ["ss", "fs"]
        voltages = ["1.7", "1.9"]

    if case == "mc":
        mc_count_start = 0
        mc_count_stop = 30
    else:
        mc_count_stop = 1
        mc_count_start = mc_count_stop - 1

    print(f'corners: {corners}')
    print(f'voltages: {voltages}')
    print(f'temperatures: {temperatures}')
    print(f'mc_count_start: {mc_count_start}, mc_count_stop: {mc_count_stop}')

    fig, axs = plt.subplots(1, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)

    data = dict()
    TCs = dict()
    avg_vouts = dict()

    zc_not_valid_count = 0
    zc_nv = dict()

    for corner in corners:  
        print(f'now processing Processing corner: {corner}')

        for voltage in voltages:
            print(f'now processing Supply voltage: {voltage} Volt')

            Vx = "Vl" if voltage == "1.7" else "Vt" if voltage == "1.8" else "Vh" if voltage == "1.9" else "Oops"

            print(f'now processing Voltage corner: {Vx}')

            if (corner == "ss" or corner == "sf") and voltage == "1.7":
                time_start = 30000  # in ns
            else:
                time_start = 13000  # in ns

            for c in range(mc_count_start, mc_count_stop):
                print(f'case: {case}, and count: {c}')

                temps = []
                vouts = []
                times = []
                duty_cycles = []
                frequencies = []
                avg_diffs = []
                idds = []
                voltage_supplies = []

                for temp in temperatures:
                    print()
                    print(f'now processing temperature: {temp} Celsius degree.')
                    
                    if case  == "mc":
                        print(f'Looking for files for Monte Carlo run {c} between {mc_count_start} and {mc_count_stop-1} at temperature {temp} and Voltage {voltage}.')

                    if case == "mc" and c > 0:
                        out_files = glob.glob(f"output_tran/tran_SchGtK{corner}Tt{Vx}_{c}_temperature{temp}celsius_frequency*mhz_dutycycle*percent_vdd{voltage}volt.out")
                        print(f'Looking for files with pattern: output_tran/tran_SchGtK{corner}Tt{Vx}_{c}_temperature{temp}celsius_frequency*mhz_dutycycle*percent_vdd{voltage}volt.out')
                    else:
                        out_files = glob.glob(f"output_tran/tran_SchGtK{corner}T*{Vx}_temperature{temp}celsius_frequency*mhz_dutycycle*percent_vdd{voltage}volt.out")
                        print(f'Looking for files with pattern: output_tran/tran_SchGtK{corner}T*{Vx}_temperature{temp}celsius_frequency*mhz_dutycycle*percent_vdd{voltage}volt.out')
                    
                    print(f'Found files: {out_files}')

                    prev_smallest_avg_diff = np.inf
                    final_zero_crossings = pd.Series([None])
                    final_zero_crossings_vout_values = pd.Series([None])
                    final_zero_crossings_time_values = pd.Series([None])

                    for file in out_files:
                        print(f'file: {file}')

                        circuit_temperature = int(file.split("temperature")[-1].split("celsius")[0]) # in Celsius degree
                        clock_frequency = int(file.split("frequency")[-1].split("mhz")[0]) # in Mega Hertz
                        clock_periode = 1 / clock_frequency  # in micro seconds
                        duty_cycle = int(file.split("dutycycle")[-1].split("percent")[0]) # in Percent
                        voltage_supply = float(file.split("vdd")[-1].split("volt")[0]) # in Volt
                        process_corner = "Typical" if "tt" in file else "Slow-Slow" if "ss" in file else "Slow-Fast" if "sf" in file else "Fast-Slow" if "fs" in file else "Fast-Fast" if "ff" in file else "Oops, something is wrong!"
                        process_corner_short = file.split("tran_")[-1].split("_temperature")[0][6:8] # tt, ss, ff, sf, fs
                        if case == "mc":
                            process_corner_short = "tt mc"

                        df = pd.read_csv(file, sep="\s+")
                        
                        # print(df.columns)
                        # print(df.head())
                        # print(df.tail())

                        df['time'] = df['time'] * 1e9 # in ns
                        df['diff'] = df['v(v1)']-df['v(v2)']
                        df['idd'] = -df['i(vdd)']

                        mask = df["time"] > time_start
                        df_masked = df.loc[mask, "diff"]
                        zero_crossings = df_masked.index[(df_masked.shift(1) * df_masked) < 0]

                        zero_crossings_time_values = df.loc[zero_crossings, 'time'].values
                        zero_crossings_vout_values = df.loc[zero_crossings, 'v(vout)'].values
                        
                        if len(zero_crossings) > 8:

                            # average diff from first to last zero crossing
                            avg_diff = df.loc[zero_crossings[-8]:zero_crossings[-2], 'diff'].mean()
                            print(f'Average diff between first ({zero_crossings[-8]}) and last ({zero_crossings[-2]}) zero crossing (V): {avg_diff}')

                            if (np.abs(avg_diff) < prev_smallest_avg_diff): # threshold to consider stable operation
                                print(f'Updating from previous avg diff: {prev_smallest_avg_diff}, to new smallest avg diff: {np.abs(avg_diff)}')
                                
                                print(f'zerocrossing count > 8: {len(zero_crossings)}, {zero_crossings.tolist()}')
                                print(f'Zero crossings found at indices: {zero_crossings.tolist()}')
                                print(f'Zero crossings found at time values (ns): {zero_crossings_time_values.tolist()}')
                                print(f'Zero crossings found at vout values (V): {zero_crossings_vout_values.tolist()}')

                                prev_smallest_avg_diff = np.abs(avg_diff)
                                final_temp = circuit_temperature
                                final_clock_frequency = clock_frequency
                                final_duty_cycle = duty_cycle
                                final_process_corner = process_corner
                                final_voltage_supply = voltage_supply
                                final_zero_crossings = zero_crossings
                                final_zero_crossings_vout_values = df.loc[final_zero_crossings, 'v(vout)'].values
                                final_zero_crossings_time_values = df.loc[final_zero_crossings, 'time'].values
                                final_idd = df.loc[final_zero_crossings, 'idd'].values
                                final_supply_voltage = voltage_supply


                        elif (len(zero_crossings) >= 2 and len(final_zero_crossings_vout_values.tolist()) <= 8):
                            print(f'Not enough zero crossings found to consider stable operation, only {len(zero_crossings)} crossings found. {zero_crossings.tolist()}')
                            final_temp = circuit_temperature
                            final_clock_frequency = clock_frequency
                            final_duty_cycle = duty_cycle
                            final_process_corner = process_corner
                            final_voltage_supply = voltage_supply
                            final_zero_crossings = zero_crossings
                            final_zero_crossings_vout_values = df.loc[final_zero_crossings, 'v(vout)'].values
                            final_zero_crossings_time_values = df.loc[final_zero_crossings, 'time'].values
                            final_idd = df.loc[final_zero_crossings, 'idd'].values
                            final_supply_voltage = float(voltage_supply)
                            # print(f'Zero crossings found at indices: {zero_crossings.tolist()}')
                            # print(f'final Zero crossings found at time values (ns): {final_zero_crossings_time_values.tolist()}')
                            # print(f'final Zero crossings found at vout values (V): {final_zero_crossings_vout_values.tolist()}')
                        else:
                            print(f'Almost no zero crossings found to consider stable operation, only {len(zero_crossings)} crossings found. {zero_crossings.tolist()}')
                            # print(f'final Zero crossings found at indices: {zero_crossings.tolist()}')
                            # print(f'final Zero crossings found at time values (ns): {zero_crossings_time_values.tolist()}')
                            # print(f'final Zero crossings found at vout values (V): {zero_crossings_vout_values.tolist()}')

                        
                
                    if (len(final_zero_crossings_vout_values.tolist()) > 4): # and not (case == "mc" and c == 5 and circuit_temperature == 125)):
                        print(f'zc > 4:Appending results for corner {corner}, voltage {voltage}, temp {final_temp}, frequency {final_clock_frequency}, duty cycle {final_duty_cycle}.')
                        times.append(final_zero_crossings_time_values.tolist()[-2]) # second last (-2) instead of last (-1) value because that is when we shift DAC
                        vouts.append(final_zero_crossings_vout_values.tolist()[-2]) # second last (-2) instead of last (-1) value because that is when we shift DAC
                        temps.append(int(final_temp))
                        duty_cycles.append(final_duty_cycle)
                        frequencies.append(final_clock_frequency)
                        avg_diffs.append(float(prev_smallest_avg_diff))
                        idds.append(float(final_idd.tolist()[-2]*1e6)) # in uA
                        voltage_supplies.append(final_supply_voltage)   
                    elif (len(final_zero_crossings_vout_values.tolist()) > 0): # and not (case == "mc" and c == 5 and circuit_temperature == 125)):
                        print(f'0 < zc < 8: Appending results for corner {corner}, voltage {voltage}, temp {temp}, frequency {clock_frequency}, duty cycle {duty_cycle}.')
                        times.append(final_zero_crossings_time_values.tolist()[-1]) # second last (-2) instead of last (-1) value because that is when we shift DAC
                        vouts.append(final_zero_crossings_vout_values.tolist()[-1]) # second last (-2) instead of last (-1) value because that is when we shift DAC
                        temps.append(int(final_temp))
                        duty_cycles.append(final_duty_cycle)
                        frequencies.append(final_clock_frequency)
                        avg_diffs.append(float(prev_smallest_avg_diff))
                        idds.append(float(final_idd.tolist()[-1]*1e6)) # in uA
                        voltage_supplies.append(final_supply_voltage)   
                    else:
                        print(f'No valid zero crossing vout values found to append for corner {corner}, voltage {voltage}, temp {temp}.')
                        zc_not_valid_count = zc_not_valid_count + 1
                        zc_nv[f"{corner}_{c}_{voltage}"] = {
                            "temp": final_temp,
                            "corner": corner,
                            "voltage": voltage,
                            "frequency": final_clock_frequency,
                            "duty_cycle": final_duty_cycle,                            
                        }

                print(f'temps: {temps}')
                print(f'vouts: {vouts}')
                print(f'times: {times}')
                print(f'duty_cycles: {duty_cycles}')
                print(f'frequencies: {frequencies}')
                print(f'avg_diffs: {avg_diffs}')
                print(f'idds (uA): {idds}')
                print(f'voltage_supplies: {voltage_supplies}')

                data[f"{corner}_{c}_{voltage}"] = {
                    "temps": temps,
                    "vouts": vouts,
                    "times": times,
                    "duty_cycles": duty_cycles,
                    "frequencies": frequencies,
                    "avg_diffs": avg_diffs,
                    "idds": idds,
                    "supply_voltages": voltage_supplies,
                }

                axs.plot(temps, vouts, marker='o', linestyle= 'dashed', markersize=4) # in V
                last_color = axs.lines[-1].get_color()

                avg_vout = sum(vouts) / len(vouts)
                avg_vouts[f"{corner}_{c}_{voltage}"] = {avg_vout}
                TC = ( (max(vouts) - min(vouts)) / (avg_vout * (max(temps) - min(temps))) ) * 1e6
                TCs[f"{corner}_{c}_{voltage}"] = {TC}
    
                if not case == "mc": 
                    # axs.lines[-1].set_label(f"{process_corner_short}, {Vx}, TC: {TC:.0f} ppm/°C, Avg: {avg_vout:.2f} V")
                    axs.lines[-1].set_label(f"{process_corner_short}, {Vx}")
                # else:
                #     axs.lines[-1].set_label(f"{process_corner_short}, {c}, {Vx}")

                # axs.plot(temps, [avg_vout]*len(temps), label=f'Avg: {avg_vout:.3f} V', linestyle='dotted', color=last_color)
                
                # find linear fit coefficients
                # fit_coeffs = np.polyfit(temps, vouts, 1)
                # fit_line = np.poly1d(fit_coeffs)
                # axs.plot(temps, fit_line(temps), color=last_color, linestyle='dotted')

    # axs.plot([], [], label=f"best fit", color="black", linestyle='dotted')

    print(f"Number of cases with no valid zero crossing vout values: {zc_not_valid_count}")
    print(f"Details of cases with no valid zero crossing vout values: {zc_nv}")

    # plot best fit line over all data
    all_temps = []
    all_vouts = []
    for corner in corners:
        for voltage in voltages:
            for c in range(mc_count_start, mc_count_stop):
                entry = data[f"{corner}_{c}_{voltage}"]
                temps = entry["temps"]
                vouts = entry["vouts"]
                all_temps.extend(temps)
                all_vouts.extend(vouts)
    fit_coeffs = np.polyfit(all_temps, all_vouts, 1)
    fit_line = np.poly1d(fit_coeffs)
    # axs.plot(sorted(all_temps), fit_line(sorted(all_temps)), color="black", linestyle='dotted', label=f"best fit")

    print(f"best fit linear trend in data: Vout = {fit_coeffs[0]*1e3:.3f} mV/°C + {fit_coeffs[1]*1e3:.3f} mV")

    # plot belt with largest deviation from best fit line
    deviations = [np.abs(vout - fit_line(temp)) for temp, vout in zip(all_temps, all_vouts)]
    max_deviation = max(deviations)
    upper_bound = [fit_line(temp) + max_deviation for temp in sorted(all_temps)]
    lower_bound = [fit_line(temp) - max_deviation for temp in sorted(all_temps)]
    # axs.fill_between(sorted(all_temps), lower_bound, upper_bound, color='gray', alpha=0.2, label='Max deviation')

    print(f"max deviation from best fit line: {max_deviation*1e3:.3f} mV") 

    # average TC over all cases
    avg_TC = sum([list(tc)[0] for tc in TCs.values()]) / len(TCs)
    print("TCs:", TCs)
    print(f"Average TC over all cases: {avg_TC:.0f} ppm/°C")

    # average Vout over all cases
    avg_vout_overall = sum([list(avg_vout)[0] for avg_vout in avg_vouts.values()]) / len(avg_vouts)
    print("avg vouts:", avg_vouts)
    print(f"Average Vout over all cases: {avg_vout_overall:.3f} V")

    # average TC over all cases without ssVl or fsVl corners
    avg_TC_filtered = sum([list(tc)[0] for key, tc in TCs.items() if not ("ss_0_1.7" in key or "fs_0_1.7" in key)]) / len([key for key in TCs.keys() if not ("ss_0_1.7" in key or "fs_0_1.7" in key)])
    print(f"Average TC over all cases without ssVl or fsVl corners: {avg_TC_filtered:.0f} ppm/°C")

    # average Vout over all cases without ssVl or fsVl corners
    avg_vout_filtered = sum([list(avg_vout)[0] for key, avg_vout in avg_vouts.items() if not ("ss_0_1.7" in key or "fs_0_1.7" in key)]) / len([key for key in avg_vouts.keys() if not ("ss_0_1.7" in key or "fs_0_1.7" in key)])
    print(f"Average Vout over all cases without ssVl or fsVl corners: {avg_vout_filtered:.3f} V")    

    # Average idds over all cases
    all_idds = []
    all_pwr = []
    all_voltage_supplies = []
    for corner in corners:
        for voltage in voltages:
            for c in range(mc_count_start, mc_count_stop):
                entry = data[f"{corner}_{c}_{voltage}"]
                idds = entry["idds"]
                all_idds.extend(idds)
                voltage_supplies = entry["supply_voltages"]
                all_voltage_supplies.extend(voltage_supplies)
                avg_pwr_case = sum([idd * vdd for idd, vdd in zip(idds, voltage_supplies)]) / len(idds)
                print(f"Average power consumption for case {corner}_{c}_{voltage}: {avg_pwr_case:.3f} uW")
    avg_idd = sum(all_idds) / len(all_idds)
    print(f"Average idd over all cases: {avg_idd:.3f} uA")
    print(f"{all_idds}")
    avg_voltage_supply = sum(all_voltage_supplies) / len(all_voltage_supplies)
    print(f"Average supply voltage over all cases: {avg_voltage_supply:.3f}")
          
    print(f"{all_voltage_supplies}")
    for idd, vdd in zip(all_idds, all_voltage_supplies):
        pwr = idd * vdd  # in uW
        all_pwr.append(pwr) 

    avg_pwr = sum(all_pwr) / len(all_pwr)
    print(f"Average power consumption over all cases: {avg_pwr:.3f} uW")
    print(f"{all_pwr}")

    axs.tick_params(axis='both', labelsize=ticks_fontsize)
    axs.grid()
    axs.set_ylabel('Voltage (V)', fontsize=label_fontsize)
    axs.set_xlabel('Temperature [°C]', fontsize=label_fontsize)
    # axs.set_title('Output vs Temperature', fontsize=title_fontsize)
    if case != "mc":
        axs.legend(loc="best", fontsize=legend_fontsize) #, ncol=2)

    fig.tight_layout()
    fig.savefig(f'figures/vout_vs_temp_bgr_{corners}_{voltages}.png', dpi=300, bbox_inches="tight")

    plt.show()

