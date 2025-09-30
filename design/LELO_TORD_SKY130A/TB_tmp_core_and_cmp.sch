v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 880 -260 920 -260 {lab=CMP}
N 480 -220 580 -220 {lab=REF}
N 480 -220 480 -160 {lab=REF}
N 180 -160 480 -160 {lab=REF}
N 480 -340 480 -240 {lab=IPTAT}
N 480 -240 580 -240 {lab=IPTAT}
N 540 -260 580 -260 {lab=VDD}
N 540 -200 580 -200 {lab=VSS}
N 180 -340 480 -340 {lab=IPTAT}
N 400 -220 400 -200 {lab=VSS}
N 260 -200 540 -200 {lab=VSS}
N 400 -340 400 -290 {lab=IPTAT}
N 180 -260 240 -260 {lab=CMP}
N 280 -260 320 -260 {lab=VSS}
N 320 -260 320 -200 {lab=VSS}
N 280 -230 280 -200 {lab=VSS}
N 280 -340 280 -330 {lab=IPTAT}
N 280 -330 280 -290 {lab=IPTAT}
C {devices/ipin.sym} 180 -160 0 0 {name=p7 lab=REF}
C {devices/opin.sym} 920 -260 0 0 {name=p15 lab=CMP}
C {LELO_TORD_SKY130A/cmp_v2.sym} 730 -230 0 0 {name=x2}
C {devices/lab_wire.sym} 570 -260 0 0 {name=p9 sig_type=std_logic lab=VDD}
C {JNW_TR_SKY130A/JNWTR_CAPX4.sym} 400 -230 0 0 {name=x1[1:0]}
C {devices/ipin.sym} 260 -200 0 0 {name=p1 lab=VSS}
C {devices/ipin.sym} 160 -390 0 0 {name=p2 lab=VDD}
C {devices/ipin.sym} 180 -340 0 0 {name=p3 lab=IPTAT}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 240 -260 0 0 {name=x1 }
C {devices/ipin.sym} 180 -260 0 0 {name=p5 lab=RST}
