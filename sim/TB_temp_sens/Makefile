

all: typical etc mc summary



TB=tran
VIEW=Sch
#VIEW=Lay
CELL=TB_temp_sens
LIB =LELO_TORD_SKY130A
OPT=

include ../../tech/make/sim.make

test:
	${MAKE} typical OPT="Debug"

typical: netlist
	cicsim run --name ${VIEW}_typical ${TB} ${OPT} ${VIEW} Gt Ktt Tt Vt

ttvl: netlist
	cicsim run --name ${VIEW}_ttvl ${TB} ${OPT} ${VIEW} Gt "Ktt" Tt Vl

ttvh: netlist
	cicsim run --name ${VIEW}_ttvh ${TB} ${OPT} ${VIEW} Gt "Ktt" Tt Vh

ssvl: netlist
	cicsim run --name ${VIEW}_ssvl ${TB} ${OPT} ${VIEW} Gt Kss Tt Vl

ssvh: netlist
	cicsim run --name ${VIEW}_ssvh ${TB} ${OPT} ${VIEW} Gt Kss Tt Vh

ffvl: netlist
	cicsim run --name ${VIEW}_ffvl ${TB} ${OPT} ${VIEW} Gt Kff Tt Vl

ffvh: netlist
	cicsim run --name ${VIEW}_ffvh ${TB} ${OPT} ${VIEW} Gt Kff Tt Vh

slow: netlist
	cicsim run --name ${VIEW}_slow ${TB} ${OPT} ${VIEW} Gt Kss "Th,Tl" Vl

fast: netlist
	cicsim run --name ${VIEW}_fast ${TB} ${OPT} ${VIEW} Gt Kff "Th,Tl" Vh

tfs: netlist
	cicsim run --name ${VIEW}_tfs ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Kff" "Tt,Th,Tl" "Vt,Vl,Vh"

etc: netlist
	cicsim run --name ${VIEW}_etc ${TB} ${OPT} ${VIEW} Gt "Kss,Kff,Ksf,Kfs" "Th,Tl" "Vl,Vh"

mc: netlist
	cicsim run --name ${VIEW}_mc --count 30 ${TB} ${OPT} ${VIEW} Gt "Kttmm" "Tt" "Vt"

ntc: netlist
	cicsim run --name ${VIEW}_ntc ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Kff" "Tt" Vt

temp: netlist
	cicsim run --name ${VIEW}_temp ${TB} ${OPT} ${VIEW} Gt "Ktt" "Tt,Th,Tl" Vt

corners: netlist
	cicsim run --name ${VIEW}_vtcorners ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Kff,Ksf,Kfs" "Tt" "Vl,Vt,Vh"

summary:
	cicsim summary --output "README.md"

slide:
	pandoc -s  -t slidy README.md -o README.html


clean:
	-rm -rf output_*
	-rm -rf __pycache__
	-rm *.run
	-rm *.pdf
	-rm *.csv
