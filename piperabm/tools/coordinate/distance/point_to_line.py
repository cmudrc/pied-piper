import numpy as np


def point_to_line(
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

    # Calculate the prependicular distance between point and line segment
    a = line_point_2 - line_point_1
    b = line_point_1 - point

    return np.linalg.norm(np.cross(a, b)) / np.linalg.norm(a)


if __name__ == "__main__":
    point = [-3, 4]
    line_point_1 = [0, 0]
    line_point_2 = [2, 0]
    distance = point_to_line(point, line_point_1, line_point_2)
    print(distance)
