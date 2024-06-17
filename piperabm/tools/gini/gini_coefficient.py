import numpy as np


def gini_coefficient(x):
    """
    Compute Gini coefficient of array of values
    """
    if isinstance(x, list):
        x = np.array(x)
    diffsum = 0
    for i, xi in enumerate(x[:-1], 1):
        diffsum += np.sum(np.abs(xi - x[i:]))
    return diffsum / (len(x)**2 * np.mean(x))


if __name__ == '__main__':
    incomes = [100, 300, 500, 700, 900, 300, 500, 700, 500]
    gini_index = gini_coefficient(incomes)
    print(gini_index)
