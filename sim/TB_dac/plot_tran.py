import tran
import sys

args = sys.argv[1:]

names = []

if len(args) == 0:
    print("No arguments provided. The typical case will be plotted by default.")
    names.append("output_tran/tran_SchGtKttTtVt")

for arg in args:
    if arg == "typical":
        names.append("output_tran/tran_SchGtKttTtVt") 
    elif arg != "typical":
        names.append("output_tran/tran_LayGtKttTtVt")
        print(f"The only option is to plot the typical case anyways.")    

if __name__ == "__main__":
    for name in names:
        tran.main(name)