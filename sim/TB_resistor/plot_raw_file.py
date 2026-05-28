import matplotlib.pyplot as plt
import sys

from spicelib import RawRead


args = sys.argv[1:]


def plot_raw_file(name="output_tran/tran_SchGtKttTtVt"):

    rawfile = RawRead(name + ".raw")

    tracenames = rawfile.get_trace_names()
    print(rawfile.get_raw_properties())

    time = rawfile.get_axis()
    time = time * 1e9 # in ns

    # ic0 = rawfile.get_trace("i(@c.xdut.xr1.xc0.c0[i])")
    # ic1 = rawfile.get_trace("i(@c.xdut.xr1.xc0.c1[i])")
    # irb = rawfile.get_trace("i(@r.xdut.xr1.rbody[i])")
    # irh = rawfile.get_trace("i(@r.xdut.xr1.rhead[i])")
    vdd = rawfile.get_trace("v(vdd)")
    idd = rawfile.get_trace("i(vdd)")
    # vss = rawfile.get_trace("v(vss)")
    # iss = rawfile.get_trace("i(vss)")
    # vrb = rawfile.get_trace("v(xdut.xr1.rb)")

    steps = rawfile.get_steps() # Get list of step numbers ([0,1,2]) for sweeped simulations
                                # Returns [0] if there is just 1 step

    fig_v = plt.figure(dpi=300, figsize=(4,4))
    ax_v = fig_v.add_subplot(1,1,1)

    fig_i = plt.figure(dpi=300, figsize=(4,4))
    ax_i = fig_i.add_subplot(1,1,1)

    fig_r = plt.figure(dpi=300, figsize=(4,4))
    ax_r = fig_r.add_subplot(1,1,1)

    for tracename in tracenames:
        print(f"trace: {tracename}")

        if tracename.startswith("v("):
            trace = rawfile.get_trace(tracename).get_wave()
            
            ax_v.plot(time, trace, label=tracename)

        if tracename.startswith("i("):
            trace = rawfile.get_trace(tracename).get_wave() 
            trace = -trace * 1e6 # in uA with a positive sign
            
            ax_i.plot(time, trace, label=tracename)

    for step in steps:             
        t = rawfile.get_axis(step)  
        t = t * 1e9 # in ns

        i = idd.get_wave(step) 
        i = -i # Flips the sign from negative to positiveS

        v = vdd.get_wave(step) 

        r = v / i

        ax_r.plot(t, r, label="R=V/I") 

    ax_name = name.split("/")[-1]

    # fig_v.suptitle(f"Voltages, {ax_name}")
    ax_v.set_title(f"{ax_name}", fontsize=10, fontweight="bold")
    ax_v.grid()
    ax_v.legend(loc="best", fontsize=9)
    ax_v.set_xlabel(f"Time (ns)")
    ax_v.set_ylabel(f"Voltage (V)")

    ax_i.set_title(f"{ax_name}", fontsize=10, fontweight="bold")
    ax_i.grid()
    ax_i.legend(loc="best", fontsize=9)
    ax_i.set_xlabel(f"Time (ns)")
    ax_i.set_ylabel(f"Current (uA)")

    ax_r.set_title(f"{ax_name}", fontsize=10, fontweight="bold")
    ax_r.grid()
    ax_r.legend(loc="best", fontsize=9)
    ax_r.set_xlabel(f"Time (ns)")
    ax_r.set_ylabel(f"Resistance (Ω)")

    return fig_v, fig_i, fig_r


def main():
    
    if len(args) > 0:
        name = args[-1]
    else:
        name = "output_tran/tran_SchGtKttTtVt"

    fig_v, fig_i, fig_r = plot_raw_file(name)

    fig_v.tight_layout()
    fig_v.savefig(f"{name}_v.png")

    fig_i.tight_layout()
    fig_i.savefig(f"{name}_i.png")

    fig_r.tight_layout()
    fig_r.savefig(f"{name}_r.png")

    # if name == "output_tran/tran_SchGtKttTtVt":
    #     plt.show()
    # else:
    #     plt.close()

    plt.close("all")
    

if __name__ == "__main__":
    main()