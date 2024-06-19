import numpy as np


def magnitude(vector) -> float:
    """
    Retrun magnitude of a vector
    """
    if vector is None:
        raise ValueError
    return float(np.sqrt(np.sum(np.square(vector))))


if __name__ == "__main__":
    vector = [3, 4]
    print(magnitude(vector))
    