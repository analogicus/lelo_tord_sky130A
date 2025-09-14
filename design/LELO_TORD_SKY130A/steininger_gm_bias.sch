v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 160 -310 200 -310 {lab=VG1}
N 120 -280 120 -220 {lab=VG2}
N 240 -280 240 -220 {lab=VG1}
N 160 -190 200 -190 {lab=VG2}
N 180 -260 240 -260 {lab=VG1}
N 180 -310 180 -260 {lab=VG1}
N 180 -240 180 -190 {lab=VG2}
N 120 -240 180 -240 {lab=VG2}
N 120 -360 120 -340 {lab=VDD}
N 80 -360 240 -360 {lab=VDD}
N 240 -160 240 -100 {lab=VS1}
N 120 -160 120 -100 {lab=VG3}
N 160 -70 200 -70 {lab=VG3}
N 180 -120 180 -70 {lab=VG3}
N 240 -40 240 0 {lab=VS1}
N 240 80 240 100 {lab=VSS}
N 120 -40 120 100 {lab=VSS}
N 80 100 380 100 {lab=VSS}
N 320 -120 320 -70 {lab=VG3}
N 320 -70 340 -70 {lab=VG3}
N 380 -140 380 -100 {lab=IBIAS}
N 380 -40 380 100 {lab=VSS}
N 120 -120 180 -120 {lab=VG3}
N 180 -120 320 -120 {lab=VG3}
N 240 -360 240 -340 {lab=VDD}
N 380 -70 410 -70 {lab=VSS}
N 90 -70 130 -70 {lab=VSS}
N 90 -190 120 -190 {lab=VSS}
N 90 -310 120 -310 {lab=VDD}
N 240 -310 270 -310 {lab=VDD}
N 240 -190 270 -190 {lab=VSS}
N 240 -70 270 -70 {lab=VSS}
N 260 40 280 40 {lab=VSS}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 200 -310 0 0 {name=x1 }
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 160 -310 0 1 {name=x2 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 200 -190 0 0 {name=x3 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 160 -190 0 1 {name=x4 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 200 -70 0 0 {name=x5[3:0]}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 240 0 3 1 {name=x7 }
C {devices/ipin.sym} 80 -360 0 0 {name=p1 lab=VDD}
C {devices/ipin.sym} 80 100 0 0 {name=p2 lab=VSS}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 160 -70 0 1 {name=x6}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 340 -70 0 0 {name=x8}
C {devices/ipin.sym} 380 -140 3 1 {name=p3 lab=IBIAS}
C {devices/lab_wire.sym} 410 -70 2 0 {name=p5 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 270 -190 2 0 {name=p4 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 270 -70 2 0 {name=p6 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 90 -70 2 1 {name=p7 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 90 -190 2 1 {name=p8 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 90 -310 0 0 {name=p9 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 270 -310 0 1 {name=p10 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 280 40 2 0 {name=p11 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 190 -260 0 1 {name=p12 sig_type=std_logic lab=VG1}
C {devices/lab_wire.sym} 170 -240 2 1 {name=p13 sig_type=std_logic lab=VG2}
C {devices/lab_wire.sym} 170 -120 2 1 {name=p14 sig_type=std_logic lab=VG3}
C {devices/lab_wire.sym} 240 -30 2 1 {name=p15 sig_type=std_logic lab=VS2}
C {devices/lab_wire.sym} 240 -150 2 1 {name=p16 sig_type=std_logic lab=VS1}
