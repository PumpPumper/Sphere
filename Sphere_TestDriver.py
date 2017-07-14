'''
Created on Jul 10, 2017

@author: JoeRippke
'''
import Sphere_Setup as sph
import Sphere_3d_scatter as scatter

TPlanet = sph.Planet(3,15,1,40)

Initial_Planet = TPlanet.sphere_setup()

scatter.Planet_Plot(Initial_Planet)

print(TPlanet.Display())
print(len(Initial_Planet))