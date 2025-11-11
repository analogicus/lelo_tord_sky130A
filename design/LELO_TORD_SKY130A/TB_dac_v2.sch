v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 400 130 540 130 {lab=vdiode}
N 540 130 540 150 {lab=vdiode}
N 540 210 540 230 {lab=vss}
N 80 230 540 230 {lab=vss}
N 80 200 80 230 {lab=vss}
N 60 200 100 200 {lab=vss}
N 60 180 100 180 {lab=b4}
N 60 160 100 160 {lab=b3}
N 60 140 100 140 {lab=b2}
N 60 120 100 120 {lab=b1}
N 60 100 100 100 {lab=b0}
N 60 80 100 80 {lab=vdd}
N 60 60 100 60 {lab=sleep}
N 500 180 500 230 {lab=vss}
N 540 130 580 130 {lab=vdiode}
C {sky130_fd_pr/pnp_05v5.sym} 520 180 0 0 {name=Q1
model=pnp_05v5_W3p40L3p40
m=1
spiceprefix=X
}
C {LELO_TORD_SKY130A/dac_v3.sym} 250 130 0 0 {name=x1}
C {devices/ipin.sym} 60 120 0 0 {name=p17 lab=b1}
C {devices/ipin.sym} 60 140 0 0 {name=p18 lab=b2}
C {devices/ipin.sym} 60 160 0 0 {name=p19 lab=b3}
C {devices/ipin.sym} 60 180 0 0 {name=p20 lab=b4}
C {devices/ipin.sym} 60 100 0 0 {name=p7 lab=b0}
C {devices/ipin.sym} 60 200 0 0 {name=p1 lab=vss}
C {devices/ipin.sym} 60 80 0 0 {name=p2 lab=vdd}
C {devices/ipin.sym} 60 60 0 0 {name=p3 lab=sleep}
C {devices/opin.sym} 580 130 0 0 {name=p54 lab=vdiode}
