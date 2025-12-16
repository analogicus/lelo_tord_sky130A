import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np


def plot_mc(names):

    fig_width = 3
    fig_height = 5
    font_size = 8
    title_fontsize = font_size
    label_fontsize = font_size
    legend_fontsize = font_size
    ticks_fontsize = font_size

    fig, axs = plt.subplots(1, 1, figsize=(fig_width, fig_height), sharex=True)

    for name in names:
        temps = []
        vouts = []
        times = []

        print(f'Plotting transient results from file: {name}.out')

        df = pd.read_csv(name + ".out", sep="\s+")
        
        print(df.columns)
        print(df.head())
        print(df.tail())

        df['time'] = df['time'] * 1e9 # in ns
        df['diff'] = df['v(v1)']-df['v(v2)']

        zero_crossings = df.index[(df['diff'].shift(1) * df['diff']) < 0]

        times.append(df.loc[zero_crossings[-2], 'time']) # second last (-2) instead of last (-1) value because that is when we shift DAC
        vouts.append(df.loc[zero_crossings[-2], 'v(vout)']) # second last (-2) instead of last (-1) value because that is when we shift DAC

        if "Tl" in name:
            temps.append(-40)
        elif "Tt" in name:
            temps.append(27)
        elif "Th" in name:
            temps.append(125)
    
        print(f'temps: {temps}')
        print(f'vouts: {vouts}')
        print(f'times: {times}')

        axs.plot(temps, vouts, label='vout', color='tab:blue', marker='o', linestyle= 'dashed') # in V

    axs.tick_params(axis='both', labelsize=ticks_fontsize)
    axs.grid()
    axs.set_ylabel('Voltage (V)', fontsize=label_fontsize)
    axs.set_xlabel('Temperature [$^\circ$C]', fontsize=label_fontsize)
        
    fig.tight_layout()
    fig.savefig(f'figures/vout_vs_temp', dpi=300, bbox_inches="tight")

    plt.show()


#
# Man function
#

def main():
    view = "Sch"
    # view = "Lay"

    names = list()
    data = dict()

    args = sys.argv[1:]

    if "mc" not in args:
        pass
    else:
        for n in range(1, 30):
            names.append(f"output_tran/tran_{view}GtKttmmTtVt_{n}")
        plot_mc(names)

    corners = list()
    voltages = list()

    if len(args) == 0:
        corners.append("tt")
        voltages.append("Vt")
    if "all" in args:
        corners = ["tt", "ff", "ss", "sf", "fs"]
        voltages = ["Vl", "Vt", "Vh"]
    elif "typical" in args:
        corners = ["tt"]
        voltages = ["Vt"]
    elif "etc" in args:
        corners = ["ff", "ss", "sf", "fs"]
        voltages = ["Vl", "Vh"]

    fig_width = 3
    fig_height = 5
    font_size = 8
    title_fontsize = font_size
    label_fontsize = font_size
    legend_fontsize = font_size
    ticks_fontsize = font_size

    fig, axs = plt.subplots(1, 1, figsize=(fig_width, fig_height), sharex=True)

    temperatures = [-40, 0, 27, 125]

    for corner in corners:

        for voltage in voltages:
    
            temps = []
            vouts = []
            times = []

            for temp in temperatures:

                name = f"output_tran/tran_SchGtK{corner}Tt{voltage}_{temp}"

                print(f'Plotting transient results from file: {name}.out')

                df = pd.read_csv(name + ".out", sep="\s+")
                
                print(df.columns)
                print(df.head())
                print(df.tail())

                df['time'] = df['time'] * 1e9 # in ns
                df['diff'] = df['v(v1)']-df['v(v2)']

                zero_crossings = df.index[(df['diff'].shift(1) * df['diff']) < 0]

                times.append(df.loc[zero_crossings[-2], 'time']) # second last (-2) instead of last (-1) value because that is when we shift DAC
                vouts.append(df.loc[zero_crossings[-2], 'v(vout)']) # second last (-2) instead of last (-1) value because that is when we shift DAC
                temps.append(temp)
        
            print(f'temps: {temps}')
            print(f'vouts: {vouts}')
            print(f'times: {times}')

            # data[f"{corner}_{voltage}"] = {[temps, vouts, times]}

            axs.plot(temps, vouts, label=f"{corner}, {voltage}", color='tab:blue', marker='o', linestyle= 'dashed') # in V

    axs.tick_params(axis='both', labelsize=ticks_fontsize)
    axs.grid()
    axs.set_ylabel('Voltage (V)', fontsize=label_fontsize)
    axs.set_xlabel('Temperature [$^\circ$C]', fontsize=label_fontsize)
        
    fig.tight_layout()
    fig.savefig(f'figures/vout_vs_temp', dpi=300, bbox_inches="tight")

    plt.show()
                
if __name__ == "__main__":
    main()

