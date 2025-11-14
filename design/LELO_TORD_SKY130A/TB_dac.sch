v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 340 250 420 250 {lab=VSS}
N 280 130 420 130 {lab=VDD}
N 280 340 420 340 {lab=SLP}
N 600 130 680 130 {lab=#net1}
N 400 290 680 290 {lab=#net1}
N 280 400 420 400 {lab=B0}
N 280 150 420 150 {lab=CLK}
N 280 170 420 170 {lab=D0}
N 280 190 420 190 {lab=D1}
N 280 210 420 210 {lab=D2}
N 280 230 420 230 {lab=D3}
N 680 130 680 290 {lab=#net1}
N 280 250 340 250 {lab=VSS}
N 720 320 780 320 {lab=#net2}
N 780 320 780 500 {lab=#net2}
N 360 580 780 580 {lab=VSS}
N 720 530 720 580 {lab=VSS}
N 720 530 740 530 {lab=VSS}
N 360 360 360 580 {lab=VSS}
N 360 360 420 360 {lab=VSS}
N 360 250 360 360 {lab=VSS}
N 380 320 420 320 {lab=VDD}
N 380 130 380 320 {lab=VDD}
N 400 290 400 380 {lab=#net1}
N 400 380 420 380 {lab=#net1}
N 780 560 780 580 {lab=VSS}
N 280 420 420 420 {lab=B0}
N 280 440 420 440 {lab=B0}
N 280 460 420 460 {lab=B0}
N 280 480 420 480 {lab=B0}
N 280 500 420 500 {lab=B0}
N 280 520 420 520 {lab=B0}
N 280 540 420 540 {lab=B0}
C {LELO_TORD_SKY130A/dig-to-time.sym} 510 190 0 0 {name=x2}
C {devices/ipin.sym} 280 400 0 0 {name=p1 lab=B0
}
C {devices/ipin.sym} 280 420 0 0 {name=p2 lab=B1}
C {devices/ipin.sym} 280 440 0 0 {name=p3 lab=B2}
C {devices/ipin.sym} 280 460 0 0 {name=p4 lab=B3
}
C {devices/ipin.sym} 280 340 0 0 {name=p5 lab=SLP}
C {devices/ipin.sym} 280 250 0 0 {name=p6 lab=VSS}
C {devices/ipin.sym} 280 230 0 0 {name=p8 lab=D3}
C {devices/ipin.sym} 280 210 0 0 {name=p9 lab=D2}
C {devices/ipin.sym} 280 190 0 0 {name=p10 lab=D1}
C {devices/ipin.sym} 280 170 0 0 {name=p11 lab=D0}
C {devices/ipin.sym} 280 150 0 0 {name=p12 lab=CLK
}
C {devices/ipin.sym} 280 130 0 0 {name=p15 lab=VDD
}
C {LELO_TORD_SKY130A/dac_v3.sym} 570 430 0 0 {name=x1}
C {devices/ipin.sym} 280 480 0 0 {name=p7 lab=B4}
C {devices/ipin.sym} 280 500 0 0 {name=p13 lab=B5}
C {devices/ipin.sym} 280 520 0 0 {name=p16 lab=B6}
C {devices/ipin.sym} 280 540 0 0 {name=p17 lab=B7}
C {sky130_fd_pr/pnp_05v5.sym} 760 530 0 0 {name=Q1
model=pnp_05v5_W3p40L3p40
m=1
spiceprefix=X
}
C {devices/lab_wire.sym} 680 130 0 1 {name=p14 sig_type=std_logic lab=BT}
C {devices/lab_wire.sym} 780 320 0 1 {name=p18 sig_type=std_logic lab=VD}
