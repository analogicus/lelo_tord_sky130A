v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 620 380 660 380 {lab=SLEEP}
N 700 410 700 450 {lab=V1}
N 700 380 740 380 {lab=VDD}
N 740 330 740 380 {lab=VDD}
N 660 1090 680 1090 {lab=VSS}
N 660 1210 680 1210 {lab=VSS}
N 700 1130 700 1170 {lab=V7}
N 740 1320 880 1320 {lab=NBIAS}
N 820 1320 820 1360 {lab=NBIAS}
N 820 1420 820 1440 {lab=VSS}
N 700 1350 700 1440 {lab=VSS}
N 920 1350 920 1440 {lab=VSS}
N 620 1440 920 1440 {lab=VSS}
N 760 1270 760 1320 {lab=NBIAS}
N 920 410 920 430 {lab=PBIAS}
N 820 330 820 350 {lab=PBIAS}
N 660 250 920 250 {lab=VDD}
N 860 380 880 380 {lab=PBIAS}
N 740 300 780 300 {lab=SLEEP_N}
N 820 300 860 300 {lab=VDD}
N 920 380 960 380 {lab=VDD}
N 860 380 860 430 {lab=PBIAS}
N 860 430 920 430 {lab=PBIAS}
N 960 330 960 380 {lab=VDD}
N 820 250 820 270 {lab=VDD}
N 380 1320 420 1320 {lab=SLEEP}
N 460 1360 460 1400 {lab=VSS}
N 460 1240 460 1280 {lab=VDD}
N 500 1320 540 1320 {lab=SLEEP_N}
N 1000 1150 1040 1150 {lab=PBIAS}
N 1000 1170 1040 1170 {lab=NBIAS}
N 460 1140 500 1140 {lab=VDD}
N 460 1160 500 1160 {lab=SLEEP}
N 460 1180 500 1180 {lab=VSS}
N 740 1390 780 1390 {lab=SLEEP}
N 700 1270 760 1270 {lab=NBIAS}
N 700 1250 700 1290 {lab=NBIAS}
N 820 1390 860 1390 {lab=VSS}
N 860 1390 860 1440 {lab=VSS}
N 660 1320 700 1320 {lab=VSS}
N 920 1320 960 1320 {lab=VSS}
N 960 1320 960 1370 {lab=VSS}
N 920 1370 960 1370 {lab=VSS}
N 700 330 740 330 {lab=VDD}
N 700 250 700 350 {lab=VDD}
N 920 330 960 330 {lab=VDD}
N 920 250 920 350 {lab=VDD}
N 820 350 820 380 {lab=PBIAS}
N 820 380 860 380 {lab=PBIAS}
N 860 250 860 300 {lab=VDD}
N 920 430 920 1290 {lab=#net1}
N 660 850 680 850 {lab=VSS}
N 660 970 680 970 {lab=VSS}
N 700 890 700 930 {lab=V5}
N 700 1010 700 1050 {lab=V6}
N 660 610 680 610 {lab=VSS}
N 660 730 680 730 {lab=VSS}
N 700 650 700 690 {lab=V3}
N 700 770 700 810 {lab=V4}
N 660 490 680 490 {lab=VSS}
N 700 530 700 570 {lab=V2}
N 660 1320 660 1440 {lab=VSS}
N 660 1210 660 1320 {lab=VSS}
N 660 1090 660 1210 {lab=VSS}
N 660 970 660 1090 {lab=VSS}
N 660 850 660 970 {lab=VSS}
N 660 730 660 850 {lab=VSS}
N 660 610 660 730 {lab=VSS}
N 660 490 660 610 {lab=VSS}
C {JNW_ATR_SKY130A/JNWATR_PCH_2C5F0.sym} 660 380 0 0 {name=x1 }
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 1130 1 1 {name=x2}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 1250 1 1 {name=x3}
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} 740 1320 0 1 {name=x5 }
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} 880 1320 0 0 {name=x6 }
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} 780 1390 0 0 {name=x7 }
C {JNW_ATR_SKY130A/JNWATR_PCH_2C5F0.sym} 880 380 0 0 {name=x8 }
C {JNW_ATR_SKY130A/JNWATR_PCH_2C5F0.sym} 780 300 0 0 {name=x9 }
C {devices/lab_wire.sym} 630 1440 0 0 {name=p1 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 690 250 0 0 {name=p2 sig_type=std_logic lab=VDD}
C {devices/ipin.sym} 460 1140 0 0 {name=p3 lab=VDD}
C {devices/ipin.sym} 460 1160 0 0 {name=p4 lab=SLEEP}
C {devices/ipin.sym} 460 1180 0 0 {name=p6 lab=VSS}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 420 1320 0 0 {name=x10 }
C {devices/lab_wire.sym} 410 1320 0 0 {name=p7 sig_type=std_logic lab=SLEEP}
C {devices/lab_wire.sym} 510 1320 0 1 {name=p8 sig_type=std_logic lab=SLEEP_N}
C {devices/lab_wire.sym} 460 1390 0 0 {name=p9 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 460 1270 0 0 {name=p10 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 650 380 0 0 {name=p11 sig_type=std_logic lab=SLEEP}
C {devices/opin.sym} 1040 1150 0 0 {name=p13 lab=PBIAS}
C {devices/opin.sym} 1040 1170 0 0 {name=p14 lab=NBIAS}
C {devices/lab_wire.sym} 760 1270 0 1 {name=p15 sig_type=std_logic lab=NBIAS}
C {devices/lab_wire.sym} 860 430 2 1 {name=p16 sig_type=std_logic lab=PBIAS}
C {devices/lab_wire.sym} 700 440 0 1 {name=p5 sig_type=std_logic lab=V1}
C {devices/lab_wire.sym} 700 1040 0 1 {name=p17 sig_type=std_logic lab=V6}
C {devices/lab_wire.sym} 770 1390 0 0 {name=p20 sig_type=std_logic lab=SLEEP}
C {devices/lab_wire.sym} 770 300 0 0 {name=p12 sig_type=std_logic lab=SLEEP_N}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 890 1 1 {name=x4}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 1010 1 1 {name=x11}
C {devices/lab_wire.sym} 700 800 0 1 {name=p18 sig_type=std_logic lab=V4}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 650 1 1 {name=x12}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 770 1 1 {name=x13}
C {devices/lab_wire.sym} 700 560 0 1 {name=p19 sig_type=std_logic lab=V2}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 530 1 1 {name=x14}
C {devices/lab_wire.sym} 700 440 0 1 {name=p21 sig_type=std_logic lab=V1}
C {devices/lab_wire.sym} 700 680 0 1 {name=p22 sig_type=std_logic lab=V3}
C {devices/lab_wire.sym} 700 920 0 1 {name=p23 sig_type=std_logic lab=V5}
C {devices/lab_wire.sym} 700 1160 0 1 {name=p24 sig_type=std_logic lab=V7}
