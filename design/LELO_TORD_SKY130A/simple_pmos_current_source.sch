v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 200 -190 240 -190 {lab=VGATE}
N 80 -240 300 -240 {lab=VDD}
N 300 -240 300 -190 {lab=VDD}
N 280 -190 300 -190 {lab=VDD}
N 140 -190 160 -190 {lab=VDD}
N 140 -240 140 -190 {lab=VDD}
N 160 -160 160 -120 {lab=VGATE}
N 280 -160 280 -90 {lab=IBIAS}
N 220 -190 220 -140 {lab=VGATE}
N 160 -140 220 -140 {lab=VGATE}
N 160 -240 160 -220 {lab=VDD}
N 280 -240 280 -220 {lab=VDD}
N 120 -80 140 -80 {lab=VSS}
N 120 -80 120 -20 {lab=VSS}
N 160 -40 160 -20 {lab=VSS}
N 80 -20 160 -20 {lab=VSS}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 200 -190 0 1 {name=x1}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 240 -190 0 0 {name=x2}
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 160 -120 1 0 {name=x3 }
C {devices/ipin.sym} 80 -20 0 0 {name=p1 lab=VSS}
C {devices/ipin.sym} 80 -240 0 0 {name=p2 lab=VDD}
C {devices/opin.sym} 280 -90 1 0 {name=p3 lab=IBIAS}
C {devices/lab_wire.sym} 220 -140 2 0 {name=p4 sig_type=std_logic lab=VGATE}
