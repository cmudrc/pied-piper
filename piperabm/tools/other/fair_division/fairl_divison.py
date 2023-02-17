import numpy as np


class FairDivision:

    def __init__(self):
        self.votes_dict = {}

    def add(self, name: str, vote: list):
        self.votes_dict[name] = vote

    def calculate(self):
        def create_mat(votes_dict):
            result = []
            for name in votes_dict:
                result.append(self.votes_dict[name])
            return np.matrix([[1, 2], [3, 4]])


if __name__ == "__main__":
    matrix = np.matrix([[1, 2], [3, 4]])

