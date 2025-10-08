v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 300 -510 320 -510 {lab=RST_BGR_CAPS}
N 300 -530 300 -510 {lab=RST_BGR_CAPS}
N 300 -550 300 -530 {lab=RST_BGR_CAPS}
N 300 -550 320 -550 {lab=RST_BGR_CAPS}
N 300 -570 300 -550 {lab=RST_BGR_CAPS}
N 300 -570 320 -570 {lab=RST_BGR_CAPS}
N 300 -590 300 -570 {lab=RST_BGR_CAPS}
N 280 -590 320 -590 {lab=RST_BGR_CAPS}
N 300 -530 320 -530 {lab=RST_BGR_CAPS}
N 280 -490 320 -490 {lab=VSS}
N 280 -850 320 -850 {lab=VDD}
N 280 -830 320 -830 {lab=VCTRL}
N 280 -810 320 -810 {lab=SEL_PTAT}
N 280 -790 320 -790 {lab=SEL_REF}
N 280 -770 320 -770 {lab=SEL_CAPL}
N 280 -750 320 -750 {lab=SEL_CAPH}
N 280 -730 320 -730 {lab=SEL_AVG}
N 280 -710 320 -710 {lab=SEL_BRANCH1}
N 280 -690 320 -690 {lab=SEL_BRANCH2}
N 280 -670 320 -670 {lab=SEL_BGR_CAP1}
N 280 -650 320 -650 {lab=SEL_BGR_CAP2}
N 280 -630 320 -630 {lab=BGR_STATE}
N 300 -630 300 -610 {lab=BGR_STATE}
N 620 -850 800 -850 {lab=IPTAT}
N 620 -490 1060 -490 {lab=V1}
N 300 -610 320 -610 {lab=BGR_STATE}
N 620 -610 1060 -610 {lab=VAVG}
N 620 -730 1060 -730 {lab=V2}
N 1360 -580 1360 -540 {lab=VSS}
N 1380 -590 1380 -550 {lab=CMP_P1}
N 1400 -600 1400 -560 {lab=CMP_P2}
N 1520 -670 1560 -670 {lab=CMP}
N 760 -870 800 -870 {lab=VDD}
N 760 -770 800 -770 {lab=VSS}
N 780 -830 800 -830 {lab=SEL_TMP_CAP1}
N 780 -810 800 -810 {lab=SEL_TMP_CAP2}
N 780 -790 800 -790 {lab=RST_TMP_CAPS}
N 1360 -800 1360 -760 {lab=VDD}
N 1380 -820 1380 -750 {lab=SLEEP}
N 1140 -650 1180 -650 {lab=VDD}
N 1140 -680 1180 -680 {lab=VSS}
N 1140 -770 1180 -770 {lab=VDD}
N 1140 -800 1180 -800 {lab=VSS}
N 1090 -770 1110 -770 {lab=V2_TO_CMP}
N 1090 -650 1110 -650 {lab=VAVG_TO_CMP}
N 1090 -530 1110 -530 {lab=V1_TO_CMP}
N 1140 -440 1180 -440 {lab=VSS}
N 1140 -530 1180 -530 {lab=VDD}
N 1140 -890 1180 -890 {lab=VDD}
N 1090 -890 1110 -890 {lab=PTAT_TO_CMP}
N 1140 -560 1180 -560 {lab=VSS}
N 1160 -610 1220 -610 {lab=VIN}
N 1160 -490 1220 -490 {lab=VIN}
N 1160 -730 1220 -730 {lab=VIP}
N 1160 -850 1220 -850 {lab=VIP}
N 1520 -700 1560 -700 {lab=VAVG}
N 1220 -850 1220 -700 {lab=VIP}
N 1220 -610 1220 -490 {lab=VIN}
N 1220 -640 1220 -610 {lab=VIN}
N 1220 -640 1300 -640 {lab=VIN}
N 1220 -700 1300 -700 {lab=VIP}
N 960 -850 1060 -850 {lab=#net1}
N 1380 -550 1380 -520 {lab=CMP_P1}
N 1400 -560 1400 -500 {lab=CMP_P2}
C {LELO_TORD_SKY130A/cmp.sym} 1400 -670 0 0 {name=x2}
C {LELO_TORD_SKY130A/bgr_core.sym} 470 -670 0 0 {name=x3}
C {LELO_TORD_SKY130A/tmp_core.sym} 880 -820 0 0 {name=x4}
C {devices/ipin.sym} 280 -850 0 0 {name=p1 lab=VDD}
C {devices/ipin.sym} 280 -490 0 0 {name=p2 lab=VSS}
C {devices/ipin.sym} 280 -830 0 0 {name=p3 lab=VCTRL}
C {devices/ipin.sym} 280 -590 0 0 {name=p4 lab=RST_BGR_CAPS}
C {devices/ipin.sym} 280 -630 0 0 {name=p5 lab=BGR_STATE}
C {devices/ipin.sym} 280 -650 0 0 {name=p6 lab=SEL_BGR_CAP2}
C {devices/ipin.sym} 280 -670 0 0 {name=p7 lab=SEL_BGR_CAP1}
C {devices/ipin.sym} 280 -710 0 0 {name=p8 lab=SEL_BRANCH1}
C {devices/ipin.sym} 280 -690 0 0 {name=p9 lab=SEL_BRANCH2}
C {devices/ipin.sym} 280 -730 0 0 {name=p10 lab=SEL_AVG}
C {devices/ipin.sym} 280 -750 0 0 {name=p11 lab=SEL_CAPH}
C {devices/ipin.sym} 280 -770 0 0 {name=p12 lab=SEL_CAPL}
C {devices/ipin.sym} 280 -790 0 0 {name=p13 lab=SEL_REF}
C {devices/ipin.sym} 280 -810 0 0 {name=p14 lab=SEL_PTAT}
C {devices/lab_wire.sym} 1290 -700 0 0 {name=p16 sig_type=std_logic lab=VIP}
C {devices/lab_wire.sym} 1290 -640 0 0 {name=p17 sig_type=std_logic lab=VIN}
C {devices/lab_wire.sym} 790 -870 0 0 {name=p18 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 790 -770 0 0 {name=p19 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 790 -850 0 0 {name=p23 sig_type=std_logic lab=IPTAT}
C {JNW_TR_SKY130A/JNWTR_TGX2_CV.sym} 1050 -490 0 0 {name=x5 }
C {JNW_TR_SKY130A/JNWTR_TGX2_CV.sym} 1050 -610 0 0 {name=x6 }
C {JNW_TR_SKY130A/JNWTR_TGX2_CV.sym} 1050 -730 0 0 {name=x7 }
C {JNW_TR_SKY130A/JNWTR_TGX2_CV.sym} 1050 -850 0 0 {name=x8 }
C {devices/lab_wire.sym} 1150 -890 0 1 {name=p24 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 1150 -770 0 1 {name=p25 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 1150 -650 0 1 {name=p26 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 1150 -530 0 1 {name=p27 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 1150 -800 0 1 {name=p28 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1150 -680 0 1 {name=p29 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1150 -560 0 1 {name=p30 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1150 -440 0 1 {name=p31 sig_type=std_logic lab=VSS}
C {devices/ipin.sym} 1380 -820 0 0 {name=p42 lab=SLEEP}
C {devices/lab_wire.sym} 1050 -730 0 0 {name=p43 sig_type=std_logic lab=V2}
C {devices/lab_wire.sym} 1050 -610 0 0 {name=p44 sig_type=std_logic lab=VAVG}
C {devices/lab_wire.sym} 1050 -490 0 0 {name=p45 sig_type=std_logic lab=V1}
C {devices/opin.sym} 1560 -670 0 0 {name=p46 lab=CMP}
C {devices/opin.sym} 1560 -700 0 0 {name=p15 lab=VAVG}
C {devices/ipin.sym} 1090 -770 0 0 {name=p36 lab=V2_TO_CMP}
C {devices/ipin.sym} 1090 -650 0 0 {name=p37 lab=VAVG_TO_CMP}
C {devices/ipin.sym} 1090 -530 0 0 {name=p38 lab=V1_TO_CMP}
C {devices/ipin.sym} 1090 -890 0 0 {name=p39 lab=PTAT_TO_CMP}
C {devices/ipin.sym} 780 -790 0 0 {name=p32 lab=RST_TMP_CAPS}
C {devices/ipin.sym} 780 -810 0 0 {name=p33 lab=SEL_TMP_CAP2}
C {devices/ipin.sym} 780 -830 0 0 {name=p34 lab=SEL_TMP_CAP1}
C {devices/lab_wire.sym} 1360 -570 2 1 {name=p20 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 1360 -770 0 0 {name=p21 sig_type=std_logic lab=VDD}
C {devices/ipin.sym} 1380 -520 0 0 {name=p35 lab=CMP_P1}
C {devices/ipin.sym} 1400 -500 0 0 {name=p47 lab=CMP_P2}
C {LELO_TORD_SKY130A/LELO_TORD.sch} 1294.698904564514 -521.0378564346382 0 0 {}
