"""
This example generates 1000 points inside a two adjacent triangles
"""

import matplotlib.pyplot as plt

from piperabm.tools.mesh import Triangle, Patch


pos_1 = [0, 0]
pos_2 = [0, 2]
pos_3 = [2, 0]
pos_4 = [1, 1]
pos_5 = [2, 1]
triangle_1 = Triangle(pos_1, pos_2, pos_3)
triangle_2 = Triangle(pos_3, pos_4, pos_5)

patch = Patch()
patch.add(triangle_1, triangle_2)

xs = []
ys = []
for _ in range(1000):
    point = patch.random_point()
    xs.append(point[0])
    ys.append(point[1])

plt.scatter(xs, ys)  # Plot points
plt.show()
