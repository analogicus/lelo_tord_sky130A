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

    if len(args) == 0 or all(arg not in ["typical", "etc", "mc", "tord", "custom"] for arg in args):
        print("Wrong/No arguments provided. Please specify a combination of 'typical', 'etc', 'mc', 'tord', and 'custom' to plot. View may be specified with 'Sch' or 'Lay' as arguments.")
        sys.exit(1)

    for arg in args:
        print(f"Argument {arg} of type: {type(arg)} recieved.")
        if arg in ["Sch", "Lay"]:
            view = arg
            print(f"View set to: {view}")
            args.remove(arg)
        elif arg =="sch":
            view = "Sch"
            print(f"View set to: {view}")
            args.remove(arg)
        elif arg =="lay":
            view = "Lay"
            print(f"View set to: {view}")
            args.remove(arg)

    files = []
    if "typical" in args:
        files.append(f"output_tran/tran_{view}GtKttTtVt")
        files.append(f"output_tran/tran_{view}GtKttTtVl")
        files.append(f"output_tran/tran_{view}GtKttTtVh")
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
                for temperature in ["Tl", "Tt", "Th"]:
                    files.append(f"output_tran/tran_{view}GtK{corner}{temperature}{voltage}")

    if "custom" in args:
        for corner in ["ss", "ff", "sf", "fs"]:
            for temperature in ["Th", "Tl"]:
                for voltage in ["Vl","Vh", "Vt"]:
                    files.append(f"output_tran/tran_{view}GtK{corner}{temperature}{voltage}")

    fig, axs = plt.subplot_mosaic([['Vl_error', 'Vt_error', 'Vh_error']], sharex=True, sharey=True, figsize=(20, 6))
    fig.suptitle('DAC and BGR Testbench Transient Errors')

    fig2, axs2 = plt.subplot_mosaic([['Vl_voltages', 'Vt_voltages', 'Vh_voltages']], sharex=True, sharey=True, figsize=(20, 6))
    fig2.suptitle('DAC and BGR Testbench Transient Voltages')

    for file in files:

        fname = file + fend
        print(f"Processing file: {fname}")
        df = pd.read_csv(fname, sep='\s+')

        df['time'] = df['time'] * 1e9 # in ns

        # print(df.columns)
        # print(df.head())
        # print(df.tail())

        labelname = fname.split('/')[-1].replace(fend, '')

        if "Vl" in file:
            axs['Vl_error'].plot(df['time'], df['v(v1)']-df['v(v2)'], label='v(v1) - v(v2)'+labelname, linestyle='-')
            axs['Vl_error'].plot(df['time'], df['v(v1a)']-df['v(v2a)'], label='v(v1a) - v(v2a) '+labelname, linestyle='--')
            axs['Vl_error'].plot(df['time'], df['v(v1b)']-df['v(v2b)'], label='v(v1b) - v(v2b) '+labelname, linestyle=':')

            # axs['Vl_voltages'].plot(df['time'], df['v(v1)'], label='v(v1) '+labelname, linestyle='solid')
            # axs['Vl_voltages'].plot(df['time'], df['v(v2)'], label='v(v2) '+labelname, linestyle='dashed')
            # axs['Vl_voltages'].plot(df['time'], df['v(v1a)'], label='v(v1a) '+labelname, linestyle='solid')
            # axs['Vl_voltages'].plot(df['time'], df['v(v2a)'], label='v(v2a) '+labelname, linestyle='dashed')
            # axs['Vl_voltages'].plot(df['time'], df['v(v1b)'], label='v(v1b) '+labelname, linestyle='solid')
            # axs['Vl_voltages'].plot(df['time'], df['v(v2b)'], label='v(v2b) '+labelname, linestyle='dashed')
            axs2['Vl_voltages'].plot(df['time'], df['v(vout)'], label=labelname, linestyle='solid')
            # axs['Vl_voltages'].plot(df['time'], df['v(vref)'], label='v(vref) '+labelname, linestyle='dashed')

        elif "Vt" in file:
            axs['Vt_error'].plot(df['time'], df['v(v1)']-df['v(v2)'], label='v(v1) - v(v2) '+labelname, linestyle='-')
            axs['Vt_error'].plot(df['time'], df['v(v1a)']-df['v(v2a)'], label='v(v1a) - v(v2a) '+labelname, linestyle='--')
            axs['Vt_error'].plot(df['time'], df['v(v1b)']-df['v(v2b)'], label='v(v1b) - v(v2b), '+labelname, linestyle=':')

            # axs['Vt_voltages'].plot(df['time'], df['v(v1)'], label='v(v1) '+labelname, linestyle='solid') 
            # axs['Vt_voltages'].plot(df['time'], df['v(v2)'], label='v(v2) '+labelname, linestyle='dashed')
            # axs['Vt_voltages'].plot(df['time'], df['v(v1a)'], label='v(v1a) '+labelname, linestyle='solid')
            # axs['Vt_voltages'].plot(df['time'], df['v(v2a)'], label='v(v2a) '+labelname, linestyle='dashed')
            # axs['Vt_voltages'].plot(df['time'], df['v(v1b)'], label='v(v1b) '+labelname, linestyle='solid')
            # axs['Vt_voltages'].plot(df['time'], df['v(v2b)'], label='v(v2b) '+labelname, linestyle='dashed')
            axs2['Vt_voltages'].plot(df['time'], df['v(vout)'], label=labelname, linestyle='solid')
            # axs['Vt_voltages'].plot(df['time'], df['v(vref)'], label='v(vref) '+labelname, linestyle='dashed')

        elif "Vh" in file:
            axs['Vh_error'].plot(df['time'], df['v(v1)']-df['v(v2)'], label='v(v1) - v(v2) '+labelname, linestyle='-')
            axs['Vh_error'].plot(df['time'], df['v(v1a)']-df['v(v2a)'], label='v(v1a) - v(v2a) '+labelname, linestyle='--')
            axs['Vh_error'].plot(df['time'], df['v(v1b)']-df['v(v2b)'], label='v(v1b) - v(v2b) '+labelname, linestyle=':')

            # axs['Vh_voltages'].plot(df['time'], df['v(v1)'], label='v(v1) '+labelname, linestyle='solid') 
            # axs['Vh_voltages'].plot(df['time'], df['v(v2)'], label='v(v2) '+labelname, linestyle='dashed')
            # axs['Vh_voltages'].plot(df['time'], df['v(v1a)'], label='v(v1a) '+labelname, linestyle='solid')
            # axs['Vh_voltages'].plot(df['time'], df['v(v2a)'], label='v(v2a) '+labelname, linestyle='dashed')
            # axs['Vh_voltages'].plot(df['time'], df['v(v1b)'], label='v(v1b) '+labelname, linestyle='solid')
            # axs['Vh_voltages'].plot(df['time'], df['v(v2b)'], label='v(v2b) '+labelname, linestyle='dashed')
            axs2['Vh_voltages'].plot(df['time'], df['v(vout)'], label=labelname, linestyle='solid')
            # axs['Vh_voltages'].plot(df['time'], df['v(vref)'], label='v(vref) '+labelname, linestyle='dashed')
        
        else:   
            print(f"Warning: File {fname} does not match any known temperature category (Tl, Tt, Th). Skipping.")
            continue

         # times given in nano seconds (ns)
        if "Vl" in file:
            for tstart in [2400, 4400, 6400, 8400, 10400, 12400, 14400, 16400]:
                axs['Vl_error'].axvline(x=tstart, color='gray', linestyle='--')
                axs2['Vl_voltages'].axvline(x=tstart, color='gray', linestyle='--')
        elif "Vt" in file:
            for tstart in [2400, 4400, 6400, 8400, 10400, 12400, 14400, 16400]:
                axs['Vt_error'].axvline(x=tstart, color='gray', linestyle='--')
                axs2['Vt_voltages'].axvline(x=tstart, color='gray', linestyle='--')
        elif "Vh" in file:
            for tstart in [2400, 4400, 6400, 8400, 10400, 12400, 14400, 16400]:
                axs['Vh_error'].axvline(x=tstart, color='gray', linestyle='--')
                axs2['Vh_voltages'].axvline(x=tstart, color='gray', linestyle='--')
            
        if "Vl" in file:
            Vl_error_handle = axs['Vl_error'].lines[-1]
            Vl_voltages_handle = axs2['Vl_voltages'].lines[-1]
        if "Vt" in file:
            Vt_error_handle = axs['Vt_error'].lines[-1]
            Vt_voltages_handle = axs2['Vt_voltages'].lines[-1]
        if "Vh" in file:
            Vh_error_handle = axs['Vh_error'].lines[-1]
            Vh_voltages_handle = axs2['Vh_voltages'].lines[-1]

    if files == []:
        print("No valid files to process for transient errors and voltages. Exiting.")
    else:
        Vl_error_handle.set_label(f'Measurement times')
        Vl_voltages_handle.set_label(f'Measurement times')

        Vt_error_handle.set_label(f'Measurement times')          
        Vt_voltages_handle.set_label(f'Measurement times')

        Vh_error_handle.set_label(f'Measurement times')
        Vh_voltages_handle.set_label(f'Measurement times')

    # line_color = axs['top_left'].lines[-1].get_color()

    for ax, voltage in zip(axs, ["Vl", "Vt", "Vh"]):
        axs[ax].set_title(f'Internal Differences in voltage across time (VDD: {1.7 if voltage=="Vl" else 1.8 if voltage=="Vt" else 1.9} V)')
        axs[ax].set_xlabel('Time (ns)')
        axs[ax].set_ylabel('Internal Branch Differences (V)')
        axs[ax].legend(loc='lower center', bbox_to_anchor=(0.5, 1.1), fancybox=True, shadow=True, ncol=2)
        axs[ax].grid()

    for ax, voltage in zip(axs2, ["Vl", "Vt", "Vh"]):
        axs2[ax].set_title(f'Output voltage across time (VDD: {1.7 if voltage=="Vl" else 1.8 if voltage=="Vt" else 1.9} V)')
        axs2[ax].set_xlabel('Time (ns)')
        axs2[ax].set_ylabel('Output Voltage (V)')
        axs2[ax].legend(loc='lower center', bbox_to_anchor=(0.5, 1.1), fancybox=True, shadow=True, ncol=2)
        axs2[ax].grid()

    fig.tight_layout()
    fig2.tight_layout()

    image_path = f"./figures/plot_transient_errors_{view}_{'_'.join(args)}_tb_dac_and_bgr"
    fig.savefig(image_path + ".png")
    print("Figure saved to " + image_path + ".png")

    image_path2 = f"./figures/plot_transient_voltages_{view}_{'_'.join(args)}_tb_dac_and_bgr"
    fig2.savefig(image_path2 + ".png")
    print("Figure saved to " + image_path2 + ".png")

    # with open(f"{image_path}.fig.pickle", 'wb') as file:
    #     pickle.dump(fig, file)
    # print("Figure pickled to " + image_path + ".fig.pickle")

    if "tord" in args:

        fig3, axs3 = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(18, 6))

        fig3.suptitle('DAC and BGR Testbench - Temperature Variation', fontsize=16)

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
                axs3[0].plot(temps_out, v_out, label=labelname, marker='o', linestyle='dashed')
            elif "Vt" in file:
                # axs2[1].plot(temps_ref, v_ref, label='vref ' + labelname, marker='o', linestyle='solid')
                axs3[1].plot(temps_out, v_out, label=labelname, marker='o', linestyle='dashed')
            elif "Vh" in file:
                # axs2[2].plot(temps_ref, v_ref, label='vref ' + labelname, marker='o', linestyle='solid')
                axs3[2].plot(temps_out, v_out, label=labelname, marker='o', linestyle='dashed')

        for ax, voltage in zip(axs3, ["Vl", "Vt", "Vh"]):
            ax.set_title(f'Output voltage across temperatures (VDD: {1.7 if voltage=="Vl" else 1.8 if voltage=="Vt" else 1.9} V)')
            ax.set_xlabel('Temperature (°C)')
            ax.set_ylabel('Output Voltage (V)')
            ax.legend()
            ax.grid()

        fig3.tight_layout()

        image_path3 = f"./figures/temp_vs_vout_{view}_tord_tb_dac_and_bgr"
        fig3.savefig(image_path3 + ".png")
        print("Figure saved to " + image_path3 + ".png")

        # with open(f"{image_path3}.fig.pickle", 'wb') as pickledfile:
        #     pickle.dump(fig3, pickledfile)
        # print("Figure pickled to " + image_path3 + ".fig.pickle")

    plt.show()


