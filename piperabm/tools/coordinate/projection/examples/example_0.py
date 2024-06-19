"""
10*10 grid of equally spaced points in xy plane are projected
"""

import numpy as np
import matplotlib.pyplot as plt

from piperabm.tools.coordinate.projection.latlong_xy import xy_latlong


latitude_0 = 0
longitude_0 = 0
DELTA = 1000000 # m
num = 10

# Calculate x and y values
xs_linspace = list(np.linspace(0 - DELTA/2, 0 + DELTA/2, num))
ys_linspace = list(np.linspace(0 - DELTA/2, 0 + DELTA/2, num))
xs_mesh, ys_mesh = np.meshgrid(xs_linspace, ys_linspace)
xs = xs_mesh.flatten()
ys = ys_mesh.flatten()

# Calculate latitude and longitude values
latitudes = []
longitudes = []
for i in range(num ** 2):
    latitude, longitude = xy_latlong(latitude_0, longitude_0, xs[i], ys[i])
    latitudes.append(latitude)
    longitudes.append(longitude)

# Draw
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('xy_to_latlong')

ax1.scatter(xs, ys)
ax1.set_title('before')
ax1.set_xlabel('x (meters)')
ax1.set_ylabel('y (meters)')

ax2.scatter(longitudes, latitudes)
ax2.set_title('after')
ax2.set_xlabel('longitude (degree)')
ax2.set_ylabel('latitude (degree)')

# Display the plots
plt.tight_layout()
plt.show()