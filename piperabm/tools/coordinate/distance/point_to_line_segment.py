import numpy as np


def point_to_line_segment(
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

    # Normalized tangent vector
    delta_vector = line_point_2 - line_point_1
    delta = np.divide(delta_vector, np.linalg.norm(delta_vector))

    # Signed parallel distance components
    s = np.dot(line_point_1 - point, delta)
    t = np.dot(point - line_point_2, delta)

    # Clamped parallel distance
    h = np.maximum.reduce([s, t, 0])

    # Perpendicular distance component
    c = np.cross(point - line_point_1, delta)

    return np.hypot(h, np.linalg.norm(c))


if __name__ == "__main__":
    point = [-3, 4]
    line_point_1 = [0, 0]
    line_point_2 = [2, 0]
    distance = point_to_line_segment(point, line_point_1, line_point_2)
    print(distance)