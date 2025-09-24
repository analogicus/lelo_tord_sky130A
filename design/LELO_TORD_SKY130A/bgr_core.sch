v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 0 90 40 90 {lab=VDD}
N 40 40 40 90 {lab=VDD}
N 0 40 40 40 {lab=VDD}
N 0 0 0 60 {lab=VDD}
N -80 90 -40 90 {lab=CTRL}
N 0 120 0 260 {lab=#net1}
N -300 260 -300 400 {lab=#net1}
N 300 880 300 940 {lab=V2C}
N 320 840 340 840 {lab=VSS}
N 340 840 340 1040 {lab=VSS}
N -720 1040 680 1040 {lab=VSS}
N -300 1000 -300 1040 {lab=VSS}
N -360 970 -340 970 {lab=VSS}
N -360 970 -360 1040 {lab=VSS}
N 300 1000 300 1040 {lab=VSS}
N 240 970 260 970 {lab=VSS}
N 240 970 240 1040 {lab=VSS}
N 300 500 300 650 {lab=V2A}
N -120 660 -80 660 {lab=V1B}
N -380 480 -340 480 {lab=VDD}
N -380 450 -340 450 {lab=SWBRANCH1}
N 350 480 390 480 {lab=VSS}
N 220 480 260 480 {lab=VDD}
N 220 450 260 450 {lab=SWBRANCH2}
N 520 870 520 1040 {lab=VSS}
N 520 660 520 800 {lab=V2}
N 300 260 300 400 {lab=#net1}
N -300 260 480 260 {lab=#net1}
N -300 500 -300 650 {lab=V1A}
N -520 870 -520 1040 {lab=VSS}
N -300 670 -300 940 {lab=V1A}
N -80 660 -80 800 {lab=V1B}
N -80 880 -80 920 {lab=#net2}
N -80 1000 -80 1040 {lab=VSS}
N -60 840 -40 840 {lab=VSS}
N -40 840 -40 1040 {lab=VSS}
N -60 960 -40 960 {lab=VSS}
N 80 880 80 920 {lab=#net3}
N 40 840 60 840 {lab=VSS}
N 40 840 40 1040 {lab=VSS}
N 40 960 60 960 {lab=VSS}
N 80 1000 80 1040 {lab=VSS}
N 460 710 460 750 {lab=VSS}
N 460 580 460 620 {lab=VDD}
N 430 580 430 620 {lab=SWCAP2}
N 480 660 720 660 {lab=V2}
N 310 660 380 660 {lab=V2A}
N -520 660 -520 800 {lab=V1}
N -460 710 -460 750 {lab=VSS}
N -460 580 -460 620 {lab=VDD}
N -430 580 -430 620 {lab=SWCAP1}
N -380 660 -310 660 {lab=V1A}
N 300 670 300 800 {lab=V2A}
N -310 650 -310 670 {lab=V1A}
N -310 670 -290 670 {lab=V1A}
N -290 650 -290 670 {lab=V1A}
N -310 650 -290 650 {lab=V1A}
N 290 650 290 670 {lab=V2A}
N 290 670 310 670 {lab=V2A}
N 310 650 310 670 {lab=V2A}
N 290 650 310 650 {lab=V2A}
N -140 710 -140 750 {lab=VSS}
N -140 580 -140 620 {lab=VDD}
N -170 580 -170 620 {lab=SWREF1}
N -290 660 -220 660 {lab=V1A}
N 140 710 140 750 {lab=VSS}
N 140 580 140 620 {lab=VDD}
N 170 580 170 620 {lab=SWREF2}
N 80 660 120 660 {lab=V2B}
N 220 660 290 660 {lab=V2A}
N 80 660 80 800 {lab=V2B}
N -250 480 -210 480 {lab=VSS}
N 680 660 680 800 {lab=V2}
N 680 860 680 1040 {lab=VSS}
N -720 660 -480 660 {lab=V1}
N -680 660 -680 800 {lab=V1}
N -680 860 -680 1040 {lab=VSS}
N -760 830 -720 830 {lab=SWDRAIN}
N -680 830 -640 830 {lab=VSS}
N -640 830 -640 880 {lab=VSS}
N -680 880 -640 880 {lab=VSS}
N 640 830 680 830 {lab=VSS}
N 640 830 640 880 {lab=VSS}
N 640 880 680 880 {lab=VSS}
N 720 830 760 830 {lab=SWDRAIN}
N -720 180 -680 180 {lab=SWBRANCH1}
N -720 210 -680 210 {lab=SWBRANCH2}
N -720 420 -680 420 {lab=SWDRAIN}
N -720 240 -680 240 {lab=SWCAP1}
N -720 270 -680 270 {lab=SWCAP2}
N -720 300 -680 300 {lab=SWREF1}
N -720 330 -680 330 {lab=SWREF2}
N -720 120 -680 120 {lab=CTRL}
N -720 70 -680 70 {lab=VDD}
N -720 470 -680 470 {lab=VSS}
N 680 630 720 630 {lab=V1}
N 580 260 720 260 {lab=IOUT}
N 560 310 560 350 {lab=VSS}
N 560 180 560 220 {lab=VDD}
N 530 180 530 220 {lab=SWOUT}
N -720 360 -680 360 {lab=SWOUT}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} -40 90 0 0 {name=x1 }
C {sky130_fd_pr/pnp_05v5.sym} -320 970 0 0 {name=Q1
model=pnp_05v5_W3p40L3p40
m=1
spiceprefix=X
}
C {sky130_fd_pr/pnp_05v5.sym} 280 970 0 0 {name=Q2
model=pnp_05v5_W3p40L3p40
m=1
spiceprefix=X
}
C {JNW_TR_SKY130A/JNWTR_RPPO4.sym} 300 880 3 0 {name=x12[3:0] }
C {JNW_TR_SKY130A/JNWTR_TGX2_CV.sym} -300 390 3 1 {name=x2 }
C {JNW_TR_SKY130A/JNWTR_TGX2_CV.sym} 300 390 3 1 {name=x3 }
C {JNW_TR_SKY130A/JNWTR_CAPX4.sym} 520 860 0 0 {name=x11[9:0]
}
C {JNW_TR_SKY130A/JNWTR_CAPX4.sym} -520 860 0 0 {name=x10[9:0]
}
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} -80 880 3 0 {name=x13[2:0]}
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 80 880 1 1 {name=x16[2:0]}
C {JNW_TR_SKY130A/JNWTR_TGX2_CV.sym} 370 660 0 0 {name=x4 }
C {JNW_TR_SKY130A/JNWTR_TGX2_CV.sym} -370 660 0 1 {name=x5 }
C {devices/opin.sym} 720 660 0 0 {name=p6 lab=V2}
C {devices/ipin.sym} -720 470 0 0 {name=p4 lab=VSS}
C {JNW_TR_SKY130A/JNWTR_TGX2_CV.sym} -230 660 0 0 {name=x6 }
C {JNW_TR_SKY130A/JNWTR_TGX2_CV.sym} 230 660 0 1 {name=x7 }
C {devices/ipin.sym} -720 70 0 0 {name=p3 lab=VDD}
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} -720 830 0 0 {name=x8 }
C {JNW_ATR_SKY130A/JNWATR_NCH_2C5F0.sym} 720 830 0 1 {name=x9 }
C {devices/ipin.sym} -720 420 0 0 {name=p7 lab=SWDRAIN}
C {devices/lab_wire.sym} -460 740 0 0 {name=p9 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} -460 610 0 0 {name=p10 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} -350 450 0 0 {name=p11 sig_type=std_logic lab=SWBRANCH1}
C {devices/lab_wire.sym} -350 480 0 0 {name=p12 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} -240 480 0 1 {name=p13 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} -140 610 0 1 {name=p14 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} -140 740 0 1 {name=p15 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} -430 610 0 1 {name=p16 sig_type=std_logic lab=SWCAP1}
C {devices/lab_wire.sym} -170 610 0 0 {name=p17 sig_type=std_logic lab=SWREF1}
C {devices/lab_wire.sym} 170 610 0 1 {name=p18 sig_type=std_logic lab=SWREF2}
C {devices/lab_wire.sym} 430 610 0 0 {name=p19 sig_type=std_logic lab=SWCAP2}
C {devices/lab_wire.sym} 140 610 0 0 {name=p20 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 460 610 0 1 {name=p21 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 140 740 0 0 {name=p22 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 460 740 0 1 {name=p23 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 360 480 0 1 {name=p2 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 250 450 0 0 {name=p24 sig_type=std_logic lab=SWBRANCH2}
C {devices/lab_wire.sym} 250 480 0 0 {name=p25 sig_type=std_logic lab=VDD}
C {devices/opin.sym} 720 630 0 0 {name=p26 lab=V1}
C {devices/opin.sym} 720 260 0 0 {name=p5 lab=IOUT}
C {devices/ipin.sym} -720 180 0 0 {name=p27 lab=SWBRANCH1}
C {devices/ipin.sym} -720 210 0 0 {name=p28 lab=SWBRANCH2}
C {devices/ipin.sym} -720 240 0 0 {name=p30 lab=SWCAP1}
C {devices/ipin.sym} -720 270 0 0 {name=p31 lab=SWCAP2}
C {devices/ipin.sym} -720 300 0 0 {name=p32 lab=SWREF1}
C {devices/ipin.sym} -720 330 0 0 {name=p33 lab=SWREF2}
C {devices/ipin.sym} -720 120 0 0 {name=p34 lab=CTRL}
C {devices/lab_wire.sym} -690 1040 0 0 {name=p35 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} -700 660 0 0 {name=p36 sig_type=std_logic lab=V1}
C {devices/lab_wire.sym} 0 20 0 0 {name=p38 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} -50 90 0 0 {name=p37 sig_type=std_logic lab=CTRL}
C {devices/lab_wire.sym} -730 830 0 0 {name=p1 sig_type=std_logic lab=SWDRAIN}
C {devices/lab_wire.sym} 730 830 0 1 {name=p39 sig_type=std_logic lab=SWDRAIN}
C {devices/lab_wire.sym} -310 650 0 0 {name=p8 sig_type=std_logic lab=V1A}
C {devices/lab_wire.sym} -80 660 0 1 {name=p29 sig_type=std_logic lab=V1B}
C {devices/lab_wire.sym} 80 660 0 0 {name=p40 sig_type=std_logic lab=V2B}
C {devices/lab_wire.sym} 310 650 0 1 {name=p41 sig_type=std_logic lab=V2A}
C {devices/lab_wire.sym} 300 920 0 1 {name=p42 sig_type=std_logic lab=V2C}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 80 920 1 0 {name=x14[1:0]}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} -80 920 3 1 {name=x15[1:0]}
C {JNW_TR_SKY130A/JNWTR_TGX2_CV.sym} 470 260 0 0 {name=x10 }
C {devices/lab_wire.sym} 530 210 0 0 {name=p43 sig_type=std_logic lab=SWOUT}
C {devices/lab_wire.sym} 560 210 0 1 {name=p44 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 560 340 0 1 {name=p45 sig_type=std_logic lab=VSS}
C {devices/ipin.sym} -720 360 0 0 {name=p46 lab=SWOUT}
