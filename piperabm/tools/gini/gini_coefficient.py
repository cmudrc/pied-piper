import numpy as np


def gini_coefficient(values) -> float:
    """
    Compute Gini coefficient of array of values
    """
    values = np.array(values)
    values = np.sort(values)
    n = len(values)
    index = np.arange(1, n + 1)
    return float((2 * np.sum(index * values) / np.sum(values) - (n + 1)) / n)
    
    '''
    diffsum = 0
    for i, xi in enumerate(x[:-1], 1):
        diffsum += np.sum(np.abs(xi - x[i:]))
    return float(diffsum / (len(x)**2 * np.mean(x)))
    '''


if __name__ == "__main__":
    incomes = [100, 300, 500, 700, 900, 300, 500, 700, 500]
    gini_index = gini_coefficient(incomes)
    print(gini_index)
