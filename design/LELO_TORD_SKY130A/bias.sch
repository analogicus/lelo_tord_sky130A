v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 340 130 380 130 {lab=SLEEP}
N 420 160 420 200 {lab=V1}
N 420 130 460 130 {lab=VDD}
N 460 80 460 130 {lab=VDD}
N 380 240 400 240 {lab=VSS}
N 380 360 400 360 {lab=VSS}
N 380 480 400 480 {lab=VSS}
N 420 400 420 440 {lab=V3}
N 420 280 420 320 {lab=V2}
N 460 590 620 590 {lab=NBIAS}
N 560 590 560 630 {lab=NBIAS}
N 560 690 560 730 {lab=VSS}
N 420 620 420 730 {lab=VSS}
N 660 620 660 730 {lab=VSS}
N 340 730 660 730 {lab=VSS}
N 380 240 380 730 {lab=VSS}
N 500 520 500 590 {lab=NBIAS}
N 570 160 570 180 {lab=PBIAS}
N 750 160 750 180 {lab=PBIAS}
N 570 180 750 180 {lab=PBIAS}
N 570 80 570 100 {lab=VDD}
N 380 80 750 80 {lab=VDD}
N 750 80 750 100 {lab=VDD}
N 510 130 530 130 {lab=PBIAS}
N 790 130 830 130 {lab=SLEEP_N}
N 710 130 750 130 {lab=VDD}
N 570 130 610 130 {lab=VDD}
N 510 130 510 180 {lab=PBIAS}
N 510 180 570 180 {lab=PBIAS}
N 610 80 610 130 {lab=VDD}
N 710 80 710 130 {lab=VDD}
N 660 180 660 560 {lab=PBIAS}
N 420 80 420 100 {lab=VDD}
N 90 490 130 490 {lab=SLEEP}
N 170 530 170 570 {lab=VSS}
N 170 410 170 450 {lab=VDD}
N 210 490 250 490 {lab=SLEEP_N}
N 740 320 780 320 {lab=PBIAS}
N 740 340 780 340 {lab=NBIAS}
N 170 310 210 310 {lab=VDD}
N 170 330 210 330 {lab=SLEEP}
N 170 350 210 350 {lab=VSS}
N 480 660 520 660 {lab=SLEEP}
N 420 560 500 560 {lab=NBIAS}
N 420 520 460 520 {lab=V4}
N 460 190 460 520 {lab=V4}
N 460 190 500 190 {lab=V4}
N 500 400 500 440 {lab=V6}
N 500 280 500 320 {lab=V5}
N 380 540 480 540 {lab=VSS}
N 480 240 480 540 {lab=VSS}
N 500 190 500 200 {lab=V4}
C {JNW_ATR_SKY130A/JNWATR_PCH_2C5F0.sym} 380 130 0 0 {name=x1 }
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 420 280 1 1 {name=x2}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 420 400 1 1 {name=x3}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 420 520 1 1 {name=x4}
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} 460 590 0 1 {name=x5 }
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} 620 590 0 0 {name=x6 }
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} 520 660 0 0 {name=x7 }
C {JNW_ATR_SKY130A/JNWATR_PCH_2C5F0.sym} 530 130 0 0 {name=x8 }
C {JNW_ATR_SKY130A/JNWATR_PCH_2C5F0.sym} 790 130 0 1 {name=x9 }
C {devices/lab_wire.sym} 370 730 0 0 {name=p1 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 410 80 0 0 {name=p2 sig_type=std_logic lab=VDD}
C {devices/ipin.sym} 170 310 0 0 {name=p3 lab=VDD}
C {devices/ipin.sym} 170 330 0 0 {name=p4 lab=SLEEP}
C {devices/ipin.sym} 170 350 0 0 {name=p6 lab=VSS}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 130 490 0 0 {name=x10 }
C {devices/lab_wire.sym} 120 490 0 0 {name=p7 sig_type=std_logic lab=SLEEP}
C {devices/lab_wire.sym} 220 490 0 1 {name=p8 sig_type=std_logic lab=SLEEP_N}
C {devices/lab_wire.sym} 170 560 0 0 {name=p9 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 170 440 0 0 {name=p10 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 370 130 0 0 {name=p11 sig_type=std_logic lab=SLEEP}
C {devices/opin.sym} 780 320 0 0 {name=p13 lab=PBIAS}
C {devices/opin.sym} 780 340 0 0 {name=p14 lab=NBIAS}
C {devices/lab_wire.sym} 500 580 0 1 {name=p15 sig_type=std_logic lab=NBIAS}
C {devices/lab_wire.sym} 640 180 2 1 {name=p16 sig_type=std_logic lab=PBIAS}
C {devices/lab_wire.sym} 420 190 0 1 {name=p5 sig_type=std_logic lab=V1}
C {devices/lab_wire.sym} 420 310 0 1 {name=p17 sig_type=std_logic lab=V2}
C {devices/lab_wire.sym} 420 430 0 1 {name=p18 sig_type=std_logic lab=V3}
C {devices/lab_wire.sym} 510 660 0 0 {name=p20 sig_type=std_logic lab=SLEEP}
C {devices/lab_wire.sym} 800 130 0 1 {name=p12 sig_type=std_logic lab=SLEEP_N}
C {JNW_TR_SKY130A/JNWTR_RPPO8.sym} 500 440 1 0 {name=x11 }
C {JNW_TR_SKY130A/JNWTR_RPPO4.sym} 500 320 1 0 {name=x12 }
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 500 200 1 0 {name=x13 }
C {devices/lab_wire.sym} 490 190 0 0 {name=p19 sig_type=std_logic lab=V4}
C {devices/lab_wire.sym} 500 310 0 1 {name=p21 sig_type=std_logic lab=V5}
C {devices/lab_wire.sym} 500 430 0 1 {name=p22 sig_type=std_logic lab=V6}
