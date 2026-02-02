v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 220 -560 260 -560 {lab=VDD}
N 220 -100 260 -100 {lab=VSS}
N 820 -350 860 -350 {lab=VOUT}
N 300 -440 300 -240 {lab=VBIAS}
N 260 -480 280 -480 {lab=VSS}
N 260 -560 300 -560 {lab=VDD}
N 300 -560 300 -520 {lab=VDD}
N 260 -170 300 -170 {lab=VSS}
N 300 -140 300 -100 {lab=VSS}
N 260 -100 300 -100 {lab=VSS}
N 340 -170 520 -170 {lab=VBIAS}
N 300 -100 560 -100 {lab=VSS}
N 560 -140 560 -100 {lab=VSS}
N 460 -320 460 -280 {lab=VSRC}
N 460 -280 660 -280 {lab=VSRC}
N 660 -320 660 -280 {lab=VSRC}
N 560 -280 560 -200 {lab=VSRC}
N 460 -350 500 -350 {lab=VSS}
N 620 -350 660 -350 {lab=VSS}
N 560 -170 600 -170 {lab=VSS}
N 600 -170 600 -100 {lab=VSS}
N 560 -100 600 -100 {lab=VSS}
N 460 -460 460 -380 {lab=VINDRN}
N 660 -460 660 -380 {lab=VIPDRN}
N 700 -350 740 -350 {lab=VIP}
N 380 -350 420 -350 {lab=VIN}
N 500 -490 620 -490 {lab=VINDRN}
N 660 -490 700 -490 {lab=VDD}
N 700 -560 700 -490 {lab=VDD}
N 420 -490 460 -490 {lab=VDD}
N 420 -560 420 -490 {lab=VDD}
N 460 -560 460 -520 {lab=VDD}
N 660 -560 660 -520 {lab=VDD}
N 260 -170 260 -100 {lab=VSS}
N 260 -480 260 -170 {lab=VSS}
N 300 -560 420 -560 {lab=VDD}
N 420 -560 460 -560 {lab=VDD}
N 460 -560 660 -560 {lab=VDD}
N 660 -560 700 -560 {lab=VDD}
N 460 -420 540 -420 {lab=VINDRN}
N 540 -490 540 -420 {lab=VINDRN}
N 660 -420 740 -420 {lab=VIPDRN}
N 740 -490 780 -490 {lab=VIPDRN}
N 740 -490 740 -420 {lab=VIPDRN}
N 300 -240 380 -240 {lab=VBIAS}
N 380 -240 380 -170 {lab=VBIAS}
N 300 -240 300 -200 {lab=VBIAS}
N 380 -240 740 -240 {lab=VBIAS}
N 740 -240 740 -170 {lab=VBIAS}
N 740 -170 780 -170 {lab=VBIAS}
N 820 -460 820 -200 {lab=VOUT}
N 820 -140 820 -100 {lab=VSS}
N 600 -100 820 -100 {lab=VSS}
N 700 -560 820 -560 {lab=VDD}
N 820 -560 820 -520 {lab=VDD}
N 820 -490 860 -490 {lab=VDD}
N 860 -560 860 -490 {lab=VDD}
N 820 -560 860 -560 {lab=VDD}
N 820 -170 860 -170 {lab=VSS}
N 860 -170 860 -100 {lab=VSS}
N 820 -100 860 -100 {lab=VSS}
C {devices/ipin.sym} 220 -560 0 0 {name=p3 lab=VDD}
C {devices/ipin.sym} 220 -100 0 0 {name=p4 lab=VSS}
C {devices/opin.sym} 860 -350 0 0 {name=p5 lab=VOUT
}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 300 -520 1 0 {name=x9}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 700 -350 0 1 {name=x2[4:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 520 -170 0 0 {name=x3[1:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 420 -350 0 0 {name=x1[4:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 340 -170 0 1 {name=x4[1:0]}
C {devices/ipin.sym} 380 -350 0 0 {name=p1 lab=VIN}
C {devices/ipin.sym} 740 -350 0 1 {name=p2 lab=VIP}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 500 -490 0 1 {name=x5[4:0]
}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 620 -490 0 0 {name=x6[4:0]
}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 780 -490 0 0 {name=x7[4:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 780 -170 0 0 {name=x8[4:0]}
C {devices/lab_wire.sym} 360 -240 0 0 {name=p6 sig_type=std_logic lab=VBIAS}
C {devices/lab_wire.sym} 520 -420 0 0 {name=p7 sig_type=std_logic lab=VINDRN}
C {devices/lab_wire.sym} 580 -280 0 0 {name=p8 sig_type=std_logic lab=VSRC}
C {devices/lab_wire.sym} 680 -420 0 1 {name=p9 sig_type=std_logic lab=VIPDRN}
C {devices/lab_wire.sym} 480 -350 2 0 {name=p10 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 640 -350 2 1 {name=p11 sig_type=std_logic lab=VSS}
