"""
This example generates 1000 points inside a single triangle
"""

import matplotlib.pyplot as plt

from piperabm.tools.mesh import Triangle


pos_1 = [0, 0]
pos_2 = [2, 0]
pos_3 = [0, 1]
triangle = Triangle(pos_1, pos_2, pos_3)

xs = []
ys = []
for _ in range(1000):
    point = triangle.random_point()
    xs.append(point[0])
    ys.append(point[1])

plt.scatter(xs, ys)  # Plot points
plt.show()
