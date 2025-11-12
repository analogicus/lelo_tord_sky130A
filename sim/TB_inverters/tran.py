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

    fig, axes = plt.subplots(3, 2)
    fig.suptitle('Inverter currents and voltages', fontsize=16)
    fig.set_size_inches(8, 8)

    ax4 = axes[0, 0]
    ax5 = axes[0, 1]
    ax0 = axes[1, 0]
    ax1 = axes[1, 1]
    ax2 = axes[2, 0]
    ax3 = axes[2, 1]

    ax0.set_title('Inverter 1 voltages')
    ax0.plot(df['time'], df['v(in1)'], label='input 1')
    ax0.plot(df['time'], df['v(out1)'], label='output 1')
    ax0.legend()
    ax0.set_ylabel('Voltage (V)')
    ax0.grid()

    ax1.set_title('Inverter 2 voltages')
    ax1.plot(df['time'], df['v(in2)'], label='input 2')
    ax1.plot(df['time'], df['v(out2)'], label='output 2')
    ax1.legend()
    ax1.set_ylabel('Voltage (V)')
    ax1.grid()

    ax2.set_title('Inverter 3 voltages')
    ax2.plot(df['time'], df['v(in3)'], label='input 3')
    ax2.plot(df['time'], df['v(out3)'], label='output 3')
    ax2.legend()
    ax2.set_ylabel('Voltage (V)')
    ax2.grid()

    ax3.set_title('Inverter 4 voltages')
    ax3.plot(df['time'], df['v(in4)'], label='input 4')
    ax3.plot(df['time'], df['v(out4)'], label='output 4')
    ax3.legend()
    ax3.set_ylabel('Voltage (V)')
    ax3.grid()

    ax4.set_title('Inverter Currents')
    ax4.plot(df['time'], -df['i(v1)']*1e6, label='input 1')
    ax4.plot(df['time'], -df['i(v2)']*1e6, label='input 2')
    ax4.plot(df['time'], -df['i(v3)']*1e6, label='input 3')
    ax4.plot(df['time'], -df['i(v4)']*1e6, label='input 4')
    ax4.legend()
    ax4.set_ylabel('Current (uA)')
    ax4.grid()

    ax5.set_title('Current Ratios')
    ax5.plot(df['time'], df['i(v2)']/df['i(v1)'], label='i(v2)/i(v1)', color='tab:orange')
    ax5.plot(df['time'], df['i(v3)']/df['i(v1)'], label='i(v3)/i(v1)', color='tab:green')
    ax5.plot(df['time'], df['i(v4)']/df['i(v1)'], label='i(v4)/i(v1)', color='tab:red')
    ax5.legend()
    ax5.set_ylabel('Ratio magnitude')
    ax5.grid()

    for ax in (ax0, ax1, ax2, ax3, ax4, ax5):
      ax.set(xlabel='Time (ns)')

    plt.tight_layout()

    image_path = "./figures/" + name.split('/')[-1] + ".png"
    print(f"Saving plot as {image_path}")
    plt.savefig(image_path, dpi=300)

    plt.show()