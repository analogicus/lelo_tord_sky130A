v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 220 300 260 300 {lab=vss}
N 240 90 260 90 {lab=vss}
N 180 -30 260 -30 {lab=vdd}
N 200 -30 200 260 {lab=vdd}
N 180 280 260 280 {lab=sleep}
N 560 -30 600 -30 {lab=Q}
N 240 130 580 130 {lab=Q}
N 240 130 240 240 {lab=Q}
N 240 240 260 240 {lab=Q}
N 180 220 260 220 {lab=b3}
N 180 200 260 200 {lab=b2}
N 180 180 260 180 {lab=b1}
N 180 160 260 160 {lab=b0}
N 180 -10 260 -10 {lab=clk}
N 180 10 260 10 {lab=d0}
N 180 30 260 30 {lab=d1}
N 180 50 260 50 {lab=d2}
N 180 70 260 70 {lab=d3}
N 560 -10 600 -10 {lab=Q_not}
N 580 -30 580 130 {lab=Q}
N 180 90 240 90 {lab=vss}
N 220 90 220 300 {lab=vss}
N 200 260 260 260 {lab=vdd}
C {LELO_TORD_SKY130A/dac.sym} 410 230 0 0 {name=x1}
C {LELO_TORD_SKY130A/dig-to-time.sym} 410 30 0 0 {name=x2}
C {devices/ipin.sym} 180 160 0 0 {name=p1 lab=b0}
C {devices/ipin.sym} 180 180 0 0 {name=p2 lab=b1}
C {devices/ipin.sym} 180 200 0 0 {name=p3 lab=b2}
C {devices/ipin.sym} 180 220 0 0 {name=p4 lab=b3}
C {devices/ipin.sym} 180 280 0 0 {name=p5 lab=sleep}
C {devices/ipin.sym} 180 90 0 0 {name=p6 lab=vss}
C {devices/ipin.sym} 180 70 0 0 {name=p8 lab=d3}
C {devices/ipin.sym} 180 50 0 0 {name=p9 lab=d2}
C {devices/ipin.sym} 180 30 0 0 {name=p10 lab=d1}
C {devices/ipin.sym} 180 10 0 0 {name=p11 lab=d0}
C {devices/ipin.sym} 180 -10 0 0 {name=p12 lab=clk
}
C {devices/opin.sym} 600 -10 0 0 {name=p13 lab=Q_not}
C {devices/opin.sym} 600 -30 0 0 {name=p14 lab=Q}
C {devices/ipin.sym} 180 -30 0 0 {name=p15 lab=vdd
}
