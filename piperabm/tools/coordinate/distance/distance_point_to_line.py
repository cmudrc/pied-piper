import numpy as np


def distance_point_to_line(
        point: list,
        line_point_1: list,
        line_point_2: list
):
    """
    Calculate perpendicular distance between point and line segment
    """
    point = np.array(point)
    line_point_1 = np.array(line_point_1)
    line_point_2 = np.array(line_point_2)

    ''' Calculate the closest distance between point and line segment '''
    # normalized tangent vector
    delta_vector = line_point_2 - line_point_1
    delta = np.divide(delta_vector, np.linalg.norm(delta_vector))

    # signed parallel distance components
    s = np.dot(line_point_1 - point, delta)
    t = np.dot(point - line_point_2, delta)

    # clamped parallel distance
    h = np.maximum.reduce([s, t, 0])

    # perpendicular distance component
    c = np.cross(point - line_point_1, delta)

    distance_closest = np.hypot(h, np.linalg.norm(c))

    ''' Calculate the prependicular distance between point and line segment '''
    a = line_point_2 - line_point_1
    b = line_point_1 - point

    distance_perpendicular = np.linalg.norm(np.cross(a, b)) / np.linalg.norm(a)

    ''' Check whether perpendicular is inside the line segment or not '''
    if distance_closest == distance_perpendicular:
        result = distance_perpendicular
    else:
        result = None
    
    return result


if __name__ == '__main__':
    point = [0, 2]
    line_point_1 = [0, 0]
    line_point_2 = [2, 0]
    distance = distance_point_to_line(point, line_point_1, line_point_2)
    print(distance)