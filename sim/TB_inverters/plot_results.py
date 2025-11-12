import pandas as pd
import yaml
import matplotlib.pyplot as plt
import sys

fend = ".out" # File extension for output files, can be changed to ".yaml", ".csv" or others if needed

args = sys.argv[1:]

if len(args) == 0 or all(arg not in ["typical", "etc", "mc"] for arg in args):
    print("Wrong/No arguments provided. Please specify a combination of 'typical', 'etc', and 'mc' to be plotted.")
    sys.exit(1)

else:
    # print(f"Arguments: {args}")
    # for arg in args:
    #     print(f"{arg}")
    #     print(f"type: {type(arg)}")

    files = []
    if "typical" in args:
        files.append("output_tran/tran_SchGtKttTtVt")
    if "etc" in args:
        for corner in ["ff", "ss", "sf", "fs"]:
            for temperature in ["Tl", "Th"]:
                for voltage in ["Vl", "Vh"]:
                    files.append(f"output_tran/tran_SchGtK{corner}{temperature}{voltage}")
    if "mc" in args:
        for n in range(1, 30):
            files.append(f"output_tran/tran_SchGtKttmmTtVt_{n}")

    for file in files:
        fname = file + fend
        print(f"Processing file: {fname}")
        df = pd.read_csv(fname, sep='\s+')

        df['time'] = df['time'] * 1e9 # in ns

        # print(df.columns)
        # print(df.head())

        plt.plot(df['time'], df['v(out1)'], label=f'{fname}')

    plt.xlabel('Time (ns)')
    plt.ylabel('Voltage (V)')
    plt.title('Transient Response of Different Inverters')
    plt.legend()
    plt.tight_layout()
    plt.grid()

    image_path = "./figures/plot_results.png"
    plt.savefig(image_path)
    print("Figure saved to " + image_path)

    plt.show()
