v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 740 -250 780 -250 {lab=CMP}
N 500 -240 580 -240 {lab=REF}
N 500 -240 500 -180 {lab=REF}
N 180 -180 500 -180 {lab=REF}
N 500 -280 500 -260 {lab=VPTAT}
N 500 -260 580 -260 {lab=VPTAT}
N 660 -340 660 -320 {lab=VDD}
N 220 -340 660 -340 {lab=VDD}
N 180 -280 260 -280 {lab=IPTAT}
N 420 -280 500 -280 {lab=VPTAT}
N 180 -260 260 -260 {lab=SEL_CAP1}
N 180 -240 260 -240 {lab=SEL_CAP2}
N 180 -220 260 -220 {lab=RST}
N 180 -200 260 -200 {lab=VSS}
N 180 -300 260 -300 {lab=VDD}
N 220 -200 220 -160 {lab=VSS}
N 220 -340 220 -300 {lab=VDD}
N 660 -180 660 -160 {lab=VSS}
N 220 -160 660 -160 {lab=VSS}
C {devices/ipin.sym} 180 -180 0 0 {name=p7 lab=REF}
C {devices/opin.sym} 780 -250 0 0 {name=p15 lab=CMP}
C {LELO_TORD_SKY130A/cmp_v2.sym} 660 -250 0 0 {name=x2}
C {devices/ipin.sym} 180 -200 0 0 {name=p1 lab=VSS}
C {devices/ipin.sym} 180 -300 0 0 {name=p2 lab=VDD}
C {devices/ipin.sym} 180 -280 0 0 {name=p3 lab=IPTAT}
C {devices/ipin.sym} 180 -220 0 0 {name=p4 lab=RST}
C {LELO_TORD_SKY130A/tmp_core.sym} 340 -250 0 0 {name=x1}
C {devices/ipin.sym} 180 -260 0 0 {name=p5 lab=SEL_CAP1}
C {devices/ipin.sym} 180 -240 0 0 {name=p6 lab=SEL_CAP2}
C {devices/lab_wire.sym} 500 -280 0 0 {name=p8 sig_type=std_logic lab=VPTAT}
