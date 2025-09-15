v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 160 -310 200 -310 {lab=VG3}
N 120 -280 120 -220 {lab=VG3}
N 240 -280 240 -220 {lab=#net1}
N 160 -90 200 -90 {lab=VG2}
N 120 -260 180 -260 {lab=VG3}
N 180 -310 180 -260 {lab=VG3}
N 180 -140 180 -90 {lab=VG2}
N 180 -140 240 -140 {lab=VG2}
N 120 -360 120 -340 {lab=VDD}
N 80 -360 240 -360 {lab=VDD}
N 120 -60 120 0 {lab=#net2}
N 160 130 200 130 {lab=#net3}
N 180 80 180 130 {lab=#net3}
N 120 160 120 220 {lab=VR}
N 120 400 120 420 {lab=VSS}
N 240 -360 240 -340 {lab=VDD}
N 100 -90 120 -90 {lab=VSS}
N 100 -310 120 -310 {lab=VDD}
N 240 -310 260 -310 {lab=VDD}
N 240 130 260 130 {lab=VSS}
N 180 80 240 80 {lab=#net3}
N 240 -60 240 0 {lab=#net4}
N 80 420 240 420 {lab=VSS}
N 240 160 240 340 {lab=#net5}
N 120 300 120 340 {lab=#net6}
N 240 400 240 420 {lab=VSS}
N 100 130 120 130 {lab=VSS}
N 240 -90 260 -90 {lab=VSS}
N 80 260 100 260 {lab=VSS}
N 240 -160 240 -120 {lab=VG2}
N 120 -160 120 -120 {lab=#net7}
N 240 60 240 100 {lab=#net3}
N 120 60 120 100 {lab=#net8}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 200 -310 0 0 {name=x5}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 160 -310 0 1 {name=x6}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 200 -90 0 0 {name=x3 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 160 -90 0 1 {name=x4 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 200 130 0 0 {name=x1}
C {devices/ipin.sym} 80 -360 0 0 {name=p1 lab=VDD}
C {devices/ipin.sym} 80 420 0 0 {name=p2 lab=VSS}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 160 130 0 1 {name=x2[3:0]}
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 120 300 1 1 {name=x7}
C {devices/vsource.sym} 240 370 0 0 {name=V1 value=0 savecurrent=true}
C {devices/vsource.sym} 120 370 0 0 {name=V2 value=0 savecurrent=true}
C {devices/lab_wire.sym} 100 -310 0 0 {name=p3 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 260 -310 0 1 {name=p4 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 100 -90 2 1 {name=p5 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 260 -90 2 0 {name=p6 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 100 130 2 1 {name=p7 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 260 130 2 0 {name=p8 sig_type=std_logic lab=VSS}
C {devices/vsource.sym} 240 30 0 0 {name=V3 value=0 savecurrent=true}
C {devices/vsource.sym} 120 30 0 0 {name=V4 value=0 savecurrent=true}
C {devices/vsource.sym} 240 -190 0 0 {name=V5 value=0 savecurrent=true}
C {devices/vsource.sym} 120 -190 0 0 {name=V6 value=0 savecurrent=true}
C {devices/lab_wire.sym} 80 260 2 1 {name=p9 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 180 80 2 0 {name=p10 sig_type=std_logic lab=VG1}
C {devices/lab_wire.sym} 180 -140 2 0 {name=p11 sig_type=std_logic lab=VG2}
C {devices/lab_wire.sym} 180 -260 0 0 {name=p12 sig_type=std_logic lab=VG3}
C {devices/lab_wire.sym} 120 180 2 1 {name=p13 sig_type=std_logic lab=VR}
