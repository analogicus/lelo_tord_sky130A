v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 320 460 360 460 {lab=vss}
N 340 250 360 250 {lab=vss}
N 280 130 360 130 {lab=vdd}
N 300 130 300 420 {lab=vdd}
N 280 440 360 440 {lab=sleep}
N 660 130 700 130 {lab=Q}
N 340 290 680 290 {lab=Q}
N 340 290 340 400 {lab=Q}
N 340 400 360 400 {lab=Q}
N 280 380 360 380 {lab=b3}
N 280 360 360 360 {lab=b2}
N 280 340 360 340 {lab=b1}
N 280 320 360 320 {lab=b0}
N 280 150 360 150 {lab=clk}
N 280 170 360 170 {lab=d0}
N 280 190 360 190 {lab=d1}
N 280 210 360 210 {lab=d2}
N 280 230 360 230 {lab=d3}
N 680 130 680 290 {lab=Q}
N 280 250 340 250 {lab=vss}
N 320 250 320 460 {lab=vss}
N 300 420 360 420 {lab=vdd}
C {LELO_TORD_SKY130A/dac.sym} 510 390 0 0 {name=x1}
C {LELO_TORD_SKY130A/dig-to-time.sym} 510 190 0 0 {name=x2}
C {devices/ipin.sym} 280 320 0 0 {name=p1 lab=b0}
C {devices/ipin.sym} 280 340 0 0 {name=p2 lab=b1}
C {devices/ipin.sym} 280 360 0 0 {name=p3 lab=b2}
C {devices/ipin.sym} 280 380 0 0 {name=p4 lab=b3}
C {devices/ipin.sym} 280 440 0 0 {name=p5 lab=sleep}
C {devices/ipin.sym} 280 250 0 0 {name=p6 lab=vss}
C {devices/ipin.sym} 280 230 0 0 {name=p8 lab=d3}
C {devices/ipin.sym} 280 210 0 0 {name=p9 lab=d2}
C {devices/ipin.sym} 280 190 0 0 {name=p10 lab=d1}
C {devices/ipin.sym} 280 170 0 0 {name=p11 lab=d0}
C {devices/ipin.sym} 280 150 0 0 {name=p12 lab=clk
}
C {devices/opin.sym} 700 130 0 0 {name=p14 lab=Q}
C {devices/ipin.sym} 280 130 0 0 {name=p15 lab=vdd
}
