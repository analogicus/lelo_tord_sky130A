v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 200 300 260 300 {lab=vss}
N 220 300 220 320 {lab=vss}
N 220 320 740 320 {lab=vss}
N 740 280 740 320 {lab=vss}
N 740 280 760 280 {lab=vss}
N 740 160 760 160 {lab=vdd}
N 740 140 740 160 {lab=vdd}
N 220 140 740 140 {lab=vdd}
N 220 140 220 260 {lab=vdd}
N 220 260 260 260 {lab=vdd}
N 200 280 260 280 {lab=sleep}
N 1060 160 1100 160 {lab=Q}
N 1100 120 1100 160 {lab=Q}
N 240 120 1100 120 {lab=Q}
N 240 120 240 240 {lab=Q}
N 240 240 260 240 {lab=Q}
N 200 220 260 220 {lab=b3}
N 200 200 260 200 {lab=b2}
N 200 180 260 180 {lab=b1}
N 200 160 260 160 {lab=b0}
N 200 140 220 140 {lab=vdd}
N 720 180 760 180 {lab=clk}
N 720 200 760 200 {lab=d0}
N 720 220 760 220 {lab=d1}
N 720 240 760 240 {lab=d2}
N 720 260 760 260 {lab=d3}
N 1060 180 1090 180 {lab=#net1}
C {LELO_TORD_SKY130A/dac.sym} 410 230 0 0 {name=x1}
C {LELO_TORD_SKY130A/dig-to-time.sym} 910 220 0 0 {name=x2}
C {devices/ipin.sym} 200 160 0 0 {name=p1 lab=b0}
C {devices/ipin.sym} 200 180 0 0 {name=p2 lab=b1}
C {devices/ipin.sym} 200 200 0 0 {name=p3 lab=b2}
C {devices/ipin.sym} 200 220 0 0 {name=p4 lab=b3}
C {devices/ipin.sym} 200 280 0 0 {name=p5 lab=sleep}
C {devices/ipin.sym} 200 300 0 0 {name=p6 lab=vss}
C {devices/ipin.sym} 200 140 0 0 {name=p7 lab=vdd}
C {devices/ipin.sym} 720 260 0 0 {name=p8 lab=d3}
C {devices/ipin.sym} 720 240 0 0 {name=p9 lab=d2}
C {devices/ipin.sym} 720 220 0 0 {name=p10 lab=d1}
C {devices/ipin.sym} 720 200 0 0 {name=p11 lab=d0}
C {devices/ipin.sym} 720 180 0 0 {name=p12 lab=clk
}
C {devices/opin.sym} 1090 180 0 0 {name=p13 lab=Q_not}
C {devices/lab_pin.sym} 1100 160 0 1 {name=p14 sig_type=std_logic lab=Q}
