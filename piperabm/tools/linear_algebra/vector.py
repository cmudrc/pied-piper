import numpy as np


def vector(point_start, point_end):
    if isinstance(point_start, list):
        point_start = np.array(point_start)
    if isinstance(point_end, list):
        point_end = np.array(point_end)
    return point_end - point_start


if __name__ == '__main__':
    point_start = [1, 1]
    point_end = [4, 5]
    print(vector(point_start, point_end))
