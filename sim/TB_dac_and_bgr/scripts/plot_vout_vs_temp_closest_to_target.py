import sys
import yaml
import matplotlib.pyplot as plt
import pickle


if __name__ == "__main__":

    fend = ".out" # File extension for output files, can be changed to ".yaml", ".csv" or others if needed
    view = "Sch" # Sets schematic is default view if none is specified
    # view = "Lay" # Sets schematic is default view if none is specified

    target = 1 # in Volts

    args = sys.argv[1:]   

    if len(args) == 0 or all(arg not in ["typical", "etc", "mc", "tord"] for arg in args):
        print("Wrong/No arguments provided. Please specify a combination of 'typical', 'etc', 'mc', and 'tord' to plot. View may be specified with 'Sch' or 'Lay' as arguments.")
        sys.exit(1)     

    for arg in args:
        print(f"Argument: \"{arg}\", of type: {type(arg)} recieved.")
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

    if "tord" in args:
        for corner in ["tt", "ff", "ss", "sf", "fs"]:
            for temperature in ["Tt"]:
                for voltage in ["Vl", "Vt", "Vh"]:
                    files.append(f"output_tran/tran_{view}GtK{corner}{temperature}{voltage}")
    
    fig, axs = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(24, 8))
    fig.suptitle(f'DAC and BGR Testbench Vout closest to target of {target} Volt vs Temperature', fontsize=16)

    # ax0 = axs[0].twinx()
    # ax1 = axs[1].twinx()
    # ax2 = axs[2].twinx()

    figVl, axVl = plt.subplots(1,1)
    figVt, axVt = plt.subplots(1,1)
    figVh, axVh = plt.subplots(1,1)

    Vl_TCs = []
    Vt_TCs = []
    Vh_TCs = []

    vouts = {}

    for file in files:

        yamlfile = file + '.yaml'
        print(f"Processing file: {yamlfile}")
        labelname = yamlfile.split('/')[-1].replace('.yaml', '').split('_')[-1]

        with open(yamlfile, "r") as yfile:
            data = yaml.load(yfile, Loader=yaml.FullLoader)
            vout = {}
            for key, value in data.items():
                if key.count("_") == 2 and key.startswith("vout"):
                    bit = key.split("_")[-1]
                    temperature = int(key.split("_")[-2])

                    if temperature not in vout:
                        vout[temperature] = {}

                    vout[temperature][bit] = value
            
        vouts[file] = vout
                                
        vout_to_plot = []
        temperatures_to_plot = []

        for temperature, info in vout.items():
            closest_value = list(info.values())[0] # Initialize with the first bit's value

            for bit, value in info.items():
                if abs(value - target) < abs(closest_value - target):
                    closest_value = value   
                    closest_bit = bit

            vout_to_plot.append(closest_value)  
            temperatures_to_plot.append(temperature)       

        vout_to_plot, temperatures_to_plot = zip(*sorted(zip(vout_to_plot, temperatures_to_plot), key=lambda x: x[1]))
                        

        if "Vl" in file:
            avg_vout = sum(vout_to_plot) / len(vout_to_plot)
            TC = ( (max(vout_to_plot) - min(vout_to_plot)) / (avg_vout * (max(temperatures_to_plot) - min(temperatures_to_plot))) ) * 1e6
            Vl_TCs.append(TC)
            axs[0].plot(temperatures_to_plot, vout_to_plot, label=f'{labelname}, TC: {TC:.0f} ppm/°C', marker='o', linestyle='dashed', linewidth=2.0)
            line_color = axs[0].lines[-1].get_color()
            axs[0].plot(temperatures_to_plot, [avg_vout]*len(temperatures_to_plot), label=f'Avg output: {avg_vout:.3f} V', linestyle='dotted', color=line_color, linewidth=2.0)
            axVl.plot(temperatures_to_plot, vout_to_plot, label=f'{labelname}, TC: {TC:.0f} ppm/°C', marker='o', linestyle='dashed', linewidth=2.0)
    
        elif "Vt" in file:
            avg_vout = sum(vout_to_plot) / len(vout_to_plot)
            TC = ( (max(vout_to_plot) - min(vout_to_plot)) / (avg_vout * (max(temperatures_to_plot) - min(temperatures_to_plot))) ) * 1e6
            Vt_TCs.append(TC)
            axs[1].plot(temperatures_to_plot, vout_to_plot, label=f'{labelname}, TC: {TC:.0f} ppm/°C', marker='o', linestyle='dashed', linewidth=2.0)
            line_color = axs[1].lines[-1].get_color()
            axs[1].plot(temperatures_to_plot, [avg_vout]*len(temperatures_to_plot), label=f'Avg output: {avg_vout:.3f} V', linestyle='dotted', color=line_color, linewidth=2.0)
            axVt.plot(temperatures_to_plot, vout_to_plot, label=f'{labelname}, TC: {TC:.0f} ppm/°C', marker='o', linestyle='dashed', linewidth=2.0)
   
        elif "Vh" in file:
            avg_vout = sum(vout_to_plot) / len(vout_to_plot)
            TC = ( (max(vout_to_plot) - min(vout_to_plot)) / (avg_vout * (max(temperatures_to_plot) - min(temperatures_to_plot))) ) * 1e6
            Vh_TCs.append(TC)
            axs[2].plot(temperatures_to_plot, vout_to_plot, label=f'{labelname}, TC: {TC:.0f} ppm/°C', marker='o', linestyle='dashed', linewidth=2.0)
            line_color = axs[2].lines[-1].get_color()
            axs[2].plot(temperatures_to_plot, [avg_vout]*len(temperatures_to_plot), label=f'Avg output: {avg_vout:.3f} V', linestyle='dotted', color=line_color, linewidth=2.0)
            axVh.plot(temperatures_to_plot, vout_to_plot, label=f'{labelname}, TC: {TC:.0f} ppm/°C', marker='o', linestyle='dashed', linewidth=2.0)

    print("vouts:", vouts)

    Vl_avg_TC = sum(Vl_TCs)/len(Vl_TCs) if len(Vl_TCs) > 0 else 0
    Vt_avg_TC = sum(Vt_TCs)/len(Vt_TCs) if len(Vt_TCs) > 0 else 0
    Vh_avg_TC = sum(Vh_TCs)/len(Vh_TCs) if len(Vh_TCs) > 0 else 0

    Vl_std_TC = (sum((x - Vl_avg_TC)**2 for x in Vl_TCs) / len(Vl_TCs))**0.5 if len(Vl_TCs) > 0 else 0
    Vt_std_TC = (sum((x - Vt_avg_TC)**2 for x in Vt_TCs) / len(Vt_TCs))**0.5 if len(Vt_TCs) > 0 else 0
    Vh_std_TC = (sum((x - Vh_avg_TC)**2 for x in Vh_TCs) / len(Vh_TCs))**0.5 if len(Vh_TCs) > 0 else 0
    

    for ax, voltage in zip(axs, ["Vl", "Vt", "Vh"]):
        ax.set_title(f'Output voltage across temperatures (VDD: {1.7 if voltage=="Vl" else 1.8 if voltage=="Vt" else 1.9} V)')
        ax.set_xlabel('Temperature (°C)')
        ax.set_ylabel('Output (V)')
        ax.yaxis.set_tick_params(labelleft=True)
        ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.1), fancybox=True, shadow=True, ncol=2, 
                  title=f'Average TC of plots: {Vl_avg_TC:.0f} ppm/°C' if voltage=="Vl" else f'Average TC of plots: {Vt_avg_TC:.0f} ppm/°C' if voltage=="Vt" else f'Average TC of plots: {Vh_avg_TC:.0f} ppm/°C')
        ax.grid()

    fig.tight_layout()

    image_path2 = f"./figures/plot_vout_closest_to_{target}_volt_args_{'_'.join(args)}_{view}_tb_dac_and_bgr"
    fig.savefig(image_path2 + ".png")
    print("Figure saved to " + image_path2 + ".png")

    # with open(f"{image_path2}.fig.pickle", 'wb') as pickledfile:
    #     pickle.dump(fig, pickledfile)
    # print("Figure pickled to " + image_path2 + ".fig.pickle")

    axVl.sharey(axVt)
    axVt.sharey(axVh)

    axVl.set_title(f'Output voltage across temperatures (VDD: 1.7 V)')
    axVl.set_xlabel('Temperature (°C)')
    axVl.set_ylabel('Voltage (V)')
    axVl.legend(loc='lower center', bbox_to_anchor=(0.5, 1.1), fancybox=True, shadow=True, ncol=2, 
                title=f'Average TC of plots: {Vl_avg_TC:.0f} ppm/°C')
    axVl.grid()
    figVl.tight_layout()

    axVt.set_title(f'Output voltage across temperatures (VDD: 1.8 V)')
    axVt.set_xlabel('Temperature (°C)')
    axVt.set_ylabel('Voltage (V)')
    axVt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.1), fancybox=True, shadow=True, ncol=2, 
                title=f'Average TC of plots: {Vt_avg_TC:.0f} ppm/°C')
    axVt.grid()
    figVt.tight_layout()

    axVh.set_title(f'Output voltage across temperatures (VDD: 1.9 V)')
    axVh.set_xlabel('Temperature (°C)')
    axVh.set_ylabel('Voltage (V)')
    axVh.legend(loc='lower center', bbox_to_anchor=(0.5, 1.1), fancybox=True, shadow=True, ncol=2, 
                title=f'Average TC of plots: {Vh_avg_TC:.0f} ppm/°C')
    axVh.grid()
    figVh.tight_layout()

    plt.show()