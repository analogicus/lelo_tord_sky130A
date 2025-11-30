import sys
import yaml
import matplotlib.pyplot as plt
import pickle


if __name__ == "__main__":

    fend = ".out" # File extension for output files, can be changed to ".yaml", ".csv" or others if needed
    view = "Sch" # Sets schematic is default view if none is specified
    # view = "Lay" # Sets schematic is default view if none is specified

    target = 1.0

    args = sys.argv[1:]        

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
    for corner in ["ff", "ss", "tt", "sf", "fs"]:
        for temperature in ["Tt"]:
            for voltage in ["Vl", "Vt", "Vh"]:
                files.append(f"output_tran/tran_{view}GtK{corner}{temperature}{voltage}")
    
    fig, axs = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(18, 6))

    fig.suptitle('DAC and BGR Testbench - Temperature Variation', fontsize=16)

    # ax0 = axs[0].twinx()
    # ax1 = axs[1].twinx()
    # ax2 = axs[2].twinx()

    for file in files:

        yamlfile = file + '.yaml'
        print(f"Processing file: {yamlfile}")

        labelname = yamlfile.split('/')[-1].replace('.yaml', '')
        # print(f"Label name: {labelname}")

        # temps_ref = []
        # v_ref = []
        # bits_ref = []
        temps_out = []
        # v_out = []
        # bits_out = []

        vout_out_neg50 = []
        vout_out_neg25 = []
        vout_out_0 = []
        vout_out_25 = []
        vout_out_50 = []
        vout_out_75 = []
        vout_out_100 = []
        vout_out_125 = []

        bit_out_neg50 = []
        bit_out_neg25 = []
        bit_out_0 = []
        bit_out_25 = []
        bit_out_50 = []
        bit_out_75 = []
        bit_out_100 = []
        bit_out_125 = []

        with open(yamlfile, "r") as yfile:
            data = yaml.load(yfile, Loader=yaml.FullLoader)

            # Iterate through all keys in the YAML data
            for key, value in data.items():
                # print(key, value)
                if key.count("_") == 2:
                    if key.startswith("vout"):
                        bit_out = key.split("_")[-1]
                        temp_out = int(key.split("_")[-2])

                        if temp_out == -50:
                            vout_out_neg50.append(value)
                            bit_out_neg50.append(bit_out)
                        elif temp_out == -25:
                            vout_out_neg25.append(value)
                            bit_out_neg25.append(bit_out)   
                        elif temp_out == 0:
                            vout_out_0.append(value)
                            bit_out_0.append(bit_out)
                        elif temp_out == 25:    
                            vout_out_25.append(value)
                            bit_out_25.append(bit_out)
                        elif temp_out == 50:
                            vout_out_50.append(value)
                            bit_out_50.append(bit_out)
                        elif temp_out == 75:
                            vout_out_75.append(value)
                            bit_out_75.append(bit_out)
                        elif temp_out == 100:
                            vout_out_100.append(value)
                            bit_out_100.append(bit_out)
                        elif temp_out == 125:
                            vout_out_125.append(value)
                            bit_out_125.append(bit_out)
                        
        temps_out = [-50, -25, 0, 25, 50, 75, 100, 125]
        v_out = []

        for lst in [vout_out_neg50, vout_out_neg25, vout_out_0, vout_out_25, vout_out_50, vout_out_75, vout_out_100, vout_out_125]:
            closest_value = lst[0]
            for i in range(len(lst)):
                print(f"i: {i}, Value: {lst[i]}, Target: {target}, Difference: {abs(lst[i] - target)}")
                if abs(lst[i] - target) < abs(closest_value - target):
                    closest_value = lst[i]
            v_out.append(closest_value)            
                        
        if "Vl" in file:
            # axs2[0].plot(temps_ref, v_ref, label='vref ' + labelname, marker='o', linestyle='solid')
            axs[0].plot(temps_out, v_out, label=f'vout {labelname}', marker='o', linestyle='dashed')
            line_color = axs[0].lines[-1].get_color()
            avg_vout = sum(v_out) / len(v_out)
            axs[0].plot(temps_out, [avg_vout]*len(temps_out), label=f'Avg vout {labelname}: {avg_vout:.4f} V', linestyle='dotted', color=line_color)
            ppm_tc = ( (max(v_out) - min(v_out)) / (avg_vout * (max(temps_out) - min(temps_out))) ) * 1e6
            handle = axs[0].lines[-1]
            handle.set_label(handle.get_label() + f' (TC: {ppm_tc:.2f} ppm/°C)')
        elif "Vt" in file:
            # axs2[1].plot(temps_ref, v_ref, label='vref ' + labelname, marker='o', linestyle='solid')
            axs[1].plot(temps_out, v_out, label=f'vout {labelname}', marker='o', linestyle='dashed')
            line_color = axs[1].lines[-1].get_color()
            avg_vout = sum(v_out) / len(v_out)
            axs[1].plot(temps_out, [avg_vout]*len(temps_out), label=f'Avg vout {labelname}: {avg_vout:.4f} V', linestyle='dotted', color=line_color)
            ppm_tc = ( (max(v_out) - min(v_out)) / (avg_vout * (max(temps_out) - min(temps_out))) ) * 1e6
            handle = axs[1].lines[-1]
            handle.set_label(handle.get_label() + f' (TC: {ppm_tc:.2f} ppm/°C)')
        elif "Vh" in file:
            # axs2[2].plot(temps_ref, v_ref, label='vref ' + labelname, marker='o', linestyle='solid')
            axs[2].plot(temps_out, v_out, label=f'vout {labelname}', marker='o', linestyle='dashed')
            line_color = axs[2].lines[-1].get_color()
            avg_vout = sum(v_out) / len(v_out)
            axs[2].plot(temps_out, [avg_vout]*len(temps_out), label=f'Avg vout {labelname}: {avg_vout:.4f} V', linestyle='dotted', color=line_color)
            ppm_tc = ( (max(v_out) - min(v_out)) / (avg_vout * (max(temps_out) - min(temps_out))) ) * 1e6
            handle = axs[2].lines[-1]
            handle.set_label(handle.get_label() + f' (TC: {ppm_tc:.2f} ppm/°C)')


    for ax, voltage in zip(axs, ["Vl", "Vt", "Vh"]):
        ax.set_title(f'Output voltage across temperatures (VDD: {1.7 if voltage=="Vl" else 1.8 if voltage=="Vt" else 1.9} V)')
        ax.set_xlabel('Temperature (°C)')
        ax.set_ylabel('Voltage (V)')
        ax.legend()
        ax.grid()

    fig.tight_layout()

    image_path2 = f"./figures/plot_vout_closest_to_{target}volt_{view}_tb_dac_and_bgr"
    fig.savefig(image_path2 + ".png")
    print("Figure saved to " + image_path2 + ".png")

    # with open(f"{image_path2}.fig.pickle", 'wb') as pickledfile:
    #     pickle.dump(fig, pickledfile)
    # print("Figure pickled to " + image_path2 + ".fig.pickle")

    plt.show()