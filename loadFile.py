# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:50:11 2018

@author: William
"""

import numpy as np
import pandas as pd


def loadFile():
    filename = input("Name of file to load: ")
    data = list(pd.read_csv(filename+".csv"))
    del data[-1]
    beamLength = float(data[0])
    beamSupport = data[1]
    split = int(2+(len(data)-2)/2)
    loadPositions = data[2:split]
    loadForces = data[split:]
    return loadForces

print(loadFile())