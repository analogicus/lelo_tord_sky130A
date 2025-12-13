#!/usr/bin/env python3
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import numpy as np

from scripts import plot_transients as pt

def main(name):
  # # Delete next line if you want to use python post processing
  # return
  # yamlfile = name + ".yaml"

  # # Read result yaml file
  # with open(yamlfile) as fi:
  #   obj = yaml.safe_load(fi)

  # # Do something to parameters
  # print(obj)

  # # Save new yaml file
  # with open(yamlfile,"w") as fo:
  #   yaml.dump(obj,fo)

  if name == "output_tran/tran_SchGtKttTtVt":
    pt.plot_tran(name)
    # print("Skipping tran_SchGtKttTtVt")

if __name__ == "__main__":
  default_name = "output_tran/tran_SchGtKttTtVt"
  main(default_name)
