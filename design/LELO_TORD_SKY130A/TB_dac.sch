v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 380 340 420 340 {lab=SLP}
N 720 320 900 320 {lab=VOUT1}
N 860 320 860 470 {lab=VOUT1}
N 800 500 800 550 {lab=VSS}
N 800 500 820 500 {lab=VSS}
N 860 530 860 550 {lab=VSS}
N 380 320 420 320 {lab=VDD}
N 860 640 860 770 {lab=VOUT2}
N 860 850 860 870 {lab=VSS}
N 820 810 840 810 {lab=VSS}
N 820 810 820 870 {lab=VSS}
N 800 550 860 550 {lab=VSS}
N 820 870 860 870 {lab=VSS}
N 720 640 900 640 {lab=VOUT2}
N 380 360 420 360 {lab=VSS}
N 380 380 420 380 {lab=BT}
N 380 400 420 400 {lab=B0}
N 380 420 420 420 {lab=B1}
N 380 440 420 440 {lab=B2}
N 380 460 420 460 {lab=B3}
N 380 480 420 480 {lab=B4}
N 380 500 420 500 {lab=B5}
N 380 520 420 520 {lab=B6}
N 380 540 420 540 {lab=B7}
N 380 660 420 660 {lab=SLP}
N 380 640 420 640 {lab=VDD}
N 380 680 420 680 {lab=VSS}
N 380 700 420 700 {lab=BT}
N 380 720 420 720 {lab=B0}
N 380 740 420 740 {lab=B1}
N 380 760 420 760 {lab=B2}
N 380 780 420 780 {lab=B3}
N 380 800 420 800 {lab=B4}
N 380 820 420 820 {lab=B5}
N 380 840 420 840 {lab=B6}
N 380 860 420 860 {lab=B7}
N 380 980 420 980 {lab=SLP}
N 380 960 420 960 {lab=VDD}
N 380 1000 420 1000 {lab=VSS}
N 380 1020 420 1020 {lab=BT}
N 380 1040 420 1040 {lab=B0}
N 380 1060 420 1060 {lab=B1}
N 380 1080 420 1080 {lab=B2}
N 380 1100 420 1100 {lab=B3}
N 380 1120 420 1120 {lab=B4}
N 380 1140 420 1140 {lab=B5}
N 380 1160 420 1160 {lab=B6}
N 380 1180 420 1180 {lab=B7}
N 860 960 860 1090 {lab=VOUT3}
N 860 1170 860 1190 {lab=VSS}
N 820 1190 860 1190 {lab=VSS}
N 820 960 900 960 {lab=VOUT3}
N 720 960 820 960 {lab=VOUT3}
N 820 1130 820 1190 {lab=VSS}
N 820 1130 840 1130 {lab=VSS}
C {devices/ipin.sym} 380 400 0 0 {name=p1 lab=B0
}
C {devices/ipin.sym} 380 420 0 0 {name=p2 lab=B1}
C {devices/ipin.sym} 380 440 0 0 {name=p3 lab=B2}
C {devices/ipin.sym} 380 460 0 0 {name=p4 lab=B3
}
C {devices/ipin.sym} 380 340 0 0 {name=p5 lab=SLP}
C {LELO_TORD_SKY130A/dac_v3.sym} 570 430 0 0 {name=x1}
C {devices/ipin.sym} 380 480 0 0 {name=p7 lab=B4}
C {devices/ipin.sym} 380 500 0 0 {name=p13 lab=B5}
C {devices/ipin.sym} 380 520 0 0 {name=p16 lab=B6}
C {devices/ipin.sym} 380 540 0 0 {name=p17 lab=B7}
C {devices/ipin.sym} 380 380 0 0 {name=p6 lab=BT
}
C {devices/ipin.sym} 380 360 0 0 {name=p8 lab=VSS}
C {devices/ipin.sym} 380 320 0 0 {name=p9 lab=VDD}
C {devices/opin.sym} 900 640 0 0 {name=p10 lab=VOUT2}
C {LELO_TORD_SKY130A/dac_v3.sym} 570 750 0 0 {name=x2}
C {LELO_TORD_SKY130A/dac_v3.sym} 570 1070 0 0 {name=x3}
C {devices/opin.sym} 900 320 0 0 {name=p11 lab=VOUT1}
C {sky130_fd_pr/pnp_05v5.sym} 840 500 0 0 {name=Q1
model=pnp_05v5_W3p40L3p40
m=1
spiceprefix=X
}
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 860 770 1 0 {name=x4 }
C {devices/lab_wire.sym} 800 550 0 0 {name=p12 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 820 870 0 0 {name=p14 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 900 960 0 0 {name=p15 lab=VOUT3}
C {devices/lab_wire.sym} 820 1190 0 0 {name=p18 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 380 640 0 0 {name=p19 sig_type=std_logic lab=VDD}
C {devices/lab_pin.sym} 380 660 0 0 {name=p20 sig_type=std_logic lab=SLP}
C {devices/lab_pin.sym} 380 680 0 0 {name=p21 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 380 700 0 0 {name=p22 sig_type=std_logic lab=BT}
C {devices/lab_pin.sym} 380 720 0 0 {name=p23 sig_type=std_logic lab=B0}
C {devices/lab_pin.sym} 380 740 0 0 {name=p24 sig_type=std_logic lab=B1}
C {devices/lab_pin.sym} 380 760 0 0 {name=p25 sig_type=std_logic lab=B2}
C {devices/lab_pin.sym} 380 780 0 0 {name=p26 sig_type=std_logic lab=B3}
C {devices/lab_pin.sym} 380 800 0 0 {name=p27 sig_type=std_logic lab=B4}
C {devices/lab_pin.sym} 380 820 0 0 {name=p28 sig_type=std_logic lab=B5}
C {devices/lab_pin.sym} 380 840 0 0 {name=p29 sig_type=std_logic lab=B6}
C {devices/lab_pin.sym} 380 860 0 0 {name=p30 sig_type=std_logic lab=B7}
C {devices/lab_pin.sym} 380 960 0 0 {name=p31 sig_type=std_logic lab=VDD}
C {devices/lab_pin.sym} 380 980 0 0 {name=p32 sig_type=std_logic lab=SLP}
C {devices/lab_pin.sym} 380 1000 0 0 {name=p33 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 380 1020 0 0 {name=p34 sig_type=std_logic lab=BT}
C {devices/lab_pin.sym} 380 1040 0 0 {name=p35 sig_type=std_logic lab=B0}
C {devices/lab_pin.sym} 380 1060 0 0 {name=p36 sig_type=std_logic lab=B1}
C {devices/lab_pin.sym} 380 1080 0 0 {name=p37 sig_type=std_logic lab=B2}
C {devices/lab_pin.sym} 380 1100 0 0 {name=p38 sig_type=std_logic lab=B3}
C {devices/lab_pin.sym} 380 1120 0 0 {name=p39 sig_type=std_logic lab=B4}
C {devices/lab_pin.sym} 380 1140 0 0 {name=p40 sig_type=std_logic lab=B5}
C {devices/lab_pin.sym} 380 1160 0 0 {name=p41 sig_type=std_logic lab=B6}
C {devices/lab_pin.sym} 380 1180 0 0 {name=p42 sig_type=std_logic lab=B7}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 860 1090 1 0 {name=x5 }
