v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 620 -700 820 -700 {lab=VG1}
N 860 -670 860 -510 {lab=VG1}
N 580 -670 580 -510 {lab=VG2}
N 860 -450 860 -380 {lab=VR}
N 580 -760 580 -730 {lab=VDD}
N 860 -760 860 -730 {lab=VDD}
N 790 -700 790 -630 {lab=VG1}
N 790 -630 860 -630 {lab=VG1}
N 580 -550 650 -550 {lab=VG2}
N 650 -550 650 -480 {lab=VG2}
N 580 -180 580 -160 {lab=VSS}
N 860 -180 860 -160 {lab=VSS}
N 540 -700 580 -700 {lab=VDD}
N 540 -760 540 -700 {lab=VDD}
N 860 -700 900 -700 {lab=VDD}
N 900 -760 900 -700 {lab=VDD}
N 540 -480 580 -480 {lab=VSS}
N 860 -480 900 -480 {lab=VSS}
N 900 -480 900 -160 {lab=VSS}
N 500 -160 900 -160 {lab=VSS}
N 620 -480 820 -480 {lab=VG2}
N 860 -300 860 -240 {lab=V1}
N 580 -450 580 -240 {lab=V2}
N 880 -340 900 -340 {lab=VSS}
N 540 -480 540 -160 {lab=VSS}
N 500 -760 900 -760 {lab=VDD}
N 220 -590 260 -590 {lab=SPARK}
N 300 -660 300 -620 {lab=VG1}
N 300 -560 300 -500 {lab=VSS}
N 300 -590 350 -590 {lab=VSS}
N 350 -590 350 -540 {lab=VSS}
N 300 -540 350 -540 {lab=VSS}
C {devices/ipin.sym} 500 -160 0 0 {name=p1 lab=VSS}
C {devices/ipin.sym} 500 -760 0 0 {name=p2 lab=VDD}
C {devices/lab_wire.sym} 790 -630 0 1 {name=p3 sig_type=std_logic lab=VG1}
C {devices/lab_wire.sym} 650 -550 2 1 {name=p4 sig_type=std_logic lab=VG2}
C {devices/lab_wire.sym} 580 -280 2 0 {name=p5 sig_type=std_logic lab=V2}
C {devices/lab_wire.sym} 860 -280 2 0 {name=p6 sig_type=std_logic lab=V1}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 820 -700 0 0 {name=x1[3:0]}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 620 -700 0 1 {name=x2 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 820 -480 0 0 {name=x3}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 620 -480 0 1 {name=x4 }
C {devices/vsource.sym} 860 -210 0 1 {name=V1 value=0 savecurrent=true}
C {devices/vsource.sym} 580 -210 0 0 {name=V2 value=0 savecurrent=true}
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 860 -300 3 0 {name=x5}
C {devices/lab_wire.sym} 860 -420 2 0 {name=p7 sig_type=std_logic lab=VR}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 260 -590 0 0 {name=x8}
C {devices/lab_wire.sym} 300 -500 2 1 {name=p23 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 300 -660 0 0 {name=p8 sig_type=std_logic lab=VG1}
C {devices/ipin.sym} 220 -590 0 0 {name=p21 lab=SPARK}
