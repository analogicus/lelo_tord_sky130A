import sys
import pandas as pd
import matplotlib.pyplot as plt


args = sys.argv[1:]
tempeartures = [-40, 0, 40, 80, 125]
files = list()


stepping_direction = ""
if "up" in args:
    args.remove("up")
    stepping_direction = "up"
elif "down" in args:
    args.remove("down")
    stepping_direction = "down"
else: 
    stepping_direction = "down"
print(f"Plotting for transient signals stepping {stepping_direction}")


figure_width = 4
figure_height = 4
font_size = 6
title_size = font_size
label_size = font_size
legend_size = font_size
ticks_size = font_size


if "custom" in args:
    corner = args[-3]
    voltage = float(args[-2]) # Volt (V)
    Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
    temperature = int(args[-1]) # Celsius (degree C)
    
    file = f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out"
    filename = file.split("/")[-1].split(".out")[0]
    print(f"Custom settings: corner={corner}, voltage={voltage} V, Vx={Vx}, temperature={temperature} °C")
    print(f"Processing transient results from file: {file}")
    print(f"File name: {filename}")

    circuit_temperature = float(filename.split("_")[-2].replace("celsius", "")) # in degrees Celsius
    voltage_supply = float(filename.split("_")[-1].replace("volt", "")) # in Volt
    process_shorthand = filename.split("GtK")[-1].split("Tt")[0] # tt/ss/ff/sf/fs

    if process_shorthand == "tt":
        process_corner = "Typical"
    elif process_shorthand == "ss":
        process_corner = "Slow-Slow"
    elif process_shorthand == "ff":
        process_corner = "Fast-Fast"
    elif process_shorthand == "sf":
        process_corner = "Slow-Fast"
    elif process_shorthand == "fs":
        process_corner = "Fast-Slow"
    else:
        process_corner = "Oops, something is wrong!"

    df = pd.read_csv(file, sep="\s+")
    df['time'] = df['time'] * 1e6 # in us

    correct_output_found_time = df.loc[df["v(correct_output_found)"] > 0.99*1.8, "time"].max() # in us
    slp_low_time = df.loc[(df["v(slp)"] > 0.99*1.8) & (df["time"] < correct_output_found_time), "time"].max() # in us
    start_up_time = correct_output_found_time - slp_low_time # in us
    print(f"Correct output found at {correct_output_found_time:.2f} us, slp low at {slp_low_time:.2f} us, start-up time is {start_up_time:.2f} us")

    fig, axs = plt.subplots(3, 1, figsize=(figure_width, figure_height), sharex=True, dpi=300)

    axs[0].plot(df["time"], df["v(dac.vctl)"], label="vctl")
    axs[0].plot(df["time"], df["v(cmp_async)"], label="cmp")
    axs[0].plot(df["time"], df["v(rst)"], label="rst")
    axs[0].plot(df["time"], df["v(slp)"], label="slp")
    axs[0].plot(df["time"], df["v(mode)"], label="mode")
    axs[0].plot(df["time"], df["v(correct_output_found)"], label="out_en")

    axs[1].plot(df["time"], df["v(bgr.v1)"], label="v1")
    axs[1].plot(df["time"], df["v(bgr.v2)"], label="v2")
    axs[1].plot(df["time"], df["v(vout)"], label="vout")

    axs[2].plot(df["time"], df["v(dec_finetuning_duty_cycle)"], label="v(dec_finetuning_duty_cycle)")
    axs[2].plot(df["time"], df["v(dec_coarse_step_counter)"], label="v(dec_coarse_step_counter)")

    # get upper and lower limits for the shaded area
    upper_limit = max(axs[0].get_ylim()[1], axs[1].get_ylim()[1], axs[2].get_ylim()[1])
    lower_limit = min(axs[0].get_ylim()[0], axs[1].get_ylim()[0], axs[2].get_ylim()[0])
        
    axs[0].fill_betweenx([axs[0].get_ylim()[0], axs[0].get_ylim()[1]], slp_low_time, correct_output_found_time, color="gray", alpha=0.3)
    axs[1].fill_betweenx([axs[1].get_ylim()[0], axs[1].get_ylim()[1]], slp_low_time, correct_output_found_time, color="gray", alpha=0.3, label=f"start-up time: {start_up_time:.2f} us")
    axs[2].fill_betweenx([axs[2].get_ylim()[0], axs[2].get_ylim()[1]], slp_low_time, correct_output_found_time, color="gray", alpha=0.3)
    
    axs[0].axvline(x=correct_output_found_time, color="black", linestyle="dashed")
    axs[0].axvline(x=slp_low_time, color="black", linestyle="dashed")
    axs[1].axvline(x=correct_output_found_time, color="black", linestyle="dashed", label=f"correct output found at {correct_output_found_time:.2f} us")
    axs[1].axvline(x=slp_low_time, color="black", linestyle="dashed", label=f"sleep last went low at {slp_low_time:.2f} us")
    axs[2].axvline(x=correct_output_found_time, color="black", linestyle="dashed")
    axs[2].axvline(x=slp_low_time, color="black", linestyle="dashed")

    for i, ax in enumerate(axs):
        ax.tick_params(axis="both", labelsize=ticks_size)
        ax.grid()
        ax.legend(loc="best", ncol=2, fontsize=legend_size)
        ax.set_ylabel("Voltage (V)", fontsize=label_size)

    axs[0].set_title(f"Start-up time, {process_corner} corner, {voltage_supply} V, {circuit_temperature} °C", fontsize=title_size, fontweight='bold')
    axs[-1].set_xlabel("Time (us)", fontsize=label_size)

    fig.tight_layout()
    fig.savefig(f"plots/{filename}_start_up_time.png", dpi=300, bbox_inches="tight")
    print(f"Saved figure to plots/{filename}_start_up_time.png")


fig_startup_time = plt.figure(figsize=(4, 4), dpi=300)
axs_startup_time = fig_startup_time.add_subplot(1, 1, 1)

if "etc" in args:
    for corner in ["ss", "ff", "sf", "fs"]:
        for voltage in [1.7, 1.9]: # Volt (V)
            Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
            
            start_up_times = []

            for temperature in tempeartures: # Celsius (degree C)
                file = f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out"

                print(f"Processing transient results from file: {file}")
                figure_name = file.split("/")[-1].split(".out")[0]

                circuit_temperature = float(figure_name.split("_")[-2].replace("celsius", "")) # in degrees Celsius
                voltage_supply = float(figure_name.split("_")[-1].replace("volt", "")) # in Volt
                shorthand_name = figure_name.split("GtK")[-1].split("Tt")[0] # tt/ss/ff/sf/fs

                if shorthand_name == "tt":
                    process_corner = "Typical"
                elif shorthand_name == "ss":
                    process_corner = "Slow-Slow"
                elif shorthand_name == "ff":
                    process_corner = "Fast-Fast"
                elif shorthand_name == "sf":
                    process_corner = "Slow-Fast"
                elif shorthand_name == "fs":
                    process_corner = "Fast-Slow"
                else:
                    process_corner = "Oops, something is wrong!"

                df = pd.read_csv(file, sep="\s+")

                df['time'] = df['time'] * 1e6 # in us

                # find the time bewteen when df["v(correct_output_found)"] goes high after df["v(slp)"] goes low as long as the time slp goes low is before the correct output flag goes high
                correct_output_found_time = df.loc[df["v(correct_output_found)"] > 0.99*1.8, "time"].max() # in us
                slp_low_time = df.loc[(df["v(slp)"] > 0.99*1.8) & (df["time"] < correct_output_found_time), "time"].max() # in us
                start_up_time = correct_output_found_time - slp_low_time # in us
                print(f"Correct output found at {correct_output_found_time:.2f} us, slp low at {slp_low_time:.2f} us, start-up time is {start_up_time:.2f} us")

                start_up_times.append(start_up_time)

            axs_startup_time.plot(tempeartures, start_up_times, marker="o", label=f"{corner}{Vx}")

    start_up_times = []

    for temperature in tempeartures: # Celsius (degree C)
        corner = "tt"
        voltage = 1.8 # Volt (V)
        Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"

        file = f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out"

        print(f"Processing transient results from file: {file}")
        figure_name = file.split("/")[-1].split(".out")[0]

        circuit_temperature = float(figure_name.split("_")[-2].replace("celsius", "")) # in degrees Celsius
        voltage_supply = float(figure_name.split("_")[-1].replace("volt", "")) # in Volt
        shorthand_name = figure_name.split("GtK")[-1].split("Tt")[0] # tt/ss/ff/sf/fs

        if shorthand_name == "tt":
            process_corner = "Typical"
        elif shorthand_name == "ss":
            process_corner = "Slow-Slow"
        elif shorthand_name == "ff":
            process_corner = "Fast-Fast"
        elif shorthand_name == "sf":
            process_corner = "Slow-Fast"
        elif shorthand_name == "fs":
            process_corner = "Fast-Slow"
        else:
            process_corner = "Oops, something is wrong!"

        df = pd.read_csv(file, sep="\s+")

        df['time'] = df['time'] * 1e6 # in us

        # find the time bewteen when df["v(correct_output_found)"] goes high after df["v(slp)"] goes low as long as the time slp goes low is before the correct output flag goes high
        correct_output_found_time = df.loc[df["v(correct_output_found)"] > 0.99*1.8, "time"].max() # in us
        slp_low_time = df.loc[(df["v(slp)"] > 0.99*1.8) & (df["time"] < correct_output_found_time), "time"].max() # in us
        start_up_time = correct_output_found_time - slp_low_time # in us
        print(f"Correct output found at {correct_output_found_time:.2f} us, slp low at {slp_low_time:.2f} us, start-up time is {start_up_time:.2f} us")

        start_up_times.append(start_up_time)

    axs_startup_time.plot(tempeartures, start_up_times, marker="o", label=f"{corner}{Vx}")

    axs_startup_time.set_title(f"Start-up time", fontweight='bold')
    axs_startup_time.set_xlabel("Temperature (°C)")
    axs_startup_time.set_ylabel("Start-up time (us)")
    axs_startup_time.legend(loc="best")
    axs_startup_time.tick_params(axis='both')
    axs_startup_time.grid()

    fig_startup_time.tight_layout()
    fig_startup_time.savefig(f"plots/{'_'.join(args)}_stepping_{stepping_direction}_temperature_vs_start_up_time.png", dpi=300, bbox_inches="tight")




runs = 30

if "mc" in args:
    for corner in ["ttmm"]:
        for voltage in [1.8]: # Volt (V)
            Vx = "Vl" if voltage == 1.7 else "Vt" if voltage == 1.8 else "Vh" if voltage == 1.9 else "Oops"
            for temperature in tempeartures: # Celsius (degree C)
                for run in range(1, runs): # Assuming 30 Monte Carlo runs
                    if run == 0:
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")
                    else:
                        files.append(f"output_tran/tran_SchGtK{corner}Tt{Vx}_{run}_stepping_{stepping_direction}_{temperature}celsius_{voltage}volt.out")

