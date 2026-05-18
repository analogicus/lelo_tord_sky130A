v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 220 310 220 360 {lab=VSS}
N 160 280 200 280 {lab=VSS}
N 160 280 160 360 {lab=VSS}
N 120 200 220 200 {lab=VDD}
N 120 360 220 360 {lab=VSS}
N 220 200 220 250 {lab=VDD}
C {devices/iopin.sym} 120 200 0 1 {name=p1 lab=VDD}
C {devices/iopin.sym} 120 360 0 1 {name=p2 lab=VSS}
C {sky130_fd_pr/res_high_po.sym} 220 280 0 0 {name=R1
W=0.36
L=7.36
model=res_high_po
spiceprefix=X
mult=1}
