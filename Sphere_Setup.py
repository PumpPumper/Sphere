'''
Created on Jul 10, 2017

@author: JoeRippke

Sphere setup

This module outputs a sphere composed of an inner sphere and an outer sphere. The purpose of
the sphere is to model convection cells in the outer sphere. Temperature boundary conditions
will be defined for the small inner sphere and the outer shell of the large sphere.
'''
import numpy as np



class Planet():
    def __init__(self,inner_radius=0,outer_radius=0,parameters=1,resolution=0):
        self.__inner_radius=inner_radius
        self.__outer_radius=outer_radius
        self.__parameters=parameters
        self.__mantle_thickness=outer_radius-inner_radius
        self.__resolution=resolution
        
    def getParameters(self):
        return self.__parameters

    def Display(self):
        print('Inner Radius:'+str(self.__inner_radius)+'\n'
              'Outer Radius: '+str(self.__outer_radius)+'\n'
              'Parameters: '+str(self.__parameters)+'\n'
              'Mantle Thickness: '+str(self.__mantle_thickness)+'\n'
              'Resolution: '+str(self.__resolution))
        
    def sphere_setup(self):
        points=[]
        for x in range(self.__resolution):
            for y in range(int(self.__resolution/2)):
                for r in range(self.__outer_radius):
                    values = []
                    phi = 2*np.pi*x/self.__resolution
                    theta = np.pi*y/(self.__resolution/2)-(np.pi/2)
                    values.extend([phi,theta,r])
                    params=np.zeros(self.__parameters)
                    for p in (range(self.__parameters)):
                        values.append(params[p])
                    if r <= self.__inner_radius:
                        values[3] = 1
                    if r > self.__inner_radius and r < self.__outer_radius:
                        values[3] = 2
                    if r == self.__outer_radius-1:
                        values[3] = 3         
                    points.append(values)
        return points
                
