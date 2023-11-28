import numpy as np
import matplotlib.pyplot as plt

from piperabm.tools.coordinate.projection.flatten import Flatten, deg_to_rad, rad_to_deg

latitude_0 = deg_to_rad(0)
#print(latitude_0)
longitude_0 = deg_to_rad(0)
DELTA = deg_to_rad(1)
radius = 6378
projection = Flatten(latitude_0, longitude_0, radius)

locations = [
    [latitude_0, longitude_0],
    [latitude_0, longitude_0 + DELTA],
    [latitude_0 + DELTA, longitude_0 + DELTA],
    [latitude_0 + DELTA, longitude_0],
]

xs = []
ys = []
for location in locations:
    alpha, theta = projection.calcualte_alpha_theta(location[0], location[1])
    #print("alpha: ", rad_to_deg(alpha), "// theta: ", rad_to_deg(theta))
    latitude_prime, longitude_prime = projection.calculate_latitude_longitude_prime(alpha, theta)
    #print("latitude_prime: ", rad_to_deg(latitude_prime), "// longitude_prime: ", rad_to_deg(longitude_prime))
    x, y = projection.mercator_projection(latitude_prime, longitude_prime)
    xs.append(x)
    ys.append(y)
    x, y = projection.convert(location[0], location[1])
plt.scatter(xs, ys)
plt.show()

xs = []
ys = []
for location in locations:
    x = rad_to_deg(location[1])
    y = rad_to_deg(location[0])
    xs.append(x)
    ys.append(y)
    x, y = projection.convert(location[0], location[1])
plt.scatter(xs, ys)
plt.show()
