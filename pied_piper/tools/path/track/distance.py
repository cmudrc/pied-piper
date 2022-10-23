import numpy as np


def euclidean_distance(x_start, y_start, x_end, y_end):
    if x_start is not None and y_start is not None \
        and x_end is not None and y_end is not None:
        val_1 = np.power(x_end - x_start, 2)
        val_2 = np.power(y_end - y_start, 2)
        dist = np.power(val_1 + val_2, 0.5)
    else:
        dist = None
    return dist

def distance(self, other):
    return np.sum(np.square(np.array(self.pos) - np.array(other.pos)))


if __name__ == "__main__":
    pos_1 = [0, 3]
    pos_2 = [4, 0]
    print(euclidean_distance(*pos_1, *pos_2))