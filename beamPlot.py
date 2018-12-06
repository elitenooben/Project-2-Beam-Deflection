# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 12:12:18 2018

@author: William
"""

import numpy as np
import matplotlib.pyplot as plt
from beamDeflection import beamSuperposition
from matplotlib import style
from decimal import Decimal

def beamPlot(beamLength, loadPositions, loadForces, beamSupport, constrainedScaling):
    """
    Plots the deflection of the given beam with the given loads. Uses beamSuperposition to calculate deflection.
    constrainedScaling is whether the axes are scaling constrained
    """
    x_plot = np.arange(beamLength*1.001, step = beamLength/100)
    y_plot = beamSuperposition(x_plot, beamLength, loadPositions, loadForces, beamSupport)
    
    if(y_plot[0]==y_plot[1]):
        print("All loads are on support points. No deflection.")
        return
    
    l = beamLength
    a = loadPositions
    W = loadForces
    
    #Invert y axis
    plt.gca().invert_yaxis()
    
    #Write title and axis labels
    plt.title("Beam Deflection\nBeamType: %s" %beamSupport)
    plt.xlabel("Horizontal Length [m]")
    plt.ylabel("Deflection [m]")
    
    #Allow constrained scaling
    if(constrainedScaling):
        plt.axis("equal")
    
    #Plot deflection curve
    plt.plot(x_plot, y_plot, color = "b", label = "Beam", alpha =0.3)
    
    #Get beam deflection at load points.
    y_a = beamSuperposition(a,l,a,W,beamSupport)
    #Plot beam loads and maximum deflection on the deflection curve
    plt.scatter(a, y_a, color = "r", s = 100, label = "Load Pos.")
    plt.scatter(x_plot[np.where(abs(y_plot) == max(abs(y_plot)))], max(y_plot, key = abs), color = "g", s = 100, label = "Defl_max")
    
    #Make some gui constants so we can find out text offsets whether the axes are constrained or not
    ymax = beamLength/2 if constrainedScaling else max(y_plot,key=abs)
    xoffset = (0.5/14)*beamLength
    yoffset = (0.5/14)*ymax
    
    #Write loads and maximum deflection on the deflection curve, and add legend. 0.5/14 and 0.4/14 is just a constant to offset text by.
    for i in range(len(y_a)):
        plt.text(a[i]+xoffset, y_a[i]-yoffset, str(W[i]) + " N")
    plt.text(x_plot[np.where(y_plot == max(y_plot, key = abs))]+xoffset,max(y_plot,key=abs)+2*yoffset, "%.2E m" % Decimal(str(max(y_plot, key = abs))))  
    style.use("ggplot")
    plt.legend()
    
    plt.show()
    
    print("Scaling " + ("constrained" if constrainedScaling else "unconstrained"))
    return 

