v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 120 60 160 60 {lab=VDD}
N 120 520 160 520 {lab=VSS}
N 720 270 760 270 {lab=VOUT}
N 200 180 200 380 {lab=VNBIAS}
N 160 140 180 140 {lab=VSS}
N 160 60 200 60 {lab=VDD}
N 200 60 200 100 {lab=VDD}
N 160 450 200 450 {lab=VSS}
N 200 480 200 520 {lab=VSS}
N 160 520 200 520 {lab=VSS}
N 240 450 420 450 {lab=VNBIAS}
N 200 520 460 520 {lab=VSS}
N 460 480 460 520 {lab=VSS}
N 360 300 360 340 {lab=VSRC}
N 360 340 560 340 {lab=VSRC}
N 560 300 560 340 {lab=VSRC}
N 460 340 460 420 {lab=VSRC}
N 360 270 400 270 {lab=VSS}
N 520 270 560 270 {lab=VSS}
N 460 450 500 450 {lab=VSS}
N 500 450 500 520 {lab=VSS}
N 460 520 500 520 {lab=VSS}
N 360 160 360 240 {lab=VINDRN}
N 560 160 560 240 {lab=VIPDRN}
N 600 270 640 270 {lab=VIP}
N 280 270 320 270 {lab=VIN}
N 400 130 520 130 {lab=VINDRN}
N 560 130 600 130 {lab=VDD}
N 600 60 600 130 {lab=VDD}
N 320 130 360 130 {lab=VDD}
N 320 60 320 130 {lab=VDD}
N 360 60 360 100 {lab=VDD}
N 560 60 560 100 {lab=VDD}
N 160 450 160 520 {lab=VSS}
N 160 140 160 450 {lab=VSS}
N 200 60 320 60 {lab=VDD}
N 320 60 360 60 {lab=VDD}
N 360 60 560 60 {lab=VDD}
N 560 60 600 60 {lab=VDD}
N 360 200 440 200 {lab=VINDRN}
N 440 130 440 200 {lab=VINDRN}
N 560 200 640 200 {lab=VIPDRN}
N 640 130 680 130 {lab=VIPDRN}
N 640 130 640 200 {lab=VIPDRN}
N 200 380 280 380 {lab=VNBIAS}
N 280 380 280 450 {lab=VNBIAS}
N 200 380 200 420 {lab=VNBIAS}
N 280 380 640 380 {lab=VNBIAS}
N 640 380 640 450 {lab=VNBIAS}
N 640 450 680 450 {lab=VNBIAS}
N 720 160 720 420 {lab=VOUT}
N 720 480 720 520 {lab=VSS}
N 500 520 720 520 {lab=VSS}
N 600 60 720 60 {lab=VDD}
N 720 60 720 100 {lab=VDD}
N 720 130 760 130 {lab=VDD}
N 760 60 760 130 {lab=VDD}
N 720 60 760 60 {lab=VDD}
N 720 450 760 450 {lab=VSS}
N 760 450 760 520 {lab=VSS}
N 720 520 760 520 {lab=VSS}
C {devices/ipin.sym} 120 60 0 0 {name=p3 lab=VDD}
C {devices/ipin.sym} 120 520 0 0 {name=p4 lab=VSS}
C {devices/opin.sym} 760 270 0 0 {name=p5 lab=VOUT
}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 200 100 1 0 {name=x9}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 420 450 0 0 {name=x3[1:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 240 450 0 1 {name=x4[1:0]}
C {devices/ipin.sym} 280 270 0 0 {name=p1 lab=VIN}
C {devices/ipin.sym} 640 270 0 1 {name=p2 lab=VIP}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 400 130 0 1 {name=x5[4:0]
}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 520 130 0 0 {name=x6[4:0]
}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 680 130 0 0 {name=x7[4:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 680 450 0 0 {name=x8[4:0]}
C {devices/lab_wire.sym} 260 380 0 0 {name=p6 sig_type=std_logic lab=VBIAS}
C {devices/lab_wire.sym} 420 200 0 0 {name=p7 sig_type=std_logic lab=VINDRN}
C {devices/lab_wire.sym} 480 340 0 0 {name=p8 sig_type=std_logic lab=VSRC}
C {devices/lab_wire.sym} 580 200 0 1 {name=p9 sig_type=std_logic lab=VIPDRN}
C {devices/lab_wire.sym} 380 270 2 0 {name=p10 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 540 270 2 1 {name=p11 sig_type=std_logic lab=VSS}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_4C5F0.sym} 320 270 0 0 {name=x1}
C {LELO_ATR_SKY130A/LELOATR_LVT_NCH_4C5F0.sym} 600 270 0 1 {name=x2}
