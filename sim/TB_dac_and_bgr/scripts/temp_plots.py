import sys
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yaml

if __name__ == "__main__":

    fend = ".out" # File extension for output files, can be changed to ".yaml", ".csv" or others if needed
    view = "Sch" # Sets schematic is default view if none is specified
    # view = "Lay" # Sets schematic is default view if none is specified

    args = sys.argv[1:]

    if len(args) == 0 or all(arg not in ["typical", "etc", "mc", "tord"] for arg in args):
        print("Wrong/No arguments provided. Please specify a combination of 'typical', 'etc', 'mc', and 'tord' to plot. View may be specified with 'Sch' or 'Lay' as arguments.")
        sys.exit(1)

    for arg in args:
        print(f"Argument {arg} of type: {type(arg)} recieved.")
        if arg in ["Sch", "Lay"]:
            view = arg
            print(f"View set to: {view}")
        elif arg =="sch":
            view = "Sch"
            print(f"View set to: {view}")
        elif arg =="lay":
            view = "Lay"
            print(f"View set to: {view}")

    files = []
    if "typical" in args:
        files.append(f"output_tran/tran_{view}GtKttTtVt")
    if "etc" in args:
        for corner in ["ff", "ss", "sf", "fs"]:
            for temperature in ["Tl", "Th"]:
                for voltage in ["Vl", "Vh"]:
                    files.append(f"output_tran/tran_{view}GtK{corner}{temperature}{voltage}")
    if "mc" in args:
        for n in range(1, 30):
            files.append(f"output_tran/tran_{view}GtKttmmTtVt_{n}")

    files_tord = []
    if "tord" in args:
        for corner in ["ff", "ss", "tt", "sf", "fs"]:
            for voltage in ["Vl", "Vt", "Vh"]:
                files_tord.append(f"output_tran/tran_{view}GtK{corner}Tt{voltage}")

    fig, axs = plt.subplot_mosaic([['Tl_error', 'Tt_error', 'Th_error'], 
                                   ['Tl_voltages', 'Tt_voltages', 'Th_voltages']],
                                    sharex=True, sharey=True, figsize=(20, 12))
    fig.suptitle('DAC and BGR Testbench')

    for file in files:
        fname = file + fend
        print(f"Processing file: {fname}")
        df = pd.read_csv(fname, sep='\s+')

        df['time'] = df['time'] * 1e9 # in ns

        # print(df.columns)
        # print(df.head())
        # print(df.tail())

        labelname = fname.split('/')[-1].replace(fend, '')

        if "Tl" in file:
            axs['Tl_error'].plot(df['time'], df['v(v1)']-df['v(v2)'], label='v(v1) - v(v2)', linestyle='-')
            axs['Tl_error'].plot(df['time'], df['v(v1a)']-df['v(v2a)'], label='v(v1a) - v(v2a)', linestyle='--')
            axs['Tl_error'].plot(df['time'], df['v(v1b)']-df['v(v2b)'], label='v(v1b) - v(v2b)', linestyle=':')

            # axs['Tl_voltages'].plot(df['time'], df['v(v1)'], label='v(v1) '+labelname, linestyle='solid')
            # axs['Tl_voltages'].plot(df['time'], df['v(v2)'], label='v(v2) '+labelname, linestyle='dashed')
            # axs['Tl_voltages'].plot(df['time'], df['v(v1a)'], label='v(v1a) '+labelname, linestyle='solid')
            # axs['Tl_voltages'].plot(df['time'], df['v(v2a)'], label='v(v2a) '+labelname, linestyle='dashed')
            # axs['Tl_voltages'].plot(df['time'], df['v(v1b)'], label='v(v1b) '+labelname, linestyle='solid')
            # axs['Tl_voltages'].plot(df['time'], df['v(v2b)'], label='v(v2b) '+labelname, linestyle='dashed')
            axs['Tl_voltages'].plot(df['time'], df['v(vout)'], label='v(vout) '+labelname, linestyle='solid')
            # axs['Tl_voltages'].plot(df['time'], df['v(vref)'], label='v(vref) '+labelname, linestyle='dashed')

        elif "Tt" in file:
            axs['Tt_error'].plot(df['time'], df['v(v1)']-df['v(v2)'], label='v(v1) - v(v2)', linestyle='-')
            axs['Tt_error'].plot(df['time'], df['v(v1a)']-df['v(v2a)'], label='v(v1a) - v(v2a)', linestyle='--')
            axs['Tt_error'].plot(df['time'], df['v(v1b)']-df['v(v2b)'], label='v(v1b) - v(v2b)', linestyle=':')

            # axs['Tt_voltages'].plot(df['time'], df['v(v1)'], label='v(v1) '+labelname, linestyle='solid') 
            # axs['Tt_voltages'].plot(df['time'], df['v(v2)'], label='v(v2) '+labelname, linestyle='dashed')
            # axs['Tt_voltages'].plot(df['time'], df['v(v1a)'], label='v(v1a) '+labelname, linestyle='solid')
            # axs['Tt_voltages'].plot(df['time'], df['v(v2a)'], label='v(v2a) '+labelname, linestyle='dashed')
            # axs['Tt_voltages'].plot(df['time'], df['v(v1b)'], label='v(v1b) '+labelname, linestyle='solid')
            # axs['Tt_voltages'].plot(df['time'], df['v(v2b)'], label='v(v2b) '+labelname, linestyle='dashed')
            axs['Tt_voltages'].plot(df['time'], df['v(vout)'], label='v(vout) '+labelname, linestyle='solid')
            # axs['Tt_voltages'].plot(df['time'], df['v(vref)'], label='v(vref) '+labelname, linestyle='dashed')

        elif "Th" in file:
            axs['Th_error'].plot(df['time'], df['v(v1)']-df['v(v2)'], label='v(v1) - v(v2)', linestyle='-')
            axs['Th_error'].plot(df['time'], df['v(v1a)']-df['v(v2a)'], label='v(v1a) - v(v2a)', linestyle='--')
            axs['Th_error'].plot(df['time'], df['v(v1b)']-df['v(v2b)'], label='v(v1b) - v(v2b)', linestyle=':')

            # axs['Th_voltages'].plot(df['time'], df['v(v1)'], label='v(v1) '+labelname, linestyle='solid') 
            # axs['Th_voltages'].plot(df['time'], df['v(v2)'], label='v(v2) '+labelname, linestyle='dashed')
            # axs['Th_voltages'].plot(df['time'], df['v(v1a)'], label='v(v1a) '+labelname, linestyle='solid')
            # axs['Th_voltages'].plot(df['time'], df['v(v2a)'], label='v(v2a) '+labelname, linestyle='dashed')
            # axs['Th_voltages'].plot(df['time'], df['v(v1b)'], label='v(v1b) '+labelname, linestyle='solid')
            # axs['Th_voltages'].plot(df['time'], df['v(v2b)'], label='v(v2b) '+labelname, linestyle='dashed')
            axs['Th_voltages'].plot(df['time'], df['v(vout)'], label='v(vout) '+labelname, linestyle='solid')
            # axs['Th_voltages'].plot(df['time'], df['v(vref)'], label='v(vref) '+labelname, linestyle='dashed')
        
        else:   
            print(f"Warning: File {fname} does not match any known temperature category (Tl, Tt, Th). Skipping.")
            continue
        
        # line_color = axs['top_left'].lines[-1].get_color()

    for ax in axs.values():
        ax.set_ylabel('Voltage (V)')
        ax.set(xlabel='Time (ns)')
        ax.legend()
        ax.grid()

    # fig.tight_layout()

    image_path = f"./figures/temperatures_plot_{view}_{'_'.join(args)}_tb_dac_and_bgr"
    fig.savefig(image_path + ".png")
    print("Figure saved to " + image_path + ".png")

    with open(f"{image_path}.fig.pickle", 'wb') as file:
        pickle.dump(fig, file)
    print("Figure pickled to " + image_path + ".fig.pickle")

    if "tord" in args:

        fig2, axs2 = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(18, 6))

        fig2.suptitle('DAC and BGR Testbench - Temperature Variation', fontsize=16)

        for file in files_tord:
            yamlfile = file + '.yaml'
            print(f"Processing file: {yamlfile}")

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

            # Sort the data by temperature for proper plotting
            temps_ref, v_ref = zip(*sorted(zip(temps_ref, v_ref)))
            temps_out, v_out = zip(*sorted(zip(temps_out, v_out)))

            if "Vl" in file:
                # axs2[0].plot(temps_ref, v_ref, label='vref ' + labelname, marker='o', linestyle='solid')
                axs2[0].plot(temps_out, v_out, label='vout ' + labelname, marker='o', linestyle='dashed')
            elif "Vt" in file:
                # axs2[1].plot(temps_ref, v_ref, label='vref ' + labelname, marker='o', linestyle='solid')
                axs2[1].plot(temps_out, v_out, label='vout ' + labelname, marker='o', linestyle='dashed')
            elif "Vh" in file:
                # axs2[2].plot(temps_ref, v_ref, label='vref ' + labelname, marker='o', linestyle='solid')
                axs2[2].plot(temps_out, v_out, label='vout ' + labelname, marker='o', linestyle='dashed')

        for ax, voltage in zip(axs2, ["Vl", "Vt", "Vh"]):
            ax.set_title(f'Output voltage across temperatures (VDD: {1.7 if voltage=="Vl" else 1.8 if voltage=="Vt" else 1.9} V)')
            ax.set_xlabel('Temperature (°C)')
            ax.set_ylabel('Voltage (V)')
            ax.legend()
            ax.grid()

        fig2.tight_layout()

        image_path2 = f"./figures/temp_vs_vout_{view}_{'_'.join(args)}_tb_dac_and_bgr"
        fig2.savefig(image_path2 + ".png")
        print("Figure saved to " + image_path2 + ".png")

        with open(f"{image_path2}.fig.pickle", 'wb') as pickledfile:
            pickle.dump(fig2, pickledfile)
        print("Figure pickled to " + image_path2 + ".fig.pickle")

    plt.show()


