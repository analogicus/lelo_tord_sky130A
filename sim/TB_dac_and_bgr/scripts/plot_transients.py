import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yaml
import pickle


def plot_tran(name):
    fname = name + ".out"
    df = pd.read_csv(fname, sep='\s+')

    df['time'] = df['time'] * 1e9 # in ns

    print(df.columns)
    print(df.head())

    # idx_dict = {'diff': 0, 'diode': 1, 'control': 2, 'bits': 3, 'sleep': 4, 'switches': 5, 'sources': 6}  # Adjust this index if the position of 'sleep' plot changes
    idx_dict = {'diff': 0, 'diode': 1, 'control': 2, 'bits': 3, 'sleep': 4, 'sources': 5}  # Adjusted index dictionary without 'switches'

    fig,axs = plt.subplots(len(idx_dict), 1, sharex=True)
    fig.suptitle('DAC currents and voltages')
    fig.set_size_inches(8, 12)

    axs[idx_dict['diff']].plot(df['time'], df['v(v1)']-df['v(v2)'], label='v(v1) - v(v2)', linestyle='-')
    axs[idx_dict['diff']].plot(df['time'], df['v(v1a)']-df['v(v2a)'], label='v(v1a) - v(v2a)', linestyle='--')
    axs[idx_dict['diff']].plot(df['time'], df['v(v1b)']-df['v(v2b)'], label='v(v1b) - v(v2b)', linestyle=':')

    axs[idx_dict['diode']].plot(df['time'], df['v(v1)'], label='v1')
    axs[idx_dict['diode']].plot(df['time'], df['v(v1a)'], label='v1a')
    axs[idx_dict['diode']].plot(df['time'], df['v(v1b)'], label='v1b')
    axs[idx_dict['diode']].plot(df['time'], df['v(v2)'], label='v2')
    axs[idx_dict['diode']].plot(df['time'], df['v(v2a)'], label='v2a')
    axs[idx_dict['diode']].plot(df['time'], df['v(v2b)'], label='v2b')
    axs[idx_dict['diode']].plot(df['time'], df['v(v2c)'], label='v2c')

    # Calculate and plot average control value between tstart and tstop
    tstart = 6000 # ns
    tstop = 14000 # ns

    axs[idx_dict['control']].plot(df['time'], df['v(x1.ctl)'], label='x1.ctl')
    avg_ctl = np.mean(df['v(x1.ctl)'][(df['time'] >= tstart) & (df['time'] <= tstop)])
    max_ctl = np.max(df['v(x1.ctl)'][(df['time'] >= tstart) & (df['time'] <= tstop)])
    min_ctl = np.min(df['v(x1.ctl)'][(df['time'] >= tstart) & (df['time'] <= tstop)])
    time_vals = df['time'][(df['time'] >= tstart) & (df['time'] <= tstop)]
    print(f'Max control value between 6000 ns and 14000 ns: {max_ctl:.3f} V')
    print(f'Avg control value between 6000 ns and 14000 ns: {avg_ctl:.3f} V')
    print(f'Min control value between 6000 ns and 14000 ns: {min_ctl:.3f} V')
    axs[idx_dict['control']].plot(time_vals, [max_ctl]*len(time_vals), label=f'max ctl val {max_ctl:.3f} V', linestyle=':', color='black')
    axs[idx_dict['control']].plot(time_vals, [avg_ctl]*len(time_vals), label=f'avg ctl val {avg_ctl:.3f} V', linestyle='--', color='black')
    axs[idx_dict['control']].plot(time_vals, [min_ctl]*len(time_vals), label=f'min ctl val {min_ctl:.3f} V', linestyle='-.', color='black')

    axs[idx_dict['bits']].plot(df['time'], df['v(b0)'], label='bit 0')
    axs[idx_dict['bits']].plot(df['time'], df['v(b1)'], label='bit 1')
    axs[idx_dict['bits']].plot(df['time'], df['v(b2)'], label='bit 2')
    axs[idx_dict['bits']].plot(df['time'], df['v(b3)'], label='bit 3')
    axs[idx_dict['bits']].plot(df['time'], df['v(b4)'], label='bit 4')
    axs[idx_dict['bits']].plot(df['time'], df['v(b5)'], label='bit 5')
    axs[idx_dict['bits']].plot(df['time'], df['v(b6)'], label='bit 6')
    axs[idx_dict['bits']].plot(df['time'], df['v(b7)'], label='bit 7')

    axs[idx_dict['sleep']].plot(df['time'], df['v(slp)'], label='slp')
    axs[idx_dict['sleep']].plot(df['time'], df['v(bt)'], label='v(bt)', linestyle='solid')

    # axs[idx_dict['switches']].plot(df['time'], df['v(swbrn1)'], label='SWBRN1')
    # axs[idx_dict['switches']].plot(df['time'], df['v(swbrn2)'], label='SWBRN2')
    # axs[idx_dict['switches']].plot(df['time'], df['v(swbrn3)'], label='SWBRN3')
    # axs[idx_dict['switches']].plot(df['time'], df['v(swbgr1)'], label='SWBGR1')
    # axs[idx_dict['switches']].plot(df['time'], df['v(swbgr2)'], label='SWBGR2')
    # axs[idx_dict['switches']].plot(df['time'], df['v(swcap1)'], label='SWCAP1')
    # axs[idx_dict['switches']].plot(df['time'], df['v(swcap2)'], label='SWCAP2')
    # axs[idx_dict['switches']].plot(df['time'], df['v(swcap3)'], label='SWCAP3')
    # axs[idx_dict['switches']].plot(df['time'], df['v(swdrn1)'], label='SWDRN1')
    # axs[idx_dict['switches']].plot(df['time'], df['v(swdrn2)'], label='SWDRN2')
    # axs[idx_dict['switches']].plot(df['time'], df['v(swdrn3)'], label='SWDRN3')

    axs[idx_dict['sources']].plot(df['time'], df['i(v.xdut.v1)']*1e6, label='iout', color='tab:blue') # in uA
    
    for tstart in [2400, 4400, 6400, 8400, 10400, 12400, 14400, 16400]: # times given in nano seconds (ns)
        axs[idx_dict['sources']].axvline(x=tstart, color='gray', linestyle='--')
                
    handle = axs[idx_dict['sources']].lines[-1]
    handle.set_label(f'Measurement times')
  

    ax2 = axs[idx_dict['sources']].twinx()
    ax2.plot(df['time'], df['v(vref)'], label='vref', linestyle='solid', color='tab:orange')
    ax2.plot(df['time'], df['v(vout)'], label='vout', linestyle='dashed', color='tab:green')
    ax2.set_ylabel('Voltage (V)')

    axs[list(idx_dict.values())[-1]].set(xlabel='Time (ns)')

    for ax in axs:
        if ax == axs[idx_dict['sources']]:
            ax.set_ylabel('Current (uA)')
            ax.legend(loc='upper left')
            ax2.legend(loc='upper right')
            ax2.grid(linestyle='dashed')
        elif ax == axs[idx_dict['diff']]:
            ax.set_ylabel('Error (V)')
            ax.legend()
        else:
            ax.set_ylabel('Voltage (V)')
            ax.legend()
        ax.grid()

    fig.tight_layout()

    image_path = "./figures/" + name.split('/')[-1] + ".png"
    plt.savefig(image_path)
    print("Figure saved to " + image_path)


    fig2, axs2 = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(18, 6))

    fig2.suptitle('DAC and BGR Testbench - Temperature Variation', fontsize=16)

    yamlfile = name + '.yaml'
    # print(f"Processing file: {yamlfile}")

    labelname = yamlfile.split('/')[-1].replace('.yaml', '')
    # print(f"Label name: {labelname}")

    temps_ref = []
    v_ref = []
    temps_out = []
    v_out = []

    with open(yamlfile, "r") as yfile:
        data = yaml.load(yfile, Loader=yaml.FullLoader)

        # Iterate through all keys in the YAML data
        for key, value in data.items():
            if key.count("_") == 1 and key.split("_")[-1] != '':
                if key.startswith("vref"):
                    temp_ref = int(key.split("_")[-1])
                    temps_ref.append(temp_ref)
                    v_ref.append(value)
                elif key.startswith("vout"):
                    temp_out = int(key.split("_")[-1])
                    temps_out.append(temp_out)
                    v_out.append(value)
            else:
                continue
                # print(f"Skipping key: {key} as it does not end with a digit of ''.\n key: {key}, value: {value}")

        # print("Temps ref:", temps_ref)
        # print("V ref:", v_ref)
        # print("Temps out:", temps_out)
        # print("V out:", v_out)

    # Sort the data by temperature for proper plotting
    temps_ref, v_ref = zip(*sorted(zip(temps_ref, v_ref)))
    temps_out, v_out = zip(*sorted(zip(temps_out, v_out)))

    if "Vl" in name:
        # axs2[0].plot(temps_ref, v_ref, label='vref ' + labelname, marker='o', linestyle='solid')
        axs2[0].plot(temps_out, v_out, label='vout ' + labelname, marker='o', linestyle='dashed')
    elif "Vt" in name:
        # axs2[1].plot(temps_ref, v_ref, label='vref ' + labelname, marker='o', linestyle='solid')
        axs2[1].plot(temps_out, v_out, label='vout ' + labelname, marker='o', linestyle='dashed')
    elif "Vh" in name:
        # axs2[2].plot(temps_ref, v_ref, label='vref ' + labelname, marker='o', linestyle='solid')
        axs2[2].plot(temps_out, v_out, label='vout ' + labelname, marker='o', linestyle='dashed')

    for ax, voltage in zip(axs2, ["Vl", "Vt", "Vh"]):
        ax.set_title(f'Output voltage across temperatures (VDD: {1.7 if voltage=="Vl" else 1.8 if voltage=="Vt" else 1.9} V)')
        ax.set_xlabel('Temperature (°C)')
        ax.set_ylabel('Voltage (V)')
        ax.legend()
        ax.grid()

    fig2.tight_layout()

    # image_path2 = f"./figures/temp_vs_vout_{name}_tb_dac_and_bgr"
    # fig2.savefig(image_path2 + ".png")
    # print("Figure saved to " + image_path2 + ".png")

    # with open(f"{image_path2}.fig.pickle", 'wb') as pickledfile:
    #     pickle.dump(fig2, pickledfile)
    # print("Figure pickled to " + image_path2 + ".fig.pickle")

    plt.show()


