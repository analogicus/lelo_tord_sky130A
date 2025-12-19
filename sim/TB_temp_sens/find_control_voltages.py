import pandas as pd
import matplotlib.pyplot as plt
import sys

args = sys.argv[1:]
files = list()

min_ctls = dict()
max_ctls = dict()

ctl_time_limit = 14000  # in ns

if "all" in args:
    for corner in ["tt", "ss", "ff", "sf", "fs"]:
        for temperature in [-40, 0, 27, 125]: # Celsius (degree C)
            for frequency in [2]: # Mega Hertz (MHz)
                for dutycycle in [10, 20, 30, 40, 50, 60, 70, 80, 90]: # Percent (%)
                    for voltage in [1.7, 1.8, 1.9]: # Volt (V)
                        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_temperature{temperature}celsius_frequency{frequency}mhz_dutycycle{dutycycle}percent_vdd{voltage}volt.out")

fig_width = 3
fig_height = 5
font_size = 8
title_fontsize = font_size
label_fontsize = font_size
legend_fontsize = font_size
ticks_fontsize = font_size

print("========================================")
for file in files:
    print(f"file: {file}")

    circuit_temperature = int(file.split("temperature")[-1].split("celsius")[0]) # in Celsius degree
    clock_frequency = int(file.split("frequency")[-1].split("mhz")[0]) # in Mega Hertz
    clock_periode = 1 / clock_frequency  # in micro seconds
    duty_cycle = int(file.split("dutycycle")[-1].split("percent")[0]) # in Percent
    voltage_supply = float(file.split("vdd")[-1].split("volt")[0]) # in Volt
    process_corner = "Typical" if "tt" in file else "Slow-Slow" if "ss" in file else "Slow-Fast" if "sf" in file else "Fast-Slow" if "fs" in file else "Fast-Fast" if "ff" in file else "Oops, something is wrong!"

    print(f"Circuit temperature: {circuit_temperature} Celsius degree.")
    print(f"Clock frequency of finetuning signal: {clock_frequency} Mega Hertz, and clock periode is: {clock_periode} micro seconds.")
    print(f"Duty cycle of fine tuning signal: {duty_cycle} %.")
    print(f"Supply voltage (VDD): {voltage_supply} Volt.")
    print(f"Circuit process corners: {process_corner}.")

    df = pd.read_csv(file, sep="\s+")

    df['time'] = df['time'] * 1e9 # in ns

    max_ctl = df['v(x1.ctl)'][(df['time'] > ctl_time_limit)].max()
    min_ctl = df['v(x1.ctl)'][(df['time'] > ctl_time_limit)].min()
    
    print("-----------------------------------------")
    print(f"Control voltage max: {max_ctl} V, min: {min_ctl} V")

    min_ctls[file] = min_ctl
    max_ctls[file] = max_ctl
    print("========================================")

min_ctl_overall = min(min_ctls.values())
max_ctl_overall = max(max_ctls.values())

min_ctl_file = [key for key, value in min_ctls.items() if value == min_ctl_overall][0]
max_ctl_file = [key for key, value in max_ctls.items() if value == max_ctl_overall][0]

max_circuit_temperature = int(max_ctl_file.split("temperature")[-1].split("celsius")[0]) # in Celsius degree
max_clock_frequency = int(max_ctl_file.split("frequency")[-1].split("mhz")[0]) # in Mega Hertz
max_clock_periode = 1 / max_clock_frequency  # in micro seconds
max_duty_cycle = int(max_ctl_file.split("dutycycle")[-1].split("percent")[0]) # in Percent
max_voltage_supply = float(max_ctl_file.split("vdd")[-1].split("volt")[0]) # in Volt
max_process_corner = "Typical" if "tt" in max_ctl_file else "Slow-Slow" if "ss" in max_ctl_file else "Slow-Fast" if "sf" in max_ctl_file else "Fast-Slow" if "fs" in max_ctl_file else "Fast-Fast" if "ff" in max_ctl_file else "Oops, something is wrong!"

min_circuit_temperature = int(min_ctl_file.split("temperature")[-1].split("celsius")[0]) # in Celsius degree
min_clock_frequency = int(min_ctl_file.split("frequency")[-1].split("mhz")[0]) # in Mega Hertz
min_clock_periode = 1 / min_clock_frequency  # in micro seconds
min_duty_cycle = int(min_ctl_file.split("dutycycle")[-1].split("percent")[0]) # in Percent
min_voltage_supply = float(min_ctl_file.split("vdd")[-1].split("volt")[0]) # in Volt
min_process_corner = "Typical" if "tt" in min_ctl_file else "Slow-Slow" if "ss" in min_ctl_file else "Slow-Fast" if "sf" in min_ctl_file else "Fast-Slow" if "fs" in min_ctl_file else "Fast-Fast" if "ff" in min_ctl_file else "Oops, something is wrong!"

print(f"Overall min vctl: {min_ctl_overall} V ({min_process_corner}, {min_circuit_temperature} C, {min_clock_frequency} MHz, {min_duty_cycle} %, {min_voltage_supply} V),\nOverall max vctl: {max_ctl_overall} V ({max_process_corner}, {max_circuit_temperature} C, {max_clock_frequency} MHz, {max_duty_cycle} %, {max_voltage_supply} V)")

plt.show()