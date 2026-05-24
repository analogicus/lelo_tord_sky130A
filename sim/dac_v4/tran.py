#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml

from spicelib import RawRead

def main(name):
  # # Delete next line if you want to use python post processing
  # return


  #
  # Plot .yaml files
  #

  # yamlfile = name + ".yaml"

  # # Read result yaml file
  # with open(yamlfile) as fi:
  #   obj = yaml.safe_load(fi)

  # # Do something to parameters

  # # Save new yaml file
  # with open(yamlfile,"w") as fo:
  #   yaml.dump(obj,fo)


  #
  # Plot .raw files
  #

  # rawfile = name + ".raw"
  # raw = RawRead(rawfile)

  # time = raw.get_axis() * 1e9 # in ns
  # idd = -(raw.get_trace("i(vdd)").get_wave() * 1e6) # in uA with positive sign
  # irfeed = raw.get_trace("i(@rfeed[i])").get_wave()
  # irfeed = irfeed * 1e6 # in uA


  #
  # Plot .out files
  #

  outfile = name + ".out"
  df = pd.read_csv(outfile, sep='\s+')

  df['time'] = df['time'] * 1e9 # in ns

  # print(df.columns)
  # print(df.head())

  fig_in = plt.figure(dpi=300)
  ax_in = fig_in.add_subplot(1,1,1)
  ax_in.set_title(f"{name} inputs")

  ax_in.plot(df["time"], df["v(b0)"], label=f"v(b0) = {df['v(b0)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b1)"], label=f"v(b1) = {df['v(b1)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b2)"], label=f"v(b2) = {df['v(b2)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b3)"], label=f"v(b3) = {df['v(b3)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b4)"], label=f"v(b4) = {df['v(b4)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b5)"], label=f"v(b5) = {df['v(b5)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b6)"], label=f"v(b6) = {df['v(b6)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b7)"], label=f"v(b7) = {df['v(b7)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b8)"], label=f"v(b8) = {df['v(b8)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b9)"], label=f"v(b9) = {df['v(b9)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b10)"], label=f"v(b10) = {df['v(b10)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b11)"], label=f"v(b11) = {df['v(b11)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b12)"], label=f"v(b12) = {df['v(b12)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b13)"], label=f"v(b13) = {df['v(b13)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b14)"], label=f"v(b14) = {df['v(b14)'].iloc[-1]:.2f} V")
  ax_in.plot(df["time"], df["v(b15)"], label=f"v(b15) = {df['v(b15)'].iloc[-1]:.2f} V")

  ax_in.set_xlabel("Time (ns)")
  ax_in.set_ylabel("Voltage (V)")
  ax_in.legend()
  ax_in.grid()
  fig_in.savefig(name + "_inputs.png")

  fig_out = plt.figure(dpi=300)
  ax_out_v = fig_out.add_subplot(1,1,1)
  ax_out_v.set_title(f"{name} outputs")
  ax_out_i = ax_out_v.twinx()

  ax_out_v.plot(df["time"], df["v(ifeed)"], label=f"v(ifeed) = {df['v(ifeed)'].iloc[-1]:.2f} V", color="steelblue")
  ax_out_v.plot(df["time"], df["v(vdd)"], label=f"v(vdd) = {df['v(vdd)'].iloc[-1]:.2f} V", color="darkorange")
  ax_out_v.plot(df["time"], df["v(vss)"], label=f"v(vss) = {df['v(vss)'].iloc[-1]:.2f} V", color="forestgreen")

  ax_out_i.plot(df["time"], df["i(vfeed)"]*1e6, label=f"i(vfeed) = {df['i(vfeed)'].iloc[-1]*1e6:.2f} uA", color="firebrick")

  ax_out_v.set_xlabel("Time (ns)")
  ax_out_v.set_ylabel("Voltage (V)")

  ax_out_i.set_ylabel("Current (uA)")
  ax_out_i.set_ylim(bottom=-df['i(vfeed)'].iloc[-1]*1e6*0.1, top=df['i(vfeed)'].iloc[-1]*1e6*1.1)

  lines1, labels1 = ax_out_v.get_legend_handles_labels()
  lines2, labels2 = ax_out_i.get_legend_handles_labels()
  ax_out_i.legend(lines1 + lines2, labels1 + labels2, loc="best")

  ax_out_v.grid()
  fig_out.savefig(name + "_outputs.png")

  if name == "output_tran/tran_SchGtKttTtVt":
    plt.show()
  else:
    plt.close()  
