#!/usr/bin/env python3
from unicodedata import name
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import pickle
import numpy as np

def main(name):
  # # Delete next line if you want to use python post processing
  # return
  # yamlfile = name + ".yaml"

  # # Read result yaml file
  # with open(yamlfile) as fi:
  #   obj = yaml.safe_load(fi)

  # # Do something to parameters

  # # Save new yaml file
  # with open(yamlfile,"w") as fo:
  #   yaml.dump(obj,fo)

  number_of_linearity_points = 9

  fname = name + ".out"
  df = pd.read_csv(fname, sep='\s+')

  if name == "output_tran/tran_SchGtKttTtVt":
    VDD = 1.8
    
    df['time'] = df['time'] * 1e9 # in ns

    print(df.columns)
    print(df.head())
    print(df.tail())

    # Defines the number of subplots and their order
    idx_dict = {'combined': 0, 'v(vout1)': 1, 'v(vout2)': 2, 'v(vout3)': 3, 'bx': 4, 'bt': 5, 'signals': 6}

    fig, axs = plt.subplots(len(idx_dict), 1, sharex=True)
    fig.suptitle('DAC currents and voltages')
    fig.set_size_inches(8, 14)

    axs[idx_dict['combined']].plot(df['time'], df['v(vout1)'], label='vout1 over diode connected transistor')
    line_color1 = axs[idx_dict['combined']].lines[-1].get_color()

    axs[idx_dict['combined']].plot(df['time'], df['v(vout2)'], label='vout2 over small resistor (2*7535 Ohm = 15070 Ohm)')
    line_color2 = axs[idx_dict['combined']].lines[-1].get_color()

    axs[idx_dict['combined']].plot(df['time'], df['v(vout3)'], label='vout3 over large resistor (16*7525 Ohm = 120400 Ohm)')
    line_color3 = axs[idx_dict['combined']].lines[-1].get_color()

    target_times = [8500 + i*62 for i in range(number_of_linearity_points)] # 62 ns is Tclk and should have been 62.5 ns, but with rise and fall times it might be better to add a bit more
    print(f'x = {target_times}')
    target_times_idx = [df.index[df['time'] == xi][0] for xi in target_times]
    print(f'target_times_idx = {target_times_idx}')

    axs[idx_dict['v(vout1)']].plot(df['time'], df['v(vout1)'], label='vout1', color=line_color1)
    axs[idx_dict['v(vout1)']].plot(target_times, df.loc[target_times_idx]['v(vout1)'], marker='o', linestyle='dashed', color='red', label='vout1 levels')

    axs[idx_dict['v(vout2)']].plot(df['time'], df['v(vout2)'], label='vout2', color=line_color2)
    axs[idx_dict['v(vout2)']].plot(target_times, df.loc[target_times_idx]['v(vout2)'], marker='o', linestyle='dashed', color='red', label='vout2 levels')

    axs[idx_dict['v(vout3)']].plot(df['time'], df['v(vout3)'], label='vout3', color=line_color3)
    axs[idx_dict['v(vout3)']].plot(target_times, df.loc[target_times_idx]['v(vout3)'], marker='o', linestyle='dashed', color='red', label='vout3 levels')

    axs[idx_dict['bx']].plot(df['time'], df['v(b0)'], label='b0', color='brown')
    axs[idx_dict['bx']].plot(df['time'], df['v(b1)'], label='b1', color='pink')
    axs[idx_dict['bx']].plot(df['time'], df['v(b2)'], label='b2', color='gray')
    axs[idx_dict['bx']].plot(df['time'], df['v(b3)'], label='b3', color='olive')
    axs[idx_dict['bx']].plot(df['time'], df['v(b4)'], label='b4', color='cyan')
    axs[idx_dict['bx']].plot(df['time'], df['v(b5)'], label='b5', color='magenta')
    axs[idx_dict['bx']].plot(df['time'], df['v(b6)'], label='b6', color='navy')
    axs[idx_dict['bx']].plot(df['time'], df['v(b7)'], label='b7', color='teal')
    
    axs[idx_dict['bt']].plot(df['time'], df['v(bt)'], label='v(bt)', color='black', linestyle='solid')

    axs[idx_dict['signals']].plot(df['time'], df['v(slp)'], label='sleep', color='purple')
    axs[idx_dict['signals']].plot(df['time'], df['v(x1.ctl)'], label='x1.ctl', color='orange')
    axs[idx_dict['signals']].plot(df['time'], df['v(x2.ctl)'], label='x2.ctl', color='green')
    axs[idx_dict['signals']].plot(df['time'], df['v(x3.ctl)'], label='x3.ctl', color='red')

    axs[list(idx_dict.values())[-1]].set(xlabel='Time (ns)')

    for ax in axs:
      ax.set_ylabel('Voltage (V)')
      ax.legend()
      ax.grid()

    fig.tight_layout()

    image_path = "./figures/" + name.split('/')[-1]
    fig.savefig(image_path + ".png")
    print("Figure saved to " + image_path + ".png")  

    with open(f"{image_path}.fig.pickle", 'wb') as file:
        pickle.dump(fig, file)
    print("Figure pickled to " + image_path + ".fig.pickle")

    plt.show()
