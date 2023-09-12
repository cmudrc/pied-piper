'''
Source: Computer Graphics by F.S. Hill
'''

import numpy as np

from piperabm.tools.coordinate.distance import distance_point_to_point


def intersect_line_line(
        line_1_point_1: list,
        line_1_point_2: list,
        line_2_point_1: list,
        line_2_point_2: list
):
    """
    Calculate intersecting point between two line segments
    """

    def perp(a):
        b = np.empty_like(a)
        b[0] = -a[1]
        b[1] = a[0]
        return b
    
    intersection = None

    line_1_point_1 = np.array(line_1_point_1)
    line_1_point_2 = np.array(line_1_point_2)
    line_2_point_1 = np.array(line_2_point_1)
    line_2_point_2 = np.array(line_2_point_2)

    delta_line_1 = line_1_point_2 - line_1_point_1
    delta_line_2 = line_2_point_2 - line_2_point_1
    delta_p = line_1_point_1 - line_2_point_1
    delta_line_1_perp = perp(delta_line_1)

    denominator = np.dot(delta_line_1_perp, delta_line_2)
    numerator = np.dot(delta_line_1_perp, delta_p)

    if denominator != 0: # check for parallel lines
        intersection = (numerator / denominator.astype(float)) * delta_line_2 + line_2_point_1
    
    if intersection is not None: # check whether intersection is within the segments
        distance_1 = distance_point_to_point(line_1_point_1, intersection)
        distance_2 = distance_point_to_point(line_1_point_2, intersection)
        total_distance = distance_point_to_point(line_1_point_1, line_1_point_2)
        if distance_1 + distance_2 != total_distance:
            intersection = None
    return intersection


if __name__ == '__main__':
    line_1_point_1 = [1, 0]
    line_1_point_2 = [1, 2]
    line_2_point_1 = [0, 1]
    line_2_point_2 = [2, 1]
    point = intersect_line_line(line_1_point_1, line_1_point_2, line_2_point_1, line_2_point_2)
    print(point)