import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yaml
import sys

args = sys.argv[1:]

names = []
if len(args) == 0:
    names.append("output_tran/tran_SchGtKttTtVt")
if "all" in args:
    for corner in ["tt", "ff", "ss", "sf", "fs"]:
        for temperature in ["Tl", "Tt", "Th"]:
            for voltage in ["Vl", "Vt", "Vh"]:
                names.append(f"output_tran/tran_SchGtK{corner}{temperature}{voltage}")

elif "typical" in args:
    names.append("output_tran/tran_SchGtKttTtVt")
elif "etc" in args:
    for corner in ["ff", "ss", "sf", "fs"]:
        for temperature in ["Tl", "Th"]:
            for voltage in ["Vl", "Vh"]:
                names.append(f"output_tran/tran_SchGtK{corner}{temperature}{voltage}")
elif "mc" in args:
    for n in range(1, 30):
        names.append(f"output_tran/tran_SchGtKttmmTtVt_{n}")
elif "temp" in args:
    for temperature in ["Tl", "Tt", "Th"]:
        names.append(f"output_tran/tran_SchGtKtt{temperature}Vt")

for name in names:
    
    print(f"Plotting transient results from file: {name}.out")

    df = pd.read_csv(name + ".out", sep="\s+")
    
    df['time'] = df['time'] * 1e9 # in ns
    
    print(df.columns)
    print(df.head())
    print(df.tail())

    fig, axs = plt.subplots(4, 1, figsize=(4, 6), sharex=True)
    axs[0].set_title('Temperature Sensing Transient Analysis')

    axs[0].plot(df['time'], df['i(v.xdut.v1)']*1e6, label='iout', color='tab:blue') # in uA
    
    axs[1].plot(df['time'], df['v(v1)']-df['v(v2)'], label='v(v1) - v(v2)', linestyle='-')
    axs[1].plot(df['time'], df['v(v1a)']-df['v(v2a)'], label='v(v1a) - v(v2a)', linestyle='--')
    axs[1].plot(df['time'], df['v(v1b)']-df['v(v2b)'], label='v(v1b) - v(v2b)', linestyle=':')

    axs[2].plot(df['time'], df['v(v1)'], label='v1')
    axs[2].plot(df['time'], df['v(v1a)'], label='v1a')
    axs[2].plot(df['time'], df['v(v1b)'], label='v1b')
    axs[2].plot(df['time'], df['v(v2)'], label='v2')
    axs[2].plot(df['time'], df['v(v2a)'], label='v2a')
    axs[2].plot(df['time'], df['v(v2b)'], label='v2b')
    axs[2].plot(df['time'], df['v(v2c)'], label='v2c')

    axs[3].plot(df['time'], df['v(bt)'], label='v(bt)', linestyle='solid')
    axs[3].plot(df['time'], df['v(x1.ctl)'], label='ctl')
    axs[3].plot(df['time'], df['v(slp)'], label='slp')

    axs[0].set_ylabel('Output Current (uA)')
    axs[1].set_ylabel('Error Voltages (V)')
    axs[2].set_ylabel('Diode Voltages (V)')
    axs[3].set_ylabel('Control Voltages (V)')

    axs[1].legend(fontsize=8)
    axs[2].legend(fontsize=8)
    axs[3].legend(fontsize=8)

    for ax in axs:
        ax.grid()
    axs[-1].set_xlabel('Time (ns)')

    fig.tight_layout()

    plt.show()