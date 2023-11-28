import numpy as np
import matplotlib.pyplot as plt

from piperabm.tools.coordinate.projection.flatten import Flatten, deg_to_rad

latitude_0 = deg_to_rad(70)
longitude_0 = deg_to_rad(150)
DELTA = deg_to_rad(1)
radius = 6378
projection = Flatten(latitude_0, longitude_0, radius)


num = 10
latitudes = list(np.linspace(latitude_0, latitude_0 + DELTA, num))
longitudes = list(np.linspace(longitude_0, longitude_0 + DELTA, num))

locations = []
for latitude in latitudes:
    for longitude in longitudes:
        locations.append([latitude, longitude])

xs = []
ys = []
for location in locations:
    x, y = projection.convert(location[0], location[1])
    xs.append(x)
    ys.append(y)

plt.scatter(xs, ys)
plt.show()

xs = []
ys = []
for latitude in latitudes:
    for longitude in longitudes:
        x, y = longitude, latitude
        xs.append(x)
        ys.append(y)
plt.scatter(xs, ys)
plt.show()
