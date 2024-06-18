import numpy as np

from piperabm.tools.vector import vector as vc


def point_to_line(
        point,
        line_point_1,
        line_point_2,
        vector: bool = False,
        ndarray: bool = False
    ):
    """
    Finds the vector connecting a point to a line that has the smallest distance.
    
    :param point: The point (np.ndarray).
    :param line_point_1: First point on the line (np.ndarray).
    :param line_point_2: Second point on the line (np.ndarray).
    :return: The vector from the point to the closest point on the line.
    """
    result = None

    point = np.array(point)
    line_point_1 = np.array(line_point_1)
    line_point_2 = np.array(line_point_2)

    # Line vector
    line_vec = line_point_2 - line_point_1

    # Vector from line_point_1 to the point
    point_vec = point - line_point_1

    # Project point_vec onto line_vec
    projection = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec) * line_vec

    # The perpendicular vector from the point to the line
    result = projection - point_vec

    if vector is True:
        if ndarray is True:
            pass
        else:
            result = list(result)
    else:
        result = vc.magnitude(result)

    return result


if __name__ == '__main__':
    point = [3, 4]
    line_point_1 = [0, 0]
    line_point_2 = [2, 0]
    vector = point_to_line(point, line_point_1, line_point_2)
    print(vector)