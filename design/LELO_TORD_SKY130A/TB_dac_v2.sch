v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 660 50 660 230 {lab=vd1a}
N 640 210 640 230 {lab=#net1}
N 660 290 660 310 {lab=vss}
N 200 310 710 310 {lab=vss}
N 200 90 200 310 {lab=vss}
N 180 90 220 90 {lab=vss}
N 180 210 220 210 {lab=b4}
N 180 190 220 190 {lab=b3}
N 180 170 220 170 {lab=b2}
N 180 150 220 150 {lab=b1}
N 180 130 220 130 {lab=b0}
N 180 50 220 50 {lab=vdd}
N 180 70 220 70 {lab=sleep}
N 600 260 600 310 {lab=#net2}
N 660 50 700 50 {lab=vd1a}
N 520 50 660 50 {lab=vd1a}
N 180 110 220 110 {lab=bt}
N 180 270 220 270 {lab=b7}
N 180 250 220 250 {lab=b6}
N 180 230 220 230 {lab=b5}
N 200 620 720 620 {lab=vss}
N 200 400 200 620 {lab=vss}
N 180 400 220 400 {lab=vss}
N 180 520 220 520 {lab=b4}
N 180 500 220 500 {lab=b3}
N 180 480 220 480 {lab=b2}
N 180 460 220 460 {lab=b1}
N 180 440 220 440 {lab=b0}
N 180 360 220 360 {lab=vdd}
N 180 380 220 380 {lab=sleep}
N 660 360 700 360 {lab=vd1b}
N 520 360 660 360 {lab=vd1b}
N 180 420 220 420 {lab=bt}
N 180 580 220 580 {lab=b7}
N 180 560 220 560 {lab=b6}
N 180 540 220 540 {lab=b5}
N 660 480 660 520 {lab=vd2}
N 600 440 600 620 {lab=vss}
N 660 580 660 620 {lab=vss}
N 600 550 620 550 {lab=vss}
N 660 360 660 400 {lab=vd1b}
N 600 260 620 260 {lab=#net2}
N 600 440 640 440 {}
C {sky130_fd_pr/pnp_05v5.sym} 640 260 0 0 {name=Q1
model=pnp_05v5_W3p40L3p40
m=1
spiceprefix=X
}
C {LELO_TORD_SKY130A/dac_v3.sym} 370 160 0 0 {name=x1}
C {devices/ipin.sym} 180 150 0 0 {name=p17 lab=b1}
C {devices/ipin.sym} 180 170 0 0 {name=p18 lab=b2}
C {devices/ipin.sym} 180 190 0 0 {name=p19 lab=b3}
C {devices/ipin.sym} 180 210 0 0 {name=p20 lab=b4}
C {devices/ipin.sym} 180 130 0 0 {name=p7 lab=b0}
C {devices/ipin.sym} 180 90 0 0 {name=p1 lab=vss}
C {devices/ipin.sym} 180 50 0 0 {name=p2 lab=vdd}
C {devices/ipin.sym} 180 70 0 0 {name=p3 lab=sleep}
C {devices/opin.sym} 700 50 0 0 {name=p54 lab=vd1a}
C {devices/ipin.sym} 180 110 0 0 {name=p4 lab=bt}
C {devices/ipin.sym} 180 230 0 0 {name=p5 lab=b5}
C {devices/ipin.sym} 180 250 0 0 {name=p6 lab=b6}
C {devices/ipin.sym} 180 270 0 0 {name=p8 lab=b7}
C {LELO_TORD_SKY130A/dac_v3.sym} 370 470 0 0 {name=x2}
C {devices/ipin.sym} 180 460 0 0 {name=p9 lab=b1}
C {devices/ipin.sym} 180 480 0 0 {name=p10 lab=b2}
C {devices/ipin.sym} 180 500 0 0 {name=p11 lab=b3}
C {devices/ipin.sym} 180 520 0 0 {name=p12 lab=b4}
C {devices/ipin.sym} 180 440 0 0 {name=p13 lab=b0}
C {devices/ipin.sym} 180 400 0 0 {name=p14 lab=vss}
C {devices/ipin.sym} 180 360 0 0 {name=p15 lab=vdd}
C {devices/ipin.sym} 180 380 0 0 {name=p16 lab=sleep}
C {devices/opin.sym} 700 360 0 0 {name=p21 lab=vd1b}
C {devices/ipin.sym} 180 420 0 0 {name=p22 lab=bt}
C {devices/ipin.sym} 180 540 0 0 {name=p23 lab=b5}
C {devices/ipin.sym} 180 560 0 0 {name=p24 lab=b6}
C {devices/ipin.sym} 180 580 0 0 {name=p25 lab=b7}
C {sky130_fd_pr/pnp_05v5.sym} 640 550 0 0 {name=Q2[7:0]
model=pnp_05v5_W3p40L3p40
m=1
spiceprefix=X
}
C {devices/lab_wire.sym} 660 510 0 1 {name=p42 sig_type=std_logic lab=vd2}
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 660 480 1 1 {name=x2[1:0]}
