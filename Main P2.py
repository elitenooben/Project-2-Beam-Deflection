#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:04:20 2018

@author: SarahMagid
"""
from beamPlot import beamPlot
from loadFile import loadFile
from saveToFile import saveToFile
import numpy as np
from beamUtils import isFloat, validLoads, checkLoads, printLoads

def configureBeam():
    """This function gets beam configurations from user and checks validity"""
    
    length = input("Enter the length of beam in meters: ")
    if not isFloat(length):
        print("You have entered an invalid input. Please enter beam length as a scalar.")
        return None
    
    support = {"1": "Both", "2": "Cantilever"}
    print("""
Support types:
1. Both
2. Cantilever
        """)
    stype = input("Choose a support type: ")
    if stype != "1" and stype != "2":
        print("Invalid input. Enter the number 1 or 2")
        return None

    return (float(length), support[stype])

def askSave(beamLength, beamSupport, loadPositions, loadForces):
    """
    Asks whether the user wants to save.
    """
    
    yn = input("Do you want to save first? [y/n] ").lower()
    if(yn == "y"):
        saveToFile(beamLength, beamSupport, loadPositions, loadForces)
    
def mainscript():
    #Initialization
    beamLength = 10.
    beamSupport = "Both"
    
    loadPositions = np.array([])
    loadForces = np.array([])

    while True:
        print(""" Main Menu
1. Configure beam
2. Configure loads
3. Save beam and loads
4. Load beam and loads
5. Generate plots
6. Quit 
              """)
        print("The current beam is %s m, support type %s" %(beamLength, beamSupport))
        if(len(loadPositions) == 0):
            print("No current loads!")
        userinput = input("Choose a menu point by entering a number: ")
        
        #Get a beam from the user, and only change anything if it is a valid beam
        if userinput == "1":
            temp = configureBeam()
            
            if(temp != None):
                #Remove invalid loads, and allow saving current state
                if not checkLoads(temp[0], loadPositions):
                    print("Your loads are not all valid for the new beam.")
                    print("All invalid loads will be removed")
                    askSave(beamLength, beamSupport, loadPositions, loadForces)
                    
                    loadTuple = validLoads(temp[0], loadPositions, loadForces)
                    loadPositions = loadTuple[0]
                    loadForces = loadTuple[1]
                
                beamLength = temp[0]
                beamSupport = temp[1]
                print("Changed beam to %s m, support type %s" %(beamLength, beamSupport))
                input("Press enter to continue ");
            
            
        elif userinput == "2":
            print("""
loads menu
1. See current loads
2. Add a load
3. Remove a load
4. Remove all loads""")
            choice = input("Choose a menu point: ")
            
            if choice =="1":
                printLoads(loadPositions, loadForces);
                input("Press enter to continue ")
                
            elif choice =="2":
                position = None
                force = None
                
                while True:
                    position = input("Enter a position in meters: ")
                    if isFloat(position) and float(position) > 0 and float(position) < beamLength:
                        break;
                    print("Invalid position of load. Enter a number in meters smaller than the beamlength")

                while True:
                    force = input("Enter size of the force at the given position in [N]: ")
                    if isFloat(force) and float(force) > 0:
                        break;
                    print("Invalid size of force. Enter a number larger than zero")
                
                loadPositions = np.append(loadPositions,float(position))
                loadForces = np.append(loadForces,float(force))
                print("A force of magnitude %s N positioned at %s m has been added." %(force, position))
                input("Press enter to continue ")
            
            elif choice == "3":
                if(printLoads(loadPositions, loadForces)):
                    toRemove = ""
                    while not toRemove.isdecimal() or int(toRemove) < 1 or int(toRemove) > len(loadPositions):
                        toRemove = input("Which index do you want to remove: ")
                        print("You have to choose a valid load index, or write Q to quit")
                        if toRemove.lower() == "q":
                            break;
                    else:
                        toRemove = int(toRemove)-1
                        removePosition = loadPositions[toRemove]
                        removeForce = loadForces[toRemove]
                        loadPositions = np.delete(loadPositions, toRemove) 
                        loadForces = np.delete(loadForces, toRemove)
                        print("Removed " + str(removeForce) + "N at " + str(removePosition) + "m")
                        input("Press enter to continue ")
                    
            elif choice == "4":
                if(len(loadPositions) == 0):
                    print("No loads to remove")
                    continue
                askSave(beamLength, beamSupport, loadPositions, loadForces)
                loadPositions = np.array([])
                loadForces = np.array([])
                print("Removed all loads.")
                
        elif userinput == "3":
            saveToFile(beamLength, beamSupport, loadPositions, loadForces)
            input("Press enter to continue ")
            
        elif userinput == "4":
            askSave(beamLength, beamSupport, loadPositions, loadForces)
            
            #Load a beam, and check if it is valid
            temp = loadFile()
            if temp != None:
                beamLength = temp[0]
                beamSupport = temp[1]
                loadPositions = temp[2]
                loadForces = temp[3]
                
                print("Loaded:")
                print("a beam of length %s m with support type %s" %(beamLength, beamSupport))
                printLoads(loadPositions, loadForces)
            
            input("Press enter to continue ")
        elif userinput == "5":
            beamPlot(beamLength, loadPositions, loadForces, beamSupport)
            input("Press enter to continue ")
            
        elif userinput == "6":
            askSave(beamLength, beamSupport, loadPositions, loadForces)
            
            print("Quitting")
            break
        else:
            print("Invalid input. Enter a menupoint number from 1 to 6")
    return
mainscript()
        
        
