v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 100 520 140 520 {lab=VSS}
N 140 440 160 440 {lab=VSS}
N 140 440 140 520 {lab=VSS}
N 180 480 180 520 {lab=VSS}
N 180 60 180 100 {lab=VDD}
N 180 160 180 400 {lab=#net1}
N 440 160 440 240 {lab=#net2}
N 360 240 440 240 {lab=#net2}
N 360 240 360 280 {lab=#net2}
N 440 240 520 240 {lab=#net2}
N 520 240 520 280 {lab=#net2}
N 280 310 320 310 {lab=VIN}
N 560 310 600 310 {lab=VIP}
N 360 340 360 420 {lab=#net3}
N 520 340 520 420 {lab=#net4}
N 360 480 360 520 {lab=VSS}
N 520 480 520 520 {lab=VSS}
N 220 130 400 130 {lab=#net1}
N 440 60 440 100 {lab=VDD}
N 400 450 480 450 {lab=#net3}
N 440 380 440 450 {lab=#net3}
N 360 380 440 380 {lab=#net3}
N 320 450 360 450 {lab=VSS}
N 320 450 320 520 {lab=VSS}
N 520 450 560 450 {lab=VSS}
N 560 450 560 520 {lab=VSS}
N 310 130 310 200 {lab=#net1}
N 820 60 820 100 {lab=VDD}
N 650 130 650 200 {lab=#net1}
N 650 130 780 130 {lab=#net1}
N 520 380 650 380 {lab=#net4}
N 650 380 650 450 {lab=#net4}
N 820 480 820 520 {lab=VSS}
N 820 160 820 420 {lab=VOUT}
N 820 130 860 130 {lab=VDD}
N 820 450 860 450 {lab=VSS}
N 860 450 860 520 {lab=VSS}
N 650 450 780 450 {lab=#net4}
N 140 520 180 520 {lab=VSS}
N 180 520 320 520 {lab=VSS}
N 320 520 360 520 {lab=VSS}
N 360 520 520 520 {lab=VSS}
N 520 520 560 520 {lab=VSS}
N 560 520 820 520 {lab=VSS}
N 820 520 860 520 {lab=VSS}
N 180 200 310 200 {lab=#net1}
N 310 200 650 200 {lab=#net1}
N 180 60 440 60 {lab=VDD}
N 140 60 180 60 {lab=VDD}
N 140 130 180 130 {lab=VDD}
N 140 60 140 130 {lab=VDD}
N 100 60 140 60 {lab=VDD}
N 820 310 860 310 {lab=VOUT}
N 860 60 860 130 {lab=VDD}
N 820 60 860 60 {lab=VDD}
N 440 60 820 60 {lab=VDD}
N 360 310 400 310 {lab=VDD}
N 480 310 520 310 {lab=VDD}
N 440 130 480 130 {lab=VDD}
N 480 60 480 130 {lab=VDD}
C {devices/ipin.sym} 100 60 0 0 {name=p1 lab=VDD}
C {devices/ipin.sym} 100 520 0 0 {name=p2 lab=VSS}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 220 130 0 1 {name=x1[1:0]
}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 400 130 0 0 {name=x2[1:0]
}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 780 130 0 0 {name=x3[4:0]
}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 400 450 0 1 {name=x7[4:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 480 450 0 0 {name=x8[4:0]}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 180 400 1 0 {name=x6}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 780 450 0 0 {name=x6[4:0]}
C {devices/ipin.sym} 600 310 2 0 {name=p3 lab=VIP}
C {devices/ipin.sym} 280 310 2 1 {name=p4 lab=VIN}
C {devices/opin.sym} 860 310 2 1 {name=p5 lab=VOUT}
C {devices/lab_wire.sym} 380 310 0 1 {name=p6 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 500 310 0 0 {name=p7 sig_type=std_logic lab=VDD}
C {/home/tordos/pro/aicex/ip/lelo_atr_sky130a/design/LELO_ATR_SKY130A/LELOATR_LVT_PCH_4C5F0.sym} 560 310 0 1 {name=x5[4:0]}
C {/home/tordos/pro/aicex/ip/lelo_atr_sky130a/design/LELO_ATR_SKY130A/LELOATR_LVT_PCH_4C5F0.sym} 320 310 0 0 {name=x4[4:0]}
