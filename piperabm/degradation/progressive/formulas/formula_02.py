import numpy as np


class Formula:

    name = "formula_02"

    def calculate(ratio: float=0):
        n = 5
        return np.exp(n * ratio)


if __name__ == "__main__":
    factor = Formula.calculate(ratio=0.3)
    print(factor)