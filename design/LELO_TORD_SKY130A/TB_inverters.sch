v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 280 240 320 240 {lab=vdd}
N 280 100 320 100 {lab=vdd}
N 280 180 320 180 {lab=vss}
N 280 320 320 320 {lab=vss}
N 240 280 280 280 {lab=in2}
N 360 280 400 280 {lab=out2}
N 360 140 400 140 {lab=out1}
N 240 140 280 140 {lab=in1}
N 280 380 320 380 {lab=vdd}
N 280 460 320 460 {lab=vss}
N 240 420 280 420 {lab=in3}
N 360 420 400 420 {lab=out3}
N 280 520 320 520 {lab=vdd}
N 280 600 320 600 {lab=vss}
N 280 600 320 600 {lab=vss}
N 240 560 280 560 {lab=in4}
N 360 560 400 560 {lab=inv4_outp}
C {JNW_TR_SKY130A/JNWTR_IVX1_CV.sym} 280 140 0 0 {name=x1 }
C {JNW_TR_SKY130A/JNWTR_IVX2_CV.sym} 280 280 0 0 {name=x2 }
C {JNW_TR_SKY130A/JNWTR_IVX4_CV.sym} 280 420 0 0 {name=x3 }
C {JNW_TR_SKY130A/JNWTR_IVX8_CV.sym} 280 560 0 0 {name=x4 }
C {devices/opin.sym} 400 560 0 0 {name=p1 lab=out4}
C {devices/opin.sym} 400 420 0 0 {name=p2 lab=out3}
C {devices/opin.sym} 400 280 0 0 {name=p3 lab=out2}
C {devices/opin.sym} 400 140 0 0 {name=p4 lab=out1
}
C {devices/ipin.sym} 240 140 0 0 {name=p5 lab=in1
}
C {devices/ipin.sym} 240 280 0 0 {name=p6 lab=in2}
C {devices/ipin.sym} 240 420 0 0 {name=p7 lab=in3}
C {devices/ipin.sym} 240 560 0 0 {name=p8 lab=in4
}
C {devices/ipin.sym} 280 100 0 0 {name=p9 lab=vdd}
C {devices/ipin.sym} 280 600 0 0 {name=p10 lab=vss}
C {devices/lab_pin.sym} 280 240 0 0 {name=p11 sig_type=std_logic lab=vdd}
C {devices/lab_pin.sym} 280 320 0 0 {name=p12 sig_type=std_logic lab=vss}
C {devices/lab_pin.sym} 280 460 0 0 {name=p13 sig_type=std_logic lab=vss}
C {devices/lab_pin.sym} 280 380 0 0 {name=p15 sig_type=std_logic lab=vdd}
C {devices/lab_pin.sym} 280 520 0 0 {name=p16 sig_type=std_logic lab=vdd}
C {devices/lab_pin.sym} 280 180 0 0 {name=p18 sig_type=std_logic lab=vss}
