import sys
import pickle
import matplotlib.pyplot as plt

args = sys.argv[1:]
print(args)

if len(args) != 1:
    print("No path provided as argument. Assumes default path to pickled figure.")
    image_path = './figures/plot_Sch_typical_tb_dac.fig.pickle'
else:
    image_path = args[0]

print(f"Loading figure from: {image_path}")
# Source - https://stackoverflow.com/a
# Posted by Demis, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-26, License - CC BY-SA 3.0

with open(image_path, 'rb') as file: figx = pickle.load(file)

plt.show() # Show the figure, edit it, etc.!
