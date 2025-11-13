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

  fend = ".out" # bias file extension, could be .out, .yaml or .csv
  fname = name + fend
  df = pd.read_csv(fname, sep='\s+')

  if name == "output_tran/tran_SchGtKttTtVt":

    df['time'] = df['time'] * 1e9 # in ns

    print(df.columns)
    print(df.head())

    fig, axs = plt.subplots(5, 1, sharex=True)
    fig.suptitle('Bias currents and voltages', fontsize=16)
    # fig.set_size_inches(8, 8)

    axs[0].plot(df['time'], df['v(iout)'], label='iout')
    # axs[0].set_title("DAC output voltage")
    # ax[0].set_yticks([-5, -2.5, 0, 2.5, 5, 7.5])
  
    axs[1].plot(df['time'], df['v(ctrl)'], label='ctrl')
    # axs[1].set_title("Time averaging control voltage")
    # axs[1].set_yticks([-0.6, 0, 0.6, 1.2])

    axs[2].plot(df['time'], df['v(b0)'], label='b0')
    axs[2].plot(df['time'], df['v(b1)'], label='b1')
    axs[2].plot(df['time'], df['v(b2)'], label='b2')
    axs[2].plot(df['time'], df['v(b3)'], label='b3')
    axs[2].plot(df['time'], df['v(b4)'], label='b4')
    axs[2].plot(df['time'], df['v(b5)'], label='b5')
    axs[2].plot(df['time'], df['v(b6)'], label='b6')
    axs[2].plot(df['time'], df['v(b7)'], label='b7')
    # axs[2].set_title("Course current steering DAC control bit signals")
    # axs[2].set_yticks([0, 0.7, 1.4, 2.1])

    axs[3].plot(df['time'], df['v(bt)'], label='bt')
    # axs[3].set_title("Fine current steering DAC control bit signals")


    axs[4].plot(df['time'], df['v(sleep)'], label='sleep')
    # axs[4].set_title("Sleep voltage")
    # axs[4].set_yticks([0, 0.9, 1.8])
    axs[4].set(xlabel='Time (ns)', ylabel='Voltage (V)')

    for ax in axs:
      ax.legend()
      ax.grid()

    fig.tight_layout()

    image_path = "./figures/" + name.split('/')[-1] + ".png"
    plt.savefig(image_path)
    print("Figure saved to " + image_path)

    plt.show()


