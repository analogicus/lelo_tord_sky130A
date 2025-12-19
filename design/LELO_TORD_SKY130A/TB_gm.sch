v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 100 170 140 170 {lab=VG}
N 340 170 380 170 {lab=VG}
N 580 170 620 170 {lab=VG}
N 660 170 700 170 {lab=VS}
N 660 200 660 240 {lab=#net1}
N 420 200 420 240 {lab=#net2}
N 180 200 180 240 {lab=#net3}
N 180 170 220 170 {lab=VS}
N 420 170 460 170 {lab=VS}
N 420 100 420 140 {lab=VS}
N 180 100 180 140 {lab=VS}
N 660 100 660 140 {lab=VS}
N 220 100 220 170 {lab=VS}
N 460 100 460 170 {lab=VS}
N 700 100 700 170 {lab=VS}
N 660 100 700 100 {lab=VS}
N 140 100 180 100 {lab=VS}
N 180 100 220 100 {lab=VS}
N 220 100 420 100 {lab=VS}
N 420 100 460 100 {lab=VS}
N 460 100 660 100 {lab=VS}
N 140 340 180 340 {lab=VD}
N 180 340 420 340 {lab=VD}
N 420 340 660 340 {lab=VD}
N 420 300 420 340 {lab=VD}
N 660 300 660 340 {lab=VD}
N 180 300 180 340 {lab=VD}
N 700 100 900 100 {lab=VS}
N 900 100 900 140 {lab=VS}
N 900 170 940 170 {lab=VS}
N 940 100 940 170 {lab=VS}
N 900 100 940 100 {lab=VS}
N 820 170 860 170 {lab=#net4}
N 900 300 900 340 {lab=VD}
N 660 340 900 340 {lab=VD}
N 900 200 900 240 {lab=#net5}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 140 170 0 0 {name=x1 }
C {JNW_ATR_SKY130A/JNWATR_PCH_8C5F0.sym} 380 170 0 0 {name=x2 }
C {JNW_ATR_SKY130A/JNWATR_PCH_12C5F0.sym} 620 170 0 0 {name=x3 }
C {devices/ipin.sym} 140 100 0 0 {name=p1 lab=VS}
C {devices/ipin.sym} 140 340 0 0 {name=p2 lab=VD}
C {devices/ipin.sym} 100 170 0 0 {name=p3 lab=VG}
C {devices/vsource.sym} 180 270 0 0 {name=V1 value=0 savecurrent=true}
C {devices/vsource.sym} 420 270 0 0 {name=V2 value=0 savecurrent=true}
C {devices/vsource.sym} 660 270 0 0 {name=V3 value=0 savecurrent=true}
C {devices/lab_wire.sym} 360 170 0 0 {name=p4 sig_type=std_logic lab=VG}
C {devices/lab_wire.sym} 600 170 0 0 {name=p5 sig_type=std_logic lab=VG}
C {JNW_ATR_SKY130A/JNWATR_PCH_2C5F0.sym} 860 170 0 0 {name=x4 }
C {devices/vsource.sym} 900 270 0 0 {name=V4 value=0 savecurrent=true}
C {devices/lab_wire.sym} 840 170 0 0 {name=p6 sig_type=std_logic lab=VG}
