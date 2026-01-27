#!/usr/bin/env python3
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import numpy as np

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
  # Parse transient simulation data saved in .out file, calculate and plot gain
  #

  outfile = name + ".out"
  df = pd.read_csv(outfile, sep="\s+")

  df["time"] = df["time"] * 1e6 # in us
  
  AVout = max(df["v(vout)"]) - min(df["v(vout)"])
  AVout_pmos = max(df["v(vout_pmos)"]) - min(df["v(vout_pmos)"])
  AVip = max(df["v(vip)"]) - min(df["v(vip)"])
  
  print(f"AVout: {AVout} V, AVout_pmos: {AVout_pmos} V, AVip: {AVip} V")
  print(f"tran Gain: {AVout/AVip} V/V, tran Gain_pmos: {AVout_pmos/AVip} V/V")
  print(f"tran Gain: {20 * np.log10(AVout/AVip)} dB, tran Gain_pmos: {20 * np.log10(AVout_pmos/AVip)} dB")

  #
  # Plot transient simulation data saved in .out file
  #

  fig, axs = plt.subplots(3, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)

  axs[0].plot(df["time"], df["v(vin)"], label=f"vin")
  axs[0].plot(df["time"], df["v(vip)"], label=f"vip")
  
  axs[1].plot(df["time"], df["v(vout)"], label=f"vout, nmos input\ngain: {AVout/AVip:.2f} V/V ({20 * np.log10(AVout/AVip):.2f} dB)")
  
  axs[2].plot(df["time"], df["v(vout_pmos)"], label=f"vout, pmos input\ngain: {AVout_pmos/AVip:.2f} V/V ({20 * np.log10(AVout_pmos/AVip):.2f} dB)")

  for ax in axs:
      ax.tick_params(axis="both", labelsize=ticks_fontsize)
      ax.legend(loc="best", fontsize=legend_fontsize)
      ax.grid()
  
  axs[0].set_title(f"{name}", fontsize=title_fontsize, fontweight="bold")
  axs[-1].set_xlabel("Time (us)", fontsize=label_fontsize)

  axs[0].set_ylabel("Voltage (V)", fontsize=label_fontsize)
  axs[1].set_ylabel("Voltage (V)", fontsize=label_fontsize)
  axs[2].set_ylabel("Voltage (V)", fontsize=label_fontsize)

  # axs[1].set_ylim(bottom=0 - (max(df["v(vout)"]) * 0.05))

  fig.tight_layout()
  fig.savefig(f"figures/{name.split('/')[-1]}.png", bbox_inches="tight", dpi=300)

  #
  # Parse AC simulation data saved in .out file
  #

  ac_outfile = name + "_ac.out"
  ac_df = pd.read_csv(ac_outfile, sep="\s+")

  ac_df["frequency"] = ac_df["frequency"] * 1e-3 # in kHz
  ac_df["gain"] = ac_df["vm(vout)"] / ac_df["vm(vip)"] # AC Gain ≈ V(out) / V(in)
  ac_df["gain_db"] = 20 * np.log10(ac_df["gain"])
  ac_df["gain_db_alt"] = ac_df["vdb(vout)"] - ac_df["vdb(vip)"]
  ac_df["gain_pmos"] = ac_df["vm(vout_pmos)"] / ac_df["vm(vip)"] # AC Gain ≈ V(out) / V(in)
  ac_df["gain_pmos_db"] = 20 * np.log10(ac_df["gain_pmos"])
  ac_df["gain_pmos_db_alt"] = ac_df["vdb(vout_pmos)"] - ac_df["vdb(vip)"]

  #
  # Plot AC simulation data saved in .out file
  #

  ac_fig, ac_axs = plt.subplots(5, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)

  ac_axs[0].plot(ac_df["frequency"], ac_df["vm(vout)"], label=f"vout")
  ac_axs[0].plot(ac_df["frequency"], ac_df["vm(vout_pmos)"], label=f"vout_pmos")
  ac_axs[0].plot(ac_df["frequency"], ac_df["vm(vip)"], label=f"vip")
  ac_axs[0].plot(ac_df["frequency"], ac_df["vm(vin)"], label=f"vin")
  
  ac_axs[1].plot(ac_df["frequency"], ac_df["gain"], label=f"gain")
  ac_axs[2].plot(ac_df["frequency"], ac_df["gain_db"], label=f"gain at 1Hz: {ac_df['gain_db'].iloc[0]:.2f} dB")

  ac_axs[3].plot(ac_df["frequency"], ac_df["gain_pmos"], label=f"pmos gain")
  ac_axs[4].plot(ac_df["frequency"], ac_df["gain_pmos_db"], label=f"pmos gain at 1Hz: {ac_df['gain_pmos_db'].iloc[0]:.2f} dB")

  for ax in ac_axs:
      ax.tick_params(axis="both", labelsize=ticks_fontsize)
      ax.legend(loc="best", fontsize=legend_fontsize)
      ax.grid()
      ax.set_xscale('log')
  
  ac_axs[0].set_title(f"{name}", fontsize=title_fontsize, fontweight="bold")
  ac_axs[-1].set_xlabel("Frequency (kHz)", fontsize=label_fontsize)

  ac_axs[0].set_ylabel("Voltage (V)", fontsize=label_fontsize)
  ac_axs[1].set_ylabel("Magnitude (dB)", fontsize=label_fontsize)
  ac_axs[2].set_ylabel("Gain (dB)", fontsize=label_fontsize)
  ac_axs[3].set_ylabel("Gain (V/V)", fontsize=label_fontsize)
  ac_axs[4].set_ylabel("Gain", fontsize=label_fontsize)
  
  ac_fig.tight_layout()
  ac_fig.savefig(f"figures/{name.split('/')[-1]}_ac.png", bbox_inches="tight", dpi=300)

  #
  # Plot figures
  #  

  plt.show()


