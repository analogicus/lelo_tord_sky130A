#!/usr/bin/env python3
import pandas as pd
import yaml
import matplotlib.pyplot as plt

fig_width = 3.2
fig_height = 4
font_size = 8
title_fontsize = font_size
label_fontsize = font_size
legend_fontsize = font_size
ticks_fontsize = font_size

def main(name):
  # Delete next line if you want to use python post processing
  # return

  #
  # Parse data saved in .yaml file
  #

  yamlfile = name + ".yaml"

  # Read result yaml file
  with open(yamlfile) as fi:
    obj = yaml.safe_load(fi)

  # Do something to parameters
  print(obj)

  # Save new yaml file
  with open(yamlfile,"w") as fo:
    yaml.dump(obj,fo)

  #
  # Parse transient simulation data saved in .out file
  #

  outfile = name + ".out"
  df = pd.read_csv(outfile, sep="\s+")

  df["time"] = df["time"] * 1e9 # in ns
  df["acgain"] = df["v(vout)"] / 1e-3 # AC Gain ≈ V(out) (mV) / 1 mV
  df["dcgain"] = df["v(vout)"].diff() / df["time"].diff() # Gain ≈ ΔVout / ΔVin

  #
  # Plot transient simulation data saved in .out file
  #

  fig, axs = plt.subplots(3, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)

  axs[0].plot(df["time"], df["v(vin)"], label=f"vin")
  axs[0].plot(df["time"], df["v(vip)"], label=f"vip")
  
  axs[1].plot(df["time"], df["v(vout)"], label=f"vout, nmos input")
  axs[1].plot(df["time"], df["v(vout_pmos)"], label=f"vout, pmos input")

  axs[2].plot(df["time"], df["acgain"], label=f"small signal gain, max: {round(max(df['acgain']), 1)}")
  axs[2].plot(df["time"], df["dcgain"], label=f"large signal gain")

  for ax in axs:
      ax.tick_params(axis="both", labelsize=ticks_fontsize)
      ax.legend(loc="best", fontsize=legend_fontsize)
      ax.grid()
  
  axs[0].set_title(f"{name}", fontsize=title_fontsize, fontweight="bold")
  axs[-1].set_xlabel("Time (ns)", fontsize=label_fontsize)

  axs[0].set_ylabel("Voltage (V)", fontsize=label_fontsize)
  axs[1].set_ylabel("Voltage (V)", fontsize=label_fontsize)
  axs[2].set_ylabel("Gain (V/V)", fontsize=label_fontsize)

  axs[1].set_ylim(bottom=0 - (max(df["v(vout)"]) * 0.05))

  fig.tight_layout()
  fig.savefig(f"figures/{name.split('/')[-1]}.png", bbox_inches="tight", dpi=300)

  #
  # Parse AC simulation data saved in .out file
  #

  ac_outfile = name + "_ac.out"
  ac_df = pd.read_csv(ac_outfile, sep="\s+")

  ac_df["frequency"] = ac_df["frequency"] * 1e-6 # in MHz
  ac_df["acgain"] = ac_df["vm(vout)"] / ac_df["vm(vip)"] # AC Gain ≈ V(out) / 1 mV
  ac_df["dcgain"] = ac_df["vm(vout)"].diff() / ac_df["frequency"].diff() # Gain ≈ ΔVout / ΔVin

  #
  # Plot AC simulation data saved in .out file
  #

  ac_fig, ac_axs = plt.subplots(4, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)

  ac_axs[0].plot(ac_df["frequency"], ac_df["vm(vout)"], label=f"vout")
  ac_axs[0].plot(ac_df["frequency"], ac_df["vm(vip)"], label=f"vip")
  ac_axs[0].plot(ac_df["frequency"], ac_df["vm(vin)"], label=f"vin")

  ac_axs[1].plot(ac_df["frequency"], ac_df["vdb(vout)"], label=f"vout")
  ac_axs[1].plot(ac_df["frequency"], ac_df["vdb(vip)"], label=f"vip")

  ac_axs[2].plot(ac_df["frequency"], ac_df["vdb(vout)"]-ac_df["vdb(vip)"], label=f"vout-vip")

  ac_axs[3].plot(ac_df["frequency"], ac_df["acgain"], label=f"small signal gain")
  ac_axs[3].plot(ac_df["frequency"], ac_df["dcgain"], label=f"large signal gain")

  for ax in ac_axs:
      ax.tick_params(axis="both", labelsize=ticks_fontsize)
      ax.legend(loc="best", fontsize=legend_fontsize)
      ax.grid()
  
  ac_axs[0].set_title(f"{name}", fontsize=title_fontsize, fontweight="bold")
  ac_axs[-1].set_xlabel("Frequency (MHz)", fontsize=label_fontsize)

  ac_axs[0].set_ylabel("Voltage (V)", fontsize=label_fontsize)
  ac_axs[1].set_ylabel("Magnitude (dB)", fontsize=label_fontsize)
  ac_axs[2].set_ylabel("Gain (V/V)", fontsize=label_fontsize)

  ac_fig.tight_layout()
  ac_fig.savefig(f"figures/{name.split('/')[-1]}_ac.png", bbox_inches="tight", dpi=300)

  #
  # Plot figures
  #  

  plt.show()


