import pandas as pd    
import matplotlib.pyplot as plt
import sys
import numpy as np
from scipy import stats

fig_width = 3
fig_height = 3
font_size = 7
title_fontsize = font_size
label_fontsize = font_size
legend_fontsize = font_size -1
ticks_fontsize = font_size

args = sys.argv[1:]


#
# Plot last output voltage detected in transient simulations vs temperature and calculate temperature sensitivity in mV/°C
#

df = pd.read_csv(f"figures/{'_'.join(args)}_df1.csv")

t = df["Temperature (°C)"].tolist()
v = df["Output voltage (V)"].tolist()

slope, intercept, r_value, p_value, std_err = stats.linregress(t, v)
v_fit = slope * np.array(t) + intercept

max_dev_idx = np.argmax(np.abs(np.array(v) - v_fit))
t_dev = t[max_dev_idx]
v_dev = v[max_dev_idx]
v_diff = np.abs(v[max_dev_idx] - v_fit[max_dev_idx]) * 1e3 # in mV

fig, axs = plt.subplots(1, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)

axs.plot(t, v, linestyle="none", color="tab:blue", marker="o", label="Simulation results")
axs.plot(t, v_fit, linestyle="dashed", color="black", label=f"Linear fit: v={slope:.4f}t+{intercept:.3f}, R²={r_value**2:.2f}")
axs.plot(t_dev, v_dev, linestyle="none", color="red", marker="x", markersize=7, markeredgewidth=2, label=f"Max deviation: {v_diff:.1f} mV at {t_dev:.1f} °C")

axs.set_title(f"Temperature sensitivity of \n the output voltage", fontsize=title_fontsize, fontweight='bold')
axs.set_xlabel("Temperature (°C)", fontsize=label_fontsize)
axs.set_ylabel("Output voltage (V)", fontsize=label_fontsize)
axs.legend(loc="best", fontsize=legend_fontsize)
axs.tick_params(axis='both', labelsize=ticks_fontsize)
# axs.set_yticks([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
# axs.set_xticks(t)
axs.grid()

fig.tight_layout()
fig.savefig(f"figures/{'_'.join(args)}_temp_vs_output_voltage_df1.png", dpi=300, bbox_inches="tight")


coarse_code = df["Coarse code"].tolist()
fine_code = df["Fine code"].tolist()

coarse_code = [code*1e3 for code in coarse_code]
fine_code = [code*1e3 for code in fine_code]

print(f"coarse code: {coarse_code}")
print(f"fine code: {fine_code}")

dac_label_string = "Temperature, coarse code, fine code:"
for temp, coarse, fine in zip(t, coarse_code, fine_code):
    dac_label_string += (f"\n{temp:6.1f}°C, {coarse:4.1f}, {fine:4.1f}")

dac_code = [coarse * 10 + (fine - 1) for coarse, fine in zip(coarse_code, fine_code)]

fig_1, axs_1 = plt.subplots(1, 1, figsize=(fig_width * 2, fig_height), sharex=True, dpi=300)
axs_1.plot(t, dac_code, color="tab:blue", marker="o", linestyle="dashed", label=dac_label_string)

axs_1.set_title(f"Temperature sensitivity of \n the DAC input code", fontsize=title_fontsize, fontweight='bold')
axs_1.set_xlabel("Temperature (°C)", fontsize=label_fontsize)
axs_1.set_ylabel("DAC code", fontsize=label_fontsize)
axs_1.grid()
axs_1.legend(loc='upper left', bbox_to_anchor=(1.05, 1.00), fontsize=legend_fontsize)
# axs_1.set_yticks([0, max(dac_code)/2, 1.1*max(dac_code)])
# axs_1.set_xticks(x)

fig_1.tight_layout()
fig_1.savefig(f"figures/{'_'.join(args)}_temp_vs_dac_code_df1.png", dpi=300, bbox_inches="tight")



#
# Plot output voltage vs temperature again, but this time at the first value aquired in the transient simulation
#

df2 = pd.read_csv(f"figures/{'_'.join(args)}_df2.csv")

t2 = df2["Temperature (°C)"].tolist()
v2 = df2["Output voltage (V)"].tolist()

slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(t2, v2)
v_fit2 = slope2 * np.array(t2) + intercept2

max_dev_idx2 = np.argmax(np.abs(np.array(v2) - v_fit2))
t_dev2 = t2[max_dev_idx2]
v_dev2 = v2[max_dev_idx2]
v_diff2 = np.abs(v2[max_dev_idx2] - v_fit2[max_dev_idx2]) * 1e3 # in mV

fig_2, axs_2 = plt.subplots(1, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)

axs_2.plot(t2, v2, linestyle="none", color="tab:orange", marker="o", label="Simulation results")
axs_2.plot(t2, v_fit2, linestyle="dashed", color="black", label=f"Linear fit: v={slope2:.4f}t+{intercept2:.3f}, R²={r_value2**2:.2f}")
axs_2.plot(t_dev2, v_dev2, linestyle="none", color="tab:red", marker="x", markersize=7, markeredgewidth=2, label=f"Max deviation: {v_diff2:.1f} mV at {t_dev2:.1f} °C")

axs_2.set_title(f"Temperature sensitivity of \n the output voltage", fontsize=title_fontsize, fontweight='bold')
axs_2.set_xlabel("Temperature (°C)", fontsize=label_fontsize)
axs_2.set_ylabel("Output voltage (V)", fontsize=label_fontsize)
axs_2.grid()
axs_2.legend(loc="best", fontsize=legend_fontsize)
# axs_2.set_yticks([0, max(dac_code)/2, 1.1*max(dac_code)])
# axs_2.set_xticks(x)

fig_2.tight_layout()
fig_2.savefig(f"figures/{'_'.join(args)}_temp_vs_output_voltage_df2.png", dpi=300, bbox_inches="tight")


coarse_code2 = df2["Coarse code"].tolist()
fine_code2 = df2["Fine code"].tolist()

coarse_code2 = [code*1e3 for code in coarse_code2]
fine_code2 = [code*1e3 for code in fine_code2]

print(f"coarse code v2: {coarse_code2}")
print(f"fine code v2: {fine_code2}")

dac_label_string2 = "Temperature, coarse code, fine code:"
for temp2, coarse2, fine2 in zip(t2, coarse_code2, fine_code2):
    dac_label_string2 += (f"\n{temp2:6.1f}°C, {coarse2:4.1f}, {fine2:4.1f}")

dac_code2 = [coarse * 10 + (fine - 1) for coarse, fine in zip(coarse_code2, fine_code2)]

fig_3, axs_3 = plt.subplots(1, 1, figsize=(fig_width * 2, fig_height * 1.5), sharex=True, dpi=300)
axs_3.plot(t2, dac_code2, color="tab:orange", marker="o", linestyle="dashed", label=dac_label_string2)

axs_3.set_title(f"Temperature sensitivity of \nthe DAC input code", fontsize=title_fontsize, fontweight='bold')
axs_3.set_xlabel("Temperature (°C)", fontsize=label_fontsize)
axs_3.set_ylabel("DAC code", fontsize=label_fontsize)
axs_3.grid()
axs_3.legend(loc='upper left', bbox_to_anchor=(1.01, 1.05), fontsize=legend_fontsize)
# axs_3.set_yticks([0, max(dac_code)/2, 1.1*max(dac_code)])
# axs_3.set_xticks(x)

fig_3.tight_layout()
fig_3.savefig(f"figures/{'_'.join(args)}_temp_vs_dac_code_df2.png", dpi=300, bbox_inches="tight")


# temperature calculated from voltage using the linear fit
t_calc2 = (np.array(v2) - intercept2) / slope2

slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(t2, t_calc2)
t_fit = slope3 * np.array(t2) + intercept3

max_t_dev_idx = np.argmax(np.abs(np.array(t_calc2) - t_fit))
t_dev = t2[max_t_dev_idx]
t_calc_dev = t_calc2[max_t_dev_idx]
t_diff = np.abs(t2[max_t_dev_idx] - t_fit[max_t_dev_idx])

fig_4, axs_4 = plt.subplots(1, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)
# axs_4.plot(t2, t_calc2, color="tab:red", marker="o", linestyle="none", label=dac_label_string2)

axs_4.plot(t2, t_calc2, linestyle="none", color="tab:green", marker="o", label="Simulation results")
axs_4.plot(t2, t_fit, linestyle="dashed", color="black", label=f"Linear fit: T={slope3:.4f}t+{intercept3:.3f}, R²={r_value3**2:.2f}")
axs_4.plot(t_dev, t_calc_dev, linestyle="none", color="tab:red", marker="x", markersize=7, markeredgewidth=2, label=f"Max deviation: {t_diff:.1f} °C at {t_dev:.1f} °C")

axs_4.set_title(f"Temperature sensitivity of \n calcualted temperature code", fontsize=title_fontsize, fontweight='bold')
axs_4.set_xlabel("Actual temperature (°C)", fontsize=label_fontsize)
axs_4.set_ylabel("Calculated temperature from voltage \nbased on linear fit function (°C)", fontsize=label_fontsize)
axs_4.grid()
axs_4.legend(loc="best", fontsize=legend_fontsize)
# axs_4.set_yticks([0, max(dac_code)/2, 1.1*max(dac_code)])
# axs_4.set_xticks(x)

fig_4.tight_layout()
fig_4.savefig(f"figures/{'_'.join(args)}_actual_temp_vs_calculated_temp_df2.png", dpi=300, bbox_inches="tight")


plt.show()