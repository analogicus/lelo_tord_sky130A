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


#
# Plot last output voltage detected in transient simulations vs temperature and calculate temperature sensitivity in mV/°C
#

dataframe1 = pd.read_csv(f"figures/{'_'.join(arguments)}_df1.csv")

temperatures = dataframe1["Temperature (°C)"].tolist()
voltages = dataframe1["Output voltage (V)"].tolist()

slope, intercept, r_value, p_value, standard_error = stats.linregress(temperatures, voltages)
linear_fit = slope * np.array(temperatures) + intercept

deviations = np.array(voltages) - linear_fit
absolute_deviations = np.abs(deviations)

max_deviation_index = np.argmax(absolute_deviations)
max_deviation_temperature = temperatures[max_deviation_index]
max_deviation_voltage = voltages[max_deviation_index]
max_deviation = absolute_deviations[max_deviation_index] * 1e3 # in mV

fig, axs = plt.subplots(1, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

axs.plot(temperatures, voltages, linestyle="none", marker="o", color="tab:blue", label="Simulation results")
axs.plot(temperatures, linear_fit, linestyle="dashed", marker="none", color="black", label=f"Linear fit: v={slope:.4f}t+{intercept:.3f}, R²={r_value**2:.2f}")
axs.plot(max_deviation_temperature, max_deviation_voltage, linestyle="none", marker="x", color="red", markersize=7, markeredgewidth=2, label=f"Max deviation: {max_deviation:.1f} mV at {max_deviation_temperature:.1f} °C")

axs.set_title(f"Temperature sensitivity of \n the output voltage using dataframe 1", fontsize=title_font_size, fontweight='bold')
axs.set_xlabel("Temperature (°C)", fontsize=label_font_size)
axs.set_ylabel("Output voltage (V)", fontsize=label_font_size)
axs.legend(loc="best", fontsize=legend_font_size)
axs.tick_params(axis='both', labelsize=ticks_font_size)
axs.grid()

fig.tight_layout()
fig.savefig(f"figures/{'_'.join(arguments)}_temperature_vs_output_voltage_dataframe1.png", bbox_inches="tight")


#
# Plot last DAC code vs temperature
#

coarse_codes = dataframe1["Coarse code"].tolist() # given in mV, but we will convert it to V for better readability in the plot
fine_codes = dataframe1["Fine code"].tolist() # given in mV, but we will convert it to V for better readability in the plot

coarse_codes = [code*1e3 for code in coarse_codes] # converted to V for better readability in the plots
fine_codes = [code*1e3 for code in fine_codes] # converted to V for better readability in the plots

dac_label = "Temp., coarse, fine:"
for temperature, coarse, fine in zip(temperatures, coarse_codes, fine_codes):
    dac_label += (f"\n{temperature:6.1f}°C, {coarse:4.1f}, {fine:4.1f}")

dac_codes = [coarse * 10 + fine for coarse, fine in zip(coarse_codes, fine_codes)]

fig_1, axs_1 = plt.subplots(1, 1, figsize=(figure_width * 1.5, figure_height*1.25), sharex=True, dpi=300)

axs_1.plot(temperatures, dac_codes, color="tab:blue", marker="o", linestyle="dashed", label=dac_label)

axs_1.set_title(f"Temperature sensitivity of \n the DAC input code", fontsize=title_font_size, fontweight='bold')
axs_1.set_xlabel("Temperature (°C)", fontsize=label_font_size)
axs_1.set_ylabel("DAC code", fontsize=label_font_size)
axs_1.legend(loc='upper left', bbox_to_anchor=(1.01, 1.05), fontsize=legend_font_size)
axs_1.tick_params(axis='both', labelsize=ticks_font_size)
axs_1.grid()

fig_1.tight_layout()
fig_1.savefig(f"figures/{'_'.join(arguments)}_temperature_vs_dac_code_dataframe1.png", dpi=300, bbox_inches="tight")


#
# Plot output voltage vs temperature again, but this time at the first value aquired in the transient simulation
#

dataframe2 = pd.read_csv(f"figures/{'_'.join(arguments)}_df2.csv")

temperatures2 = dataframe2["Temperature (°C)"].tolist()
voltages2 = dataframe2["Output voltage (V)"].tolist()

slope2, intercept2, r_value2, p_value2, standard_error2 = stats.linregress(temperatures2, voltages2)
linear_fit2 = slope2 * np.array(temperatures2) + intercept2

deviations2 = np.array(voltages2) - linear_fit2
absolute_deviations2 = np.abs(deviations2)

max_deviation_index2 = np.argmax(absolute_deviations2)
max_deviation_temperature2 = temperatures2[max_deviation_index2]
max_deviation_voltage2 = voltages2[max_deviation_index2]
max_deviation2 = absolute_deviations2[max_deviation_index2] * 1e3 # in mV

fig_2, axs_2 = plt.subplots(1, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

axs_2.plot(temperatures2, voltages2, linestyle="none", color="tab:orange", marker="o", label="Simulation results")
axs_2.plot(temperatures2, linear_fit2, linestyle="dashed", color="black", label=f"Linear fit: v={slope2:.4f}t+{intercept2:.3f}, R²={r_value2**2:.2f}")
axs_2.plot(max_deviation_temperature2, max_deviation_voltage2, linestyle="none", color="tab:red", marker="x", markersize=7, markeredgewidth=2, label=f"Max deviation: {max_deviation2:.1f} mV at {max_deviation_temperature2:.1f} °C")

axs_2.set_title(f"Temperature sensitivity of \n the output voltage using dataframe 2", fontsize=title_font_size, fontweight='bold')
axs_2.set_xlabel("Temperature (°C)", fontsize=label_font_size)
axs_2.set_ylabel("Output voltage (V)", fontsize=label_font_size)
axs_2.legend(loc="best", fontsize=legend_font_size)
axs_2.tick_params(axis='both', labelsize=ticks_font_size)
axs_2.grid()

fig_2.tight_layout()
fig_2.savefig(f"figures/{'_'.join(arguments)}_temperature_vs_output_voltage_dataframe2.png", dpi=300, bbox_inches="tight")


#
# Plot DAC code vs temperature again, but this time at the first value aquired in the transient simulation
#

coarse_codes2 = dataframe2["Coarse code"].tolist()
fine_codes2 = dataframe2["Fine code"].tolist()

coarse_codes2 = [code*1e3 for code in coarse_codes2]
fine_codes2 = [code*1e3 for code in fine_codes2]

dac_label2 = "Temp., coarse, fine:"
for temperature2, coarse2, fine2 in zip(temperatures2, coarse_codes2, fine_codes2):
    dac_label2 += (f"\n{temperature2:6.1f}°C, {coarse2:4.1f}, {fine2:4.1f}")

dac_codes2 = [coarse * 10 + fine for coarse, fine in zip(coarse_codes2, fine_codes2)]

fig_3, axs_3 = plt.subplots(1, 1, figsize=(figure_width * 1.5, figure_height*1.25), sharex=True, dpi=300)

axs_3.plot(temperatures2, dac_codes2, linestyle="dashed", marker="o", color="tab:orange", label=dac_label2)

axs_3.set_title(f"Temperature sensitivity of \nthe DAC input code", fontsize=title_font_size, fontweight='bold')
axs_3.set_xlabel("Temperature (°C)", fontsize=label_font_size)
axs_3.set_ylabel("DAC code", fontsize=label_font_size)
axs_3.legend(loc='upper left', bbox_to_anchor=(1.01, 1.05), fontsize=legend_font_size)
axs_3.tick_params(axis='both', labelsize=ticks_font_size)
axs_3.grid()

fig_3.tight_layout()
fig_3.savefig(f"figures/{'_'.join(arguments)}_temperature_vs_dac_code_dataframe2.png", dpi=300, bbox_inches="tight")


#
# temperature calculated from voltage using the linear fit
#

calculated_temperatures = (np.array(voltages2) - intercept2) / slope2

slope3, intercept3, r_value3, p_value3, standard_error3 = stats.linregress(temperatures2, calculated_temperatures)
linear_fit3 = slope3 * np.array(temperatures2) + intercept3

max_deviation_index3 = np.argmax(np.abs(np.array(calculated_temperatures) - linear_fit3))
max_deviation_temperature3 = temperatures2[max_deviation_index3]
max_deviation_calculated_temperature = calculated_temperatures[max_deviation_index3]
max_deviation3 = np.abs(max_deviation_calculated_temperature - max_deviation_temperature3)

fig_4, axs_4 = plt.subplots(1, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

axs_4.plot(temperatures2, calculated_temperatures, linestyle="none", marker="o", color="tab:green", label="Simulation results")
axs_4.plot(temperatures2, linear_fit3, linestyle="dashed", marker="none", color="black", label=f"Linear fit: T={slope3:.4f}t+{intercept3:.3f}, R²={r_value3**2:.2f}")
axs_4.plot(max_deviation_temperature3, max_deviation_calculated_temperature, linestyle="none", marker="x", color="tab:red", markersize=7, markeredgewidth=2, label=f"Max deviation: {max_deviation3:.1f} °C at {max_deviation_temperature3:.1f} °C")

axs_4.set_title(f"Calculated temperature based on linear fit", fontsize=title_font_size, fontweight='bold')
axs_4.set_xlabel("Actual temperature (°C)", fontsize=label_font_size)
axs_4.set_ylabel("Calculated temperature (°C)", fontsize=label_font_size)
axs_4.legend(loc="best", fontsize=legend_font_size)
axs_4.tick_params(axis='both', labelsize=ticks_font_size)
axs_4.grid()

fig_4.tight_layout()
fig_4.savefig(f"figures/{'_'.join(arguments)}_calculated_temperature_vs_actual_temperature_dataframe2.png", dpi=300, bbox_inches="tight")


plt.show()