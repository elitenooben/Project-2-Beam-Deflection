# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:50:11 2018

@author: Christian
"""

import pandas as pd
import os
from beamUtils import validLoads

def loadFile():
    """
    Gets a filename to load from from the user. It must be alphanumerical.
    Loads csv using 
    Returns an array [beamLength, beamSupport, loadPositions, loadForces] if succesful,none if it fails.
    """
    filename = None
    while True:
        filename = input("Name of file to load (write 'Q' to quit): ")
        if filename.lower() == "q":
            print("Better luck next time!")
            return 
        elif not filename.isalnum():
            print("Write only alphanumerical characters :). The program loads the file <filename>.csv")
        elif os.path.exists(filename+".csv") or os.path.exists(filename):
            break
        else:
            print("File %s.csv not found. Try again." %(filename))
            
    #Load data from file using pandas
    data = None
    try:
        with open(filename+".csv") as file:
            data = pd.read_csv(file)
            data = data.values
            beamLength = float(data[0,0])
            beamSupport = data[0,1]
            loadPositions = data[1:,0].astype(float)
            loadForces = data[1:,1].astype(float)
            
            #Remove illegal loads
            loadTuple = validLoads(beamLength, loadPositions, loadForces)
            loadPositions = loadTuple[0]
            loadForces = loadTuple[1]
            
            #Check whether supports are valid
            if beamSupport != "Both" and beamSupport != "Cantilever":
                print("Invalid beam support! Please only load files saved by this program")
                return
            
            return [beamLength, beamSupport, loadPositions, loadForces]
        print("Something went wrong with the io. Please retry")
        return
    #If there is some error in there
    except ValueError:
        print("Some value in the file is invalid. Please only load files saved by this program.")
    except:
        print("Something very weird happened! Please only load files saved by this program.")
