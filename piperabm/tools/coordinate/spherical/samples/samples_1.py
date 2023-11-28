import numpy as np
import matplotlib.pyplot as plt

from piperabm.tools.coordinate.spherical import FlattenSphere

phi_0 = 70
l_0 = 150
radius = 6378
fs = FlattenSphere(phi_0, l_0, radius)
num = 10
ls = np.linspace(phi_0, phi_0 + 0.05, num)
phis = np.linspace(l_0, l_0 + 0.05, num)

xs = []
ys = []
for i in range(num):
    l = ls[i]
    for j in range(num):
        phi = phis[j]
        x, y = fs.convert(phi, l)
        xs.append(x)
        ys.append(y)

print(phis[0], ls[0])
print(xs[0], ys[0])

plt.scatter(xs, ys)
plt.show()

xs = []
ys = []
for i in range(num):
    l = ls[i]
    for j in range(num):
        phi = phis[j]
        x, y = l, phi
        xs.append(x)
        ys.append(y)
plt.scatter(xs, ys)
plt.show()
