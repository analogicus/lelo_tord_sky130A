#!/usr/bin/env python3
import yaml
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig_width = 8
fig_height = 5
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
  
  AVip = max(df["v(vip)"]) - min(df["v(vip)"])
  AVout_nmos = max(df["v(vo_nmos)"]) - min(df["v(vo_nmos)"])
  AVout_pmos = max(df["v(vo_pmos)"]) - min(df["v(vo_pmos)"])
  AVout_nch_lvt = max(df["v(vo_nch_lvt)"]) - min(df["v(vo_nch_lvt)"])
  AVout_pch_lvt = max(df["v(vo_pch_lvt)"]) - min(df["v(vo_pch_lvt)"])
  AVout_nch_crs = max(df["v(vo_nch_crs)"]) - min(df["v(vo_nch_crs)"])
  AVout_pch_crs = max(df["v(vo_pch_crs)"]) - min(df["v(vo_pch_crs)"])
  AVout_nch_lvt_crs = max(df["v(vo_nch_lvt_crs)"]) - min(df["v(vo_nch_lvt_crs)"])
  AVout_pch_lvt_crs = max(df["v(vo_pch_lvt_crs)"]) - min(df["v(vo_pch_lvt_crs)"])

  Vout_nmos_gain = AVout_nmos / AVip
  Vout_pmos_gain = AVout_pmos / AVip
  Vout_nch_lvt_gain = AVout_nch_lvt / AVip
  Vout_pch_lvt_gain = AVout_pch_lvt / AVip
  Vout_nch_crs_gain = AVout_nch_crs / AVip
  Vout_pch_crs_gain = AVout_pch_crs / AVip
  Vout_nch_lvt_crs_gain = AVout_nch_lvt_crs / AVip
  Vout_pch_lvt_crs_gain = AVout_pch_lvt_crs / AVip

  Vout_nmos_gain_db = 20 * np.log10(Vout_nmos_gain)
  Vout_pmos_gain_db = 20 * np.log10(Vout_pmos_gain)
  Vout_nch_lvt_gain_db = 20 * np.log10(Vout_nch_lvt_gain)
  Vout_pch_lvt_gain_db = 20 * np.log10(Vout_pch_lvt_gain)
  Vout_nch_crs_gain_db = 20 * np.log10(Vout_nch_crs_gain)
  Vout_pch_crs_gain_db = 20 * np.log10(Vout_pch_crs_gain)
  Vout_nch_lvt_crs_gain_db = 20 * np.log10(Vout_nch_lvt_crs_gain)
  Vout_pch_lvt_crs_gain_db = 20 * np.log10(Vout_pch_lvt_crs_gain)

  print(f"AVip: {AVip*1e3:.2f} mV, AVout_nmos: {AVout_nmos*1e3:.2f} mV, Vout_nmos_gain: {Vout_nmos_gain:.2f} V/V, Vout_nmos_gain_db: {Vout_nmos_gain_db:.2f} dB")
  print(f"AVip: {AVip*1e3:.2f} mV, AVout_pmos: {AVout_pmos*1e3:.2f} mV, Vout_pmos_gain: {Vout_pmos_gain:.2f} V/V, Vout_pmos_gain_db: {Vout_pmos_gain_db:.2f} dB")
  print(f"AVip: {AVip*1e3:.2f} mV, AVout_nch_lvt: {AVout_nch_lvt*1e3:.2f} mV, Vout_nch_lvt_gain: {Vout_nch_lvt_gain:.2f} V/V, Vout_nch_lvt_gain_db: {Vout_nch_lvt_gain_db:.2f} dB")
  print(f"AVip: {AVip*1e3:.2f} mV, AVout_pch_lvt: {AVout_pch_lvt*1e3:.2f} mV, Vout_pch_lvt_gain: {Vout_pch_lvt_gain:.2f} V/V, Vout_pch_lvt_gain_db: {Vout_pch_lvt_gain_db:.2f} dB")
  print(f"AVip: {AVip*1e3:.2f} mV, AVout_nch_crs: {AVout_nch_crs*1e3:.2f} mV, Vout_nch_crs_gain: {Vout_nch_crs_gain:.2f} V/V, Vout_nch_crs_gain_db: {Vout_nch_crs_gain_db:.2f} dB")
  print(f"AVip: {AVip*1e3:.2f} mV, AVout_pch_crs: {AVout_pch_crs*1e3:.2f} mV, Vout_pch_crs_gain: {Vout_pch_crs_gain:.2f} V/V, Vout_pch_crs_gain_db: {Vout_pch_crs_gain_db:.2f} dB")
  print(f"AVip: {AVip*1e3:.2f} mV, AVout_nch_lvt_crs: {AVout_nch_lvt_crs*1e3:.2f} mV, Vout_nch_lvt_crs_gain: {Vout_nch_lvt_crs_gain:.2f} V/V, Vout_nch_lvt_crs_gain_db: {Vout_nch_lvt_crs_gain_db:.2f} dB")
  print(f"AVip: {AVip*1e3:.2f} mV, AVout_pch_lvt_crs: {AVout_pch_lvt_crs*1e3:.2f} mV, Vout_pch_lvt_crs_gain: {Vout_pch_lvt_crs_gain:.2f} V/V, Vout_pch_lvt_crs_gain_db: {Vout_pch_lvt_crs_gain_db:.2f} dB")

  #
  # Plot transient simulation data saved in .out file
  #

  fig, axs = plt.subplot_mosaic([["vin_vip", "nmos", "nch_crs"], ["vin_vip", "pmos", "pch_crs"]], figsize=(fig_width, fig_height), dpi=300) # , sharex=True)

  axs["vin_vip"].plot(df["time"], df["v(vin)"], label=f"vin")
  axs["vin_vip"].plot(df["time"], df["v(vip)"], label=f"vip")
  
  axs["nmos"].plot(df["time"], df["v(vo_nmos)"], label=f"vout, nmos input\ngain: {Vout_nmos_gain:.2f} V/V ({Vout_nmos_gain_db:.2f} dB)")
  axs["pmos"].plot(df["time"], df["v(vo_pmos)"], label=f"vout, pmos input\ngain: {Vout_pmos_gain:.2f} V/V ({Vout_pmos_gain_db:.2f} dB)")
  axs["nmos"].plot(df["time"], df["v(vo_nch_lvt)"], label=f"vout, nch_lvt input\ngain: {Vout_nch_lvt_gain:.2f} V/V ({Vout_nch_lvt_gain_db:.2f} dB)")
  axs["pmos"].plot(df["time"], df["v(vo_pch_lvt)"], label=f"vout, pch_lvt input\ngain: {Vout_pch_lvt_gain:.2f} V/V ({Vout_pch_lvt_gain_db:.2f} dB)")
  axs["nch_crs"].plot(df["time"], df["v(vo_nch_crs)"], label=f"vout, nch_crs input\ngain: {Vout_nch_crs_gain:.2f} V/V ({Vout_nch_crs_gain_db:.2f} dB)")
  axs["pch_crs"].plot(df["time"], df["v(vo_pch_crs)"], label=f"vout, pch_crs input\ngain: {Vout_pch_crs_gain:.2f} V/V ({Vout_pch_crs_gain_db:.2f} dB)")
  axs["nch_crs"].plot(df["time"], df["v(vo_nch_lvt_crs)"], label=f"vout, nch_lvt_crs input\ngain: {Vout_nch_lvt_crs_gain:.2f} V/V ({Vout_nch_lvt_crs_gain_db:.2f} dB)")
  axs["pch_crs"].plot(df["time"], df["v(vo_pch_lvt_crs)"], label=f"vout, pch_lvt_crs input\ngain: {Vout_pch_lvt_crs_gain:.2f} V/V ({Vout_pch_lvt_crs_gain_db:.2f} dB)")

  for ax in axs.values():
    ax.tick_params(axis="both", labelsize=ticks_fontsize)
    ax.legend(loc="best", fontsize=legend_fontsize)
    ax.grid()
  
  axs["vin_vip"].set_title(f"Transients: {name.split('_')[-1]}", fontsize=title_fontsize, fontweight="bold")
  axs["pch_crs"].set_xlabel("Time (us)", fontsize=label_fontsize)

  axs["vin_vip"].set_ylabel("Voltage (V)", fontsize=label_fontsize)
  axs["nmos"].set_ylabel("Voltage (V)", fontsize=label_fontsize)
  axs["pmos"].set_ylabel("Voltage (V)", fontsize=label_fontsize)
  axs["nch_crs"].set_ylabel("Voltage (V)", fontsize=label_fontsize)
  axs["pch_crs"].set_ylabel("Voltage (V)", fontsize=label_fontsize)

  # axs[1].set_ylim(bottom=0 - (max(df["v(vout)"]) * 0.05))

  fig.tight_layout()
  fig.savefig(f"figures/{name.split('/')[-1]}.png", bbox_inches="tight", dpi=300)

  #
  # Parse AC simulation data saved in .out file 
  #

  ac_outfile = name + "_ac.out"
  ac_df = pd.read_csv(ac_outfile, sep="\s+")

  ac_df["frequency"] = ac_df["frequency"] * 1e-3 # in kHz'

  ac_df["gain_nmos_vv"] = ac_df["vm(vo_nmos)"] / ac_df["vm(vip)"] # AC Gain ≈ V(out) / V(in)
  ac_df["gain_nmos_db"] = 20 * np.log10(ac_df["gain_nmos_vv"])
  # ac_df["gain_nmos_db_alt"] = ac_df["vdb(vo_nmos)"] - ac_df["vdb(vip)"] # Alternative way to calculate gain in dB

  ac_df["gain_pmos_vv"] = ac_df["vm(vo_pmos)"] / ac_df["vm(vip)"]
  ac_df["gain_pmos_db"] = 20 * np.log10(ac_df["gain_pmos_vv"])

  ac_df["gain_nch_lvt_vv"] = ac_df["vm(vo_nch_lvt)"] / ac_df["vm(vip)"]
  ac_df["gain_nch_lvt_db"] = 20 * np.log10(ac_df["gain_nch_lvt_vv"])

  ac_df["gain_pch_lvt_vv"] = ac_df["vm(vo_pch_lvt)"] / ac_df["vm(vip)"]
  ac_df["gain_pch_lvt_db"] = 20 * np.log10(ac_df["gain_pch_lvt_vv"])

  ac_df["gain_nch_crs_vv"] = ac_df["vm(vo_nch_crs)"] / ac_df["vm(vip)"]
  ac_df["gain_nch_crs_db"] = 20 * np.log10(ac_df["gain_nch_crs_vv"])

  ac_df["gain_pch_crs_vv"] = ac_df["vm(vo_pch_crs)"] / ac_df["vm(vip)"]
  ac_df["gain_pch_crs_db"] = 20 * np.log10(ac_df["gain_pch_crs_vv"])

  ac_df["gain_nch_lvt_crs_vv"] = ac_df["vm(vo_nch_lvt_crs)"] / ac_df["vm(vip)"]
  ac_df["gain_nch_lvt_crs_db"] = 20 * np.log10(ac_df["gain_nch_lvt_crs_vv"])

  ac_df["gain_pch_lvt_crs_vv"] = ac_df["vm(vo_pch_lvt_crs)"] / ac_df["vm(vip)"]
  ac_df["gain_pch_lvt_crs_db"] = 20 * np.log10(ac_df["gain_pch_lvt_crs_vv"])

  #
  # Plot AC simulation data saved in .out file
  #

  # ac_fig, ac_axs = plt.subplots(2, 1, figsize=(fig_width, fig_height), sharex=True, dpi=300)
  ac_fig, ac_axs = plt.subplot_mosaic([['gain_vv'], ['gain_db']], figsize=(fig_width, fig_height), dpi=300) # , sharex=True)
  
  ac_axs['gain_vv'].plot(ac_df["frequency"], ac_df["gain_nmos_vv"], label=f"gain at 1Hz (two staged NMOS input pair): {ac_df['gain_nmos_vv'].iloc[0]:.2f} V/V")
  ac_axs['gain_vv'].plot(ac_df["frequency"], ac_df["gain_pmos_vv"], label=f"gain at 1Hz (two staged PMOS input pair): {ac_df['gain_pmos_vv'].iloc[0]:.2f} V/V")
  ac_axs['gain_vv'].plot(ac_df["frequency"], ac_df["gain_nch_lvt_vv"], label=f"gain at 1Hz (two staged NMOS LVT input pair): {ac_df['gain_nch_lvt_vv'].iloc[0]:.2f} V/V")
  ac_axs['gain_vv'].plot(ac_df["frequency"], ac_df["gain_pch_lvt_vv"], label=f"gain at 1Hz (two staged PMOS LVT input pair): {ac_df['gain_pch_lvt_vv'].iloc[0]:.2f} V/V")
  ac_axs['gain_vv'].plot(ac_df["frequency"], ac_df["gain_nch_crs_vv"], label=f"gain at 1Hz (cross coupled and two staged NMOS input pair): {ac_df['gain_nch_crs_vv'].iloc[0]:.2f} V/V")
  ac_axs['gain_vv'].plot(ac_df["frequency"], ac_df["gain_pch_crs_vv"], label=f"gain at 1Hz (cross coupled and two staged PMOS input pair): {ac_df['gain_pch_crs_vv'].iloc[0]:.2f} V/V")
  ac_axs['gain_vv'].plot(ac_df["frequency"], ac_df["gain_nch_lvt_crs_vv"], label=f"gain at 1Hz (cross coupled and two staged NMOS LVT input pair): {ac_df['gain_nch_lvt_crs_vv'].iloc[0]:.2f} V/V")
  ac_axs['gain_vv'].plot(ac_df["frequency"], ac_df["gain_pch_lvt_crs_vv"], label=f"gain at 1Hz (cross coupled and two staged PMOS LVT input pair): {ac_df['gain_pch_lvt_crs_vv'].iloc[0]:.2f} V/V")

  ac_axs['gain_db'].plot(ac_df["frequency"], ac_df["gain_nmos_db"], label=f"gain at 1Hz (two staged NMOS input pair): {ac_df['gain_nmos_db'].iloc[0]:.2f} dB")
  ac_axs['gain_db'].plot(ac_df["frequency"], ac_df["gain_pmos_db"], label=f"gain at 1Hz (two staged PMOS input pair): {ac_df['gain_pmos_db'].iloc[0]:.2f} dB")
  ac_axs['gain_db'].plot(ac_df["frequency"], ac_df["gain_nch_lvt_db"], label=f"gain at 1Hz (two staged NMOS LVT input pair): {ac_df['gain_nch_lvt_db'].iloc[0]:.2f} dB")
  ac_axs['gain_db'].plot(ac_df["frequency"], ac_df["gain_pch_lvt_db"], label=f"gain at 1Hz (two staged PMOS LVT input pair): {ac_df['gain_pch_lvt_db'].iloc[0]:.2f} dB")
  ac_axs['gain_db'].plot(ac_df["frequency"], ac_df["gain_nch_crs_db"], label=f"gain at 1Hz (cross coupled and two staged NMOS input pair): {ac_df['gain_nch_crs_db'].iloc[0]:.2f} dB")
  ac_axs['gain_db'].plot(ac_df["frequency"], ac_df["gain_pch_crs_db"], label=f"gain at 1Hz (cross coupled and two staged PMOS input pair): {ac_df['gain_pch_crs_db'].iloc[0]:.2f} dB")
  ac_axs['gain_db'].plot(ac_df["frequency"], ac_df["gain_nch_lvt_crs_db"], label=f"gain at 1Hz (cross coupled and two staged NMOS LVT input pair): {ac_df['gain_nch_lvt_crs_db'].iloc[0]:.2f} dB")
  ac_axs['gain_db'].plot(ac_df["frequency"], ac_df["gain_pch_lvt_crs_db"], label=f"gain at 1Hz (cross coupled and two staged PMOS LVT input pair): {ac_df['gain_pch_lvt_crs_db'].iloc[0]:.2f} dB")

  for ax in ac_axs.values():
    ax.tick_params(axis="both", labelsize=ticks_fontsize)
    ax.legend(loc="best", fontsize=legend_fontsize)
    ax.grid()
    ax.set_xscale('log')
  
  ac_axs['gain_vv'].set_title(f"AC: {name.split('_')[-1]}", fontsize=title_fontsize, fontweight="bold")
  ac_axs['gain_vv'].set_ylabel("Gain (V/V)", fontsize=label_fontsize)
  ac_axs['gain_db'].set_ylabel("Gain (dB)", fontsize=label_fontsize)
  ac_axs['gain_db'].set_xlabel("Frequency (kHz)", fontsize=label_fontsize)
  
  ac_fig.tight_layout()
  ac_fig.savefig(f"figures/ac_{name.split('/')[-1].split('_')[-1]}.png", bbox_inches="tight", dpi=300)

  #
  # Plot figures
  #  

  plt.show()


