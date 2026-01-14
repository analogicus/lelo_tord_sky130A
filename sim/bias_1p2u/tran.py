#!/usr/bin/env python3
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import numpy as np

def main(name):
  print(f"name: {name}")

  # Delete next line if you want to use python post processing
  # return
  # yamlfile = name + ".yaml"

  # # Read result yaml file
  # with open(yamlfile) as fi:
  #   obj = yaml.safe_load(fi)

  # # Do something to parameters

  # # Save new yaml file
  # with open(yamlfile,"w") as fo:
  #   yaml.dump(obj,fo)

  fig_width = 8
  fig_height = 8
  font_size = 10
  title_fontsize = font_size + 2
  label_fontsize = font_size
  legend_fontsize = font_size - 2
  ticks_fontsize = font_size - 2

  fend = ".out" # bias file extension, could be .out, .yaml or .csv
    
  for i in range(2):
    if i == 0:
      fname = name + fend
    else:
      fname = name + "_sleep_high" + fend

    print(f"\nProcessing file: {fname}")
    df = pd.read_csv(fname, sep='\s+')

    df['i(vss)'] = -df['i(vss)'] * 1e6 # in uA
    df['i(vdd)'] = -df['i(vdd)'] * 1e6 # in uA
    df['iref'] = df['iref'] * 1e6 # in uA
    df['ibias'] = df['ibias'] * 1e6 # in uA

    df['time'] = df['time'] * 1e9 # in ns

    print(f"mean ivdd: {np.mean(df['i(vdd)'])/2}")
    print(f"mean iref: {np.mean(df['iref'])}")
    print(f"mean ibias: {np.mean(df['ibias'])}")

    print(df.columns)
    print(df.head())
    print(df.tail())

    idxs = {'iref': 0, 'vbias': 1, 'v': 2, 'sleep': 3}  # Adjust this index to change position of plots

    fig, axs = plt.subplots(len(idxs), 1, sharex=True)
    fig.suptitle('Bias currents (target 1.2 uA) and voltages', fontsize=title_fontsize)
    fig.set_size_inches(fig_width, fig_height)

    axs[idxs['iref']].plot(df['time'], (df['i(vdd)']/2), label='vdd current halfed', marker='')
    axs[idxs['iref']].plot(df['time'], df['iref'], label='reference current calculated over unit resistor')
    axs[idxs['iref']].plot(df['time'], df['ibias'], label='bias current calculated over total resistance')

    axs[idxs['vbias']].plot(df['time'], df['v(nbias)'], label='nmos bias voltage')
    axs[idxs['vbias']].plot(df['time'], df['v(pbias)'], label='pmos bias voltage')

    axs[idxs['v']].plot(df['time'], df['v(v1)'], label='v1')
    axs[idxs['v']].plot(df['time'], df['v(v2)'], label='v2')
    axs[idxs['v']].plot(df['time'], df['v(v3)'], label='v3')
    axs[idxs['v']].plot(df['time'], df['v(v4)'], label='v4')
    axs[idxs['v']].plot(df['time'], df['v(v5)'], label='v5')
    axs[idxs['v']].plot(df['time'], df['v(v6)'], label='v6')
    axs[idxs['v']].plot(df['time'], df['v(v7)'], label='v7')

    axs[idxs['sleep']].plot(df['time'], df['v(sleep)'], label='sleep signal')
    axs[idxs['sleep']].plot(df['time'], df['v(sleep_n)'], label='inverted sleep signal')
    
    axs[idxs['iref']].set_xlabel("Time (ns)", fontsize=label_fontsize)
    axs[idxs['iref']].set_ylabel("Current (uA)", fontsize=label_fontsize)  
    axs[idxs['iref']].tick_params(axis='both', which='major', labelsize=ticks_fontsize)
    axs[idxs['iref']].legend(fontsize=legend_fontsize)
    axs[idxs['iref']].grid()
    axs[idxs['iref']].set_ylim(-0.1, 2.6)

    for ax in (axs[idxs['vbias']], axs[idxs['v']], axs[idxs['sleep']]):
      ax.set_xlabel("Time (ns)", fontsize=label_fontsize)
      ax.set_ylabel("Voltage (V)", fontsize=label_fontsize)
      ax.tick_params(axis='both', which='major', labelsize=ticks_fontsize)
      ax.legend(fontsize=legend_fontsize)
      ax.grid()
      ax.set_ylim(-0.1, 2.1)

    fig.tight_layout()

    image_path = "./figures/" + fname.split('/')[-1].replace('.out', '') + ".png"
    
    if "output_tran/tran_SchGtKttmmTtVt_" not in name:
      plt.savefig(image_path)
      print("Figure saved to " + image_path)
    
    if "output_tran/tran_SchGtKttTtVt" in name:
      plt.show()


