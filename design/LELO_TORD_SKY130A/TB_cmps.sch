v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 620 -280 620 -260 {lab=VSS}
N 580 -260 620 -260 {lab=VSS}
N 640 -290 640 -240 {lab=VDD}
N 580 -240 640 -240 {lab=VDD}
N 660 -300 660 -220 {lab=VSS}
N 580 -220 660 -220 {lab=VSS}
N 620 -480 620 -460 {lab=VDD}
N 580 -480 620 -480 {lab=VDD}
N 640 -500 640 -450 {lab=VSS}
N 580 -500 640 -500 {lab=VSS}
N 520 -400 560 -400 {lab=VIP1}
N 520 -340 560 -340 {lab=VIN1}
N 780 -370 820 -370 {lab=VOUT1}
N 720 -630 760 -630 {lab=VOUT2}
N 600 -700 640 -700 {lab=VDD}
N 600 -560 640 -560 {lab=VSS}
N 520 -620 560 -620 {lab=VIN2}
N 520 -640 560 -640 {lab=VIP2}
N 520 -820 560 -820 {lab=VDD}
N 520 -800 560 -800 {lab=VIP3}
N 520 -780 560 -780 {lab=VIN3}
N 520 -760 560 -760 {lab=VSS}
N 860 -820 900 -820 {lab=VOUT3}
N 860 -950 900 -950 {lab=VOUT4}
N 860 -930 900 -930 {lab=VOUT4_N}
N 520 -950 560 -950 {lab=VDD}
N 520 -930 560 -930 {lab=VIP4}
N 520 -910 560 -910 {lab=VIN4}
N 520 -890 560 -890 {lab=VSS}
N 520 -1060 560 -1060 {lab=VDD}
N 520 -1040 560 -1040 {lab=VIP5}
N 520 -1020 560 -1020 {lab=VIN5}
N 520 -1000 560 -1000 {lab=VSS}
N 860 -1060 900 -1060 {lab=VOUT5}
N 860 -1040 900 -1040 {lab=VOUT5_N}
C {LELO_TORD_SKY130A/cmp.sym} 660 -370 0 0 {name=x1}
C {LELO_TORD_SKY130A/cmp_v2.sym} 640 -630 0 0 {name=x2}
C {LELO_TORD_SKY130A/cmp_v3.sym} 710 -790 0 0 {name=x3}
C {devices/opin.sym} 820 -370 0 0 {name=p5 lab=VOUT1
}
C {devices/opin.sym} 760 -630 0 0 {name=p1 lab=VOUT2
}
C {devices/opin.sym} 900 -820 0 0 {name=p2 lab=VOUT3
}
C {devices/ipin.sym} 580 -480 0 0 {name=p4 lab=VDD}
C {devices/ipin.sym} 580 -260 0 0 {name=p3 lab=VSS}
C {devices/ipin.sym} 520 -400 0 0 {name=p6 lab=VIP1}
C {devices/ipin.sym} 520 -340 0 0 {name=p7 lab=VIN1}
C {devices/ipin.sym} 520 -640 0 0 {name=p8 lab=VIP2}
C {devices/ipin.sym} 520 -620 0 0 {name=p9 lab=VIN2}
C {devices/ipin.sym} 520 -800 0 0 {name=p10 lab=VIP3}
C {devices/ipin.sym} 520 -780 0 0 {name=p11 lab=VIN3}
C {devices/lab_wire.sym} 630 -500 0 0 {name=p12 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 630 -240 2 1 {name=p13 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 650 -220 2 1 {name=p14 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 630 -560 2 1 {name=p15 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 550 -760 2 1 {name=p16 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 630 -700 0 0 {name=p17 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 550 -820 0 0 {name=p18 sig_type=std_logic lab=VDD}
C {LELO_TORD_SKY130A/cmp_v4.sym} 710 -920 0 0 {name=x4}
C {devices/opin.sym} 900 -950 0 0 {name=p19 lab=VOUT4
}
C {devices/opin.sym} 900 -930 0 0 {name=p20 lab=VOUT4_N
}
C {devices/ipin.sym} 520 -930 0 0 {name=p21 lab=VIP4}
C {devices/ipin.sym} 520 -910 0 0 {name=p22 lab=VIN4}
C {devices/lab_wire.sym} 550 -890 2 1 {name=p23 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 550 -950 0 0 {name=p24 sig_type=std_logic lab=VDD}
C {LELO_TORD_SKY130A/cmp_v5.sym} 710 -1030 0 0 {name=x5}
C {devices/ipin.sym} 520 -1040 0 0 {name=p25 lab=VIP5}
C {devices/ipin.sym} 520 -1020 0 0 {name=p26 lab=VIN5}
C {devices/lab_wire.sym} 550 -1000 2 1 {name=p27 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 550 -1060 0 0 {name=p28 sig_type=std_logic lab=VDD}
C {devices/opin.sym} 900 -1060 0 0 {name=p32 lab=VOUT5
}
C {devices/opin.sym} 900 -1040 0 0 {name=p29 lab=VOUT5_N
}
C {LELO_TORD_SKY130A/cmp_v3_pmos.sym} 1060 -730 0 0 {name=x6}
C {devices/opin.sym} 1210 -760 0 0 {name=p30 lab=VOUT3_PMOS
}
C {devices/lab_wire.sym} 910 -700 2 1 {name=p34 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 910 -760 0 0 {name=p35 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 910 -740 0 0 {name=p31 sig_type=std_logic lab=VIP3}
C {devices/lab_wire.sym} 910 -720 0 0 {name=p33 sig_type=std_logic lab=VIN3}
