#!/usr/bin/env python3
import pandas as pd
import yaml
import sys
import matplotlib.pyplot as plt

fig_width = 3
fig_height = 3
font_size = 12
title_fontsize = font_size
label_fontsize = font_size
legend_fontsize = font_size
ticks_fontsize = font_size

def main(name):
  # # Delete next line if you want to use python post processing
  # return


  # folder = name.split("/")[0]
  filename = name.split("/")[-1]

  # yamlfile = name + ".yaml"

  # # Read results from yaml file
  # with open(yamlfile) as fi:
  #   obj = yaml.safe_load(fi)

  # # Do something to parameters
  # print(obj)

  # # Save results to new yaml file
  # with open(yamlfile,"w") as fo:
  #   yaml.dump(obj,fo)


  outfile = name + ".out"

  # Read results from out file
  df = pd.read_csv(outfile, sep="\s+")

  # Do something to parameters
  df["id1"] = df["i(v.xdut.v1)"] # Current in Ampere (A)
  df["id2"] = df["i(v.xdut.v2)"]
  df["id3"] = df["i(v.xdut.v3)"]
  df["id4"] = df["i(v.xdut.v4)"]
  df["id5"] = df["i(v.xdut.v5)"]

  df["vsg"] = df["v(vs)"] - df["v(vg)"] # Voltage in Volt (V)
  df["vsd"] = df["v(vs)"] - df["v(vd)"] # Voltage in Volt (V)

  df["gm1"] = df["id1"].diff() / df["vsg"].diff() # transconductance (gm = dId1/dVsg) in Ampere per Volt (A/V)
  df["gm2"] = df["id2"].diff() / df["vsg"].diff()
  df["gm3"] = df["id3"].diff() / df["vsg"].diff()
  df["gm4"] = df["id4"].diff() / df["vsg"].diff()
  df["gm5"] = df["id5"].diff() / df["vsg"].diff()

  df["r1"] = 1 / df["gm1"] # Resistance in Ohm (Ω)
  df["r2"] = 1 / df["gm2"]
  df["r3"] = 1 / df["gm3"]
  df["r4"] = 1 / df["gm4"]
  df["r5"] = 1 / df["gm5"]

  C = 53.8*10**(-15) # Capacitance in Farad (F)
  Ctot = C * 4 * 25  # Total capacitance

  df["tau1"] = df["r1"] * Ctot # Time constant in seconds (s)
  df["tau2"] = df["r2"] * Ctot
  df["tau3"] = df["r3"] * Ctot
  df["tau4"] = df["r4"] * Ctot
  df["tau5"] = df["r5"] * Ctot

  df.to_csv(f"{name}.csv", index=False, sep=",")

  # These values were found by running find_control_voltages.py script in TB_temp_sens folder
  highest_vctl = 1.17
  lowest_vctl = 0.43
  print(f"gm values given that 0.043 < Vsg < 1.15:\n{df[['vsg','gm1','gm2','gm3','gm4','gm5']][(df['vsg'] < highest_vctl) & (df['vsg'] > lowest_vctl)]}")

  vsg_line = highest_vctl

  p1, w1, l1 = "PCH 3W2 0L94", 3.2, 0.94
  p2, w2, l2 = "PCH 5W76 0L94", 5.76, 0.94
  p3, w3, l3 = "PCH 8W32 0L94", 8.32, 0.94
  p4, w4, l4 = "PCH 2W4 0L94", 2.4, 0.94
  p5, w5, l5 = "PCH 1W2 0L94", 1.2, 0.94
  
  gm1 = df.loc[df['v-sweep'] == vsg_line, 'gm1'].item()
  r1 = 1/gm1 # uΩ
  tau1 = r1*Ctot # us

  gm2 = df.loc[df['v-sweep'] == vsg_line, 'gm2'].item()
  r2 = 1/gm2
  tau2 = r2*Ctot

  gm3 = df.loc[df['v-sweep'] == vsg_line, 'gm3'].item()
  r3 = 1/gm3
  tau3 = r3*Ctot

  gm4 = df.loc[df['v-sweep'] == vsg_line, 'gm4'].item()
  r4 = 1/gm4
  tau4 = r4*Ctot

  gm5 = df.loc[df['v-sweep'] == vsg_line, 'gm5'].item()
  r5 = 1/gm5
  tau5 = r5*Ctot

  print(f"{p1}, type: PMOS, width, {w1} um, length: {l1} um, gm at {vsg_line} V: {gm1:.5e} A/V, resistance at {vsg_line} V: {r1:.5e} Ω, time constant at {vsg_line} V: {tau1:.9e} s")
  print(f"{p2}, type: PMOS, width, {w2} um, length: {l2} um, gm at {vsg_line} V: {gm2:.5e} A/V, resistance at {vsg_line} V: {r2:.5e} Ω, time constant at {vsg_line} V: {tau2:.9e} s")
  print(f"{p3}, type: PMOS, width, {w3} um, length: {l3} um, gm at {vsg_line} V: {gm3:.5e} A/V, resistance at {vsg_line} V: {r3:.5e} Ω, time constant at {vsg_line} V: {tau3:.9e} s")
  print(f"{p4}, type: PMOS, width, {w4} um, length: {l4} um, gm at {vsg_line} V: {gm4:.5e} A/V, resistance at {vsg_line} V: {r4:.5e} Ω, time constant at {vsg_line} V: {tau4:.9e} s")
  print(f"{p5}, type: PMOS, width, {w5} um, length: {l5} um, gm at {vsg_line} V: {gm5:.5e} A/V, resistance at {vsg_line} V: {r5:.5e} Ω, time constant at {vsg_line} V: {tau5:.9e} s")


  start_idx = 81


  # Plot results
  fig_id, ax_id = plt.subplots(1, 1, figsize=(fig_width, fig_height), dpi=300)

  ax_id.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "id5"]*1e6, label=f"{p5}")
  ax_id.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "id4"]*1e6, label=f"{p4}")
  ax_id.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "id1"]*1e6, label=f"{p1}")
  ax_id.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "id2"]*1e6, label=f"{p2}")
  ax_id.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "id3"]*1e6, label=f"{p3}")

  # ax_id.set_title("PMOS Transistor drain current (Id)")
  ax_id.set_ylabel("Id (uA)", fontsize=label_fontsize)
  ax_id.set_xlabel("Vsg (V)", fontsize=label_fontsize)
  ax_id.tick_params(axis="both", which="major", labelsize=ticks_fontsize)
  ax_id.legend()
  ax_id.grid()

  fig_id.tight_layout()
  fig_id.savefig(f"figures/{filename}_id.png", dpi=300, bbox_inches="tight")



  fig_gm, ax_gm = plt.subplots(1, 1, figsize=(fig_width, fig_height), dpi=300)  

  ax_gm.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "gm5"]*1e6, label=f"{p5}")
  ax_gm.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "gm4"]*1e6, label=f"{p4}")
  ax_gm.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "gm1"]*1e6, label=f"{p1}")
  ax_gm.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "gm2"]*1e6, label=f"{p2}")
  ax_gm.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "gm3"]*1e6, label=f"{p3}")

  ax_gm.axvline(vsg_line, color="gray", linestyle="dashed")
  ax_gm.plot(vsg_line, gm5*1e6, linestyle="dashed", marker="o", color="gray", label=f"{gm5*1e6:.2f} uA/V")

  # ax_gm.set_title("PMOS Transistor transconductanse (gm)")
  ax_gm.set_xlabel("Vsg (V)", fontsize=label_fontsize)
  ax_gm.set_ylabel("gm (uA/V)", fontsize=label_fontsize)
  ax_gm.tick_params(axis="both", which="major", labelsize=ticks_fontsize)
  ax_gm.legend()
  ax_gm.grid()

  fig_gm.tight_layout()
  fig_gm.savefig(f"figures/{filename}_gm.png", dpi=300, bbox_inches="tight")  



  fig_r, ax_r = plt.subplots(1, 1, figsize=(fig_width, fig_height), dpi=300)  

  ax_r.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "r5"], label=f"{p5}")
  ax_r.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "r4"], label=f"{p4}")
  ax_r.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "r1"], label=f"{p1}")
  ax_r.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "r2"], label=f"{p2}")
  ax_r.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "r3"], label=f"{p3}")

  ax_r.axvline(vsg_line, color="gray", linestyle="dashed")
  ax_r.plot(vsg_line, r5, linestyle="dashed", marker="o", color="gray", label=f"{r5:.0f} Ω")

  # ax_gm.set_title("PMOS Transistor internal resistance (Ω)")
  ax_r.set_yscale('log')
  ax_r.set_xlabel("Vsg (V)", fontsize=label_fontsize)
  ax_r.set_ylabel("Resistance (Ω)", fontsize=label_fontsize)
  ax_r.tick_params(axis="both", which="major", labelsize=ticks_fontsize)
  ax_r.legend()
  ax_r.grid()

  fig_r.tight_layout()
  fig_r.savefig(f"figures/{filename}_r.png", dpi=300, bbox_inches="tight")  



  fig_tau, ax_tau = plt.subplots(1, 1, figsize=(fig_width, fig_height), dpi=300)  

  ax_tau.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "tau5"]*1e6, label=f"{p5}")
  ax_tau.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "tau4"]*1e6, label=f"{p4}")
  ax_tau.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "tau1"]*1e6, label=f"{p1}")
  ax_tau.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "tau2"]*1e6, label=f"{p2}")
  ax_tau.plot(df.loc[start_idx:, "vsg"], df.loc[start_idx:, "tau3"]*1e6, label=f"{p3}")

  ax_tau.axvline(vsg_line, color="gray", linestyle="dashed")
  ax_tau.plot(vsg_line, tau5*1e6, linestyle="dashed", marker="o", color="gray", label=f"{tau5*1e6:.5f} us")

  # ax_gm.set_title("PMOS Transistor internal resistance (Ω)")
  ax_tau.set_yscale('log')
  ax_tau.set_xlabel("Vsg (V)", fontsize=label_fontsize)
  ax_tau.set_ylabel("Time constant (us)", fontsize=label_fontsize)
  ax_tau.tick_params(axis="both", which="major", labelsize=ticks_fontsize)
  ax_tau.legend()
  ax_tau.grid()

  fig_tau.tight_layout()
  fig_tau.savefig(f"figures/{filename}_tau.png", dpi=300, bbox_inches="tight")  


  plt.close("all")
  # plt.show()



if __name__ == "__main__":
  main(sys.argv[1])