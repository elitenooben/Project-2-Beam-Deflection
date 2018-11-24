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
    
    #Negative beam deflection
    y_a = -beamSuperposition(a,l,a,W,beamSupport)
    
    plt.plot(x_plot, y_plot, color = "b", label = "Beam", alpha =0.3)
    plt.scatter(a, y_a, color = "r", s = 100, label = "Load Pos.")
    plt.scatter(x_plot[np.where(abs(y_plot) == max(abs(y_plot)))], max(y_plot, key = abs), color = "g", s = 100, label = "Defl_max")
    
    plt.title("Beam Deflection\nBeamType: %s" %beamSupport.capitalize())
    plt.xlabel("Horizontal Length in [m]")
    plt.ylabel("Deflection from y_0 in [m]")
    for i in range(len(y_a)):
        if beamSupport.capitalize() == "Both":
            if a[i] < (beamLength/2)+1:
                plt.text(a[i]-(1.5/14)*beamLength,y_a[i]+(0.5/14)*max(y_plot,key=abs), str(W[i]) + " N")
            else:
                plt.text(a[i]+(0.5/14)*beamLength,y_a[i]-(0.5/14)*max(y_plot,key=abs), str(W[i]) + " N")
        else:
            plt.text(a[i]+(0.5/14)*beamLength,y_a[i]-(0.5/14)*max(y_plot,key=abs), str(W[i]) + " N")
    plt.text(x_plot[np.where(y_plot == max(y_plot, key = abs))]+(0.4/14)*beamLength,max(y_plot, key = abs), "%.2E m" % Decimal(str(max(y_plot, key = abs))))    
    style.use("ggplot")
    plt.legend()
    
    plt.show()
    return

l = 20
a = np.array([10,17,5,11])
W = np.array([-2,2000,13,500])
beamSupport = "cantilever"

print(beamPlot(l,a, W, beamSupport))
