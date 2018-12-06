# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:38:42 2018

Contains utility functions.

@author: carl
"""
import numpy as np

def printLoads(loadPositions, loadForces):
    """
    Prints given loads. Returns whether any loads currently exist
    """
    if(len(loadPositions) == 0):
        print("No current loads")
        return False
    else:
        print(" Loads")
        for i, load in enumerate(zip(loadPositions, loadForces)):
            print(str(i+1) + ". " + str(load[1]) + "N at " + str(load[0]) + "m")
        return True
    
def isFloat(string):
    """
    Checks whether a string can be converted to a float.
    """
    try:
        float(string)
    except ValueError:
        return False;
    return True;


def validLoads(beamLength, loadPositions, loadForces):
    """Returns valid loads for the given beam length."""
    
    #Create indexer to index valid load positions
    indexer = np.logical_and(loadPositions >= 0, loadPositions <= beamLength)
    
    
    invalid = loadPositions[np.logical_not(indexer)]
    
    newloads = loadPositions[indexer]
    newForces = loadForces[indexer]
    
    #Informs user if any load positions are invalid
    if len(invalid)>0:
        print("The load(s) at position(s) %s have been removed, because they are not on the %s meter long beam." % (invalid,beamLength))
    
    return (newloads, newForces)

def checkLoads(beamLength, loadPosition):
    """
    Checks whether all loads are valid for current beam.
    """    
    for load in loadPosition:
        if load < 0 or load > beamLength:
            return False
    
    return True
