import numpy as np
import pandas as pd    
import matplotlib.pyplot as plt
import sys
from scipy import stats

figure_width = 3
figure_height = 3
font_size = 7
title_font_size = font_size
label_font_size = font_size
legend_font_size = font_size - 1
ticks_font_size = font_size

arguments = sys.argv[1:]

stepping_direction = ""
if "up" in arguments:
    arguments.remove("up")
    stepping_direction = "up"
    print("Plotting for transient signals stepping upwards")
else: 
    stepping_direction = "down"
    print("Plotting for transient signals stepping downwards")


df = pd.read_csv(f"figures/{'_'.join(arguments)}_stepping_{stepping_direction}.csv")


temperatures = np.array(df["Temperature (°C)"])
voltages = np.array(df["Output voltage (V)"])

average_voltage = np.mean(voltages)
average_voltages = np.full_like(voltages, average_voltage)

average_voltage_deviations = np.abs(voltages - average_voltage)
average_voltage_max_deviation = np.max(average_voltage_deviations)
average_voltage_max_deviation_index = np.argmax(average_voltage_deviations)
average_voltage_max_deviation_temperature = temperatures[average_voltage_max_deviation_index]
average_voltage_max_deviation_voltage = voltages[average_voltage_max_deviation_index]

slope, intercept, r_value, p_value, standard_error = stats.linregress(temperatures, voltages)
linear_fit = slope * np.array(temperatures) + intercept

linear_fit_deviations = np.abs(voltages - linear_fit)
linear_fit_max_deviation = np.max(linear_fit_deviations)
linear_fit_max_deviation_index = np.argmax(linear_fit_deviations)
linear_fit_max_deviation_temperature = temperatures[linear_fit_max_deviation_index]
linear_fit_max_deviation_voltage = voltages[linear_fit_max_deviation_index]

temperature_coefficient = ((np.max(voltages) - np.min(voltages)) / (np.max(temperatures) - np.min(temperatures))) # in V/°C
temperature_coefficient_in_mV_per_C = temperature_coefficient * 1e3 # in mV/°C
temperature_coefficient_in_ppm = (temperature_coefficient / average_voltage) * 1e6 # in ppm/°C relative to average voltage


fig, axs = plt.subplots(1, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

axs.plot(temperatures, voltages, linestyle="none", marker="o", color="tab:blue", label="Simulation results")
axs.plot(temperatures, average_voltages, linestyle="dashed", color="tab:orange", label=f"Average voltage = {average_voltage:.4f} V")
# axs.plot(temperatures, linear_fit, linestyle="dashed", color="tab:green", label=f"Linear fit v={slope*1e3:.2f}t mV/°C + {intercept*1e3:.1f} mV, R²={r_value**2:.4f}")
axs.plot(average_voltage_max_deviation_temperature, average_voltage_max_deviation_voltage, linestyle="none", color="tab:red", marker="x", markeredgewidth=2, label=f"Max deviation from avg.\n voltage: {average_voltage_max_deviation*1e3:.2f} mV at {average_voltage_max_deviation_temperature} °C")
# axs.plot(linear_fit_max_deviation_temperature, linear_fit_max_deviation_voltage, linestyle="none", color="tab:red", marker="+", markersize=8, markeredgewidth=2, label=f"Max deviation from lin. fit: {linear_fit_max_deviation*1e3:.2f} mV at {linear_fit_max_deviation_temperature} °C")

axs.set_title(f"Temperature sensitivity of output voltage", fontsize=title_font_size, fontweight='bold')
axs.set_xlabel("Temperature (°C)", fontsize=label_font_size)
axs.set_ylabel("Output voltage (V)", fontsize=label_font_size)
axs.legend(loc="best", fontsize=legend_font_size)
axs.tick_params(axis='both', labelsize=ticks_font_size)
axs.grid()

fig.tight_layout()
fig.savefig(f"figures/{'_'.join(arguments)}_stepping_{stepping_direction}_temperature_vs_output_voltage.png", dpi=300, bbox_inches="tight")


coarse_code = np.array(df["Coarse code"])
fine_code = np.array(df["Fine code"])

dac_code = coarse_code * 10 + fine_code

fig_dac, axs_dac = plt.subplots(1, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

axs_dac.plot(temperatures, dac_code, linestyle="none", marker="o", color="tab:blue", label="DAC code")
# axs_dac.plot(temperatures, fine_code, linestyle="none", marker="o", color="tab:orange", label="Fine code")
# axs_dac.plot(temperatures, coarse_code, linestyle="none", marker="o", color="tab:green", label="Coarse code")

axs_dac.set_title(f"Temperature sensitivity of the DAC input", fontsize=title_font_size, fontweight='bold')
axs_dac.set_xlabel("Temperature (°C)", fontsize=label_font_size)
axs_dac.set_ylabel("DAC code", fontsize=label_font_size)
axs_dac.legend(loc="best", fontsize=legend_font_size)
axs_dac.tick_params(axis='both', labelsize=ticks_font_size)
axs_dac.grid()

fig_dac.tight_layout()
fig_dac.savefig(f"figures/{'_'.join(arguments)}_stepping_{stepping_direction}_temperature_vs_dac_code.png", dpi=300, bbox_inches="tight")


min_pwr = np.array(df["Minimum power (uW)"])
avg_pwr = np.array(df["Average power (uW)"])
max_pwr = np.array(df["Maximum power (uW)"])

fig_pwr, axs_pwr = plt.subplots(1, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

axs_pwr.plot(temperatures, min_pwr, linestyle="none", marker="o", markersize=5, color="tab:blue", label="Minimum power")
axs_pwr.plot(temperatures, avg_pwr, linestyle="none", marker="s", markersize=5, color="tab:orange", label="Average power")
axs_pwr.plot(temperatures, max_pwr, linestyle="none", marker="v", markersize=5, color="tab:green", label="Maximum power")

axs_pwr.set_title(f"Temperature sensitivity of the power consumption", fontsize=title_font_size, fontweight='bold')
axs_pwr.set_xlabel("Temperature (°C)", fontsize=label_font_size)
axs_pwr.set_ylabel("Power (uW)", fontsize=label_font_size)
axs_pwr.legend(loc="best", fontsize=legend_font_size)
axs_pwr.tick_params(axis='both', labelsize=ticks_font_size)
axs_pwr.grid()

fig_pwr.tight_layout()
fig_pwr.savefig(f"figures/{'_'.join(arguments)}_stepping_{stepping_direction}_temperature_vs_power.png", dpi=300, bbox_inches="tight")


slp_min_pwr = np.array(df["Sleep min power (uW)"])
slp_avg_pwr = np.array(df["Sleep avg power (uW)"])
slp_max_pwr = np.array(df["Sleep max power (uW)"])

fig_slp, axs_slp = plt.subplots(1, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

axs_slp.plot(temperatures, slp_min_pwr, linestyle="none", marker="o", markersize=5, color="tab:blue", label="Sleep minimum power")
axs_slp.plot(temperatures, slp_avg_pwr, linestyle="none", marker="s", markersize=5, color="tab:orange", label="Sleep average power")
axs_slp.plot(temperatures, slp_max_pwr, linestyle="none", marker="v", markersize=5, color="tab:green", label="Sleep maximum power")

axs_slp.set_title(f"Temperature sensitivity of the sleep power consumption", fontsize=title_font_size, fontweight='bold')
axs_slp.set_xlabel("Temperature (°C)", fontsize=label_font_size)
axs_slp.set_ylabel("Power (uW)", fontsize=label_font_size)
axs_slp.legend(loc="best", fontsize=legend_font_size)
axs_slp.tick_params(axis='both', labelsize=ticks_font_size)
axs_slp.grid()

fig_slp.tight_layout()
fig_slp.savefig(f"figures/{'_'.join(arguments)}_stepping_{stepping_direction}_temperature_vs_sleep_power.png", dpi=300, bbox_inches="tight")



plt.show()