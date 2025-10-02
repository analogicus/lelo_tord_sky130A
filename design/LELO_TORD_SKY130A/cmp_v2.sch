v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 530 -180 570 -180 {lab=VSS}
N 570 -200 570 -180 {lab=VSS}
N 730 -180 770 -180 {lab=VSS}
N 470 -380 530 -380 {lab=VIP}
N 570 -350 570 -260 {lab=OTA_CM_gate}
N 750 -350 750 -320 {lab=VOUT}
N 570 -410 750 -410 {lab=OTA_VDD}
N 630 -280 630 -230 {lab=OTA_CM_gate}
N 570 -280 630 -280 {lab=OTA_CM_gate}
N 790 -380 830 -380 {lab=VIN}
N 570 -380 610 -380 {lab=OTA_VDD}
N 610 -380 750 -380 {lab=OTA_VDD}
N 650 -460 650 -410 {lab=OTA_VDD}
N 650 -560 650 -520 {lab=VDD}
N 250 -560 650 -560 {lab=VDD}
N 690 -540 690 -490 {lab=VDD}
N 650 -540 690 -540 {lab=VDD}
N 330 -490 610 -490 {lab=I_BIAS}
N 290 -560 290 -520 {lab=VDD}
N 270 -540 290 -540 {lab=VDD}
N 290 -440 370 -440 {lab=I_BIAS}
N 370 -490 370 -440 {lab=I_BIAS}
N 270 -140 650 -140 {lab=VSS}
N 290 -180 290 -140 {lab=VSS}
N 290 -460 290 -440 {lab=I_BIAS}
N 570 -180 650 -180 {lab=VSS}
N 650 -180 650 -160 {lab=VSS}
N 650 -180 730 -180 {lab=VSS}
N 630 -410 630 -380 {lab=OTA_VDD}
N 650 -160 650 -140 {lab=VSS}
N 230 -140 270 -140 {lab=VSS}
N 630 -230 710 -230 {lab=OTA_CM_gate}
N 610 -230 630 -230 {lab=OTA_CM_gate}
N 750 -200 750 -180 {lab=VSS}
N 750 -230 770 -230 {lab=VSS}
N 750 -300 830 -300 {lab=VOUT}
N 250 -540 250 -490 {lab=VDD}
N 770 -180 810 -180 {lab=VSS}
N 810 -230 810 -180 {lab=VSS}
N 770 -230 810 -230 {lab=VSS}
N 510 -230 530 -230 {lab=VSS}
N 510 -180 530 -180 {lab=VSS}
N 250 -490 290 -490 {lab=VDD}
N 650 -490 690 -490 {lab=VDD}
N 570 -280 570 -260 {lab=OTA_CM_gate}
N 750 -280 750 -260 {lab=VOUT}
N 750 -300 750 -280 {lab=VOUT}
N 750 -320 750 -300 {lab=VOUT}
N 830 -300 870 -300 {lab=VOUT}
N 290 -190 290 -180 {lab=VSS}
N 310 -230 350 -230 {lab=VSS}
N 350 -230 350 -140 {lab=VSS}
N 310 -320 350 -320 {lab=VSS}
N 350 -320 350 -230 {lab=VSS}
N 290 -440 290 -360 {lab=I_BIAS}
N 290 -280 290 -270 {lab=#net1}
N 510 -230 510 -180 {lab=VSS}
N 530 -230 570 -230 {lab=VSS}
N 250 -540 270 -540 {lab=VDD}
C {devices/ipin.sym} 470 -380 0 0 {name=p1 lab=VIP
}
C {devices/ipin.sym} 830 -380 2 0 {name=p2 lab=VIN}
C {devices/ipin.sym} 250 -560 0 0 {name=p3 lab=VDD}
C {devices/ipin.sym} 230 -140 0 0 {name=p4 lab=VSS}
C {devices/opin.sym} 870 -300 0 0 {name=p5 lab=VOUT
}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 610 -230 0 1 {name=x1[1:0]}
C {JNW_ATR_SKY130A/JNWATR_NCH_4C5F0.sym} 710 -230 0 0 {name=x2[1:0]}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 530 -380 0 0 {name=x3[1:0]
}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 790 -380 0 1 {name=x4[1:0]
}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 610 -490 0 0 {name=x5}
C {JNW_ATR_SKY130A/JNWATR_PCH_4C5F0.sym} 330 -490 0 1 {name=x6[11:0]}
C {devices/lab_wire.sym} 660 -410 0 1 {name=p6 sig_type=std_logic lab=OTA_VDD}
C {devices/lab_wire.sym} 500 -490 0 0 {name=p7 sig_type=std_logic lab=I_BIAS}
C {devices/lab_wire.sym} 570 -310 0 0 {name=p8 sig_type=std_logic lab=OTA_CM_gate}
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 290 -270 3 1 {name=x4 }
C {JNW_TR_SKY130A/JNWTR_RPPO16.sym} 290 -360 3 1 {name=x1 }
