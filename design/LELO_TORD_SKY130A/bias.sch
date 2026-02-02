v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 750 500 790 500 {lab=PBIAS}
N 750 520 790 520 {lab=NBIAS}
N 410 500 450 500 {lab=VDD}
N 410 520 450 520 {lab=SLEEP}
N 410 540 450 540 {lab=VSS}
C {devices/ipin.sym} 410 500 0 0 {name=p3 lab=VDD}
C {devices/ipin.sym} 410 520 0 0 {name=p4 lab=SLEEP}
C {devices/ipin.sym} 410 540 0 0 {name=p6 lab=VSS}
C {devices/opin.sym} 790 500 0 0 {name=p13 lab=PBIAS}
C {devices/opin.sym} 790 520 0 0 {name=p14 lab=NBIAS}
C {LELO_TORD_SKY130A/bias_1p2u.sym} 600 520 0 0 {name=x1}
