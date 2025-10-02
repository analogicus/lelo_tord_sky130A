#!/usr/bin/env python3
import pandas as pd
import yaml

def main(name):
  # Delete next line if you want to use python post processing
  # return
  yamlfile = name + ".yaml"
  outfile = name + ".out"

  # Read result yaml file
  with open(yamlfile) as fi:
    obj = yaml.safe_load(fi)

  # Do something to parameters
  print(obj)

  # Save new yaml file
  # with open(yamlfile,"w") as fo:
  #   yaml.dump(obj,fo)

  # Read result file
  df = pd.read_csv(outfile, sep='\s+', comment='*', header=0)
  print(df.head())
