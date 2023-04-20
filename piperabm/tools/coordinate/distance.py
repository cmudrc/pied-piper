import numpy as np


def euclidean_distance(pos_start: list, pos_end: list):
    start = np.array(pos_start)
    end = np.array(pos_end)
    return np.sqrt(np.sum(np.square(end - start)))


if __name__ == "__main__":
    pos_1 = [0, 3]
    pos_2 = [4, 0]
    print(euclidean_distance(pos_1, pos_2))