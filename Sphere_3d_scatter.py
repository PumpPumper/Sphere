#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 11:47:35 2017

@author: JoeRippke
"""
import numpy as np
import pylab as p
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

# This function creates a 3D scatter plot of the sphere

def Planet_Plot(Planet):
    
    # set the window size w,h in inches
    fig = plt.figure(figsize=(12,10))
    
    # dot size
    ds = 7
    
    # upper left figure
    ax = fig.add_subplot(2, 2, 1, projection='3d')
    for n in range(len(Planet)):
        if Planet[n][0] >= np.pi and Planet[n][1] >= 0:
            x = Planet[n][2]*np.sin(Planet[n][1])*np.cos(Planet[n][0])
            y = Planet[n][2]*np.sin(Planet[n][1])*np.sin(Planet[n][0])
            z = Planet[n][2]*np.cos(Planet[n][1])
            if Planet[n][3] == 1:
                ax.scatter3D(x,y,z,c='yellow',s=ds)
            if Planet[n][3] == 2:
                ax.scatter3D(x,y,z,c='red',s=ds)
            if Planet[n][3] == 3:
                ax.scatter3D(x,y,z,c='black',s=ds)
        ax.view_init(-25,70)
        ax.axis('equal')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
    #upper right figure
    ax = fig.add_subplot(2, 2, 2, projection='3d')
    for n in range(len(Planet)):
        if Planet[n][0] <= np.pi and Planet[n][1] >= 0:
            x = Planet[n][2]*np.sin(Planet[n][1])*np.cos(Planet[n][0])
            y = Planet[n][2]*np.sin(Planet[n][1])*np.sin(Planet[n][0])
            z = Planet[n][2]*np.cos(Planet[n][1])
            if Planet[n][3] == 1:
                ax.scatter3D(x,y,z,c='yellow',s=ds)
            if Planet[n][3] == 2:
                ax.scatter3D(x,y,z,c='red',s=ds)
            if Planet[n][3] == 3:
                ax.scatter3D(x,y,z,c='black',s=ds)
        ax.view_init(-25,-70)
        ax.axis('equal')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
    #lower left figure
    ax = fig.add_subplot(2, 2, 3, projection='3d')
    for n in range(len(Planet)):
        if Planet[n][0] <= np.pi and Planet[n][1] <= 0:
            x = Planet[n][2]*np.sin(Planet[n][1])*np.cos(Planet[n][0])
            y = Planet[n][2]*np.sin(Planet[n][1])*np.sin(Planet[n][0])
            z = -Planet[n][2]*np.cos(Planet[n][1])
            if Planet[n][3] == 1:
                ax.scatter3D(x,y,z,c='yellow',s=ds)
            if Planet[n][3] == 2:
                ax.scatter3D(x,y,z,c='red',s=ds)
            if Planet[n][3] == 3:
                ax.scatter3D(x,y,z,c='black',s=ds)
        ax.view_init(20,70)
        ax.axis('equal')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
    
    #lower right figure
    ax = fig.add_subplot(2, 2, 4, projection='3d')
    for n in range(len(Planet)):
        if Planet[n][0] >= np.pi and Planet[n][1] <= 0:
            x = Planet[n][2]*np.sin(Planet[n][1])*np.cos(Planet[n][0])
            y = Planet[n][2]*np.sin(Planet[n][1])*np.sin(Planet[n][0])
            z = -Planet[n][2]*np.cos(Planet[n][1])
            if Planet[n][3] == 1:
                ax.scatter3D(x,y,z,c='yellow',s=ds)
            if Planet[n][3] == 2:
                ax.scatter3D(x,y,z,c='red',s=ds)
            if Planet[n][3] == 3:
                ax.scatter3D(x,y,z,c='black',s=ds)
        ax.view_init(20,-70)
        ax.axis('equal')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
   
    
    plt.tight_layout()
    p.show()