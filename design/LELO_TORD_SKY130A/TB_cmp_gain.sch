v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 360 220 400 220 {lab=VDD}
N 360 240 400 240 {lab=VIP}
N 360 260 400 260 {lab=VIN}
N 360 280 400 280 {lab=VSS}
N 700 220 740 220 {lab=VOUT}
N 700 330 740 330 {lab=VOUT_PMOS}
N 360 330 400 330 {lab=VDD}
N 360 350 400 350 {lab=VIP}
N 360 370 400 370 {lab=VIN}
N 360 390 400 390 {lab=VSS}
C {devices/opin.sym} 740 220 2 1 {name=p5 lab=VOUT}
C {devices/ipin.sym} 360 220 0 0 {name=p1 lab=VDD}
C {devices/ipin.sym} 360 240 0 0 {name=p2 lab=VIP}
C {devices/ipin.sym} 360 260 0 0 {name=p3 lab=VIN}
C {devices/ipin.sym} 360 280 0 0 {name=p4 lab=VSS}
C {LELO_TORD_SKY130A/cmp_v3.sym} 550 250 0 0 {name=x1}
C {LELO_TORD_SKY130A/cmp_v3_pmos.sym} 550 360 0 0 {name=x2}
C {devices/lab_wire.sym} 380 330 0 0 {name=p6 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 380 350 0 0 {name=p7 sig_type=std_logic lab=VIP}
C {devices/lab_wire.sym} 380 370 0 0 {name=p8 sig_type=std_logic lab=VIN}
C {devices/lab_wire.sym} 380 390 0 0 {name=p9 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 740 330 2 1 {name=p10 lab=VOUT_PMOS}
