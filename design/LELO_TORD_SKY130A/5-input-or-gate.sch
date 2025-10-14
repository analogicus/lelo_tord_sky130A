v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 120 180 160 180 {lab=IN0}
N 120 200 160 200 {lab=IN1}
N 120 60 160 60 {lab=VSS}
N 120 40 160 40 {lab=VDD}
N 160 150 200 150 {lab=VDD}
N 160 230 200 230 {lab=VSS}
N 250 190 290 190 {lab=#net1}
N 160 290 200 290 {lab=VDD}
N 160 370 200 370 {lab=VSS}
N 250 330 290 330 {lab=#net1}
N 120 320 160 320 {lab=IN2}
N 120 340 160 340 {lab=IN3}
N 290 260 290 330 {lab=#net1}
N 290 260 370 260 {lab=#net1}
N 290 190 290 240 {lab=#net1}
N 120 460 370 460 {lab=IN4}
N 370 260 370 350 {lab=#net1}
N 290 240 290 260 {lab=#net1}
N 410 320 450 320 {lab=VDD}
N 410 400 450 400 {lab=VSS}
N 500 360 540 360 {lab=OUT}
N 370 350 410 350 {lab=#net1}
N 370 370 410 370 {lab=IN4}
N 370 370 370 460 {lab=IN4}
C {devices/ipin.sym} 120 180 2 1 {name=p2 lab=IN0}
C {devices/ipin.sym} 120 200 0 0 {name=p3 lab=IN1}
C {devices/ipin.sym} 120 40 2 1 {name=p9 lab=VDD}
C {devices/ipin.sym} 120 60 2 1 {name=p10 lab=VSS}
C {devices/ipin.sym} 120 320 0 0 {name=p11 lab=IN2}
C {devices/ipin.sym} 120 340 0 0 {name=p12 lab=IN3}
C {devices/ipin.sym} 120 460 0 0 {name=p13 lab=IN4}
C {JNW_TR_SKY130A/JNWTR_ORX1_CV.sym} 160 200 0 0 {name=x1 }
C {devices/lab_wire.sym} 190 150 0 0 {name=p1 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 190 230 2 1 {name=p4 sig_type=std_logic lab=VSS}
C {JNW_TR_SKY130A/JNWTR_ORX1_CV.sym} 160 340 0 0 {name=x2 }
C {devices/lab_wire.sym} 190 290 0 0 {name=p5 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 190 370 2 1 {name=p6 sig_type=std_logic lab=VSS}
C {devices/opin.sym} 540 360 0 0 {name=p7 lab=OUT}
C {JNW_TR_SKY130A/JNWTR_ORX1_CV.sym} 410 370 0 0 {name=x3 }
C {devices/lab_wire.sym} 440 320 0 0 {name=p8 sig_type=std_logic lab=VDD}
C {devices/lab_wire.sym} 440 400 2 1 {name=p14 sig_type=std_logic lab=VSS}
