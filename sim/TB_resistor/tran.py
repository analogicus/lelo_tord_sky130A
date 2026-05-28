#!/usr/bin/env python3
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import numpy as np

from spicelib import RawRead
from plot_raw_file import plot_raw_file

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



  # df = pd.read_csv(name + ".out", sep="\s+")

  # df["time"] = df["time"] * 1e9 # in ns
  # df["i(vdd)"] = -df["i(vdd)"] * 1e6 # in uA
  # df["i(vss)"] = -df["i(vss)"] * 1e6 # in uA
  # df["res"] = df['v(vdd)'] / (df['i(vdd)'] * 1e-6) # in Ohm
 
  # # ideal_res = 8 * 7535 * 1e-3 # in kOhm
  # ideal_res = 7535 # in Ohm

  # # fig, axs = plt.subplots(3, 1, sharex=True, dpi=300, figsize=(3, 3))
  # # ax_i = axs[0]
  # # ax_v = axs[1]
  # # ax_r = axs[2]

  # fig = plt.figure(dpi=300)
  # ax_i = fig.add_subplot(3, 1, 1)
  # ax_v = fig.add_subplot(3, 1, 2)
  # ax_r = fig.add_subplot(3, 1, 3)

  # ax_i.plot(df["time"], df["i(vdd)"], label="i(vdd)")
  # ax_i.plot(df["time"], df["i(vss)"], label="i(vss)")

  # # ax_i.set_title("Currents")
  # ax_i.set_ylabel("Current (uA)")
  # ax_i.legend(loc="best")
  # ax_i.grid(True)
  # ax_i.set_ylim(bottom=0-df["i(vdd)"].min()*0.2, top=df["i(vdd)"].max()*1.2)
  
  # ax_v.plot(df["time"], df["v(vdd)"], label="v(vdd)")
  # ax_v.plot(df["time"], df["v(vss)"], label="v(vss)")

  # # ax_v.set_title("Voltages")
  # ax_v.set_ylabel("Voltage (V)")
  # ax_v.legend(loc="best")
  # ax_v.grid(True)
  # ax_v.set_ylim(bottom=0-df["v(vdd)"].min()*0.2, top=df["v(vdd)"].max()*1.2)

  # ax_r.plot(df["time"], df["res"] , label="resistance (V/I)")
  # ax_r.plot([df["time"].min(), df["time"].max()], [ideal_res, ideal_res], marker="none", linestyle="dashed", color="black", label="specified resistance in schematic")

  # # ax_r.set_title("Resistance")
  # ax_r.set_ylabel("Resistance (Ω)")
  # ax_r.set_xlabel("Time (ns)")
  # ax_r.legend(loc="best")
  # ax_r.grid(True)
  # ax_r.set_ylim(bottom=0-df["res"].min()*0.2, top=df["res"].max()*1.2)

  # fig.suptitle(name, fontweight='bold')
  # fig.tight_layout()

  # fig.savefig(name + ".png", dpi=300)

  # if name == "output_tran/tran_SchGtKttTtVt":
  #   plt.show()
  # else:
  #   plt.close()



  # rawfile = RawRead(name + ".raw")

  # tracenames = rawfile.get_trace_names()
  # # print(rawfile.get_raw_properties())

  # time = rawfile.get_axis() # Gets an array of the time vector for all other wave vectors to be plotted against
  # time = time * 1e9 # in ns

  # # ic0 = rawfile.get_trace("i(@c.xdut.xr1.xc0.c0[i])")
  # # ic1 = rawfile.get_trace("i(@c.xdut.xr1.xc0.c1[i])")
  # # irb = rawfile.get_trace("i(@r.xdut.xr1.rbody[i])")
  # # irh = rawfile.get_trace("i(@r.xdut.xr1.rhead[i])")
  # vdd = rawfile.get_trace("v(vdd)")
  # idd = rawfile.get_trace("i(vdd)")
  # # vss = rawfile.get_trace("v(vss)")
  # # iss = rawfile.get_trace("i(vss)")
  # # vrb = rawfile.get_trace("v(xdut.xr1.rb)")

  # steps = rawfile.get_steps() # Get list of step numbers ([0,1,2]) for sweeped simulations
  #                             # Returns [0] if there is just 1 step

  # fig_v = plt.figure(dpi=300, figsize=(3,3))
  # ax_v = fig_v.add_subplot(1,1,1)

  # fig_i = plt.figure(dpi=300, figsize=(3,3))
  # ax_i = fig_i.add_subplot(1,1,1)

  # fig_r = plt.figure(dpi=300, figsize=(3,3))
  # ax_r = fig_r.add_subplot(1,1,1)

  # for tracename in tracenames:
  #   print(f"trace: {tracename}")

  #   if tracename.startswith("v("):
  #     trace = rawfile.get_trace(tracename).get_wave()
      
  #     ax_v.plot(time, trace, label=tracename)

  #   if tracename.startswith("i("):
  #     trace = rawfile.get_trace(tracename).get_wave() 
  #     trace = -trace * 1e6 # in uA with a positive sign
      
  #     ax_i.plot(time, trace, label=tracename)

  # for step in steps:              # On the second plot, print all the STEPS of Vout
  #   t = rawfile.get_axis(step)    # Retrieve the time from the time vector at that step
  #   t = t * 1e9                   # in ns

  #   i = idd.get_wave(step)        # Retrieve the idd-value for this step
  #   i = -i                        # Flips the sign from negative to positiveS

  #   v = vdd.get_wave(step)        # Retrieve the iss-value for this step
    
  #   r = v / i

  #   ax_r.plot(t, r, label="R=V/I")  # Do X/Y plot on second subplot

  # ax_name = name.split("/")[-1]
  
  # # fig_v.suptitle(f"Voltages, {ax_name}")
  # ax_v.set_title(f"{ax_name}", fontsize=10, fontweight="bold")
  # ax_v.grid()
  # ax_v.legend(loc="best", fontsize=9)
  # ax_v.set_xlabel(f"Time (ns)")
  # ax_v.set_ylabel(f"Voltage (V)")

  # ax_i.set_title(f"{ax_name}", fontsize=10, fontweight="bold")
  # ax_i.grid()
  # ax_i.legend(loc="best", fontsize=9)
  # ax_i.set_xlabel(f"Time (ns)")
  # ax_i.set_ylabel(f"Current (uA)")

  # ax_r.set_title(f"{ax_name}", fontsize=10, fontweight="bold")
  # ax_r.grid()
  # ax_r.legend(loc="best", fontsize=9)
  # ax_r.set_xlabel(f"Time (ns)")
  # ax_r.set_ylabel(f"Resistance (Ω)")

  # fig_v.tight_layout()
  # fig_v.savefig(f"{name}_v.png")
  
  # fig_i.tight_layout()
  # fig_i.savefig(f"{name}_i.png")
  
  # fig_r.tight_layout()
  # fig_r.savefig(f"{name}_r.png")

  # if name == "output_tran/tran_SchGtKttTtVt":
  #   plt.show()
  # else:
  #   plt.close()



  fig_v, fig_i, fig_r = plot_raw_file(name)

  fig_v.tight_layout()
  fig_v.savefig(f"{name}_v.png")

  fig_i.tight_layout()
  fig_i.savefig(f"{name}_i.png")

  fig_r.tight_layout()
  fig_r.savefig(f"{name}_r.png")

  # if name == "output_tran/tran_SchGtKttTtVt":
  #   plt.show()
  # else:
  #   plt.close()

  plt.close("all")

