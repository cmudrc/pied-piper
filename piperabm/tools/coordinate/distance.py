import numpy as np


def euclidean_distance(start_pos: list, end_pos: list):
    start = np.array(start_pos)
    end = np.array(end_pos)
    return np.sqrt(np.sum(np.square(end - start)))


if __name__ == "__main__":
    pos_1 = [0, 3]
    pos_2 = [4, 0]
    print(euclidean_distance(pos_1, pos_2))