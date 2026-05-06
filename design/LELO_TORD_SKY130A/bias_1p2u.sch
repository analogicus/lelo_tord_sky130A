v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 620 380 660 380 {lab=SLP}
N 700 410 700 450 {lab=VR1}
N 700 380 740 380 {lab=VDD}
N 740 330 740 380 {lab=VDD}
N 660 1090 680 1090 {lab=VSS}
N 660 1210 680 1210 {lab=VSS}
N 700 1130 700 1170 {lab=VR7}
N 740 1320 880 1320 {lab=VBN}
N 820 1320 820 1360 {lab=VBN}
N 820 1420 820 1440 {lab=VSS}
N 700 1350 700 1440 {lab=VSS}
N 920 1350 920 1440 {lab=VSS}
N 620 1440 920 1440 {lab=VSS}
N 760 1270 760 1320 {lab=VBN}
N 660 330 920 330 {lab=VDD}
N 860 480 880 480 {lab=VBP}
N 780 380 820 380 {lab=SLP_N}
N 860 380 920 380 {lab=VDD}
N 920 480 960 480 {lab=VDD}
N 860 530 920 530 {lab=VBP}
N 960 330 960 480 {lab=VDD}
N 860 330 860 350 {lab=VDD}
N 960 1160 1000 1160 {lab=VBP}
N 960 1180 1000 1180 {lab=VBN}
N 580 1140 620 1140 {lab=VDD}
N 580 1160 620 1160 {lab=SLP}
N 580 1200 620 1200 {lab=VSS}
N 740 1390 780 1390 {lab=SLP}
N 700 1270 760 1270 {lab=VBN}
N 700 1250 700 1290 {lab=VBN}
N 820 1390 860 1390 {lab=VSS}
N 860 1390 860 1440 {lab=VSS}
N 660 1320 700 1320 {lab=VSS}
N 920 1320 960 1320 {lab=VSS}
N 960 1320 960 1440 {lab=VSS}
N 920 1440 960 1440 {lab=VSS}
N 920 330 960 330 {lab=VDD}
N 860 410 860 530 {lab=VBP}
N 920 330 920 450 {lab=VDD}
N 920 510 920 1290 {lab=VBP}
N 660 850 680 850 {lab=VSS}
N 660 970 680 970 {lab=VSS}
N 700 890 700 930 {lab=VR5}
N 700 1010 700 1050 {lab=VR6}
N 660 610 680 610 {lab=VSS}
N 660 730 680 730 {lab=VSS}
N 700 650 700 690 {lab=VR3}
N 700 770 700 810 {lab=VR4}
N 660 490 680 490 {lab=VSS}
N 700 530 700 570 {lab=VR2}
N 660 1320 660 1440 {lab=VSS}
N 660 1210 660 1320 {lab=VSS}
N 660 1090 660 1210 {lab=VSS}
N 660 970 660 1090 {lab=VSS}
N 660 850 660 970 {lab=VSS}
N 660 730 660 850 {lab=VSS}
N 660 610 660 730 {lab=VSS}
N 660 490 660 610 {lab=VSS}
N 580 1180 620 1180 {lab=SLP_N}
N 700 330 700 350 {lab=VDD}
C {JNW_ATR_SKY130A/JNWATR_PCH_2C5F0.sym} 660 380 0 0 {name=x1 }
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 1130 1 1 {name=x2}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 1250 1 1 {name=x3}
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} 740 1320 0 1 {name=x5 }
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} 880 1320 0 0 {name=x6 }
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} 780 1390 0 0 {name=x7 }
C {JNW_ATR_SKY130A/JNWATR_PCH_2C5F0.sym} 880 480 0 0 {name=x8 }
C {JNW_ATR_SKY130A/JNWATR_PCH_2C5F0.sym} 820 380 0 0 {name=x9 }
C {devices/lab_wire.sym} 630 1440 0 0 {name=p1 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 690 330 0 0 {name=p2 sig_type=std_logic lab=VDD}
C {devices/ipin.sym} 580 1140 0 0 {name=p3 lab=VDD}
C {devices/ipin.sym} 580 1160 0 0 {name=p4 lab=SLP}
C {devices/ipin.sym} 580 1200 0 0 {name=p6 lab=VSS}
C {devices/lab_wire.sym} 650 380 0 0 {name=p11 sig_type=std_logic lab=SLP}
C {devices/opin.sym} 1000 1160 0 0 {name=p13 lab=VBP}
C {devices/opin.sym} 1000 1180 0 0 {name=p14 lab=VBN}
C {devices/lab_wire.sym} 760 1270 0 1 {name=p15 sig_type=std_logic lab=VBN}
C {devices/lab_wire.sym} 860 530 2 1 {name=p16 sig_type=std_logic lab=VBP}
C {devices/lab_wire.sym} 700 440 0 1 {name=p5 sig_type=std_logic lab=VR1}
C {devices/lab_wire.sym} 700 1040 0 1 {name=p17 sig_type=std_logic lab=VR6}
C {devices/lab_wire.sym} 770 1390 0 0 {name=p20 sig_type=std_logic lab=SLP}
C {devices/lab_wire.sym} 810 380 0 0 {name=p12 sig_type=std_logic lab=SLP_N}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 890 1 1 {name=x4}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 1010 1 1 {name=x11}
C {devices/lab_wire.sym} 700 800 0 1 {name=p18 sig_type=std_logic lab=VR4}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 650 1 1 {name=x12}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 770 1 1 {name=x13}
C {devices/lab_wire.sym} 700 560 0 1 {name=p19 sig_type=std_logic lab=VR2}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 700 530 1 1 {name=x14}
C {devices/lab_wire.sym} 700 680 0 1 {name=p22 sig_type=std_logic lab=VR3}
C {devices/lab_wire.sym} 700 920 0 1 {name=p23 sig_type=std_logic lab=VR5}
C {devices/lab_wire.sym} 700 1160 0 1 {name=p24 sig_type=std_logic lab=VR7}
C {devices/ipin.sym} 580 1180 0 0 {name=p25 lab=SLP_N}
