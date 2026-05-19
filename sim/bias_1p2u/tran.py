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
    
  df = pd.read_csv(name + ".out", sep='\s+')

  df['i(vss)'] = -df['i(vss)'] * 1e6 # in uA
  df['i(vdd)'] = -df['i(vdd)'] * 1e6 # in uA
  df['iref'] = df['iref'] * 1e6 # in uA
  df['ibias'] = df['ibias'] * 1e6 # in uA

  df['time'] = df['time'] * 1e9 # in ns

  # print(f"mean ivdd: {np.mean(df['i(vdd)'])/2}")
  # print(f"mean iref: {np.mean(df['iref'])}")
  # print(f"mean ibias: {np.mean(df['ibias'])}")

  # print(df.columns)
  # print(df.head())
  # print(df.tail())

  idxs = {'iref': 0, 'vbx': 1, 'vrx': 2, 'slp': 3}  # Adjust this index to change position of plots

  fig, axs = plt.subplots(2, 2, sharex=True, dpi=300)
  fig.suptitle('Bias currents (target 1.2 uA) and voltages')

  axs[0,0].plot(df['time'], (df['i(vdd)']/2), label=f'i(vdd)/2: {df.iloc[-1]["i(vdd)"]/2:.2f} uA', marker='')
  axs[0,0].plot(df['time'], df['iref'], label=f'iref = {df.iloc[-1]["iref"]:.2f} uA\n(through unit resistor)')
  axs[0,0].plot(df['time'], df['ibias'], label=f'ibias = {df.iloc[-1]["ibias"]:.2f} uA\n(through total resistance)')

  axs[0,1].plot(df['time'], df['v(vbn)'], label=f'vbn = {df.iloc[-1]["v(vbn)"]:.2f} V')
  axs[0,1].plot(df['time'], df['v(vbp)'], label=f'vbp = {df.iloc[-1]["v(vbp)"]:.2f} V')

  axs[1,0].plot(df['time'], df['v(vr1)'], label=f'vr1 = {df.iloc[-1]["v(vr1)"]:.2f} V')
  axs[1,0].plot(df['time'], df['v(vr2)'], label=f'vr2 = {df.iloc[-1]["v(vr2)"]:.2f} V')
  axs[1,0].plot(df['time'], df['v(vr3)'], label=f'vr3 = {df.iloc[-1]["v(vr3)"]:.2f} V')
  axs[1,0].plot(df['time'], df['v(vr4)'], label=f'vr4 = {df.iloc[-1]["v(vr4)"]:.2f} V')
  axs[1,0].plot(df['time'], df['v(vr5)'], label=f'vr5 = {df.iloc[-1]["v(vr5)"]:.2f} V')
  axs[1,0].plot(df['time'], df['v(vr6)'], label=f'vr6 = {df.iloc[-1]["v(vr6)"]:.2f} V')
  axs[1,0].plot(df['time'], df['v(vr7)'], label=f'vr7 = {df.iloc[-1]["v(vr7)"]:.2f} V')

  axs[1,1].plot(df['time'], df['v(slp)'], label=f'slp = {df.iloc[-1]["v(slp)"]:.2f} V')
  axs[1,1].plot(df['time'], df['v(slp_n)'], label=f'slp_n = {df.iloc[-1]["v(slp_n)"]:.2f} V')
  
  axs[0,0].set_xlabel("Time (ns)")
  axs[0,0].set_ylabel("Current (uA)")  
  axs[0,0].tick_params(axis='both', which='major')
  axs[0,0].legend()
  axs[0,0].grid()
  axs[0,0].set_ylim(-0.1, 2.6)

  for ax in (axs[0,1], axs[1,0], axs[1,1]):
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("Voltage (V)")
    ax.tick_params(axis='both', which='major')
    ax.legend()
    ax.grid()
    ax.set_ylim(-0.1, 2.1)

  fig.tight_layout()

  image_path = "./figures/" + name.split("/")[-1] + ".png"
  
  if "tran_SchGtKttmmTtVt" not in name:
    plt.savefig(image_path)
    print("Figure saved to " + image_path)
  
  if name == "output_tran/tran_SchGtKttTtVt":
    plt.show()
  else:
    plt.close()


