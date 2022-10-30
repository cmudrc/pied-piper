import numpy as np


def euclidean_distance(x_start, y_start, x_end, y_end):
    start = np.array([x_start, y_start])
    end = np.array([x_end, y_end])
    return np.sqrt(np.sum(np.square(end - start)))


if __name__ == "__main__":
    pos_1 = [0, 3]
    pos_2 = [4, 0]
    print(euclidean_distance(*pos_1, *pos_2))