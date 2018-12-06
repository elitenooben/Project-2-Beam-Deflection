# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:26:54 2018

@author: William
"""

import numpy as np

def beamDeflection(positions, beamLength, loadPosition, loadForce, beamSupport):
    """
    Calculates and returns an array of deflection caused by the given load at the given positions.
    """
    x = positions
    l = beamLength
    a = loadPosition
    W = loadForce
    
    # c = 6*E*I
    c = 6 * 200*10**9 * 0.001
    y = np.zeros(len(x))
    
    #Calculate the deflection array in two halves, for x<a and x>=a.
    if beamSupport == "Both":
        y[x < a] = (W*(l-a)*x*(l**2-x**2-(l-a)**2)/(c*l))[x < a]
        y[x >= a] = (W*a*(l-x)*(l**2-(l-x)**2-a**2)/(c*l))[x >= a]
    elif beamSupport == "Cantilever":
        y[x < a] = (W*x**2*(3*a-x)/c)[x < a]
        y[x >= a] = (W*a**2*(3*x-a)/c)[x >= a]
    deflection = y
    return deflection


def beamSuperposition(positions, beamLength, loadPositions, loadForces, beamSupport):
    """ Calculates deflection when multiple loads are given 
    by the use of the superposition principle.
    Returns a zero vector if no loads are given."""
    
    deflection = np.zeros(len(positions))
    
    for loadF, loadP in zip(loadForces, loadPositions):
        #The beamDeflection function is used for calculations
        deflection += beamDeflection(positions, beamLength, loadP, loadF, beamSupport)
    
    return deflection