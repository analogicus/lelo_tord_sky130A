#!/usr/bin/env python3
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import numpy as np

def main(name):
  # # Delete next line if you want to use python post processing
  # # return
  # yamlfile = name + ".yaml"

  # # Read result yaml file
  # with open(yamlfile) as fi:
  #   obj = yaml.safe_load(fi)

  # # Do something to parameters

  # # Save new yaml file
  # with open(yamlfile,"w") as fo:
  #   yaml.dump(obj,fo)

  df = pd.read_csv(name + ".out", sep="\s+")

  df["time"] = df["time"] * 1e9 # in ns
  df["i(vdd)"] = -df["i(vdd)"] * 1e6 # in uA
  df["i(vss)"] = -df["i(vss)"] * 1e6 # in uA
  df["res"] = df['v(vdd)'] / (df['i(vdd)'] * 1e-6) # in Ohm
 
  # ideal_res = 8 * 7535 * 1e-3 # in kOhm
  ideal_res = 7535 # in Ohm

  # fig, axs = plt.subplots(3, 1, sharex=True, dpi=300, figsize=(3, 3))
  # ax_i = axs[0]
  # ax_v = axs[1]
  # ax_r = axs[2]

  fig = plt.figure(dpi=300)
  ax_i = fig.add_subplot(3, 1, 1)
  ax_v = fig.add_subplot(3, 1, 2)
  ax_r = fig.add_subplot(3, 1, 3)

  ax_i.plot(df["time"], df["i(vdd)"], label="i(vdd)")
  ax_i.plot(df["time"], df["i(vss)"], label="i(vss)")

  # ax_i.set_title("Currents")
  ax_i.set_ylabel("Current (uA)")
  ax_i.legend(loc="best")
  ax_i.grid(True)
  ax_i.set_ylim(bottom=0-df["i(vdd)"].min()*0.2, top=df["i(vdd)"].max()*1.2)
  
  ax_v.plot(df["time"], df["v(vdd)"], label="v(vdd)")
  ax_v.plot(df["time"], df["v(vss)"], label="v(vss)")

  # ax_v.set_title("Voltages")
  ax_v.set_ylabel("Voltage (V)")
  ax_v.legend(loc="best")
  ax_v.grid(True)
  ax_v.set_ylim(bottom=0-df["v(vdd)"].min()*0.2, top=df["v(vdd)"].max()*1.2)

  ax_r.plot(df["time"], df["res"] , label="resistance (V/I)")
  ax_r.plot([df["time"].min(), df["time"].max()], [ideal_res, ideal_res], marker="none", linestyle="dashed", color="black", label="specified resistance in schematic")

  # ax_r.set_title("Resistance")
  ax_r.set_ylabel("Resistance (Ω)")
  ax_r.set_xlabel("Time (ns)")
  ax_r.legend(loc="best")
  ax_r.grid(True)
  ax_r.set_ylim(bottom=0-df["res"].min()*0.2, top=df["res"].max()*1.2)

  fig.suptitle(name, fontweight='bold')
  fig.tight_layout()

  fig.savefig(name + ".png", dpi=300)

  if name == "output_tran/tran_SchGtKttTtVt":
    plt.show()
  else:
    plt.close()