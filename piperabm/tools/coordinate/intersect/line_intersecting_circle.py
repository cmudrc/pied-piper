'''
# point_1 = [x_1, y_1]
# point_2 = [x_2, y_2]
# circle_center = [x_c, y_c]

# line formula from point_1 to point_2:
y = (m * x) + b
m = (y_2 - y_1) / (x_2 - x_1)
b = y_2 - m * x_2

# circle center to intercept formula:
y = m_c * x + b_c
m_c = -1 / m
b_c = y_c + (x_c / m)

# intercept: [x_p, y_p]
'''

import numpy as np

from piperabm.tools.coordinate import euclidean_distance


def line_intersecting_circle(
        point_1: list,
        point_2: list,
        circle_center: list,
        circle_radius: float
    ):
    """ Check whether the line intersecs the circle """
    x_1 = point_1[0]
    y_1 = point_1[1]
    x_2 = point_2[0]
    y_2 = point_2[1]
    m = (y_2 - y_1) / (x_2 - x_1)
    b = y_2 - (m * x_2)

    x_c = circle_center[0]
    y_c = circle_center[1]
    b_c = y_c + (x_c / m)

    
    #x_p = ((x_c / m) + y_c + (m * x_2) - y_2) / (m + 1/m)
    #y_p = m * (x_p - x_2) + y_2

    #distance = np.sqrt(np.square(x_c - x_p) + np.square(y_c - y_p))
    
    result = None
    #if distance >= circle_radius:
    #    result = False
    #else:
    #    result = True

    return result


if __name__ == '__main__':
    point_1 = [0, 0]
    point_2 = [2, 2]
    circle_center = [1.4, 0.6]
    #circle_radius = 0.6
    circle_radius = 0.5
    result = line_intersecting_circle(point_1, point_2, circle_center, circle_radius)
    print(result)
