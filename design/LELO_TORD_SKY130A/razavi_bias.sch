v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 400 -700 600 -700 {lab=VG1}
N 640 -670 640 -510 {lab=VG1}
N 360 -670 360 -510 {lab=VG2}
N 640 -450 640 -380 {lab=V3}
N 360 -760 360 -730 {lab=VDD}
N 640 -760 640 -730 {lab=VDD}
N 570 -700 570 -630 {lab=VG1}
N 570 -630 640 -630 {lab=VG1}
N 360 -550 430 -550 {lab=VG2}
N 430 -550 430 -480 {lab=VG2}
N 360 -180 360 -160 {lab=VSS}
N 640 -180 640 -160 {lab=VSS}
N 320 -700 360 -700 {lab=VDD}
N 320 -760 320 -700 {lab=VDD}
N 640 -700 680 -700 {lab=VDD}
N 680 -760 680 -700 {lab=VDD}
N 320 -480 360 -480 {lab=VSS}
N 640 -480 680 -480 {lab=VSS}
N 680 -480 680 -160 {lab=VSS}
N 280 -160 680 -160 {lab=VSS}
N 400 -480 600 -480 {lab=VG2}
N 640 -300 640 -240 {lab=V1}
N 360 -450 360 -240 {lab=V2}
N 660 -340 680 -340 {lab=VSS}
N 320 -480 320 -160 {lab=VSS}
N 280 -760 680 -760 {lab=VDD}
N 500 -560 500 -480 {lab=VG2}
N 440 -590 460 -590 {lab=VG1}
N 440 -660 440 -590 {lab=VG1}
N 440 -660 500 -660 {lab=VG1}
N 540 -640 540 -590 {lab=VG1}
N 500 -590 540 -590 {lab=VG1}
N 500 -640 540 -640 {lab=VG1}
N 500 -700 500 -620 {lab=VG1}
C {devices/ipin.sym} 280 -160 0 0 {name=p1 lab=VSS}
C {devices/ipin.sym} 280 -760 0 0 {name=p2 lab=VDD}
C {devices/lab_wire.sym} 570 -630 0 1 {name=p3 sig_type=std_logic lab=VG1}
C {devices/lab_wire.sym} 430 -550 2 1 {name=p4 sig_type=std_logic lab=VG2}
C {devices/lab_wire.sym} 360 -280 2 0 {name=p5 sig_type=std_logic lab=V2}
C {devices/lab_wire.sym} 640 -280 2 0 {name=p6 sig_type=std_logic lab=V1}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 600 -700 0 0 {name=x1[3:0]}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 400 -700 0 1 {name=x2 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 600 -480 0 0 {name=x3}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 400 -480 0 1 {name=x4 }
C {devices/vsource.sym} 640 -210 0 1 {name=V1 value=0 savecurrent=true}
C {devices/vsource.sym} 360 -210 0 0 {name=V2 value=0 savecurrent=true}
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 640 -300 3 0 {name=x5}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 460 -590 0 0 {name=x6}
C {devices/lab_wire.sym} 640 -420 2 0 {name=p7 sig_type=std_logic lab=VR}
