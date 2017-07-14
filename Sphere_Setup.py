'''
Created on Jul 10, 2017

@author: JoeRippke

This module contains a class definition for a planet, which is a sphere that
is composed of cells arranged in spherical coordinates. Also included are some
function definitions including sphere_setup that creates a Planet object data
structure.
'''
import numpy as np


# creat a planet sphere
class Planet():
    def __init__(self,inner_radius=0,outer_radius=0,parameters=1,resolution=0):
        self.__inner_radius=inner_radius
        self.__outer_radius=outer_radius
        self.__parameters=parameters
        self.__mantle_thickness=outer_radius-inner_radius
        self.__resolution=resolution
        
    def getParameters(self):
        return self.__parameters

#display basic information about a sphere
    def Display(self):
        print('Inner Radius:'+str(self.__inner_radius)+'\n'
              'Outer Radius: '+str(self.__outer_radius)+'\n'
              'Parameters: '+str(self.__parameters)+'\n'
              'Mantle Thickness: '+str(self.__mantle_thickness)+'\n'
              'Resolution: '+str(self.__resolution))

#build a list that contains each cell of the sphere
# list indexing:    0: cell number
#                   1: phi  (x,y plane angle in radians, 0-2pi)
#                   2: theta  (z plane angle in radians, -pi/2 - pi/2)
#                   3: r  (radius, distance from origin)
#                   4: layer code where 1=core, 2=mantle, 3=crust
#                   5-end: additional parameters (temperature,density, etc)
    def sphere_setup(self):
        points=[]
        for x in range(self.__resolution):
            for y in range(int(self.__resolution/2)):
                for r in range(self.__outer_radius):
                    values = []
                    phi = 2*np.pi*x/self.__resolution
                    theta = np.pi*y/(self.__resolution/2)-(np.pi/2)
                    values.extend([phi,theta,r])
                    for p in (range(self.__parameters)):
                        values.append(0)
                    if r <= self.__inner_radius:
                        values[3] = 1
                    if r > self.__inner_radius and r < self.__outer_radius:
                        values[3] = 2
                    if r == self.__outer_radius-1:
                        values[3] = 3         
                    points.append(values)
        return points
                
