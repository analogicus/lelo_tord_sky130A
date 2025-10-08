[![GDS](../../actions/workflows/gds.yaml/badge.svg)](../../actions/workflows/gds.yaml)
[![DRC](../../actions/workflows/drc.yaml/badge.svg)](../../actions/workflows/drc.yaml)
[![LVS](../../actions/workflows/lvs.yaml/badge.svg)](../../actions/workflows/lvs.yaml)
[![DOCS](../../actions/workflows/docs.yaml/badge.svg)](../../actions/workflows/docs.yaml)
[![SIM](../../actions/workflows/sim.yaml/badge.svg)](../../actions/workflows/sim.yaml)


# Who

tos4 | Tordnado | Tord Olsen Sætermo


# Why

This repository contains work related to my specialization project and master thesis on duty cycled bandgap reference (BGR) circuits at the Norwegian University of Science and Technology (NTNU) in collaboration with Nordic Semiconductor ASA.


# How

The circuit was designed and simulated using open source tools such as [Xschem](https://xschem.sourceforge.io/stefan/index.html), [Magic](http://opencircuitdesign.com/magic/), [ngspice](https://ngspice.sourceforge.io/index.html) and [cicsim](https://analogicus.com/cicsim/), as well as the open source 130 nm process technology from Skywater and Google.


# What

| What                | Cell/Name			       |
| :---                | :---     			       |
| Top level schematic | design/LELO_TORD_SKY130A/LELO_TORD.sch |
| Top level layout    | design/LELO_TORD_SKY130A/LELO_TORD.mag |


# Changelog/Plan

| Version | Status | Comment             |
| :---:   | :---:  | :---                |
| 0.1.0   | :✅:   | Make something      |
| 0.1.1   | :❌:   | Make something else |


# Signal interface

| Signal       | Direction | Domain  | Description                               |
| :---         | :---:     | :---:   | :---                                      |
| VDD_1V8      | Input     | VDD_1V8 | Main supply voltage                       |
| VSS          | Input     | Ground  | Ground                                    |
| PWRUP_1V8    | Input     | VDD_1V8 | Power up the circuit                      |


# Key parameters

| Parameter  | Min   | Typ             | Max   | Unit  |
| :---       | :---: | :---:           | :---: | :---: |
| Technology |       | Skywater 130 nm |       |       |
| AVDD       | 1.7   | 1.8             | 1.9   | V     |
| Temperatur | -40   | 27              | 125   | C     |
