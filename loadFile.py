# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:50:11 2018

@author: William
"""

import numpy as np
import pandas as pd
import os

def loadFile():
    while True:
        filename = input("Name of file to load (write 'I surrender' to quit): ")
        if os.path.exists(filename+".csv") or os.path.exists(filename):
            data = list(pd.read_csv(filename+".csv"))
            break
        elif filename.lower() == "i surrender":
            return "Better luck next time"
        else:
            print("File not found. Try again.")
    del data[-1]
    beamLength = float(data[0])
    beamSupport = data[1]
    split = int(2+(len(data)-2)/2)
    loadPositions = data[2:split]
    loadForces = data[split:]
    return loadForces

print(loadFile())