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

  # Read result .out file
  fname = name + ".out"
  df = pd.read_csv(fname, sep='\s+')

  if name == "output_tran/tran_SchGtKttTtVt":

    df['time'] = df['time'] * 1e9 # in ns

    print(df.columns)
    print(df.head())

    fig,(ax0, ax4, ax1, ax2, ax3) = plt.subplots(5, 1)
    fig.suptitle('DAC currents and voltages')
    fig.set_size_inches(8, 8)

    ax0.plot(df['time'], df['v(vdiode)'], label='diode voltage')
    # ax0.set_title("Diode voltage")
    # ax0.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax0.legend(loc='upper right')
    ax0.grid()

    ax1.plot(df['time'], df['v(b0)'], label='bit 0')
    ax1.plot(df['time'], df['v(b1)'], label='bit 1')
    ax1.plot(df['time'], df['v(b2)'], label='bit 2')
    ax1.plot(df['time'], df['v(b3)'], label='bit 3')
    # ax1.set_title("Select lines")
    # ax1.set_yticks([0, 0.9, 1.8])
    ax1.legend(loc='upper right')
    ax1.grid()

    ax2.plot(df['time'], df['v(b4)'], label='bit 4')
    # ax2.set_title("Counter")
    # ax2.set_yticks([])
    ax2.legend(loc='upper right')
    ax2.grid()

    ax3.plot(df['time'], df['v(clk)'], label='clock')
    ax3.plot(df['time'], df['v(rst)'], label='reset')
    ax3.plot(df['time'], df['v(sleep)'], label='sleep')
    # ax3.set_title("Sleep voltage")
    # ax3.set_yticks([0, 0.9, 1.8])
    ax3.legend(loc='upper right')
    ax3.grid()

    ax4.plot(df['time'], df['v(vctrl)'], label='control')
    ax4.legend(loc='upper right')
    ax4.grid()

    for ax in (ax0, ax1, ax2, ax3, ax4):
      ax.set(xlabel='Time (ns)', ylabel='Voltage (V)')

    # fig.tight_layout()

    image_path = "./figures/" + name.split('/')[-1] + ".png"
    plt.savefig(image_path)
    print("Figure saved to " + image_path)

    plt.show()

