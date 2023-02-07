"""
dimension of the column space equals the dimension of the row space
"""


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pdb

v1 = np.array([[1], [2], [3]])*5
v2 = np.array([[2], [5], [1]])*5
v3 = 0.5*v1+0.3*v2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot([0, v1[0]], [0, v1[1]], [0, v1[2]], color='red')
ax.plot([0, v2[0]], [0, v2[1]], [0, v2[2]], color='red')
ax.plot([0, v3[0]], [0, v3[1]], [0, v3[2]], color='red')


ax.plot([0, v1[0]], [0, v2[0]], [0, v3[0]], color='blue')
ax.plot([0, v1[1]], [0, v2[1]], [0, v3[1]], color='blue')
ax.plot([0, v1[2]], [0, v2[2]], [0, v3[2]], color='blue')


plt.show()
fig.savefig('fig.png')