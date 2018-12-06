#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:04:20 2018

@author: Carl and Sarah
"""
from beamPlot import beamPlot
from loadFile import loadFile
from saveToFile import saveToFile
import numpy as np
from beamUtils import isFloat, validLoads, checkLoads, printLoads

def getBeam():
    """This function gets a valid beam from the user."""
    
    length = None
    
    while True:
        length = input("Enter the length of beam in meters: ")
        if not isFloat(length) or float(length) <= 0:
            print("You have entered an invalid input.\nPlease enter beam length as a positive scalar.")
        else:
            break
    
    support = {"1": "Both", "2": "Cantilever"}
    print("""
Support types:
1. Both
2. Cantilever
        """)
    stype = None
    while True:
        stype = input("Choose a support type: ")
        if stype != "1" and stype != "2":
            print("Invalid input. Enter the number 1 or 2")
        else:
            break

    return (float(length), support[stype])

def askSave(beamLength, beamSupport, loadPositions, loadForces):
    """
    Asks whether the user wants to save, if there is anything to save.
    """
    if(len(loadPositions) == 0):
        return
    
    yn = None
    yn = input("Do you want to save first? [y/n] ").lower()
    if(yn == "y"):
        saveToFile(beamLength, beamSupport, loadPositions, loadForces)
    else:
        print("Ok, not saving.")


def loadMenu(beamLength, beamSupport, loadPositions, loadForces):
    """
    The menu for doing stuff with loads.
    Returns a tuple of new loadPositions and loadForces if the user picks a valid menu point.
    Otherwise, returns None.
    """
    print("""
 Loads menu
1. See current loads
2. Add a load
3. Remove a load
4. Remove all loads
5. Exit""")
    choice = input("Choose a menu point: ")
    
    if choice =="1":
        printLoads(loadPositions, loadForces);
        input("Press enter to continue ")
        
    elif choice =="2":
        #Get valid position and force from the user.
        position = None
        force = None
        
        while True:
            position = input("Enter a position in meters: ")
            if isFloat(position) and float(position) >= 0 and float(position) <= beamLength:
                break;
            print("Invalid position of load.\nEnter a number in meters smaller than the beam length.")

        while True:
            force = input("Enter size of the force at the given position in [N]: ")
            if isFloat(force) and float(force) > 0:
                break;
            print("Invalid size of force.\nEnter a number larger than zero")
        
        #Add positions and forces to their respective arrays.
        loadPositions = np.append(loadPositions,float(position))
        loadForces = np.append(loadForces,float(force))
        print("A force of magnitude %s N positioned at %s m has been added." %(force, position))
        input("Press enter to continue ")
    
    elif choice == "3":
        #Give the user a menu of all current loads, and get a valid load index to remove.
        if(printLoads(loadPositions, loadForces)):
            toRemove = ""
            while True:
                toRemove = input("Which index do you want to remove: ")
                
                #Allow user to quit if they don't want to remove anything.
                if toRemove.lower() == "q":
                    break
                elif(not toRemove.isdecimal() or int(toRemove) < 1 or int(toRemove) > len(loadPositions)):
                    print("You have to choose a valid load index, or write Q to quit")
                else:
                    break

            #If the user doesn't quit, remove load at given index.
            if toRemove.lower() != "q":
                toRemove = int(toRemove)-1
                removePosition = loadPositions[toRemove]
                removeForce = loadForces[toRemove]
                loadPositions = np.delete(loadPositions, toRemove) 
                loadForces = np.delete(loadForces, toRemove)
                print("Removed " + str(removeForce) + "N at " + str(removePosition) + "m")
                input("Press enter to continue ")
    
    elif choice == "4":
        #Remove all loads if any exist. First, ask the user if they want to save.
        if(len(loadPositions) == 0):
            print("No loads to remove")
            return (loadPositions, loadForces)
        askSave(beamLength, beamSupport, loadPositions, loadForces)
        
        loadPositions = np.array([])
        loadForces = np.array([])
        print("Removed all loads.")
        
    elif choice == "5":
        print("Quitting submenu.")
    else:
        print("Enter a valid menu point!")
        return None
    return (loadPositions, loadForces)
                
def mainscript():
    """
    The main point of user interaction.
    """
    #Initialization
    beamLength = 10.
    beamSupport = "Both"
    
    loadPositions = np.array([])
    loadForces = np.array([])
    while True:
        print("""
 Main Menu
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
        
        if userinput == "1":
            #Get a valid beam from the user
            temp = getBeam()
            
            #Remove invalid loads, and allow saving current state
            if not checkLoads(temp[0], loadPositions):
                print("Your loads are not all valid for the new beam.")
                print("All invalid loads will be removed")
                askSave(beamLength, beamSupport, loadPositions, loadForces)
                
                loadTuple = validLoads(temp[0], loadPositions, loadForces)
                loadPositions = loadTuple[0]
                loadForces = loadTuple[1]
            
            #Finally change beam
            beamLength = temp[0]
            beamSupport = temp[1]
            print("Changed beam length to %s m, support type to %s" %(beamLength, beamSupport))
            input("Press enter to continue ");
            
            
        elif userinput == "2":
            #Go through loads menu until the user does a valid menu point.
            loadTuple = None
            while(loadTuple == None):
                loadTuple = loadMenu(beamLength, beamSupport, loadPositions, loadForces)
            loadPositions = loadTuple[0]
            loadForces = loadTuple[1]
            
        elif userinput == "3":
            saveToFile(beamLength, beamSupport, loadPositions, loadForces)
            input("Press enter to continue ")
            
        elif userinput == "4":
            askSave(beamLength, beamSupport, loadPositions, loadForces)
            
            #Load a beam, and check if it is a valid file
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
            
            if len(loadPositions) == 0:
                print("Could not generate plot as there are no loads currently!")
                continue
            
            #Ask whether the user wants constrained scaling
            constrainedScaling = input("Do you want the x- and y-axes to have constrained scaling? [y/n] ") == "y"
            
            beamPlot(beamLength, loadPositions, loadForces, beamSupport, constrainedScaling)
            input("Press enter to continue ")
            
        elif userinput == "6":
            askSave(beamLength, beamSupport, loadPositions, loadForces)
            
            print("Quitting")
            break
        else:
            print("Invalid input. Enter a menu point, number from 1 to 6")
    return
mainscript()
        
        
