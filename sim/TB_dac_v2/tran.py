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

    fig,axs = plt.subplots(8, 1)
    fig.suptitle('DAC currents and voltages')
    fig.set_size_inches(8, 12)

    axs[0].plot(df['time'], df['v(vdiode)'], label='diode voltage')
    # axs[0].set_title("Diode voltage")
    # axs[0].set_yticks([0, 0.25, 0.5, 0.75, 1.0])

    axs[1].plot(df['time'], df['v(vctrl)'], label='control')

    axs[2].plot(df['time'], df['v(b0)'], label='bit 0')
    axs[3].plot(df['time'], df['v(b1)'], label='bit 1')
    axs[4].plot(df['time'], df['v(b2)'], label='bit 2')
    axs[5].plot(df['time'], df['v(b3)'], label='bit 3')
    # axs[1].set_title("Select lines")
    # axs[1].set_yticks([0, 0.9, 1.8])

    axs[6].plot(df['time'], df['v(b4)'], label='bit 4')
    # axs[2].set_title("Counter")
    # axs[2].set_yticks([])

    axs[7].plot(df['time'], df['v(sleep)'], label='sleep')
    # axs[3].set_title("Sleep voltage")
    # axs[3].set_yticks([0, 0.9, 1.8])

    for ax in axs:
      ax.set(xlabel='Time (ns)', ylabel='Voltage (V)')
      ax.legend()
      ax.grid()

    fig.tight_layout()

    image_path = "./figures/" + name.split('/')[-1] + ".png"
    plt.savefig(image_path)
    print("Figure saved to " + image_path)

    plt.show()


