import pandas as pd
import matplotlib.pyplot as plt
import sys

# 
# Function for plotting transients
#
    
def plot_transient(name):
    print(f'Plotting transient results from file: {name}.out')

    df = pd.read_csv(name + ".out", sep="\s+")
    
    print(df.columns)
    print(df.head())
    print(df.tail())

    df['time'] = df['time'] * 1e9 # in ns

    fig_width = 3
    fig_height = 5
    font_size = 8
    title_fontsize = font_size
    label_fontsize = font_size
    legend_fontsize = font_size
    ticks_fontsize = font_size

    fig, axs = plt.subplots(4, 1, figsize=(fig_width, fig_height), sharex=True)
    axs[0].set_title(name.split("/")[-1], fontweight='bold', fontsize=title_fontsize)
    
    ax_iout = axs[0].twinx()
    ax_iout.plot(df['time'], df['i(v.xdut.v1)']*1e6, label='iout', color='tab:orange') # in uA

    axs[0].plot(df['time'], df['v(vout)'], label='vout', color='tab:blue') # in V

    axs[1].plot(df['time'], df['v(v1)']-df['v(v2)'], label='v(v1) - v(v2)', linestyle='solid')
    axs[1].plot(df['time'], df['v(v1a)']-df['v(v2a)'], label='v(v1a) - v(v2a)', linestyle='dashed')
    axs[1].plot(df['time'], df['v(v1b)']-df['v(v2b)'], label='v(v1b) - v(v2b)', linestyle='dotted')

    axs[2].plot(df['time'], df['v(v1)'], label='v1')
    axs[2].plot(df['time'], df['v(v1a)'], label='v1a')
    # axs[2].plot(df['time'], df['v(v1b)'], label='v1b')
    axs[2].plot(df['time'], df['v(v2)'], label='v2')
    axs[2].plot(df['time'], df['v(v2a)'], label='v2a')
    # axs[2].plot(df['time'], df['v(v2b)'], label='v2b')
    axs[2].plot(df['time'], df['v(v2c)'], label='v2c')

    axs[3].plot(df['time'], df['v(bt)'], label='v(bt)', linestyle='solid')
    axs[3].plot(df['time'], df['v(x1.ctl)'], label='ctl')
    axs[3].plot(df['time'], df['v(slp)'], label='slp')

    for ax in axs:
        ax.set_ylabel('Voltage (V)', fontsize=label_fontsize)
        ax.tick_params(axis='both', labelsize=ticks_fontsize)
        ax.grid()

    axs[0].legend(loc='upper left', fontsize=legend_fontsize)
    axs[1].legend(loc='upper left', fontsize=legend_fontsize)
    axs[2].legend(loc='upper left', fontsize=legend_fontsize)
    axs[3].legend(loc='upper left', fontsize=legend_fontsize)
    
    ax_iout.set_ylabel('Current (uA)', fontsize=label_fontsize)
    ax_iout.legend(loc='lower right', fontsize=legend_fontsize)
    ax_iout.tick_params(axis='both', labelsize=ticks_fontsize)
  
    axs[-1].set_xlabel('Time (ns)', fontsize=label_fontsize)
    
    fig.tight_layout()
    fig.savefig(f'figures/{name.split("/")[-1]}', dpi=300, bbox_inches="tight")

    return fig

#
# Parsing Arguments
#

def main(args, view):
    names = []

    if len(args) == 0:
        names.append("output_tran/tran_SchGtKttTtVt")
    if "all" in args:
        for corner in ["tt", "ff", "ss", "sf", "fs"]:
            for temperature in ["Tl", "Tt", "Th"]:
                for voltage in ["Vl", "Vt", "Vh"]:
                    names.append(f"output_tran/tran_{view}GtK{corner}{temperature}{voltage}")
    elif "typical" in args:
        names.append("output_tran/tran_SchGtKttTtVt")
    elif "etc" in args:
        for corner in ["ff", "ss", "sf", "fs"]:
            for temperature in ["Tl", "Th"]:
                for voltage in ["Vl", "Vh"]:
                    names.append(f"output_tran/tran_{view}GtK{corner}{temperature}{voltage}")
    elif "mc" in args:
        for n in range(1, 30):
            names.append(f"output_tran/tran_{view}GtKttmmTtVt_{n}")
    elif "temp" in args:
        for temperature in ["Tl", "Tt", "Th"]:
            names.append(f"output_tran/tran_{view}GtKtt{temperature}Vt")
    elif "custom" in args:
        for corner in ["tt"]:
            for temperature in ["Tt"]:
                for voltage in ["Vt"]:
                    for custom in [-40, 0, 27, 125]:
                        names.append(f"output_tran/tran_{view}GtK{corner}{temperature}{voltage}_{custom}")

    for name in names:
        fig = plot_transient(name)
        plt.show()

#
# Running script
#
                
if __name__ == "__main__":

    args = sys.argv[1:]

    view = "Sch"
    # view = "Lay"

    main(args, view)

