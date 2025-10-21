v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 220 140 300 140 {lab=CLK}
N 340 60 340 100 {lab=VDD}
N 340 180 340 220 {lab=VSS}
N 220 100 240 100 {lab=VDD}
N 210 280 240 280 {lab=VSS}
N 380 140 460 140 {lab=#net1}
N 500 60 500 100 {lab=VDD}
N 500 180 500 220 {lab=VSS}
N 540 140 620 140 {lab=A}
N 660 60 660 100 {lab=VDD}
N 660 180 660 220 {lab=VSS}
N 700 140 780 140 {lab=#net2}
N 820 60 820 100 {lab=VDD}
N 820 180 820 220 {lab=VSS}
N 860 140 940 140 {lab=B}
N 980 60 980 100 {lab=VDD}
N 980 180 980 220 {lab=VSS}
N 1020 140 1100 140 {lab=#net3}
N 1140 60 1140 100 {lab=VDD}
N 1140 180 1140 220 {lab=VSS}
N 1180 140 1260 140 {lab=C}
N 1300 60 1300 100 {lab=VDD}
N 1300 180 1300 220 {lab=VSS}
N 1340 140 1420 140 {lab=#net4}
N 1460 60 1460 100 {lab=VDD}
N 1460 180 1460 220 {lab=VSS}
N 1490 140 1540 140 {lab=D}
N 260 140 260 840 {lab=CLK}
N 930 300 970 300 {lab=VSS}
N 810 300 850 300 {lab=VDD}
N 900 140 900 260 {lab=B}
N 880 220 880 260 {lab=d1}
N 890 350 890 390 {lab=D1andB}
N 610 300 650 300 {lab=VSS}
N 490 300 530 300 {lab=VDD}
N 560 220 560 260 {lab=d0}
N 580 140 580 260 {lab=A}
N 570 350 570 390 {lab=D0andA}
N 770 470 810 470 {lab=VSS}
N 650 470 690 470 {lab=VDD}
N 730 520 730 560 {lab=AorB}
N 740 390 740 430 {lab=D1andB}
N 720 390 720 430 {lab=D0andA}
N 1090 640 1130 640 {lab=VSS}
N 970 640 1010 640 {lab=VDD}
N 1050 690 1050 730 {lab=R}
N 1040 560 1040 600 {lab=AorB}
N 1060 560 1060 600 {lab=CorD}
N 570 390 720 390 {lab=D0andA}
N 740 390 890 390 {lab=D1andB}
N 730 560 1040 560 {lab=AorB}
N 1060 560 1370 560 {lab=CorD}
N 1570 300 1610 300 {lab=VSS}
N 1450 300 1490 300 {lab=VDD}
N 1540 140 1540 260 {lab=D}
N 1520 220 1520 260 {lab=d3}
N 1530 350 1530 390 {lab=D3andD}
N 1250 300 1290 300 {lab=VSS}
N 1130 300 1170 300 {lab=VDD}
N 1200 220 1200 260 {lab=d2}
N 1220 140 1220 260 {lab=C}
N 1210 350 1210 390 {lab=D2andC}
N 1410 470 1450 470 {lab=VSS}
N 1290 470 1330 470 {lab=VDD}
N 1370 520 1370 560 {lab=CorD}
N 1380 390 1380 430 {lab=D3andD}
N 1360 390 1360 430 {lab=D2andC}
N 1210 390 1360 390 {lab=D2andC}
N 1380 390 1530 390 {lab=D3andD}
N 220 180 240 180 {lab=d0}
N 220 220 240 220 {lab=d2}
N 220 200 240 200 {lab=d1}
N 220 240 240 240 {lab=d3}
N 260 840 1280 840 {lab=CLK}
N 1050 730 1160 730 {lab=R}
N 1240 730 1320 730 {lab=R_n}
N 1200 770 1200 810 {lab=VSS}
N 1200 650 1200 690 {lab=VDD}
N 1280 750 1280 840 {lab=CLK}
N 1280 750 1320 750 {lab=CLK}
N 1360 780 1360 820 {lab=VSS}
N 1360 660 1360 700 {lab=VDD}
N 1410 740 1490 740 {lab=Q}
C {devices/ipin.sym} 220 140 0 0 {name=p1 lab=CLK}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 300 140 0 0 {name=x1 }
C {devices/ipin.sym} 220 100 0 0 {name=p2 lab=VDD}
C {devices/ipin.sym} 220 280 0 0 {name=p3 lab=VSS}
C {devices/lab_wire.sym} 340 80 0 0 {name=p4 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 340 200 2 1 {name=p5 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 460 140 0 0 {name=x2 }
C {devices/lab_wire.sym} 500 80 0 0 {name=p6 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 500 200 2 1 {name=p7 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 620 140 0 0 {name=x3 }
C {devices/lab_wire.sym} 660 80 0 0 {name=p8 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 660 200 2 1 {name=p9 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 780 140 0 0 {name=x4 }
C {devices/lab_wire.sym} 820 80 0 0 {name=p10 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 820 200 2 1 {name=p11 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 940 140 0 0 {name=x5 }
C {devices/lab_wire.sym} 980 80 0 0 {name=p12 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 980 200 2 1 {name=p13 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 1100 140 0 0 {name=x6 }
C {devices/lab_wire.sym} 1140 80 0 0 {name=p14 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 1140 200 2 1 {name=p15 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 1260 140 0 0 {name=x7 }
C {devices/lab_wire.sym} 1300 80 0 0 {name=p16 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 1300 200 2 1 {name=p17 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 1420 140 0 0 {name=x8 }
C {devices/lab_wire.sym} 1460 80 0 0 {name=p18 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 1460 200 2 1 {name=p19 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 570 140 0 1 {name=p20 sig_type=std_logic lab=A}
C {devices/lab_wire.sym} 890 140 0 1 {name=p21 sig_type=std_logic lab=B}
C {devices/lab_wire.sym} 1210 140 0 1 {name=p22 sig_type=std_logic lab=C}
C {devices/lab_wire.sym} 1530 140 0 1 {name=p23 sig_type=std_logic lab=D}
C {JNW_TR_SKY130A/JNWTR_ANX1_CV.sym} 1220 260 3 1 {name=x11 }
C {devices/lab_wire.sym} 950 300 1 0 {name=p28 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 830 300 3 1 {name=p29 sig_type=std_logic lab=VDD}
C {JNW_TR_SKY130A/JNWTR_ANX1_CV.sym} 580 260 3 1 {name=x9 }
C {devices/lab_wire.sym} 630 300 0 1 {name=p25 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 510 300 0 0 {name=p31 sig_type=std_logic lab=VDD}
C {JNW_TR_SKY130A/JNWTR_ORX1_CV.sym} 1060 600 3 1 {name=x17 }
C {devices/lab_wire.sym} 790 470 0 1 {name=p41 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 670 470 0 0 {name=p42 sig_type=std_logic lab=VDD}
C {JNW_TR_SKY130A/JNWTR_ORX1_CV.sym} 1380 430 3 1 {name=x14 }
C {JNW_TR_SKY130A/JNWTR_ANX1_CV.sym} 900 260 3 1 {name=x10 }
C {devices/lab_wire.sym} 1590 300 1 0 {name=p24 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1470 300 3 1 {name=p26 sig_type=std_logic lab=VDD}
C {JNW_TR_SKY130A/JNWTR_ANX1_CV.sym} 1540 260 3 1 {name=x12 }
C {devices/lab_wire.sym} 1270 300 0 1 {name=p27 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1150 300 0 0 {name=p30 sig_type=std_logic lab=VDD}
C {JNW_TR_SKY130A/JNWTR_ORX1_CV.sym} 740 430 3 1 {name=x13 }
C {devices/lab_wire.sym} 1430 470 0 1 {name=p32 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1310 470 0 0 {name=p33 sig_type=std_logic lab=VDD}
C {devices/ipin.sym} 220 180 0 0 {name=p36 lab=d0}
C {devices/ipin.sym} 220 220 0 0 {name=p37 lab=d2}
C {devices/ipin.sym} 220 200 0 0 {name=p38 lab=d1}
C {devices/ipin.sym} 220 240 0 0 {name=p39 lab=d3}
C {devices/lab_wire.sym} 560 250 0 0 {name=p40 sig_type=std_logic lab=d0}
C {devices/lab_wire.sym} 880 250 0 0 {name=p43 sig_type=std_logic lab=d1}
C {devices/lab_wire.sym} 1200 250 0 0 {name=p44 sig_type=std_logic lab=d2}
C {devices/lab_wire.sym} 1520 250 0 0 {name=p45 sig_type=std_logic lab=d3}
C {devices/lab_wire.sym} 1110 640 0 1 {name=p34 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 990 640 0 0 {name=p35 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 1030 560 0 0 {name=p52 sig_type=std_logic lab=AorB}
C {devices/lab_wire.sym} 1070 560 0 1 {name=p53 sig_type=std_logic lab=CorD}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 1160 730 0 0 {name=x15 }
C {devices/lab_wire.sym} 1200 790 2 0 {name=p46 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1200 670 0 1 {name=p47 sig_type=std_logic lab=VDD}
C {JNW_TR_SKY130A/JNWTR_ANX1_CV.sym} 1320 750 0 0 {name=x16 }
C {devices/lab_wire.sym} 1360 800 2 0 {name=p48 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1360 680 0 1 {name=p49 sig_type=std_logic lab=VDD}
C {devices/opin.sym} 1490 740 0 0 {name=p50 lab=Q}
C {devices/lab_wire.sym} 1110 730 0 1 {name=p51 sig_type=std_logic lab=R}
C {devices/lab_wire.sym} 1270 730 0 1 {name=p54 sig_type=std_logic lab=R_n}
C {devices/lab_wire.sym} 670 390 0 1 {name=p55 sig_type=std_logic lab=D0andA}
C {devices/lab_wire.sym} 750 390 0 1 {name=p56 sig_type=std_logic lab=D1andB}
C {devices/lab_wire.sym} 1310 390 0 1 {name=p57 sig_type=std_logic lab=D2andC}
C {devices/lab_wire.sym} 1390 390 0 1 {name=p58 sig_type=std_logic lab=D3andD}
