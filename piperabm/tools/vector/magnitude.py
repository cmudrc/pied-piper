import numpy as np


def magnitude(vector):
    if vector is None:
        raise ValueError
    return np.sqrt(np.sum(np.square(vector)))


if __name__ == '__main__':
    vector = [3, 4]
    magnitude = magnitude(vector)
    print(magnitude)
    