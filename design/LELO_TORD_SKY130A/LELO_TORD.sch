v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
T {Shift-I          Insert new component
Shift-Z         Zoom in
Ctrl-Z           Zoom out
R                 Rotate
F                 Full view

Manual: https://xschem.sourceforge.io/stefan/xschem_man/xschem_man.pdf
} -580 -490 0 0 0.6 0.6 {}
N -150 -10 -130 -10 {lab=IBPS_5U}
N -150 10 -130 10 {lab=VSS}
N 170 -10 190 -10 {lab=IBNS_20U}
C {devices/ipin.sym} -150 -10 0 0 {name=p1 lab=IBPS_5U}
C {devices/ipin.sym} -150 10 0 0 {name=p2 lab=VSS}
C {LELO_TORD_SKY130A/test_ex.sym} 20 0 0 0 {name=x1}
C {cborder/border_s.sym} 440 310 0 0 {}
C {devices/opin.sym} 190 -10 0 0 {name=p3 lab=IBNS_20U}
