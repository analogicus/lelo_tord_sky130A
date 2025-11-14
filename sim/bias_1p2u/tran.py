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

  R16 = 7535*16
  R8 = 7535*8
  R4 = 7535*4
  R2 = 7535*2
  Rtot = 7*R16
  vdiff = df['v(v1)'] - df['v(nbias)']

  if name == "output_tran/tran_SchGtKttTtVt":

    df['ib'] = (vdiff / Rtot) * 1e6 # in uA
    df['time'] = df['time'] * 1e9 # in ns

    print(df.columns)
    print(df.head())

    idxs = {'ibias': 0, 'vbias': 1, 'v1': 2, 'sleep': 3}  # Adjust this index to change position of plots

    fig, axs = plt.subplots(len(idxs), 1, sharex=True)
    fig.suptitle('Bias currents and voltages (target 1.2 uA)', fontsize=16)
    fig.set_size_inches(8, 8)

    axs[idxs['ibias']].plot(df['time'], (-df['i(vdd)']/2)*1e6, label='vdd current halfed') # in uA
    axs[idxs['ibias']].plot(df['time'], df['ibias']*1e6, label='bias current from table') # in uA
    axs[idxs['ibias']].plot(df['time'], df['ib'], linestyle='dashed', label='bias current calculated')
    axs[idxs['vbias']].plot(df['time'], df['v(nbias)'], label='nmos bias voltage')
    axs[idxs['vbias']].plot(df['time'], df['v(pbias)'], label='pmos bias voltage')
    axs[idxs['v1']].plot(df['time'], df['v(v1)'], label='v1')
    axs[idxs['sleep']].plot(df['time'], df['v(sleep)'], label='sleep signal')
    
    axs[idxs['ibias']].set(xlabel='Time (ns)', ylabel='Current (uA)')
    axs[idxs['ibias']].legend()
    axs[idxs['ibias']].grid()

    for ax in (axs[idxs['vbias']], axs[idxs['v1']], axs[idxs['sleep']]):
      ax.set(xlabel='Time (ns)', ylabel='Voltage (V)')
      ax.legend()
      ax.grid()

    fig.tight_layout()

    image_path = "./figures/" + name.split('/')[-1] + ".png"
    plt.savefig(image_path)
    print("Figure saved to " + image_path)

    plt.show()


