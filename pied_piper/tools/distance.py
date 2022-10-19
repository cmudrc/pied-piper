import numpy as np


def euclidean_distance(start_x, start_y, end_x, end_y):
    if start_x is not None and start_y is not None \
        and end_x is not None and end_y is not None:
        val_1 = np.power(end_x - start_x, 2)
        val_2 = np.power(end_y - start_y, 2)
        dist = np.power(val_1 + val_2, 0.5)
    else:
        dist = None
    return dist
        