# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:06:20 2018

@author: William
"""

import numpy as np
import pandas as pd


def saveToFile(beamLength, beamSupport, loadPositions, loadForces):
    #Make sure there is something to save
    try:
        print("You are saving the following:\n\nBeamlength: %s\nBeamSupport: %s\nLoad position(s): %s\nForce(s) of load(s): %s" % (beamLength, beamSupport, loadPositions, loadForces))
    except NameError:
        return print("One must walk before one can fly. Please choose some values before trying to save.")
    
    #Get a filename, save to filename.csv
    while True:
        filename = input("Please type the desired filename: ")
        if not filename.isalnum():
            print("please choose a name consisting of alphanumerical characters :)")
        else:
            #Create a matrix of values, 0th row is beam, rest are the loads.
            values = np.array([beamLength, beamSupport])
            for loadPosition, loadForce in zip(list(loadPositions), list(loadForces)):
                values = np.vstack((values, np.array([loadPosition, loadForce])))
            
            with open(filename+".csv", "w+") as f:
                pd.DataFrame(values).to_csv(f, index=False)
                print("Your file was saved as '" + filename + ".csv'. Good job! :D")
            return
