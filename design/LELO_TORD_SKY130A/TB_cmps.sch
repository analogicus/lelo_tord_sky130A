v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 500 340 580 340 {lab=VSS}
N 500 240 580 240 {lab=VDD}
N 500 280 540 280 {lab=VIP}
N 500 300 540 300 {lab=VIN}
N 660 290 700 290 {lab=VOUT}
C {LELO_TORD_SKY130A/cmp.sym} 600 290 0 0 {name=x1}
C {devices/opin.sym} 700 290 0 0 {name=p5 lab=VOUT
}
C {devices/ipin.sym} 500 240 0 0 {name=p4 lab=VDD}
C {devices/ipin.sym} 500 340 0 0 {name=p3 lab=VSS}
C {devices/ipin.sym} 500 280 0 0 {name=p6 lab=VIP}
C {devices/ipin.sym} 500 300 0 0 {name=p7 lab=VIN}
