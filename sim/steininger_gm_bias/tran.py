#!/usr/bin/env python3
import pandas as pd
import yaml

def main(name):
  # Delete next line if you want to use python post processing
  # return
  yamlfile = name + ".yaml"

  # Read result yaml file
  with open(yamlfile) as fi:
    obj = yaml.safe_load(fi)

  # Do something to parameters
  print(obj)

  # Save new yaml file
  # with open(yamlfile,"w") as fo:
  #   yaml.dump(obj,fo)

  iv1 = []
  vg1 = []
  gm = []

  for key, val in obj.items():
    if key.startswith("iv1"):
      iv1.append(val)
    elif key.startswith("vg1"):
      vg1.append(val)
    else:
      continue

  if len(iv1) == len(vg1):
    gm = [x / y for x, y in zip(iv1, vg1)]
  print(gm)
