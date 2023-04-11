import numpy as np


class Formula:

    name = "formula_01"

    def calculate(ratio: float=0):
        n = 1
        return np.exp(n * ratio)


if __name__ == "__main__":
    formula = Formula
    factor = formula.calculate(ratio=0.3)
    print(formula.name)