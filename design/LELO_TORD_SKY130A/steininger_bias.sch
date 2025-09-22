v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 600 -950 700 -950 {lab=VG3}
N 560 -920 560 -860 {lab=VG3}
N 740 -920 740 -860 {lab=VG2_2}
N 600 -710 700 -710 {lab=VG2}
N 620 -950 620 -890 {lab=VG3}
N 680 -770 680 -710 {lab=VG2}
N 680 -770 740 -770 {lab=VG2}
N 560 -1000 560 -980 {lab=VDD}
N 520 -1000 740 -1000 {lab=VDD}
N 560 -680 560 -620 {lab=VG1_3}
N 600 -470 700 -470 {lab=VG1}
N 680 -530 680 -470 {lab=VG1}
N 560 -440 560 -380 {lab=VR}
N 560 -180 560 -160 {lab=VSS}
N 740 -1000 740 -980 {lab=VDD}
N 540 -710 560 -710 {lab=VSS}
N 540 -950 560 -950 {lab=VDD}
N 740 -950 760 -950 {lab=VDD}
N 740 -470 760 -470 {lab=VSS}
N 680 -530 740 -530 {lab=VG1}
N 740 -680 740 -620 {lab=VG1_2}
N 520 -160 740 -160 {lab=VSS}
N 740 -440 740 -240 {lab=V1}
N 560 -300 560 -240 {lab=V2}
N 740 -180 740 -160 {lab=VSS}
N 540 -470 560 -470 {lab=VSS}
N 740 -710 760 -710 {lab=VSS}
N 520 -340 540 -340 {lab=VSS}
N 740 -800 740 -740 {lab=VG2}
N 740 -560 740 -500 {lab=VG1}
N 560 -890 620 -890 {lab=VG3}
N 560 -800 560 -740 {lab=VG3_2}
N 560 -560 560 -500 {lab=VG1_4}
N 200 -590 240 -590 {lab=xxx}
N 280 -660 280 -620 {lab=VG3}
N 280 -560 280 -500 {lab=VSS}
N 280 -590 330 -590 {lab=VSS}
N 330 -590 330 -540 {lab=VSS}
N 280 -540 330 -540 {lab=VSS}
C {devices/ipin.sym} 520 -1000 0 0 {name=p1 lab=VDD}
C {devices/ipin.sym} 520 -160 0 0 {name=p2 lab=VSS}
C {devices/vsource.sym} 740 -210 0 0 {name=V1 value=0 savecurrent=true}
C {devices/vsource.sym} 560 -210 0 0 {name=V2 value=0 savecurrent=true}
C {devices/lab_wire.sym} 540 -950 0 0 {name=p3 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 760 -950 0 1 {name=p4 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 540 -710 2 1 {name=p5 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 760 -710 2 0 {name=p6 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 540 -470 2 1 {name=p7 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 760 -470 2 0 {name=p8 sig_type=std_logic lab=VSS}
C {devices/vsource.sym} 740 -590 0 0 {name=V3 value=0 savecurrent=true}
C {devices/vsource.sym} 560 -590 0 0 {name=V4 value=0 savecurrent=true}
C {devices/vsource.sym} 740 -830 0 0 {name=V5 value=0 savecurrent=true}
C {devices/vsource.sym} 560 -830 0 0 {name=V6 value=0 savecurrent=true}
C {devices/lab_wire.sym} 520 -340 2 1 {name=p9 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 680 -530 2 0 {name=p10 sig_type=std_logic lab=VG1}
C {devices/lab_wire.sym} 680 -770 2 0 {name=p11 sig_type=std_logic lab=VG2}
C {devices/lab_wire.sym} 620 -890 0 0 {name=p12 sig_type=std_logic lab=VG3}
C {devices/lab_wire.sym} 560 -420 2 0 {name=p13 sig_type=std_logic lab=VR}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 700 -470 0 0 {name=x1 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 600 -470 0 1 {name=x2[3:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 700 -710 0 0 {name=x3 }
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 600 -710 0 1 {name=x4 }
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 700 -950 0 0 {name=x5 }
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 600 -950 0 1 {name=x6 }
C {devices/lab_wire.sym} 560 -280 2 0 {name=p14 sig_type=std_logic lab=V2
}
C {devices/lab_wire.sym} 740 -280 2 1 {name=p15 sig_type=std_logic lab=V1
}
C {devices/lab_wire.sym} 560 -660 2 0 {name=p16 sig_type=std_logic lab=VG1_3
}
C {devices/lab_wire.sym} 560 -780 2 0 {name=p17 sig_type=std_logic lab=VG3_2}
C {devices/lab_wire.sym} 740 -900 2 1 {name=p18 sig_type=std_logic lab=VG2_2}
C {devices/lab_wire.sym} 740 -660 2 1 {name=p19 sig_type=std_logic lab=VG1_2
}
C {devices/lab_wire.sym} 560 -540 2 0 {name=p20 sig_type=std_logic lab=VG1_4
}
C {JNW_TR_SKY130A/JNWTR_RPPO2.sym} 560 -300 1 1 {name=x7}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 240 -590 0 0 {name=x8}
C {devices/lab_wire.sym} 280 -500 2 1 {name=p23 sig_type=std_logic lab=VSS}
C {devices/lab_wire.sym} 280 -660 0 0 {name=p22 sig_type=std_logic lab=VG3}
C {devices/ipin.sym} 200 -590 0 0 {name=p21 lab=SPARK}
