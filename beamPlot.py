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

def beamPlot(beamLength, loadPositions, loadForces, beamSupport):
    x_plot = np.arange(beamLength*1.001, step = beamLength/100)
    y_plot = -beamSuperposition(x_plot, beamLength, loadPositions, loadForces, beamSupport)
    beamSupport = beamSupport.capitalize()
    
    #Negative beam deflection
    y_a = -beamSuperposition(a,l,a,W,beamSupport)
    
    plt.plot(x_plot, y_plot, color = "b", label = "Beam", alpha =0.3)
    plt.scatter(a, y_a, color = "r", s = 100, label = "Load Pos.")
    plt.scatter(x_plot[np.where(abs(y_plot) == max(abs(y_plot)))], max(y_plot, key = abs), color = "g", s = 100, label = "Defl_max")
    
    plt.title("Beam Deflection\nBeamType: %s" %beamSupport)
    plt.xlabel("Horizontal Length in [m]")
    plt.ylabel("Deflection from y_0 in [m]")
    for i in range(len(y_a)):
        plt.text(a[i]+(0.5/14)*beamLength,y_a[i]-(0.5/14)*max(y_plot,key=abs), str(W[i]) + " N")
    plt.text(x_plot[np.where(y_plot == max(y_plot, key = abs))]+(0.4/14)*beamLength,max(y_plot, key = abs)*1.04, "%.2E m" % Decimal(str(max(y_plot, key = abs))))  
    style.use("ggplot")
    plt.legend()
    
    plt.show()
    return 


l = 20
a = np.array([10,3,17,6])
W = np.array([200,150,240,560])
beamSupport = "both"

print(beamPlot(l,a, W, beamSupport))
