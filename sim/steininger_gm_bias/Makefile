

all: typical etc mc summary



TB=tran
VIEW=Sch
#VIEW=Lay
CELL=steininger_gm_bias
LIB =LELO_TORD_SKY130A
OPT=

include ../../tech/make/sim.make

test:
	${MAKE} typical OPT="Debug"

typical: netlist
	cicsim run --name ${VIEW}_typical ${TB} ${OPT} ${VIEW} Gt Ktt Tt Vt

supply: netlist
	cicsim run --name ${VIEW}_supply ${TB} ${OPT} ${VIEW} Gt Ktt Tt "Vl,Vt,Vh"

supply_fs: netlist
	cicsim run --name ${VIEW}_supply_fs ${TB} ${OPT} ${VIEW} Gt Kfs Tt "Vl,Vt,Vh"

supply_sf: netlist
	cicsim run --name ${VIEW}_supply_sf ${TB} ${OPT} ${VIEW} Gt Ksf Tt "Vl,Vt,Vh"

supply_ss: netlist
	cicsim run --name ${VIEW}_supply_ss ${TB} ${OPT} ${VIEW} Gt Kss Tt "Vl,Vt,Vh"

supply_ff: netlist
	cicsim run --name ${VIEW}_supply_ff ${TB} ${OPT} ${VIEW} Gt Kff Tt "Vl,Vt,Vh"

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
