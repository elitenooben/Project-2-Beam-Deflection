# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:06:20 2018

@author: Carl
"""

import numpy as np
import pandas as pd
from beamUtils import printLoads
import os

def saveToFile(beamLength, beamSupport, loadPositions, loadForces):
    """
    Saves beam and loads to a file given the beam length, beam support, load positions and load forces.
    Gets a filename from the user to save as that must be alphanumerical.
    Returns None if something goes wrong.
    """
    #Make sure there is something to save
    try:
        print("You are saving a beam of length %s m with support type %s" % (beamLength, beamSupport))
        printLoads(loadPositions, loadForces)
    except NameError:
        print("One must walk before one can fly. Please choose some values before trying to save.")
        return 
    
    #Get a filename, save to filename.csv
    while True:
        filename = input("Please type the desired filename: ")
        if not filename.isalnum():
            print("please choose a name consisting of alphanumerical characters :)")
        #Check if file already exists.
        elif os.path.exists(filename+".csv") or os.path.exists(filename):
            if input("%s.csv already exists.Do you want to overwrite file? [y/n] " %(filename+".csv")) == "y":
                print("Overwriting")
                break
            else:
                print("Not overwriting.")
        else:
            break
    
    #Create a matrix of values, 0th row is beam, rest are the loads.
    values = np.array([beamLength, beamSupport])
    for loadPosition, loadForce in zip(list(loadPositions), list(loadForces)):
        values = np.vstack((values, np.array([loadPosition, loadForce])))
        
    with open(filename+".csv", "w+") as f:
        pd.DataFrame(values).to_csv(f, index=False)
        print("Your file was saved as '" + filename + ".csv'.")
        
