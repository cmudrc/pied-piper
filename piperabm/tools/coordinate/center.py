import numpy as np


def center(start_pos: list, end_pos: list):
    start = np.array(start_pos)
    end = np.array(end_pos)
    result = (start + end) / 2
    return list(result)


if __name__ == "__main__":
    pos_1 = [0, 0]
    pos_2 = [2, 2]
    print(center(pos_1, pos_2))