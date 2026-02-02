v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 360 220 400 220 {lab=VDD}
N 360 240 400 240 {lab=VIP}
N 360 260 400 260 {lab=VIN}
N 360 280 400 280 {lab=VSS}
N 700 220 740 220 {lab=VO_NMOS}
N 700 330 740 330 {lab=VO_PMOS}
N 360 330 400 330 {lab=VDD}
N 360 350 400 350 {lab=VIP}
N 360 370 400 370 {lab=VIN}
N 360 390 400 390 {lab=VSS}
N 700 440 740 440 {lab=VO_NCH_LVT}
N 360 440 400 440 {lab=VDD}
N 360 460 400 460 {lab=VIP}
N 360 480 400 480 {lab=VIN}
N 360 500 400 500 {lab=VSS}
N 700 550 740 550 {lab=VO_PCH_LVT}
N 360 550 400 550 {lab=VDD}
N 360 570 400 570 {lab=VIP}
N 360 590 400 590 {lab=VIN}
N 360 610 400 610 {lab=VSS}
N 700 660 740 660 {lab=VO_NCH_CRS}
N 360 660 400 660 {lab=VDD}
N 360 680 400 680 {lab=VIP}
N 360 700 400 700 {lab=VIN}
N 360 720 400 720 {lab=VSS}
N 700 770 740 770 {lab=VO_PCH_CRS}
N 360 770 400 770 {lab=VDD}
N 360 790 400 790 {lab=VIP}
N 360 810 400 810 {lab=VIN}
N 360 830 400 830 {lab=VSS}
N 700 790 740 790 {lab=VO_PCH_CRS}
N 700 680 740 680 {lab=VO_NCH_CRS_N}
C {devices/opin.sym} 740 220 2 1 {name=p5 lab=VO_NMOS}
C {devices/ipin.sym} 360 220 0 0 {name=p1 lab=VDD}
C {devices/ipin.sym} 360 240 0 0 {name=p2 lab=VIP}
C {devices/ipin.sym} 360 260 0 0 {name=p3 lab=VIN}
C {devices/ipin.sym} 360 280 0 0 {name=p4 lab=VSS}
C {devices/lab_wire.sym} 380 330 0 0 {name=p6 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 380 350 0 0 {name=p7 sig_type=std_logic lab=VIP}
C {devices/lab_wire.sym} 380 370 0 0 {name=p8 sig_type=std_logic lab=VIN}
C {devices/lab_wire.sym} 380 390 0 0 {name=p9 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 740 330 2 1 {name=p10 lab=VO_PMOS}
C {LELO_TORD_SKY130A/cmp_two_stage_nmos.sym} 550 250 0 0 {name=x1}
C {LELO_TORD_SKY130A/cmp_two_stage_pmos.sym} 550 360 0 0 {name=x2}
C {devices/lab_wire.sym} 380 440 0 0 {name=p11 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 380 460 0 0 {name=p12 sig_type=std_logic lab=VIP}
C {devices/lab_wire.sym} 380 480 0 0 {name=p13 sig_type=std_logic lab=VIN}
C {devices/lab_wire.sym} 380 500 0 0 {name=p14 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 740 440 2 1 {name=p15 lab=VO_NCH_LVT}
C {devices/lab_wire.sym} 380 550 0 0 {name=p16 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 380 570 0 0 {name=p17 sig_type=std_logic lab=VIP}
C {devices/lab_wire.sym} 380 590 0 0 {name=p18 sig_type=std_logic lab=VIN}
C {devices/lab_wire.sym} 380 610 0 0 {name=p19 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 740 550 2 1 {name=p20 lab=VO_PCH_LVT}
C {LELO_TORD_SKY130A/cmp_two_stage_nmos_lvt.sym} 550 470 0 0 {name=x3}
C {LELO_TORD_SKY130A/cmp_two_stage_pmos_lvt.sym} 550 580 0 0 {name=x4}
C {devices/lab_wire.sym} 380 660 0 0 {name=p21 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 380 680 0 0 {name=p22 sig_type=std_logic lab=VIP}
C {devices/lab_wire.sym} 380 700 0 0 {name=p23 sig_type=std_logic lab=VIN}
C {devices/lab_wire.sym} 380 720 0 0 {name=p24 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 740 660 2 1 {name=p25 lab=VO_NCH_CRS}
C {devices/lab_wire.sym} 380 770 0 0 {name=p26 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 380 790 0 0 {name=p27 sig_type=std_logic lab=VIP}
C {devices/lab_wire.sym} 380 810 0 0 {name=p28 sig_type=std_logic lab=VIN}
C {devices/lab_wire.sym} 380 830 0 0 {name=p29 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 740 770 2 1 {name=p30 lab=VO_PCH_CRS}
C {LELO_TORD_SKY130A/cmp_two_stage_nmos_cross_armed.sym} 550 690 0 0 {name=x5}
C {LELO_TORD_SKY130A/cmp_two_stage_pmos_cross_armed.sym} 550 800 0 0 {name=x6}
C {devices/opin.sym} 740 680 2 1 {name=p31 lab=VO_NCH_CRS_N}
C {devices/opin.sym} 740 790 2 1 {name=p32 lab=VO_PCH_CRS_N}
