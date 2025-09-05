v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N -20 -70 20 -70 {lab=VGATE}
N -140 -120 80 -120 {lab=VDD}
N 80 -120 80 -70 {lab=VDD}
N 60 -70 80 -70 {lab=VDD}
N -80 -70 -60 -70 {lab=VDD}
N -80 -120 -80 -70 {lab=VDD}
N -60 -40 -60 0 {lab=VGATE}
N 60 -40 60 0 {lab=IOUT}
N 0 -70 0 -20 {lab=VGATE}
N -60 -20 0 -20 {lab=VGATE}
N -60 -120 -60 -100 {lab=VDD}
N 60 -120 60 -100 {lab=VDD}
N -100 40 -80 40 {lab=VSS}
N -100 40 -100 100 {lab=VSS}
N -60 80 -60 100 {lab=VSS}
N -140 100 -60 100 {lab=VSS}
N 60 0 140 0 {lab=IOUT}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} -20 -70 0 1 {name=x1}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 20 -70 0 0 {name=x2}
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} -60 0 1 0 {name=x3 }
C {devices/ipin.sym} -140 100 0 0 {name=p1 lab=VSS}
C {devices/ipin.sym} -140 -120 0 0 {name=p2 lab=VDD}
C {devices/opin.sym} 140 0 0 0 {name=p3 lab=IOUT}
C {devices/lab_wire.sym} 0 -20 2 0 {name=p4 sig_type=std_logic lab=VGATE}
