import pandas as pd
import yaml
import matplotlib.pyplot as plt
import sys

fend = ".out" # File extension for output files, can be changed to ".yaml", ".csv" or others if needed
view = "Sch" # Sets the view to schematic as a default
# view = "Lay" # Sets the view to layout as a default

args = sys.argv[1:]

for arg in args:
    print(f"Argument {arg} of type: {type(arg)} recieved.")
    if arg in ["Sch", "Lay"]:
        view = arg
        print(f"View set to: {view}")

if len(args) == 0 or all(arg not in ["typical", "etc", "mc"] for arg in args):
    print("Wrong/No arguments provided. Please specify a combination of 'typical', 'etc', and 'mc' to be plotted.")
    sys.exit(1)

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

for file in files:
    fname = file + fend
    print(f"Processing file: {fname}")
    df = pd.read_csv(fname, sep='\s+')

    df['time'] = df['time'] * 1e9 # in ns

    # print(df.columns)
    # print(df.head())

    # linecolor = 'C' + str(files.index(file) % 10)  # Cycle through colors C0 to C9
    plt_inp, = plt.plot(df['time'], df['v(in1)'], linestyle='--', label=f'vin1 ({file.split("/")[-1]})')
    plt_outp, = plt.plot(df['time'], df['v(out1)'], color=plt_inp.get_color(), label=f'vout1 ({file.split("/")[-1]})')

plt.xlabel('Time (ns)')
plt.ylabel('Voltage (V)')
plt.title('Transient Response of Different Inverters')
plt.legend()
plt.tight_layout()
plt.grid()

image_path = f"./figures/plot_results_{view}.png"
plt.savefig(image_path)
print("Figure saved to " + image_path)

plt.show()
