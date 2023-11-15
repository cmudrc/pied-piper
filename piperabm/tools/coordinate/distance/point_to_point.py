import numpy as np


def point_to_point(
    point_1,
    point_2
):
    """
    Calculate the Euclidean distance between two points
    """
    if isinstance(point_1, list):
        point_1 = np.array(point_1)
    if isinstance(point_2, list):
        point_2 = np.array(point_2)
    return np.sqrt(np.sum(np.square(point_2 - point_1)))


if __name__ == "__main__":
    point_1 = [0, 3]
    point_2 = [4, 0]
    distance = point_to_point(point_1, point_2)
    print(distance)
