import matplotlib.pyplot as plt

from spicelib import RawRead

filename = "output_tran/tran_SchGtKttTtVt"
rawfile = RawRead(filename + ".raw")

tracenames = rawfile.get_trace_names()
print(rawfile.get_raw_properties())

time = rawfile.get_axis()

ic0 = rawfile.get_trace("i(@c.xdut.xr1.xc0.c0[i])")
ic1 = rawfile.get_trace("i(@c.xdut.xr1.xc0.c1[i])")
irb = rawfile.get_trace("i(@r.xdut.xr1.rbody[i])")
irh = rawfile.get_trace("i(@r.xdut.xr1.rhead[i])")
vdd = rawfile.get_trace("v(vdd)")
idd = rawfile.get_trace("i(vdd)")
vss = rawfile.get_trace("v(vss)")
iss = rawfile.get_trace("i(vss)")
vrb = rawfile.get_trace("v(xdut.xr1.rb)")

steps = rawfile.get_steps()             # Get list of step numbers ([0,1,2]) for sweeped simulations
                                        # Returns [0] if there is just 1 step

fig_i = plt.figure(dpi=300)
ax_i = fig_i.add_subplot(1,1,1)

fig_v = plt.figure(dpi=300)
ax_v = fig_v.add_subplot(1,1,1)

fig2 = plt.figure(dpi=300)
ax2 = fig2.add_subplot(1,1,1)

for tracename in tracenames:
    print(f"trace: {tracename}")

    if tracename.startswith("i("):
        trace = rawfile.get_trace(tracename).get_wave()
        ax_i.plot(time, trace, label=tracename)
        ax_i.grid()
        ax_i.legend()

    if tracename.startswith("v("):
        trace = rawfile.get_trace(tracename).get_wave()
        ax_v.plot(time, trace, label=tracename)
        ax_v.grid()
        ax_v.legend()

    for step in steps:                      # On the second plot, print all the STEPS of Vout
        x = rawfile.get_axis(step)      # Retrieve the time vector
        
        y = idd.get_wave(step)          # Retrieve the values for this step
        ax2.plot(x, y, label="1")              # Do X/Y plot on second subplot

        y = iss.get_wave(step)          # Retrieve the values for this step
        ax2.plot(x, y, label="2")              # Do X/Y plot on second subplot

plt.show()                              # Show matplotlib's interactive window with the plots