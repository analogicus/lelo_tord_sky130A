#!/usr/bin/env python3
import pandas as pd
import yaml
import matplotlib.pyplot as plt

def main(name):
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

  # Read result .out file
  fname = name + ".out"
  df = pd.read_csv(fname, sep='\s+')

  if name == "output_tran/tran_SchGtKttTtVt":

    R = 7535*16

    df['ib'] = ((df['v(v1)'] - df['v(v2)']) / R) * 1e6 # in uA
    df['time'] = df['time'] * 1e9 # in ns

    print(df.columns)
    print(df.head())

    fig,(ax0, ax1, ax2, ax3) = plt.subplots(4, 1)
    fig.suptitle('Bias currents and voltages')

    ax0.plot(df['time'], df['ib'], label='ib')
    ax0.set_title("Bias current")
    ax0.set_yticks([-5, -2.5, 0, 2.5, 5, 7.5])
    ax0.legend(loc='upper right')
    ax0.grid()
  
    ax1.plot(df['time'], df['v(nbias)'], label='nbias')
    ax1.set_title("NMOS bias voltage")
    ax1.set_yticks([-0.6, 0, 0.6, 1.2])
    ax1.legend(loc='upper right')
    ax1.grid()

    ax2.plot(df['time'], df['v(pbias)'], label='pbias')
    ax2.set_title("PMOS bias voltage")
    ax2.set_yticks([0, 0.7, 1.4, 2.1])
    ax2.legend(loc='upper right')
    ax2.grid()

    ax3.plot(df['time'], df['v(sleep)'], label='sleep')
    ax3.set_title("Sleep voltage")
    ax3.set_yticks([0, 0.9, 1.8])
    ax3.legend(loc='upper right')
    ax3.grid()

    ax0.set(xlabel='Time (ns)', ylabel='Current (uA)')
    for ax in (ax1, ax2, ax3):
      ax.set(xlabel='Time (ns)', ylabel='Voltage (V)')

    fig.tight_layout()

    image_path = "./figures/" + name.split('/')[-1] + ".png"
    plt.savefig(image_path)
    print("Figure saved to " + image_path)

    plt.show()

