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
  fend = ".out" # bias file extension, could be .out, .yaml or .csv
  fname = name + fend

  print(f"Processing file: {fname}")

  df = pd.read_csv(fname, sep='\s+')

  R16 = 7535*16
  R8 = 7535*8
  R4 = 7535*4
  R2 = 7535*2
  Rtot = 7*R16
  v_difference = df['v(vr1)'] - df['v(vbn)']

  if name == "output_tran/tran_SchGtKttTtVt":

    df['ib_calc'] = (v_difference / Rtot) * 1e6 # in uA
    df['time'] = df['time'] * 1e9 # in ns

    print(df.columns)
    print(df.head())

    fig, axs = plt.subplots(3, 1, figsize=(6, 4), sharex=True, dpi=300)

    axs[0].plot(df['time'], df['ib_total'] * 1e6, label='ib_total') # in uA
    axs[0].plot(df['time'], df['ib_single'] * 1e6, label='ib_single') # in uA
    # axs[0].plot(df['time'], df['ib_drain'] * 1e6, label='ib_drain') # in uA
    axs[0].plot(df['time'], df['ib_calc'], label='ib_calc') # in uA

    axs[1].plot(df['time'], df['v(vr1)'], label='vr1')
    axs[1].plot(df['time'], df['v(vbn)'], label='vbn')
    axs[1].plot(df['time'], df['v(vbp)'], label='vbp')

    # axs[2].plot(df['time'], df['v(vdd)'], label='vdd')
    # axs[2].plot(df['time'], df['v(vss)'], label='vss')
    axs[2].plot(df['time'], df['v(slp)'], label='slp')
    axs[2].plot(df['time'], df['v(slp_n)'], label='slp_n')
    axs[2].plot(df['time'], df['v(xdut.slp)'], label='xdut.slp')
    axs[2].plot(df['time'], df['v(xdut.slp_n)'], label='xdut.slp_n')

    axs[0].set(ylabel='Current (uA)')
    axs[1].set(ylabel='Voltage (V)')
    axs[2].set(ylabel='Voltage (V)')

    for ax in axs:
        ax.legend()
        ax.grid()

    fig.tight_layout()

    image_path = "./figures/" + name.split('/')[-1]
    
    fig.savefig(image_path + "_currents_and_voltages.png")
    print("Figure saved to " + image_path + "_currents_and_voltages.png")


    fig_pwr, axs_pwr = plt.subplots(2, 1, figsize=(6, 4), sharex=True, dpi=300)

    df['pwr'] = df['v(vdd)'] * -(df['i(vdd)']) # in W
    axs_pwr[0].plot(df['time'], df['pwr'] * 1e6, label='Power from vdd', color='tab:blue') # in uW

    axs_pwr[1].plot(df['time'], df['i(vslp)'], label='i(vslp)')
    axs_pwr[1].plot(df['time'], df['i(vslpn)'], label='i(vslpn)')
    
    axs_pwr[0].set(ylabel='Power (uW)')
    axs_pwr[0].legend(loc='upper left')
    axs_pwr[0].grid()

    axs_pwr[1].set(xlabel='Time (ns)', ylabel='Current (A)')
    axs_pwr[1].legend()
    axs_pwr[1].grid()

    axs_volt = axs_pwr[0].twinx()
    axs_volt.plot(df['time'], df['v(vdd)'], label='v(vdd)', color='tab:orange')
    
    axs_volt.set(ylabel='Power (uW)')
    axs_volt.legend(loc='upper right')

    fig_pwr.savefig(image_path + "_power_consumption.png")
    print("Figure saved to " + image_path + "_power_consumption.png")
    
    plt.show()

