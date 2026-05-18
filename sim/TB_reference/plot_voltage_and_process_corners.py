import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d.art3d import Poly3DCollection

process_corners = dict(s=1, t=2, f=3)
voltage_corners = dict(Vl=1.7, Vt=1.8, Vh=1.9)
temperature_corners = dict(Tl=-40, Tt=25, Th=125)

fig = plt.figure(dpi=200)
ax = fig.add_subplot(111, projection='3d')

# for process_corner in ["ff", "fs", "tt", "ss", "sf"]:
#     for _, voltage in voltages.items():

#         nmos_process_corner = process_corners[process_corner[0]]
#         pmos_process_corner = process_corners[process_corner[-1]]

#         if process_corner == "ff":
#             plot_color = "red"
#         elif process_corner == "ss":
#             plot_color = "blue"
#         elif process_corner == "tt":
#             plot_color = "green"
#         elif process_corner == "sf":
#             plot_color = "orange"
#         elif process_corner == "fs":
#             plot_color = "purple"
#         else:
#             plot_color = "black"

#         if voltage == 1.7:
#             plot_marker = "s"
#         elif voltage == 1.8:
#             plot_marker = "o"
#         elif voltage == 1.9:
#             plot_marker = "v"
#         else:
#             plot_marker = "x"
        
#         ax.scatter(nmos_process_corner, pmos_process_corner, voltage, label=f"{process_corner}, {voltage} V", color=plot_color, marker=plot_marker)
    
plot_markersize_default = 36

for voltage_corner in ["Vl", "Vt", "Vh"]:

    x = []
    y = []

    if voltage_corner == "Vl":
        plot_color = "red"
    elif voltage_corner == "Vt":
        plot_color = "blue"
    elif voltage_corner == "Vh":
        plot_color = "green"
    else:
        plot_color = "black"

    voltage = voltage_corners[voltage_corner]

    for process_corner in ["ff", "fs", "tt", "ss", "sf"]:

        if process_corner == "ff":
            plot_marker = "s"
            plot_markersize = plot_markersize_default
        elif process_corner == "ss":
            plot_marker = "o"
            plot_markersize = plot_markersize_default
        elif process_corner == "tt":
            plot_marker = "v"
            plot_markersize = plot_markersize_default
        elif process_corner == "sf":
            plot_marker = "D"
            plot_markersize = 25
        elif process_corner == "fs":
            plot_marker = "*"
            plot_markersize = 49
        else:
            plot_marker = "x"
            plot_markersize = plot_markersize_default
    
        nmos_process_corner = process_corners[process_corner[0]]
        pmos_process_corner = process_corners[process_corner[-1]]
        
        ax.scatter(nmos_process_corner, pmos_process_corner, voltage, label=f"{process_corner}, {voltage} V", color=plot_color, marker=plot_marker, s=plot_markersize)

        if process_corner != "tt":
            x.append(nmos_process_corner)
            y.append(pmos_process_corner)

    # xtp = process_corners["t"]
    # ytp = process_corners["t"]

    # for xp in x:
    #     for yp in y:
    #         ax.plot([xp, xtp], [yp, ytp], voltage, color=plot_color, alpha=0.02) 

    x = np.append(x, x[0])
    y = np.append(y, y[0])

    vert = [list(zip(x, y, [voltage]*len(x)))]

    poly = Poly3DCollection(vert, alpha=0.2, facecolor=plot_color, edgecolor=plot_color)
    ax.add_collection3d(poly)

ax.set_xlabel("NMOS Process Corner", labelpad=10)
ax.set_ylabel("PMOS Process Corner", labelpad=10)
ax.set_zlabel("Supply Voltage", labelpad=10)

ax.set_xticks([1, 2, 3])
ax.set_xticklabels(['Slow', 'Typical', 'Fast'])
ax.set_yticks([1, 2, 3])
ax.set_yticklabels(['Slow', 'Typical', 'Fast'])
ax.set_zticks([1.7, 1.8, 1.9])
ax.set_zticklabels(['Low', 'Typical', 'High'])

ax.set_title('3D Scatter Plot')
ax.legend(bbox_to_anchor=(-0.01, 1), loc='upper right')
ax.grid(True)

# fig.tight_layout()

fig.savefig("../../media/process_corners_and_voltages.png")

plt.show()

