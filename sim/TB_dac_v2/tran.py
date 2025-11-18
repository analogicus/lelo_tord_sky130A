#!/usr/bin/env python3
import pandas as pd
import yaml
import matplotlib.pyplot as plt

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

  fname = name + ".out"
  df = pd.read_csv(fname, sep='\s+')

  if name == "output_tran/tran_SchGtKttTtVt":

    df['time'] = df['time'] * 1e9 # in ns

    print(df.columns)
    print(df.head())

    idx_dict = {'diff': 0, 'diode': 1, 'control': 2, 'bits': 3, 'sleep': 4}  # Adjust this index if the position of 'sleep' plot changes

    fig,axs = plt.subplots(len(idx_dict), 1, sharex=True)
    fig.suptitle('DAC currents and voltages')
    fig.set_size_inches(8, 12)

    # axs[idx_dict['diff']].plot(df['time'], df['v(v1)']-df['v(v2)'], label='v(v1) - v(v2)')
    axs[idx_dict['diff']].plot(df['time'], df['v(v1a)']-df['v(v2a)'], label='v(v1a) - v(v2a)')
    axs[idx_dict['diff']].plot(df['time'], df['v(v1b)']-df['v(v2b)'], label='v(v1b) - v(v2b)', linestyle='--')

    # axs[idx_dict['diode']].plot(df['time'], df['v(v1)'], label='v1')
    axs[idx_dict['diode']].plot(df['time'], df['v(v1a)'], label='v1a')
    axs[idx_dict['diode']].plot(df['time'], df['v(v1b)'], label='v1b')
    # axs[idx_dict['diode']].plot(df['time'], df['v(v2)'], label='v2')
    axs[idx_dict['diode']].plot(df['time'], df['v(v2a)'], label='v2a')
    axs[idx_dict['diode']].plot(df['time'], df['v(v2b)'], label='v2b')
    axs[idx_dict['diode']].plot(df['time'], df['v(v2c)'], label='v2c')

    axs[idx_dict['control']].plot(df['time'], df['v(x1.vt)'], label='x1.vt')
    axs[idx_dict['control']].plot(df['time'], df['v(x2.vt)'], label='x2.vt', linestyle='--')
    axs[idx_dict['bits']].plot(df['time'], df['v(b0)'], label='bit 0')
    axs[idx_dict['bits']].plot(df['time'], df['v(b1)'], label='bit 1')
    axs[idx_dict['bits']].plot(df['time'], df['v(b2)'], label='bit 2')
    axs[idx_dict['bits']].plot(df['time'], df['v(b3)'], label='bit 3')

    axs[idx_dict['sleep']].plot(df['time'], df['v(slp)'], label='sleep')
    axs[list(idx_dict.values())[-1]].set(xlabel='Time (ns)')

    for ax in axs:
      ax.set_ylabel('Voltage (V)')
      ax.legend()
      ax.grid()

    fig.tight_layout()

    image_path = "./figures/" + name.split('/')[-1] + ".png"
    plt.savefig(image_path)
    print("Figure saved to " + image_path)

    plt.show()


