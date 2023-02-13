import numpy as np


def gini_coefficient(x):
    """
    Compute Gini coefficient of array of values
    """
    x = np.array(x)
    diffsum = 0
    for i, xi in enumerate(x[:-1], 1):
        diffsum += np.sum(np.abs(xi - x[i:]))
    return diffsum / (len(x)**2 * np.mean(x))


def generate_random(gini, n):
    """
    Generate a random array of size n which gini index is equal to *gini*
    """
    def gen(gini):
        return 0

    result = []
    for _ in range(n):
        result.append(gen(gini))
    return result


if __name__ == "__main__":
    array = [1, 3, 5, 7, 9, 3, 5, 7, 5]
    print(gini_coefficient(array))