"""
script plots 
basis vectors of matrix A, 
null space of A transpose,
range of A
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pdb


# ---------------------------- basis vectors -------------------------------
v1 = np.array([[1], [2], [3]])*5
v2 = np.array([[2], [5], [1]])*5

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot([0, v1[0]], [0, v1[1]], [0, v1[2]], color='red')
ax.plot([0, v2[0]], [0, v2[1]], [0, v2[2]], color='blue')

# A [3, 2]
A = np.concatenate((v1, v2), axis=1)

                                                                            
# ------------------------------- range(A) ---------------------------------
pts = np.arange(0, 10, 1)/10
xx, yy = np.meshgrid(pts, pts)
xx, yy = xx.reshape(-1), yy.reshape(-1)

x = v1[0]*xx + v2[0]*yy
y = v1[1]*xx + v2[1]*yy
z = v1[2]*xx + v2[2]*yy

ax.scatter(x, y, z, color='green')

                                                                            
# ---------------------------- null(A.transpose) --------------------------- 
Atilde = A.T[:, :2]
C = A.T[:, 2:]

x3 = np.arange(0, 10, 1)/10
null = np.zeros((3, len(x3)))
for i in range(len(x3)):
    # pdb.set_trace()
    null[:2, i:i+1] = np.linalg.solve(Atilde, -C*x3[i])
    null[2, i:i+1] = x3[i]

ax.scatter(null[0], null[1], null[2], color='orange')
ax.set_aspect('auto')

# plt.show()
fig.savefig('nullandrange.png')
