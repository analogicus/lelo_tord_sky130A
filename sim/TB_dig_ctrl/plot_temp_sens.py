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

df = pd.read_csv(f"figures/{'_'.join(args)}.csv")

t = df["Temperature (°C)"].tolist()
v = df["Output voltage (V)"].tolist()

slope, intercept, r_value, p_value, std_err = stats.linregress(t, v)
v_fit = slope * np.array(t) + intercept

max_dev_idx = np.argmax(np.abs(np.array(v) - v_fit))
t_dev = t[max_dev_idx]
v_dev = v[max_dev_idx]
v_diff = np.abs(v[max_dev_idx] - v_fit[max_dev_idx]) * 1e3 # in mV

fig, axs = plt.subplots(1, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)

axs.plot(t, v, linestyle="none", color="gray", marker="o", label="Simulation results")
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
fig.savefig(f"figures/{'_'.join(args)}.png", dpi=300, bbox_inches="tight")

plt.show()