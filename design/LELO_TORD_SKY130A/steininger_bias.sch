v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 440 -950 540 -950 {lab=VG3}
N 400 -920 400 -860 {lab=VG3}
N 580 -920 580 -860 {lab=VG2_2}
N 440 -710 540 -710 {lab=VG2}
N 460 -950 460 -890 {lab=VG3}
N 520 -770 520 -710 {lab=VG2}
N 520 -770 580 -770 {lab=VG2}
N 400 -1000 400 -980 {lab=VDD}
N 360 -1000 580 -1000 {lab=VDD}
N 400 -680 400 -620 {lab=VG1_3}
N 440 -470 540 -470 {lab=VG1}
N 520 -530 520 -470 {lab=VG1}
N 400 -440 400 -380 {lab=VR}
N 400 -180 400 -160 {lab=VSS}
N 580 -1000 580 -980 {lab=VDD}
N 380 -710 400 -710 {lab=VSS}
N 380 -950 400 -950 {lab=VDD}
N 580 -950 600 -950 {lab=VDD}
N 580 -470 600 -470 {lab=VSS}
N 520 -530 580 -530 {lab=VG1}
N 580 -680 580 -620 {lab=VG1_2}
N 360 -160 580 -160 {lab=VSS}
N 580 -440 580 -240 {lab=V1}
N 400 -300 400 -240 {lab=V2}
N 580 -180 580 -160 {lab=VSS}
N 380 -470 400 -470 {lab=VSS}
N 580 -710 600 -710 {lab=VSS}
N 360 -340 380 -340 {lab=VSS}
N 580 -800 580 -740 {lab=VG2}
N 580 -560 580 -500 {lab=VG1}
N 400 -890 460 -890 {lab=VG3}
N 400 -800 400 -740 {lab=VG3_2}
N 400 -560 400 -500 {lab=VG1_4}
N 180 -590 220 -590 {lab=xxx}
N 260 -660 260 -620 {lab=VG3}
N 260 -560 260 -500 {lab=VSS}
N 260 -590 310 -590 {lab=VSS}
N 310 -590 310 -540 {lab=VSS}
N 260 -540 310 -540 {lab=VSS}
C {devices/ipin.sym} 360 -1000 0 0 {name=p1 lab=VDD}
C {devices/ipin.sym} 360 -160 0 0 {name=p2 lab=VSS}
C {devices/vsource.sym} 580 -210 0 0 {name=V1 value=0 savecurrent=true}
C {devices/vsource.sym} 400 -210 0 0 {name=V2 value=0 savecurrent=true}
C {devices/lab_wire.sym} 380 -950 0 0 {name=p3 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 600 -950 0 1 {name=p4 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 380 -710 2 1 {name=p5 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 600 -710 2 0 {name=p6 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 380 -470 2 1 {name=p7 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 600 -470 2 0 {name=p8 sig_type=std_logic lab=VSS}
C {devices/vsource.sym} 580 -590 0 0 {name=V3 value=0 savecurrent=true}
C {devices/vsource.sym} 400 -590 0 0 {name=V4 value=0 savecurrent=true}
C {devices/vsource.sym} 580 -830 0 0 {name=V5 value=0 savecurrent=true}
C {devices/vsource.sym} 400 -830 0 0 {name=V6 value=0 savecurrent=true}
C {devices/lab_wire.sym} 360 -340 2 1 {name=p9 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 520 -530 2 0 {name=p10 sig_type=std_logic lab=VG1}
C {devices/lab_wire.sym} 520 -770 2 0 {name=p11 sig_type=std_logic lab=VG2}
C {devices/lab_wire.sym} 460 -890 0 0 {name=p12 sig_type=std_logic lab=VG3}
C {devices/lab_wire.sym} 400 -420 2 0 {name=p13 sig_type=std_logic lab=VR}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 540 -470 0 0 {name=x1 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 440 -470 0 1 {name=x2[3:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 540 -710 0 0 {name=x3 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 440 -710 0 1 {name=x4 }
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 540 -950 0 0 {name=x5 }
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 440 -950 0 1 {name=x6 }
C {devices/lab_wire.sym} 400 -280 2 0 {name=p14 sig_type=std_logic lab=V2
}
C {devices/lab_wire.sym} 580 -280 2 1 {name=p15 sig_type=std_logic lab=V1
}
C {devices/lab_wire.sym} 400 -660 2 0 {name=p16 sig_type=std_logic lab=VG1_3
}
C {devices/lab_wire.sym} 400 -780 2 0 {name=p17 sig_type=std_logic lab=VG3_2}
C {devices/lab_wire.sym} 580 -900 2 1 {name=p18 sig_type=std_logic lab=VG2_2}
C {devices/lab_wire.sym} 580 -660 2 1 {name=p19 sig_type=std_logic lab=VG1_2
}
C {devices/lab_wire.sym} 400 -540 2 0 {name=p20 sig_type=std_logic lab=VG1_4
}
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 400 -300 1 1 {name=x7}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 220 -590 0 0 {name=x8}
C {devices/lab_wire.sym} 260 -500 2 1 {name=p23 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 260 -660 0 0 {name=p22 sig_type=std_logic lab=VG3}
C {devices/ipin.sym} 180 -590 0 0 {name=p21 lab=SPARK}
