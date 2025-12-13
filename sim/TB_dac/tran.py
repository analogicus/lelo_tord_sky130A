#!/usr/bin/env python3
from unicodedata import name
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import pickle
import numpy as np

freq = 1  # MHz
duty = 65  # %

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
  step_start = 6000 # ns
  step_length = 2000 # ns

  fname = name + ".out"
  df = pd.read_csv(fname, sep='\s+')

  if name == "output_tran/tran_SchGtKttTtVt":
    VDD = 1.8
    
    df['time'] = df['time'] * 1e9 # in ns

    print(df.columns)
    print(df.head())
    print(df.tail())

    #
    # Plot DAC output current and calculate average, min, max values
    #

    fig_iout, axs_iout = plt.subplots(1, 1, figsize=(8, 7))
    fig_iout.suptitle(f"DAC Output Current ({freq} MHz, {duty} % duty cycle)")

    axs_iout.plot(df['time'], df['i(v.xdut.v1)']*1e6, label=f'{name.split("_")[-1]} iout')

    # Calculate and plot average output value
    for i, b in enumerate(["bt", "b0", "b1", "b2", "b3", "b4", "b5", "b6", "b7"]):      
      print(f'Calculating avg, min and max iout values for {b}...')

      tstart = step_start + i*step_length + 150 # ns
      tstop = step_start + (i+1)*step_length - 150 # ns
      
      avg_iout = np.mean(df[f'i(v.xdut.v1)'][(df['time'] >= tstart) & (df['time'] <= tstop)])*1e6 # in uA
      max_iout = np.max(df[f'i(v.xdut.v1)'][(df['time'] >= tstart) & (df['time'] <= tstop)])*1e6 # in uA
      min_iout = np.min(df[f'i(v.xdut.v1)'][(df['time'] >= tstart) & (df['time'] <= tstop)])*1e6 # in uA
      time_vals = df['time'][(df['time'] >= tstart) & (df['time'] <= tstop)]
      print(f'Max iout value between {tstart} ns and {tstop} ns: {max_iout:.3f} uA')
      print(f'Avg iout value between {tstart} ns and {tstop} ns: {avg_iout:.3f} uA')
      print(f'Min iout value between {tstart} ns and {tstop} ns: {min_iout:.3f} uA')
      axs_iout.plot(time_vals, [max_iout]*len(time_vals), label=f'max {b}: {max_iout:.3f} uA', linestyle=':')
      line_color2 = axs_iout.lines[-1].get_color()
      axs_iout.plot(time_vals, [avg_iout]*len(time_vals), label=f'avg {b}: {avg_iout:.3f} uA', linestyle='--', color=line_color2)
      axs_iout.plot(time_vals, [min_iout]*len(time_vals), label=f'min {b}: {min_iout:.3f} uA', linestyle='-.', color=line_color2)

    axs_iout.set_xlabel('Time (ns)')
    axs_iout.set_ylabel('Current (uA)')
    axs_iout.legend(bbox_to_anchor=(1.01, 1), loc='upper left')
    axs_iout.grid()
    # axs_iout.set_title("DAC Output Current")
    fig_iout.tight_layout()
    fig_iout.savefig(f"./figures/tb_dac_plot_tran_iout_{name.split('_')[-1]}.png")

    #
    # Plot all relevant signals
    #

    # Defines the number of subplots and their order
    # idx_dict = {'combined': 0, 'v(vout1)': 1, 'v(vout2)': 2, 'v(vout3)': 3, 'i(vout4)': 4, 'bx': 5, 'bt': 6, 'signals': 7}
    idx_dict = {'i(vout4)': 0, 'bx': 1, 'bt': 2, 'signals': 3}

    fig, axs = plt.subplots(len(idx_dict), 1, sharex=True)
    fig.suptitle(f'DAC Output Current ({freq} MHz, {duty} % duty cycle)')
    fig.set_size_inches(6, 10)

    # axs[idx_dict['combined']].plot(df['time'], df['v(vout1)'], label='vout1 over diode connected transistor')
    # line_color1 = axs[idx_dict['combined']].lines[-1].get_color()

    # axs[idx_dict['combined']].plot(df['time'], df['v(vout2)'], label='vout2 over small resistor (2*7535 Ohm = 15070 Ohm)')
    # line_color2 = axs[idx_dict['combined']].lines[-1].get_color()

    # axs[idx_dict['combined']].plot(df['time'], df['v(vout3)'], label='vout3 over large resistor (16*7525 Ohm = 120400 Ohm)')
    # line_color3 = axs[idx_dict['combined']].lines[-1].get_color()

    target_times = [step_start - 100 + (i+1)*step_length for i in range(number_of_linearity_points)] # 62 ns is Tclk and should have been 62.5 ns, but with rise and fall times it might be better to add a bit more
    print(f'x = {target_times}')

    target_times_idx = []
    for t in target_times:
      print(f'Finding closest time to {t} ns...')
      target_times_idx.append((df['time'] - t).abs().idxmin())
      print(f'Closest time to {t} ns is {df["time"][target_times_idx[-1]]} ns at index {target_times_idx[-1]}')

    # axs[idx_dict['v(vout1)']].plot(df['time'], df['v(vout1)'], label='vout1', color=line_color1)
    # axs[idx_dict['v(vout1)']].plot(target_times, df.loc[target_times_idx]['v(vout1)'], marker='o', linestyle='dashed', color='gray', label='vout1 levels')

    # axs[idx_dict['v(vout2)']].plot(df['time'], df['v(vout2)'], label='vout2', color=line_color2)
    # axs[idx_dict['v(vout2)']].plot(target_times, df.loc[target_times_idx]['v(vout2)'], marker='o', linestyle='dashed', color='gray', label='vout2 levels')

    # axs[idx_dict['v(vout3)']].plot(df['time'], df['v(vout3)'], label='vout3', color=line_color3)
    # axs[idx_dict['v(vout3)']].plot(target_times, df.loc[target_times_idx]['v(vout3)'], marker='o', linestyle='dashed', color='gray', label='vout3 levels')

    axs[idx_dict['i(vout4)']].plot(df['time'], df['i(v.xdut.v1)']*1e6, label='iout')
    axs[idx_dict['i(vout4)']].plot(target_times, df.loc[target_times_idx]['i(v.xdut.v1)']*1e6, marker='o', linestyle='dashed', color='gray', label='measurements')

    axs[idx_dict['bx']].plot(df['time'], df['v(b0)'], label='b0')
    axs[idx_dict['bx']].plot(df['time'], df['v(b1)'], label='b1')
    axs[idx_dict['bx']].plot(df['time'], df['v(b2)'], label='b2')
    axs[idx_dict['bx']].plot(df['time'], df['v(b3)'], label='b3')
    axs[idx_dict['bx']].plot(df['time'], df['v(b4)'], label='b4')
    axs[idx_dict['bx']].plot(df['time'], df['v(b5)'], label='b5')
    axs[idx_dict['bx']].plot(df['time'], df['v(b6)'], label='b6')
    axs[idx_dict['bx']].plot(df['time'], df['v(b7)'], label='b7')
    
    axs[idx_dict['bt']].plot(df['time'], df['v(bt)'], label='v(bt)', linestyle='solid')

    axs[idx_dict['signals']].plot(df['time'], df['v(slp)'], label='sleep')
    # axs[idx_dict['signals']].plot(df['time'], df['v(x1.ctl)'], label='x1.ctl')
    # axs[idx_dict['signals']].plot(df['time'], df['v(x2.ctl)'], label='x2.ctl')
    # axs[idx_dict['signals']].plot(df['time'], df['v(x3.ctl)'], label='x3.ctl')
    axs[idx_dict['signals']].plot(df['time'], df['v(x4.ctl)'], label='ctl')

    # Calculate and plot average control value between tstart and tstop
    tstart = 10000 # ns
    tstop = 15000 # ns

    avg_ctl = np.mean(df['v(x4.ctl)'][(df['time'] >= tstart) & (df['time'] <= tstop)])
    max_ctl = np.max(df['v(x4.ctl)'][(df['time'] >= tstart) & (df['time'] <= tstop)])
    min_ctl = np.min(df['v(x4.ctl)'][(df['time'] >= tstart) & (df['time'] <= tstop)])
    time_vals = df['time'][(df['time'] >= tstart) & (df['time'] <= tstop)]
    print(f'Max control value between {tstart} ns and {tstop} ns: {max_ctl:.3f} V')
    print(f'Avg control value between {tstart} ns and {tstop} ns: {avg_ctl:.3f} V')
    print(f'Min control value between {tstart} ns and {tstop} ns: {min_ctl:.3f} V')
    axs[idx_dict['signals']].plot(time_vals, [max_ctl]*len(time_vals), label=f'max {max_ctl:.3f} V', linestyle=':', color='black')
    axs[idx_dict['signals']].plot(time_vals, [avg_ctl]*len(time_vals), label=f'avg {avg_ctl:.3f} V', linestyle='--', color='black')
    axs[idx_dict['signals']].plot(time_vals, [min_ctl]*len(time_vals), label=f'min {min_ctl:.3f} V', linestyle='-.', color='black')


    axs[list(idx_dict.values())[-1]].set(xlabel='Time (ns)')

    for ax in axs:
      if ax == axs[idx_dict['i(vout4)']]:
        ax.set_ylabel('Current (uA)')
      else:
        ax.set_ylabel('Voltage (V)')
      ax.legend()
      ax.grid()

    fig.tight_layout()

    image_path = "./figures/tb_dac_plot_tran_" + name.split('_')[-1]
    fig.savefig(image_path + ".png")
    print("Figure saved to " + image_path + ".png")  

    # with open(f"{image_path}.fig.pickle", 'wb') as file:
    #     pickle.dump(fig, file)
    # print("Figure pickled to " + image_path + ".fig.pickle")

    plt.show()
