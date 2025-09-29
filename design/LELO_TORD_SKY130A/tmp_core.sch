v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 780 585 780 620 {lab=VSS}
N 640 620 1080 620 {lab=VSS}
N 940 585 940 620 {lab=VSS}
N 640 480 640 520 {lab=VCAP1}
N 640 480 780 480 {lab=VCAP1}
N 780 480 780 515 {lab=VCAP1}
N 1080 480 1080 520 {lab=VCAP2}
N 940 480 1080 480 {lab=VCAP2}
N 940 480 940 515 {lab=VCAP2}
N 1080 580 1080 620 {lab=VSS}
N 640 580 640 620 {lab=VSS}
N 370 540 410 540 {lab=RST}
N 370 560 410 560 {lab=SEL_CAP2}
N 1310 540 1350 540 {lab=RST}
N 1310 560 1350 560 {lab=SEL_CAP1}
N 700 390 740 390 {lab=SEL_CAP1}
N 980 390 1020 390 {lab=SEL_CAP2}
N 780 300 1080 300 {lab=VPTAT}
N 780 230 820 230 {lab=RST}
N 860 260 860 300 {lab=VPTAT}
N 860 160 860 200 {lab=IPTAT}
N 1120 550 1220 550 {lab=DRAINCAP2}
N 780 300 780 340 {lab=VPTAT}
N 780 440 780 480 {lab=VCAP1}
N 940 440 940 480 {lab=VCAP2}
N 940 300 940 340 {lab=VPTAT}
N 500 550 600 550 {lab=DRAINCAP1}
N 700 420 740 420 {lab=VDD}
N 980 420 1020 420 {lab=VDD}
N 1040 600 1080 600 {lab=VSS}
N 1040 550 1040 600 {lab=VSS}
N 1040 550 1080 550 {lab=VSS}
N 640 600 680 600 {lab=VSS}
N 680 550 680 600 {lab=VSS}
N 640 550 680 550 {lab=VSS}
N 450 470 450 510 {lab=VDD}
N 450 590 450 630 {lab=VSS}
N 1270 470 1270 510 {lab=VDD}
N 1270 590 1270 630 {lab=VSS}
N 620 300 660 300 {lab=SEL_CAP2}
N 620 320 660 320 {lab=RST}
N 620 340 660 340 {lab=VSS}
N 620 280 660 280 {lab=SEL_CAP1}
N 620 260 660 260 {lab=IPTAT}
N 620 240 660 240 {lab=VDD}
N 830 420 890 420 {lab=VSS}
N 860 230 900 230 {lab=VDD}
C {devices/opin.sym} 1080 300 0 0 {name=p19 lab=VPTAT}
C {devices/ipin.sym} 620 240 0 0 {name=p59 lab=VDD}
C {devices/ipin.sym} 620 300 0 0 {name=p79 lab=SEL_CAP2}
C {devices/ipin.sym} 620 280 0 0 {name=p80 lab=SEL_CAP1}
C {devices/ipin.sym} 620 340 0 0 {name=p1 lab=VSS}
C {devices/ipin.sym} 620 260 0 0 {name=p2 lab=IPTAT}
C {JNW_TR_SKY130A/JNWTR_CAPX4.sym} 780 575 0 1 {name=x1[1:0]}
C {JNW_TR_SKY130A/JNWTR_CAPX4.sym} 940 575 0 0 {name=x2[1:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_2C1F2.sym} 600 550 0 0 {name=x1 }
C {JNW_ATR_SKY130A/JNWATR_NCH_2C1F2.sym} 1120 550 0 1 {name=x2 }
C {devices/lab_wire.sym} 860 170 0 0 {name=p4 sig_type=std_logic lab=IPTAT}
C {devices/lab_wire.sym} 810 230 0 0 {name=p5 sig_type=std_logic lab=RST}
C {JNW_TR_SKY130A/JNWTR_ORX1_CV.sym} 410 560 0 0 {name=x6 }
C {devices/lab_wire.sym} 370 540 0 0 {name=p7 sig_type=std_logic lab=RST}
C {devices/lab_wire.sym} 370 560 0 0 {name=p8 sig_type=std_logic lab=SEL_CAP2}
C {devices/lab_wire.sym} 450 500 0 1 {name=p9 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 850 620 0 1 {name=p10 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 450 600 2 0 {name=p11 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_ORX1_CV.sym} 1310 560 0 1 {name=x9 }
C {devices/lab_wire.sym} 1270 500 0 0 {name=p12 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 1270 600 2 1 {name=p13 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1350 540 0 1 {name=p14 sig_type=std_logic lab=RST}
C {devices/lab_wire.sym} 730 390 0 0 {name=p24 sig_type=std_logic lab=SEL_CAP1}
C {JNW_ATR_SKY130A/JNWATR_PCH_2C1F2.sym} 820 230 0 0 {name=x5 }
C {devices/lab_wire.sym} 870 230 0 1 {name=p20 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 990 480 0 1 {name=p18 sig_type=std_logic lab=VCAP2}
C {devices/lab_wire.sym} 730 480 0 0 {name=p21 sig_type=std_logic lab=VCAP1}
C {JNW_TR_SKY130A/JNWTR_TGX2_CV.sym} 940 330 1 0 {name=x3 }
C {JNW_TR_SKY130A/JNWTR_TGX2_CV.sym} 780 330 3 1 {name=x4 }
C {devices/lab_wire.sym} 730 420 0 0 {name=p28 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 1140 550 0 1 {name=p6 sig_type=std_logic lab=DRAINCAP2}
C {devices/lab_wire.sym} 580 550 0 0 {name=p22 sig_type=std_logic lab=DRAINCAP1}
C {devices/lab_wire.sym} 990 390 0 1 {name=p17 sig_type=std_logic lab=SEL_CAP2}
C {devices/lab_wire.sym} 1350 560 0 1 {name=p15 sig_type=std_logic lab=SEL_CAP1}
C {devices/lab_wire.sym} 850 420 0 1 {name=p25 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 990 420 0 1 {name=p26 sig_type=std_logic lab=VDD}
C {devices/ipin.sym} 620 320 0 0 {name=p3 lab=RST}
