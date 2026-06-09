v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 1720 390 1760 390 {lab=GATE}
N 1640 390 1680 390 {lab=SOURCE}
N 1640 340 1640 390 {lab=SOURCE}
N 1640 340 1680 340 {lab=SOURCE}
N 1680 320 1680 360 {lab=SOURCE}
N 1760 320 1760 390 {lab=GATE}
N 1680 420 1680 460 {lab=DRAIN}
C {devices/lab_pin.sym} 1680 320 0 0 {name=p1 sig_type=std_logic lab=SOURCE}
C {devices/lab_pin.sym} 1680 460 0 1 {name=p3 sig_type=std_logic lab=DRAIN}
C {devices/lab_pin.sym} 1760 320 0 0 {name=p2 sig_type=std_logic lab=GATE}
C {devices/iopin.sym} 1440 340 0 0 {name=p0 lab=DRAIN}
C {devices/iopin.sym} 1440 360 0 0 {name=p4 lab=GATE}
C {devices/iopin.sym} 1440 380 0 0 {name=p5 lab=SOURCE}
C {sky130_fd_pr/pfet_01v8.sym} 1700 390 0 1 {name=M1
W=10
L=0.94
nf=2
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X
}
