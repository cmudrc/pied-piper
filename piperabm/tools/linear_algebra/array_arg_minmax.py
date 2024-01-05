import numpy as np


def array_argmax(array):
    if isinstance(array, list):
        array = np.array(array)
    index_flat = np.argmax(array)
    return list(np.unravel_index(index_flat, array.shape))

def array_argmin(array):
    if isinstance(array, list):
        array = np.array(array)
    index_flat = np.argmin(array)
    return list(np.unravel_index(index_flat, array.shape))


if __name__ == "__main__":
    array = [
            [1, 2],
            [4, 3]
        ]
    result = array_argmax(array)
    #result = array_argmin(array)
    print(result)
