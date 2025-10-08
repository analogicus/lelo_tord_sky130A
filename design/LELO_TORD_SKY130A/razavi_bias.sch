v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 620 -630 700 -630 {lab=VG2}
N 740 -600 740 -490 {lab=VG1}
N 580 -440 580 -400 {lab=VR}
N 740 -690 740 -660 {lab=VDD}
N 580 -690 580 -660 {lab=VDD}
N 640 -630 640 -570 {lab=VG2}
N 580 -570 640 -570 {lab=VG2}
N 680 -530 740 -530 {lab=VG1}
N 740 -630 780 -630 {lab=VDD}
N 780 -690 780 -630 {lab=VDD}
N 540 -630 580 -630 {lab=VDD}
N 540 -690 540 -630 {lab=VDD}
N 740 -470 780 -470 {lab=VSS}
N 540 -470 580 -470 {lab=VSS}
N 540 -470 540 -280 {lab=VSS}
N 500 -280 780 -280 {lab=VSS}
N 620 -470 700 -470 {lab=VG1}
N 580 -320 580 -280 {lab=VSS}
N 740 -440 740 -280 {lab=VSS}
N 540 -360 560 -360 {lab=VSS}
N 780 -470 780 -280 {lab=VSS}
N 500 -690 780 -690 {lab=VDD}
N 330 -530 370 -530 {lab=SPARK}
N 410 -600 410 -560 {lab=VG1}
N 410 -500 410 -440 {lab=VSS}
N 410 -530 460 -530 {lab=VSS}
N 460 -530 460 -480 {lab=VSS}
N 410 -480 460 -480 {lab=VSS}
N 580 -600 580 -500 {lab=VG2}
N 680 -530 680 -470 {lab=VG1}
N 740 -540 810 -540 {lab=VG1}
C {devices/ipin.sym} 500 -280 0 0 {name=p1 lab=VSS}
C {devices/ipin.sym} 500 -690 0 0 {name=p2 lab=VDD}
C {devices/lab_wire.sym} 630 -570 0 0 {name=p4 sig_type=std_logic lab=VG2}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 620 -630 0 1 {name=x1[3:0]}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 700 -630 0 0 {name=x2 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 620 -470 0 1 {name=x3}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 700 -470 0 0 {name=x4 }
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 580 -320 1 1 {name=x5}
C {devices/lab_wire.sym} 580 -430 2 0 {name=p7 sig_type=std_logic lab=VR}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 370 -530 0 0 {name=x8}
C {devices/lab_wire.sym} 410 -440 2 1 {name=p23 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 410 -600 0 0 {name=p8 sig_type=std_logic lab=VG1}
C {devices/ipin.sym} 330 -530 0 0 {name=p21 lab=SPARK}
C {devices/opin.sym} 810 -540 0 0 {name=p5 lab=VG1}
