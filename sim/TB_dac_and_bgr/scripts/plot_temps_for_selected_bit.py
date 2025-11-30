import sys
import yaml
import matplotlib.pyplot as plt
import pickle


if __name__ == "__main__":

    fend = ".out" # File extension for output files, can be changed to ".yaml", ".csv" or others if needed
    view = "Sch" # Sets schematic is default view if none is specified
    # view = "Lay" # Sets schematic is default view if none is specified

    target = 1

    args = sys.argv[1:]      
    print(args)  

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
    for corner in ["ff", "ss", "tt", "sf", "fs"]:
        for temperature in ["Tt"]:
            for voltage in ["Vl", "Vt", "Vh"]:
                files.append(f"output_tran/tran_{view}GtK{corner}{temperature}{voltage}")
    
    fig2, axs2 = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(18, 6))

    fig2.suptitle('DAC and BGR Testbench - Temperature Variation', fontsize=16)

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

        with open(yamlfile, "r") as yfile:
            data = yaml.load(yfile, Loader=yaml.FullLoader)

            # Iterate through all keys in the YAML data
            for key, value in data.items():
                # print(key, value)
                if key.count("_") == 2:
                    if key.startswith("vout"):
                        if key.endswith(args[0]):
                            temp_out = int(key.split("_")[-2])
                            print(key, value)

                            if temp_out == -50:
                                vout_out_neg50.append(value)
                            elif temp_out == -25:
                                vout_out_neg25.append(value)
                            elif temp_out == 0:
                                vout_out_0.append(value)
                            elif temp_out == 25:    
                                vout_out_25.append(value)
                            elif temp_out == 50:
                                vout_out_50.append(value)
                            elif temp_out == 75:
                                vout_out_75.append(value)
                            elif temp_out == 100:
                                vout_out_100.append(value)
                            elif temp_out == 125:
                                vout_out_125.append(value)

        temps_out = [-50, -25, 0, 25, 50, 75, 100, 125]
        v_out = []

        for lst in [vout_out_neg50, vout_out_neg25, vout_out_0, vout_out_25, vout_out_50, vout_out_75, vout_out_100, vout_out_125]:
            print(lst)
            
            closest_value = min(lst, key=lambda x: abs(x - target))
            v_out.append(closest_value)
                        
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

    image_path2 = f"./figures/plot_temps_for_selected_bit_{view}_{'_'.join(args)}_tb_dac_and_bgr"
    fig2.savefig(image_path2 + ".png")
    print("Figure saved to " + image_path2 + ".png")

    # with open(f"{image_path2}.fig.pickle", 'wb') as pickledfile:
    #     pickle.dump(fig2, pickledfile)
    # print("Figure pickled to " + image_path2 + ".fig.pickle")

    plt.show()