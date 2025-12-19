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


  folder = name.split("/")[0]
  filename = name.split("/")[-1]


  # yamlfile = filepath + ".yaml"

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
  df["id1"] = df["i(v.xdut.v1)"]*1e6 # convert from A to uA
  df["id2"] = df["i(v.xdut.v2)"]*1e6 # convert from A to uA
  df["id3"] = df["i(v.xdut.v3)"]*1e6 # convert from A to uA
  df["id4"] = df["i(v.xdut.v4)"]*1e6 # convert from A to uA

  df["vsg"] = df["v(vs)"] - df["v(vg)"]
  df["vsd"] = df["v(vs)"] - df["v(vd)"]

  df["gm1"] = df["id1"].diff() / df["vsg"].diff() # gm1 = dId1/dVsg
  df["gm2"] = df["id2"].diff() / df["vsg"].diff() # gm2 = dId2/dVsg
  df["gm3"] = df["id3"].diff() / df["vsg"].diff() # gm3 = dId3/dVsg
  df["gm4"] = df["id4"].diff() / df["vsg"].diff() # gm4 = dId4/dVsg

  # Save results to different out file
  df.to_csv(f"{outfile}_gm", index=False, sep=" ")

  # These values were found by running find_control_voltages.py script in TB_temp_sens folder
  highest_vctl = 1.17
  lowest_vctl = 0.43
  print(f"gm values given that 1.0 < Vsg < 1.15:\n{df[['gm1','vsg']][(df['vsg'] < highest_vctl) & (df['vsg'] > lowest_vctl)]}")

  # Plot gm results
  fig_gm, ax_gm = plt.subplots(1, 1, figsize=(fig_width, fig_height), dpi=300)  
  fig_id, ax_id = plt.subplots(1, 1, figsize=(fig_width, fig_height), dpi=300)

  ax_id.plot(df.loc[10:, "vsg"], df.loc[10:, "id4"], label="PCH 2C5F0")
  ax_id.plot(df.loc[10:, "vsg"], df.loc[10:, "id1"], label="PCH 4C5F0")
  ax_id.plot(df.loc[10:, "vsg"], df.loc[10:, "id2"], label="PCH 8C5F0")
  ax_id.plot(df.loc[10:, "vsg"], df.loc[10:, "id3"], label="PCH 12C5F0")

  ax_id.set_ylabel("Id (uA)", fontsize=label_fontsize)
  ax_id.set_xlabel("Vsg (V)", fontsize=label_fontsize)
  ax_id.tick_params(axis="both", which="major", labelsize=ticks_fontsize)
  ax_id.legend()
  ax_id.grid()

  fig_id.tight_layout()
  fig_id.savefig(f"figures/{filename}_id.png", dpi=300, bbox_inches="tight")

  ax_gm.axvline(1.0, color="gray", linestyle="dashed")

  ax_gm.plot(df.loc[10:, "vsg"], df.loc[10:, "gm4"], label="PCH 2C5F0")
  ax_gm.plot(df.loc[10:, "vsg"], df.loc[10:, "gm1"], label="PCH 4C5F0")
  ax_gm.plot(df.loc[10:, "vsg"], df.loc[10:, "gm2"], label="PCH 8C5F0")
  ax_gm.plot(df.loc[10:, "vsg"], df.loc[10:, "gm3"], label="PCH 12C5F0")

  ax_gm.set_xlabel("Vsg (V)", fontsize=label_fontsize)
  ax_gm.set_ylabel("gm (uA/V)", fontsize=label_fontsize)
  ax_gm.tick_params(axis="both", which="major", labelsize=ticks_fontsize)
  ax_gm.legend()
  ax_gm.grid()

  fig_gm.tight_layout()
  fig_gm.savefig(f"figures/{filename}_gm.png", dpi=300, bbox_inches="tight")  

  plt.show()


if __name__ == "__main__":
  main(sys.argv[1])