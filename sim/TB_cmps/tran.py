#!/usr/bin/env python3
import pandas as pd
import yaml
import matplotlib.pyplot as plt

def main(name):
  # Delete next line if you want to use python post processing
  # return
  yamlfile = name + ".yaml"

  # Read result yaml file
  with open(yamlfile) as fi:
    obj = yaml.safe_load(fi)

  # Do something to parameters
  print(obj)

  # Save new yaml file
  with open(yamlfile,"w") as fo:
    yaml.dump(obj,fo)

  outfile = name + ".out"
  df = pd.read_csv(outfile, sep='\s+')

  df['time'] = df['time'] * 1e9 # in ns

  # print(df.columns)
  # print(df.head())
  # print(df.tail())

  fig_width = 3
  fig_height = 5
  font_size = 10
  title_fontsize = font_size + 2
  label_fontsize = font_size
  legend_fontsize = font_size - 2
  ticks_fontsize = font_size - 2

  idxs = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4}  # Adjust this index to change position of plots

  fig, axs = plt.subplots(5, 1, dpi=200, figsize=(fig_width, fig_height), sharex=True)
  fig.suptitle('Comparator comparison', fontsize=title_fontsize)

  axs[idxs['1']].plot(df['time'], df['v(vip1)'], label='vip1')
  axs[idxs['1']].plot(df['time'], df['v(vin1)'], label='vin1')
  axs[idxs['1']].plot(df['time'], df['v(vout1)'], label='vout1')

  axs[idxs['2']].plot(df['time'], df['v(vip2)'], label='vin2')
  axs[idxs['2']].plot(df['time'], df['v(vin2)'], label='vin2')
  axs[idxs['2']].plot(df['time'], df['v(vout2)'], label='vin2')

  axs[idxs['3']].plot(df['time'], df['v(vip3)'], label='vip3')
  axs[idxs['3']].plot(df['time'], df['v(vin3)'], label='vin3')
  axs[idxs['3']].plot(df['time'], df['v(vout3)'], label='vout3')
  axs[idxs['3']].plot(df['time'], df['v(vout3_pmos)'], label='vout3_pmos')

  axs[idxs['4']].plot(df['time'], df['v(vip4)'], label='vin4')
  axs[idxs['4']].plot(df['time'], df['v(vin4)'], label='vin4')
  axs[idxs['4']].plot(df['time'], df['v(vout4)'], label='vin4')

  axs[idxs['5']].plot(df['time'], df['v(vip5)'], label='vin5')
  axs[idxs['5']].plot(df['time'], df['v(vin5)'], label='vin5')
  axs[idxs['5']].plot(df['time'], df['v(vout5)'], label='vin5')

  for ax in axs:
    ax.set_xlabel("Time (ns)", fontsize=label_fontsize)
    ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
    ax.set_ylim(-0.1, 2.1)
    ax.set_yticks([0, 1, 1.8])
    ax.tick_params(axis='both', which='major', labelsize=ticks_fontsize)
    ax.legend(loc="upper right", fontsize=legend_fontsize)
    ax.grid()

  fig.tight_layout()

  image_path = f"./figures/{name.split('/')[-1]}.png"

  if "output_tran/tran_SchGtKttmmTtVt_" not in name:
    plt.savefig(image_path)
    print("Figure saved to " + image_path)

  if "output_tran/tran_SchGtKttTtVt" in name:
    plt.show()