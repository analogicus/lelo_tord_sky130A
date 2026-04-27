

# all: typical etc mc summary
slowfast: slow fast


# Testbench: 1stb, dc, ac, tran, ...
TB=tran

# Circuit view: Sch, Lay, ...
VIEW=Sch
#VIEW=Lay

# Cell name: TB_dig_ctrl, ...
CELL=TB_dig_ctrl

# Library name: LELO_TORD_SKY130A, ...
LIB=LELO_TORD_SKY130A

OPT=

include ../../tech/make/sim.make

test:
	${MAKE} typical OPT="Debug"

typical: netlist
	cicsim run --name ${VIEW}_typical ${TB} ${OPT} ${VIEW} Gt Ktt Tt Vt

slow: netlist
	cicsim run --name ${VIEW}_slow ${TB} ${OPT} ${VIEW} Gt Kss "Tt" Vl

fast: netlist
	cicsim run --name ${VIEW}_fast ${TB} ${OPT} ${VIEW} Gt Kff "Tt" Vh

tfs: netlist
	cicsim run --name ${VIEW}_tfs ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Kff" "Tt" "Vt,Vl,Vh"

etc: netlist
	cicsim run --name ${VIEW}_etc ${TB} ${OPT} ${VIEW} Gt "Kss,Kff,Ksf,Kfs" "Tt" "Vl,Vh"

mc: netlist
	cicsim run --name ${VIEW}_mc --count 30 ${TB} ${OPT} ${VIEW} Gt "Kttmm" "Tt" "Vt"

ntc: netlist
	cicsim run --name ${VIEW}_ntc ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Kff" "Tt" Vt

temp: netlist
	cicsim run --name ${VIEW}_temp ${TB} ${OPT} ${VIEW} Gt "Ktt" "Tt" Vt

all: netlist
	cicsim run --name ${VIEW}_all ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Ksf,Kfs,Kff" "Tt" "Vt,Vl,Vh"

custom: netlist
	cicsim run --name ${VIEW}_custom ${TB} ${OPT} ${VIEW} Gt "Kss,Kff" "Tt" "Vl,Vh"

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
