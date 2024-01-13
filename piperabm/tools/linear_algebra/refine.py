import numpy as np


def refine(input):
    """
    Refine input and convert is to ndarray if was not
    """
    if isinstance(input, list):
        input = np.array(input)
    elif isinstance(input, np.ndarray):
        pass
    else:
        raise ValueError
    return input


if __name__ == '__main__':
    val = [1, 2]
    val = refine(val)
    print(type(val))