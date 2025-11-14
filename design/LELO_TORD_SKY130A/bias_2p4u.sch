v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 580 320 620 320 {lab=SLEEP}
N 660 350 660 390 {lab=V1}
N 660 320 700 320 {lab=VDD}
N 700 270 700 320 {lab=VDD}
N 620 430 640 430 {lab=VSS}
N 620 550 640 550 {lab=VSS}
N 620 670 640 670 {lab=VSS}
N 660 590 660 630 {lab=V3}
N 660 470 660 510 {lab=V2}
N 700 1140 840 1140 {lab=NBIAS}
N 780 1140 780 1180 {lab=NBIAS}
N 780 1240 780 1260 {lab=VSS}
N 660 1170 660 1260 {lab=VSS}
N 880 1170 880 1260 {lab=VSS}
N 580 1260 880 1260 {lab=VSS}
N 620 430 620 1260 {lab=VSS}
N 720 1090 720 1140 {lab=NBIAS}
N 880 350 880 370 {lab=PBIAS}
N 780 270 780 290 {lab=PBIAS}
N 620 190 880 190 {lab=VDD}
N 820 320 840 320 {lab=PBIAS}
N 700 240 740 240 {lab=SLEEP_N}
N 780 240 820 240 {lab=VDD}
N 880 320 920 320 {lab=VDD}
N 820 320 820 370 {lab=PBIAS}
N 820 370 880 370 {lab=PBIAS}
N 920 270 920 320 {lab=VDD}
N 780 190 780 210 {lab=VDD}
N 880 370 880 1110 {lab=PBIAS}
N 330 680 370 680 {lab=SLEEP}
N 410 720 410 760 {lab=VSS}
N 410 600 410 640 {lab=VDD}
N 450 680 490 680 {lab=SLEEP_N}
N 980 510 1020 510 {lab=PBIAS}
N 980 530 1020 530 {lab=NBIAS}
N 410 500 450 500 {lab=VDD}
N 410 520 450 520 {lab=SLEEP}
N 410 540 450 540 {lab=VSS}
N 700 1210 740 1210 {lab=SLEEP}
N 660 1090 720 1090 {lab=NBIAS}
N 620 1030 640 1030 {lab=VSS}
N 660 710 660 750 {lab=V4}
N 660 950 660 990 {lab=V6}
N 660 830 660 870 {lab=V5}
N 660 1070 660 1110 {lab=NBIAS}
N 620 790 640 790 {lab=VSS}
N 620 910 640 910 {lab=VSS}
N 780 1210 820 1210 {lab=VSS}
N 820 1210 820 1260 {lab=VSS}
N 620 1140 660 1140 {lab=VSS}
N 880 1140 920 1140 {lab=VSS}
N 920 1140 920 1190 {lab=VSS}
N 880 1190 920 1190 {lab=VSS}
N 660 270 700 270 {lab=VDD}
N 660 190 660 290 {lab=VDD}
N 880 270 920 270 {lab=VDD}
N 880 190 880 290 {lab=VDD}
N 780 290 780 320 {lab=PBIAS}
N 780 320 820 320 {lab=PBIAS}
N 820 190 820 240 {lab=VDD}
C {JNW_ATR_SKY130A/JNWATR_PCH_2C5F0.sym} 620 320 0 0 {name=x1 }
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 660 470 1 1 {name=x2}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 660 590 1 1 {name=x3}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 660 710 1 1 {name=x4}
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} 700 1140 0 1 {name=x5 }
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} 840 1140 0 0 {name=x6 }
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} 740 1210 0 0 {name=x7 }
C {JNW_ATR_SKY130A/JNWATR_PCH_2C5F0.sym} 840 320 0 0 {name=x8 }
C {JNW_ATR_SKY130A/JNWATR_PCH_2C5F0.sym} 740 240 0 0 {name=x9 }
C {devices/lab_wire.sym} 590 1260 0 0 {name=p1 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 650 190 0 0 {name=p2 sig_type=std_logic lab=VDD}
C {devices/ipin.sym} 410 500 0 0 {name=p3 lab=VDD}
C {devices/ipin.sym} 410 520 0 0 {name=p4 lab=SLEEP}
C {devices/ipin.sym} 410 540 0 0 {name=p6 lab=VSS}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 370 680 0 0 {name=x10 }
C {devices/lab_wire.sym} 360 680 0 0 {name=p7 sig_type=std_logic lab=SLEEP}
C {devices/lab_wire.sym} 460 680 0 1 {name=p8 sig_type=std_logic lab=SLEEP_N}
C {devices/lab_wire.sym} 410 750 0 0 {name=p9 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 410 630 0 0 {name=p10 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 610 320 0 0 {name=p11 sig_type=std_logic lab=SLEEP}
C {devices/opin.sym} 1020 510 0 0 {name=p13 lab=PBIAS}
C {devices/opin.sym} 1020 530 0 0 {name=p14 lab=NBIAS}
C {devices/lab_wire.sym} 720 1090 0 1 {name=p15 sig_type=std_logic lab=NBIAS}
C {devices/lab_wire.sym} 820 370 2 1 {name=p16 sig_type=std_logic lab=PBIAS}
C {devices/lab_wire.sym} 660 380 0 1 {name=p5 sig_type=std_logic lab=V1}
C {devices/lab_wire.sym} 660 500 0 1 {name=p17 sig_type=std_logic lab=V2}
C {devices/lab_wire.sym} 660 620 0 1 {name=p18 sig_type=std_logic lab=V3}
C {devices/lab_wire.sym} 730 1210 0 0 {name=p20 sig_type=std_logic lab=SLEEP}
C {devices/lab_wire.sym} 730 240 0 0 {name=p12 sig_type=std_logic lab=SLEEP_N}
C {JNW_TR_SKY130A/JNWTR_RPPO8.sym} 660 990 1 0 {name=x11 }
C {JNW_TR_SKY130A/JNWTR_RPPO4.sym} 660 870 1 0 {name=x12 }
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 660 750 1 0 {name=x13 }
C {devices/lab_wire.sym} 660 740 0 1 {name=p19 sig_type=std_logic lab=V4}
C {devices/lab_wire.sym} 660 860 0 1 {name=p21 sig_type=std_logic lab=V5}
C {devices/lab_wire.sym} 660 980 0 1 {name=p22 sig_type=std_logic lab=V6}
