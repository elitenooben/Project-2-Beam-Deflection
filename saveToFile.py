# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:06:20 2018

@author: William
"""

import numpy as np
import pandas as pd

beamLength = 20
beamSupport = "Both"
loadPositions = np.array([5,11,17,15,0,17])
loadForces = np.array([1000,430,17,9,8,7])


def saveToFile():
    safechars = "abcdefghijklmnopqrstuvwxyzæøå1234567890 -_."
    try:
        print("You are saving the following:\n\nBeamlength: %s\nBeamSupport: %s\nLoad position(s): %s\nForce(s) of load(s): %s" % (beamLength, beamSupport, loadPositions, loadForces))
    except NameError:
        print("One must walk before one can fly. Please choose some values before trying to save.")
    while True:
        filename = input("Please type the desired filename: ")
        if len(set(filename.lower()+safechars)) != len(safechars):
            print("please choose a name without weird characters :)")
        else:
            values = [beamLength, beamSupport] + list(loadPositions) + list(loadForces)
            with open(filename+".csv", "w+") as f:
                for item in values:
                    f.write("%s," % item)
            print("Your file was saved as '" + filename + ".csv'. Good job! :D")
                         
print(saveToFile())
