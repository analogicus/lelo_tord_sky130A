v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 80 -250 140 -250 {lab=VDD}
N 100 -190 120 -190 {lab=VSS}
N 100 -190 100 -30 {lab=VSS}
N 140 -50 140 -30 {lab=VSS}
N 80 -30 280 -30 {lab=VSS}
N 140 -250 140 -230 {lab=VDD}
N 180 -80 220 -80 {lab=#net1}
N 140 -150 140 -110 {lab=#net1}
N 260 -50 260 -30 {lab=VSS}
N 140 -130 200 -130 {lab=#net1}
N 200 -130 200 -80 {lab=#net1}
N 260 -180 260 -110 {lab=IBIAS}
N 120 -80 140 -80 {lab=VSS}
N 120 -80 120 -30 {lab=VSS}
N 260 -80 280 -80 {lab=VSS}
N 280 -80 280 -30 {lab=VSS}
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 140 -230 1 0 {name=x3 }
C {devices/ipin.sym} 80 -30 0 0 {name=p1 lab=VSS}
C {devices/ipin.sym} 80 -250 0 0 {name=p2 lab=VDD}
C {devices/ipin.sym} 260 -180 3 1 {name=p3 lab=IBIAS}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 180 -80 0 1 {name=x1 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 220 -80 0 0 {name=x2 }
C {devices/lab_wire.sym} 200 -130 0 1 {name=p4 sig_type=std_logic lab=VGATE}
