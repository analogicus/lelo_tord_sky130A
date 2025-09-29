v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 390 -300 480 -300 {lab=#net1}
N 790 -230 830 -230 {lab=CMP}
N 480 -200 570 -200 {lab=REF}
N 480 -200 480 -160 {lab=REF}
N 190 -160 480 -160 {lab=REF}
N 480 -300 480 -260 {lab=#net1}
N 480 -260 570 -260 {lab=#net1}
N 190 -220 230 -220 {lab=VSS}
N 190 -240 230 -240 {lab=RST}
N 190 -260 230 -260 {lab=SEL_C2}
N 190 -280 230 -280 {lab=SEL_C1}
N 190 -300 230 -300 {lab=IPTAT}
N 190 -320 230 -320 {lab=VDD}
N 630 -340 630 -320 {lab=VDD}
N 650 -360 650 -310 {lab=SLEEP}
N 670 -380 670 -300 {lab=PBIAS}
N 690 -400 690 -290 {lab=NBIAS}
N 670 -160 670 -80 {lab=CMP_P2}
N 650 -150 650 -100 {lab=CMP_P1}
N 630 -140 630 -120 {lab=VSS}
N 630 -400 690 -400 {lab=NBIAS}
N 630 -380 670 -380 {lab=PBIAS}
N 630 -360 650 -360 {lab=SLEEP}
N 630 -100 650 -100 {lab=CMP_P1}
N 630 -80 670 -80 {lab=CMP_P2}
N 620 -120 630 -120 {lab=VSS}
N 620 -340 630 -340 {lab=VDD}
C {LELO_TORD_SKY130A/tmp_core.sym} 310 -270 0 0 {name=x1}
C {LELO_TORD_SKY130A/cmp.sym} 670 -230 0 0 {name=x2}
C {devices/ipin.sym} 190 -320 2 1 {name=p1 lab=VDD}
C {devices/ipin.sym} 190 -300 0 0 {name=p2 lab=IPTAT}
C {devices/ipin.sym} 190 -280 0 0 {name=p3 lab=SEL_C1}
C {devices/ipin.sym} 190 -260 0 0 {name=p4 lab=SEL_C2}
C {devices/ipin.sym} 190 -240 0 0 {name=p5 lab=RST}
C {devices/ipin.sym} 190 -220 0 0 {name=p6 lab=VSS}
C {devices/ipin.sym} 190 -160 0 0 {name=p7 lab=REF}
C {devices/opin.sym} 830 -230 0 0 {name=p15 lab=CMP}
C {devices/ipin.sym} 630 -360 2 1 {name=p9 lab=SLEEP}
C {devices/ipin.sym} 630 -380 2 1 {name=p16 lab=PBIAS}
C {devices/ipin.sym} 630 -400 2 1 {name=p17 lab=NBIAS}
C {devices/ipin.sym} 630 -100 2 1 {name=p10 lab=CMP_P1}
C {devices/ipin.sym} 630 -80 2 1 {name=p11 lab=CMP_P2}
C {devices/lab_pin.sym} 620 -120 0 0 {name=p12 sig_type=std_logic lab=VSS}
C {devices/lab_pin.sym} 620 -340 0 0 {name=p8 sig_type=std_logic lab=VDD}
