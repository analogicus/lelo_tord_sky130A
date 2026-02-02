v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 320 560 360 560 {lab=VSS}
N 360 480 380 480 {lab=VSS}
N 360 480 360 560 {lab=VSS}
N 400 520 400 560 {lab=VSS}
N 400 100 400 140 {lab=VDD}
N 400 200 400 440 {lab=#net1}
N 660 200 660 280 {lab=#net2}
N 580 280 660 280 {lab=#net2}
N 580 280 580 320 {lab=#net2}
N 660 280 740 280 {lab=#net2}
N 740 280 740 320 {lab=#net2}
N 500 350 540 350 {lab=VIN}
N 780 350 820 350 {lab=VIP}
N 580 380 580 460 {lab=#net3}
N 740 380 740 460 {lab=#net4}
N 580 520 580 560 {lab=VSS}
N 740 520 740 560 {lab=VSS}
N 440 170 620 170 {lab=#net1}
N 660 100 660 140 {lab=VDD}
N 620 490 700 490 {lab=#net3}
N 660 420 660 490 {lab=#net3}
N 580 420 660 420 {lab=#net3}
N 540 490 580 490 {lab=VSS}
N 540 490 540 560 {lab=VSS}
N 740 490 780 490 {lab=VSS}
N 780 490 780 560 {lab=VSS}
N 530 170 530 240 {lab=#net1}
N 1040 100 1040 140 {lab=VDD}
N 870 170 870 240 {lab=#net1}
N 870 170 1000 170 {lab=#net1}
N 740 420 870 420 {lab=#net4}
N 870 420 870 490 {lab=#net4}
N 1040 520 1040 560 {lab=VSS}
N 1040 200 1040 460 {lab=VOUT}
N 1040 170 1080 170 {lab=VDD}
N 1040 490 1080 490 {lab=VSS}
N 1080 490 1080 560 {lab=VSS}
N 870 490 1000 490 {lab=#net4}
N 360 560 400 560 {lab=VSS}
N 400 560 540 560 {lab=VSS}
N 540 560 580 560 {lab=VSS}
N 580 560 740 560 {lab=VSS}
N 740 560 780 560 {lab=VSS}
N 780 560 1040 560 {lab=VSS}
N 1040 560 1080 560 {lab=VSS}
N 400 240 530 240 {lab=#net1}
N 530 240 870 240 {lab=#net1}
N 400 100 660 100 {lab=VDD}
N 360 100 400 100 {lab=VDD}
N 360 170 400 170 {lab=VDD}
N 360 100 360 170 {lab=VDD}
N 320 100 360 100 {lab=VDD}
N 1040 350 1080 350 {lab=VOUT}
N 1080 100 1080 170 {lab=VDD}
N 1040 100 1080 100 {lab=VDD}
N 660 100 1040 100 {lab=VDD}
N 580 350 620 350 {lab=VDD}
N 700 350 740 350 {lab=VDD}
N 660 170 700 170 {lab=VDD}
N 700 100 700 170 {lab=VDD}
C {devices/ipin.sym} 320 100 0 0 {name=p1 lab=VDD}
C {devices/ipin.sym} 320 560 0 0 {name=p2 lab=VSS}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 440 170 0 1 {name=x1[1:0]
}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 620 170 0 0 {name=x2[1:0]
}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 1000 170 0 0 {name=x3[4:0]
}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 540 350 0 0 {name=x4[4:0]
}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 780 350 0 1 {name=x5[4:0]
}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 620 490 0 1 {name=x7[4:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 700 490 0 0 {name=x8[4:0]}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 400 440 1 0 {name=x6}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 1000 490 0 0 {name=x6[4:0]}
C {devices/ipin.sym} 820 350 2 0 {name=p3 lab=VIP}
C {devices/ipin.sym} 500 350 2 1 {name=p4 lab=VIN}
C {devices/opin.sym} 1080 350 2 1 {name=p5 lab=VOUT}
C {devices/lab_wire.sym} 600 350 0 1 {name=p6 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 720 350 0 0 {name=p7 sig_type=std_logic lab=VDD}
