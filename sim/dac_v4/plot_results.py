import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats   

plot_colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown", "tab:pink"]

args = sys.argv[1:]
case = args[0]

runs = 30
bin_count = 7

temperatures = [-40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
voltages = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]

if case  == "typical":

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title(case)

    tt = []
    ii = []
    for voltage in voltages:
        t = []
        i = []
        for temperature in temperatures:

            outfile = f"output_tran/tran_SchGtKttTtVt_{temperature}celsius_{voltage}volt.out"
            df = pd.read_csv(outfile, sep='\s+')

            t.append(temperature)
            i.append(np.mean(df["i(vfeed)"]) * 1e6) # in uA

        ax.plot(t, i, label=f"v(ifeed) = {voltage} V")

        tt.append(t)
        ii.append(i)

    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Current (uA)")
    ax.legend(loc="best")
    ax.grid(True)
    fig.savefig("figures/" + case + ".png")

    plt.show()

if case  == "etc":

    fig_px, axs_px = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(24, 14))
    fig_px.suptitle("process corners")
    fig_vx, axs_vx = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(24, 14))
    fig_vx.suptitle("Voltage corners")
    # fig_tx, axs_tx = plt.subplots(1, 1, sharex=True, sharey=True, figsize=(24, 14))
    # fig_tx.suptitle("Temperature corners")

    fig_pvx, axs_pvx = plt.subplots(2, 4, sharex=True, sharey=True, figsize=(24, 14))
    fig_pvx.suptitle("Temperature corners")

    fig_v, axs_v = plt.subplots(2, 4, sharex=True, sharey=True, figsize=(24, 14))
    fig_v.suptitle("Voltage Sweep corners")


    tt = []
    ii = []

    for Px in ["ff", "fs",  "ss", "sf"]:
        for Vx in ["Vh", "Vl"]:
            for Tx in ["Tt"]:
                for voltage in voltages:
                    t = []
                    i = []

                    for temperature in temperatures:

                        outfile = f"output_tran/tran_SchGtK{Px}{Tx}{Vx}_{temperature}celsius_{voltage}volt.out"
                        print(f"Processing {outfile}")
                        df = pd.read_csv(outfile, sep='\s+')

                        t.append(temperature)
                        i.append(np.mean(df["i(vfeed)"]) * 1e6) # in uA

                    if Px == "ss": 
                        ax = axs_px[1,0]
                    elif Px == "fs":
                        ax = axs_px[1,1]
                    elif Px == "sf": 
                        ax = axs_px[0,0]
                    elif Px == "ff": 
                        ax = axs_px[0,1]

                    ax.plot(t, i, label=f"{outfile.split('/')[-1].split('_')[1]}, v(ifeed) = {voltage} V")
                    ax.set_title(f"{Px}")

                    if Vx == "Vl": 
                        ax = axs_vx[0]
                    elif Vx == "Vh": 
                        ax = axs_vx[1]

                    ax.plot(t, i, label=f"{outfile.split('/')[-1].split('_')[1]}, v(ifeed) = {voltage} V")
                    ax.set_title(f"{Vx}")

                    if Px == "ss" and Vx == "Vl":
                        ax = axs_pvx[0,0]
                    elif Px == "fs" and Vx == "Vl":
                        ax = axs_pvx[0,1]
                    elif Px == "sf" and Vx == "Vl":
                        ax = axs_pvx[0,2]
                    elif Px == "ff" and Vx == "Vl":
                        ax = axs_pvx[0,3]
                    if Px == "ss" and Vx == "Vh":
                        ax = axs_pvx[1,0]
                    elif Px == "fs" and Vx == "Vh":
                        ax = axs_pvx[1,1]
                    elif Px == "sf" and Vx == "Vh":
                        ax = axs_pvx[1,2]
                    elif Px == "ff" and Vx == "Vh":
                        ax = axs_pvx[1,3]

                    ax.plot(t, i, label=f"{outfile.split('/')[-1].split('_')[1]}, v(ifeed) = {voltage} V")
                    ax.set_title(f"{Px}, {Vx}")

                    if voltage == 0.2: 
                        ax = axs_v[0,0]
                    elif voltage == 0.4: 
                        ax = axs_v[0,1]
                    elif voltage == 0.6: 
                        ax = axs_v[0,2]
                    elif voltage == 0.8: 
                        ax = axs_v[0,3]
                    elif voltage == 1.0: 
                        ax = axs_v[1,0]
                    elif voltage == 1.2: 
                        ax = axs_v[1,1]
                    elif voltage == 1.4: 
                        ax = axs_v[1,2]
                    elif voltage == 1.6: 
                        ax = axs_v[1,3]

                    ax.plot(t, i, label=f"{outfile.split('/')[-1].split('_')[1]}")
                    ax.set_title(f"v(ifeed) = {voltage} V")

                    tt.append(t)
                    ii.append(i)        

    for row in range(2):
        for col in range(2): 
            axs_px[row, col].set_xlabel("Temperature (°C)")  
            axs_px[row, col].set_ylabel("Current (uA)") 
            axs_px[row, col].legend(loc="best")
            axs_px[row, col].grid(True)

    for row in range(1):
        for col in range(2):
            axs_vx[col].set_xlabel("Temperature (°C)")  
            axs_vx[col].set_xlabel("Current (uA)")  
            axs_vx[col].legend(loc="best")
            axs_vx[col].grid(True)


    for row in range(2):
        for col in range(4): 
            axs_pvx[row, col].set_xlabel("Temperature (°C)")  
            axs_pvx[row, col].set_ylabel("Current (uA)")
            axs_pvx[row, col].legend(loc="best")
            axs_pvx[row, col].grid(True)


    for row in range(2):
        for col in range(4): 
            axs_v[row, col].set_xlabel("Temperature (°C)")  
            axs_v[row, col].set_ylabel("Current (uA)")
            axs_v[row, col].legend(loc="best")
            axs_v[row, col].grid(True)
    

    fig_px.savefig("figures/" + case + "px.png")
    fig_vx.savefig("figures/" + case + "vx.png")
    # fig_tx.savefig("figures/" + case + "tx.png")
    
    fig_pvx.savefig("figures/" + case + "pvx.png")

    fig_v.savefig("figures/" + case + ".png")


    plt.show()

if case  == "all":

    fig_pvx, axs_pvx = plt.subplots(3, 5, sharex=True, sharey=True, figsize=(24, 14))
    fig_pvx.suptitle("All corners")

    tt = []
    ii = []

    for Px in ["tt", "sf", "ff", "fs", "ss"]:
        for Vx in ["Vl", "Vt", "Vh"]:
            for Tx in ["Tt"]:
                for voltage in voltages:
                    t = []
                    i = []

                    for temperature in temperatures:

                        outfile = f"output_tran/tran_SchGtK{Px}{Tx}{Vx}_{temperature}celsius_{voltage}volt.out"
                        print(f"Processing {outfile}")
                        df = pd.read_csv(outfile, sep='\s+')

                        t.append(temperature)
                        i.append(np.mean(df["i(vfeed)"]) * 1e6) # in uA

                    if Px == "ss" and Vx == "Vl":
                        ax = axs_pvx[0,0]
                    elif Px == "fs" and Vx == "Vl":
                        ax = axs_pvx[0,1]
                    elif Px == "tt" and Vx == "Vl":
                        ax = axs_pvx[0,2]
                    elif Px == "sf" and Vx == "Vl":
                        ax = axs_pvx[0,3]
                    elif Px == "ff" and Vx == "Vl":
                        ax = axs_pvx[0,4]
                    elif Px == "ss" and Vx == "Vt":
                        ax = axs_pvx[1,0]
                    elif Px == "fs" and Vx == "Vt":
                        ax = axs_pvx[1,1]
                    elif Px == "tt" and Vx == "Vt":
                        ax = axs_pvx[1,2]
                    elif Px == "sf" and Vx == "Vt":
                        ax = axs_pvx[1,3]
                    elif Px == "ff" and Vx == "Vt":
                        ax = axs_pvx[1,4]
                    elif Px == "ss" and Vx == "Vh":
                        ax = axs_pvx[2,0]
                    elif Px == "fs" and Vx == "Vh":
                        ax = axs_pvx[2,1]
                    elif Px == "tt" and Vx == "Vh":
                        ax = axs_pvx[2,2]
                    elif Px == "sf" and Vx == "Vh":
                        ax = axs_pvx[2,3]
                    elif Px == "ff" and Vx == "Vh":
                        ax = axs_pvx[2,4]

                    ax.plot(t, i, label=f"{outfile.split('/')[-1].split('_')[1]}, v(ifeed) = {voltage} V")
                    ax.set_title(f"{Px}, {Vx}")

                    tt.append(t)
                    ii.append(i)        

    for row in range(3):
        for col in range(5): 
            axs_pvx[row, col].set_xlabel("Temperature (°C)")  
            axs_pvx[row, col].set_ylabel("Current (uA)") 
            axs_pvx[row, col].legend(loc="best")
            axs_pvx[row, col].grid(True)
    
    fig_pvx.savefig("figures/" + case + "pvx.png")


    plt.show()