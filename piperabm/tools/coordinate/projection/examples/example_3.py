"""
10*10 grid of points (not equally spaced) having equal latitude and longitude difference on sphere are projected
"""

import numpy as np
import matplotlib.pyplot as plt

from piperabm.tools.coordinate.projection.latlong_xy import latlong_xy


latitude_0 = 70
longitude_0 = -150
DELTA = 5 # degrees
num = 10

# Calculate latitude and longitude values
latitudes_linspace = list(np.linspace(latitude_0 - DELTA/2, latitude_0 + DELTA/2, num))
longitudes_linspace = list(np.linspace(longitude_0 - DELTA/2, longitude_0 + DELTA/2, num))
latitudes_mesh, longitudes_mesh = np.meshgrid(latitudes_linspace, longitudes_linspace)
latitudes = latitudes_mesh.flatten()
longitudes = longitudes_mesh.flatten()

# Calculate x and y values
xs = []
ys = []
for i in range(num ** 2):
    x, y = latlong_xy(latitude_0, longitude_0, latitude=latitudes[i], longitude=longitudes[i])
    xs.append(x)
    ys.append(y)

# Draw
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('latlong_to_xy')

ax1.scatter(longitudes, latitudes)
ax1.set_title('before')
ax1.set_xlabel('longitude (degree)')
ax1.set_ylabel('latitude (degree)')

ax2.scatter(xs, ys)
ax2.set_title('after')
ax2.set_xlabel('x (meters)')
ax2.set_ylabel('y (meters)')

# Display the plots
plt.tight_layout()
plt.show()
