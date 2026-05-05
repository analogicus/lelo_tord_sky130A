v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 200 120 240 120 {lab=VDD}
N 200 140 240 140 {lab=VIP}
N 200 160 240 160 {lab=VIN}
N 200 220 240 220 {lab=VSS}
N 540 120 580 120 {lab=VOUT}
N 200 200 240 200 {lab=SLP_N}
N 200 180 240 180 {lab=SLP}
C {devices/ipin.sym} 200 220 0 0 {name=p4 lab=VSS
}
C {devices/ipin.sym} 200 120 2 1 {name=p1 lab=VDD
}
C {devices/ipin.sym} 200 160 0 0 {name=p3 lab=VIN
}
C {devices/ipin.sym} 200 140 0 0 {name=p2 lab=VIP
}
C {devices/opin.sym} 580 120 2 1 {name=p5 lab=VOUT}
C {LELO_TORD_SKY130A/cmp_two_stage_nmos_cross_coupled.sym} 390 170 0 0 {name=x1}
C {devices/ipin.sym} 200 200 0 0 {name=p6 lab=SLP_N
}
C {devices/ipin.sym} 200 180 0 0 {name=p7 lab=SLP
}
