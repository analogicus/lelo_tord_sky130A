#!/usr/bin/env python3
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import numpy as np
import plot_transients as pt

def main(name):
  # Delete next line if you want to use python post processing
  # return
  yamlfile = name + '.yaml'

  # Read result yaml file
  with open(yamlfile) as fi:
    obj = yaml.safe_load(fi)

  # Do something to parameters
  print(obj)

  # Save new yaml file
  with open(yamlfile, 'w') as fo:
    yaml.dump(obj, fo)

  if name == 'output_tran/tran_SchGtKttTtVt':
    print(f'Plotting transient results from file: {name}.out')

    df = pd.read_csv(name + ".out", sep="\s+")
    
    df['time'] = df['time'] * 1e9 # in ns
    
    print(df.columns)
    print(df.head())
    print(df.tail())

    fig_width = 5
    fig_height = 8
    fig_fontsize = 14

    fig, axs = plt.subplots(4, 1, figsize=(fig_width, fig_height), sharex=True)
    
    ax_iout = axs[0].twinx()
    ax_iout.plot(df['time'], df['i(v.xdut.v1)']*1e6, label='iout', color='tab:orange') # in uA

    axs[0].set_title('Temperature Sensing Transient Analysis', fontsize=16)
    axs[0].plot(df['time'], df['v(vout)'], label='vout', color='tab:blue') # in V

    axs[1].plot(df['time'], df['v(v1)']-df['v(v2)'], label='v(v1) - v(v2)', linestyle='-')
    axs[1].plot(df['time'], df['v(v1a)']-df['v(v2a)'], label='v(v1a) - v(v2a)', linestyle='--')
    axs[1].plot(df['time'], df['v(v1b)']-df['v(v2b)'], label='v(v1b) - v(v2b)', linestyle=':')

    axs[2].plot(df['time'], df['v(v1)'], label='v1')
    axs[2].plot(df['time'], df['v(v1a)'], label='v1a')
    # axs[2].plot(df['time'], df['v(v1b)'], label='v1b')
    axs[2].plot(df['time'], df['v(v2)'], label='v2')
    axs[2].plot(df['time'], df['v(v2a)'], label='v2a')
    # axs[2].plot(df['time'], df['v(v2b)'], label='v2b')
    axs[2].plot(df['time'], df['v(v2c)'], label='v2c')

    axs[3].plot(df['time'], df['v(bt)'], label='v(bt)', linestyle='solid')
    axs[3].plot(df['time'], df['v(x1.ctl)'], label='ctl')
    axs[3].plot(df['time'], df['v(slp)'], label='slp')

    for ax in axs:
        ax.set_ylabel('Voltage (V)', fontsize=fig_fontsize)
        ax.grid()
    axs[0].legend(loc='upper left', fontsize=fig_fontsize-1)
    axs[1].legend(loc='upper left', fontsize=fig_fontsize-1)
    axs[2].legend(loc='upper left', fontsize=fig_fontsize-1)
    axs[3].legend(loc='upper left', fontsize=fig_fontsize-1)
    
    ax_iout.set_ylabel('Current (uA)', fontsize=fig_fontsize)
    ax_iout.legend(loc='lower right', fontsize=fig_fontsize-2)
    ax_iout.grid(linestyle='dashed')
    
    axs[-1].set_xlabel('Time (ns)', fontsize=fig_fontsize)
    
    fig.tight_layout()

    plt.show()




