'''
Created on Jul 10, 2017

@author: JoeRippke
'''
import Sphere_Setup as sph
import Sphere_3d_scatter as scatter

# create a Planet object
# arguments: inner radius, outer radius, number of parameters, number of spokes
TPlanet = sph.Planet(3,15,1,40)

# create a data structure that contains a list for each cell in the sphere
Initial_Planet = TPlanet.sphere_setup()

# create a 3D scatter plot of the sphere
scatter.Planet_Plot(Initial_Planet)

# print the number of cells in the sphere
print(len(Initial_Planet))