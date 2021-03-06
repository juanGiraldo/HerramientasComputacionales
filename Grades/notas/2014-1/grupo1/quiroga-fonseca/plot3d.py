# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

filename = sys.argv[1]
data = numpy.loadtxt(filename).T

x = data[0]
y = data[1]
z = data[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
        
ax.scatter(x,y,z, c='r', marker = 'o')
        
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
fig.suptitle('Marcha Aleatoria')
fig.savefig('3dplot.png')

plt.show()

# <codecell>


