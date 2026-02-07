v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 660 -910 700 -910 {lab=VDD}
N 660 -890 700 -890 {lab=VIP}
N 660 -870 700 -870 {lab=VIN}
N 660 -850 700 -850 {lab=VSS}
N 1000 -910 1040 -910 {lab=VOUT}
N 1000 -890 1040 -890 {lab=VOUT_N}
C {devices/ipin.sym} 660 -850 0 0 {name=p4 lab=VSS
}
C {devices/ipin.sym} 660 -910 2 1 {name=p1 lab=VDD
}
C {devices/ipin.sym} 660 -870 0 0 {name=p3 lab=VIN
}
C {devices/ipin.sym} 660 -890 0 0 {name=p2 lab=VIP
}
C {devices/opin.sym} 1040 -910 2 1 {name=p5 lab=VOUT}
C {LELO_TORD_SKY130A/cmp_two_stage_nmos_cross_coupled.sym} 850 -880 0 0 {name=x1}
C {devices/opin.sym} 1040 -890 2 1 {name=p6 lab=VOUT_N}
