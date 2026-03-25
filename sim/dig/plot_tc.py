import pandas as pd    
import matplotlib.pyplot as plt
import sys

fig_width = 3
fig_height = 4
font_size = 6
title_fontsize = font_size
label_fontsize = font_size
legend_fontsize = font_size
ticks_fontsize = font_size

args = sys.argv[1:]

print(f"reading data from: figures/{'_'.join(args)}.csv")
df = pd.read_csv(f"figures/{'_'.join(args)}.csv")

x = df["Temperature (°C)"].tolist()
y = df["Reference voltage (V)"].tolist()

tmax = max(x)
print(f"Maximum temperature: {tmax:.2f} °C")
tmin = min(x) 
print(f"Minimum temperature: {tmin:.2f} °C")
vmax = max(y)
print(f"Maximum reference voltage: {vmax:.4f} V")
vmin = min(y)
print(f"Minimum reference voltage: {vmin:.4f} V")
vavg = sum(y) / len(y)
print(f"Average reference voltage: {vavg:.4f} V")
tc = (vmax - vmin) / (vavg * (tmax - tmin)) * 1e6 # temperature coefficient in ppm per degree Celsius
print(f"Temperature coefficient (TC) of the reference voltage: {tc:.2f} ppm/°C")

fig_6, axs_6 = plt.subplots(1, 1, figsize=(5, 5), sharex=True, dpi=300)

axs_6.plot(x, y, marker="o", linestyle="dashed", label="Temperature coefficient (TC) = {:.2f} ppm/°C".format(tc))

axs_6.set_xlabel("Temperature (°C)", fontsize=label_fontsize)
axs_6.set_ylabel("Reference voltage (V)", fontsize=label_fontsize)
axs_6.grid()
axs_6.legend(loc="best", fontsize=legend_fontsize)
# axs_6.set_yticks([0, 0.9, 1.8])
# axs_6.set_xticks(x)

fig_6.tight_layout()
fig_6.savefig(f"figures/{'_'.join(args)}_tc.png", dpi=300, bbox_inches="tight")

plt.show()