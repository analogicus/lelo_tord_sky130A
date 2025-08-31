v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N -120 -50 -60 -50 {lab=IBPS_4U}
N -60 -50 -60 -30 {lab=IBPS_4U}
N -120 50 -60 50 {lab=VSS}
N -60 30 -60 50 {lab=VSS}
N 60 30 60 50 {lab=VSS}
N -120 50 60 50 {lab=VSS}
N 60 0 100 0 {lab=VSS}
N 100 0 100 50 {lab=VSS}
N 60 50 100 50 {lab=VSS}
N -100 0 -60 0 {lab=VSS}
N -100 0 -100 50 {lab=VSS}
N 60 -50 60 -30 {lab=IBNS_20U}
N 60 -50 100 -50 {lab=IBNS_20U}
N -60 -50 0 -50 {lab=IBPS_4U}
N 0 -50 0 0 {lab=IBPS_4U}
N -20 0 20 0 {lab=IBPS_4U}
C {devices/ipin.sym} -120 -50 0 0 {name=p1 lab=IBPS_5U}
C {devices/ipin.sym} -120 50 0 0 {name=p2 lab=VSS}
C {devices/opin.sym} 100 -50 0 0 {name=p3 lab=IBNS_20U}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} -20 0 0 1 {name=xi }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 20 0 0 0 {name=xo[3:0] }
