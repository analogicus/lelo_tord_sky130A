v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 600 -750 700 -750 {lab=VG3}
N 560 -720 560 -640 {lab=VG3}
N 600 -610 700 -610 {lab=VG2}
N 620 -750 620 -690 {lab=VG3}
N 680 -670 680 -610 {lab=VG2}
N 680 -670 740 -670 {lab=VG2}
N 560 -800 560 -780 {lab=VDD}
N 520 -800 740 -800 {lab=VDD}
N 600 -470 700 -470 {lab=VG1}
N 680 -530 680 -470 {lab=VG1}
N 560 -440 560 -400 {lab=VR}
N 740 -800 740 -780 {lab=VDD}
N 540 -610 560 -610 {lab=VSS}
N 540 -750 560 -750 {lab=VDD}
N 740 -750 760 -750 {lab=VDD}
N 740 -470 760 -470 {lab=VSS}
N 680 -530 740 -530 {lab=VG1}
N 520 -280 740 -280 {lab=VSS}
N 740 -440 740 -280 {lab=VSS}
N 560 -320 560 -280 {lab=VSS}
N 540 -470 560 -470 {lab=VSS}
N 740 -610 760 -610 {lab=VSS}
N 520 -360 540 -360 {lab=VSS}
N 740 -580 740 -500 {lab=VG1}
N 560 -690 620 -690 {lab=VG3}
N 560 -580 560 -500 {lab=V1}
N 200 -590 240 -590 {lab=SPARK}
N 280 -660 280 -620 {lab=VG3}
N 280 -560 280 -500 {lab=VSS}
N 280 -590 330 -590 {lab=VSS}
N 330 -590 330 -540 {lab=VSS}
N 280 -540 330 -540 {lab=VSS}
N 740 -720 740 -640 {lab=VG2}
N 740 -540 790 -540 {lab=VG1}
C {devices/ipin.sym} 520 -800 0 0 {name=p1 lab=VDD}
C {devices/ipin.sym} 520 -280 0 0 {name=p2 lab=VSS}
C {devices/lab_wire.sym} 540 -750 0 0 {name=p3 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 760 -750 0 1 {name=p4 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 540 -610 2 1 {name=p5 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 760 -610 2 0 {name=p6 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 540 -470 2 1 {name=p7 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 760 -470 2 0 {name=p8 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 520 -360 2 1 {name=p9 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 690 -670 2 0 {name=p11 sig_type=std_logic lab=VG2}
C {devices/lab_wire.sym} 610 -690 0 0 {name=p12 sig_type=std_logic lab=VG3}
C {devices/lab_wire.sym} 560 -430 2 0 {name=p13 sig_type=std_logic lab=VR}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 700 -470 0 0 {name=x1 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 600 -470 0 1 {name=x2[3:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 700 -610 0 0 {name=x3 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 600 -610 0 1 {name=x4 }
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 700 -750 0 0 {name=x5 }
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 600 -750 0 1 {name=x6 }
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 560 -320 1 1 {name=x7}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 240 -590 0 0 {name=x8}
C {devices/lab_wire.sym} 280 -500 2 1 {name=p23 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 280 -660 0 0 {name=p22 sig_type=std_logic lab=VG3}
C {devices/ipin.sym} 200 -590 0 0 {name=p21 lab=SPARK}
C {devices/opin.sym} 790 -540 0 0 {name=p14 lab=VBIAS}
C {devices/lab_wire.sym} 560 -550 2 0 {name=p10 sig_type=std_logic lab=V1}
