v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 540 -620 600 -620 {lab=VG1}
N 640 -590 640 -510 {lab=VG1}
N 500 -590 500 -510 {lab=VG2}
N 500 -450 500 -400 {lab=V2}
N 500 -320 640 -320 {lab=VSS}
N 640 -450 640 -400 {lab=V1}
N 500 -680 500 -650 {lab=VDD}
N 500 -680 640 -680 {lab=VDD}
N 640 -680 640 -650 {lab=VDD}
N 580 -620 580 -560 {lab=VG1}
N 580 -560 640 -560 {lab=VG1}
N 500 -540 560 -540 {lab=VG2}
N 560 -540 560 -480 {lab=VG2}
N 450 -320 500 -320 {lab=VSS}
N 450 -680 500 -680 {lab=VDD}
N 500 -340 500 -320 {lab=VSS}
N 640 -340 640 -320 {lab=VSS}
N 470 -620 500 -620 {lab=VDD}
N 470 -680 470 -620 {lab=VDD}
N 640 -620 670 -620 {lab=VDD}
N 670 -680 670 -620 {lab=VDD}
N 640 -680 670 -680 {lab=VDD}
N 470 -480 500 -480 {lab=VSS}
N 470 -480 470 -320 {lab=VSS}
N 640 -480 670 -480 {lab=VSS}
N 670 -480 670 -320 {lab=VSS}
N 640 -320 670 -320 {lab=VSS}
N 540 -480 600 -480 {lab=VG2}
C {devices/ipin.sym} 450 -320 0 0 {name=p1 lab=VSS}
C {devices/ipin.sym} 450 -680 0 0 {name=p2 lab=VDD}
C {devices/lab_wire.sym} 580 -560 0 0 {name=p3 sig_type=std_logic lab=VG1}
C {devices/lab_wire.sym} 560 -540 2 0 {name=p4 sig_type=std_logic lab=VG2}
C {devices/lab_wire.sym} 500 -430 2 1 {name=p5 sig_type=std_logic lab=V2}
C {devices/lab_wire.sym} 640 -430 2 0 {name=p6 sig_type=std_logic lab=V1}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 600 -620 0 0 {name=x1[9:0]}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 540 -620 0 1 {name=x2 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 600 -480 0 0 {name=x3[9:0] }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 540 -480 0 1 {name=x4 }
C {devices/vsource.sym} 640 -370 0 1 {name=V1 value=0 savecurrent=true}
C {devices/vsource.sym} 500 -370 0 0 {name=V2 value=0 savecurrent=true}
