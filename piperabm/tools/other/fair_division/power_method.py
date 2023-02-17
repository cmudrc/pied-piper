import numpy as np
from copy import deepcopy


class PowerMethod:

    def __init__(self, matrix, threashold):

        def default_weight():
            default_weight = []
            val = 1 / self.len
            for _ in range(self.len):
                default_weight.append(val)
            default_weight = np.array(default_weight)
            return default_weight

        def matrix_len(matrix):
            shape = matrix.shape
            if shape[0] == shape[1]:
                return shape[0]
            else:
                raise ValueError

        self.threashold = threashold
        if isinstance(matrix, np.matrix):
            pass
        elif isinstance(matrix, list):
            matrix = np.matrix(matrix)
        else:
            raise ValueError
        self.len = matrix_len(matrix)
        self.default_weight = default_weight()
        self.result_dict = {
            0: {
                'matrix': deepcopy(matrix),
                'weight': deepcopy(self.default_weight)
            }
        }
        self.current_step = 1 # next round starts...
    
    def last_matrix(self):
        return self.result_dict[self.current_step-1]['matrix']

    def last_weight(self):
        return self.result_dict[self.current_step-1]['weight']

    def run_step(self):

        def calculate_new_matrix():
            matrix = self.last_matrix()
            new_matrix = matrix @ matrix
            return new_matrix
        
        def calculate_new_weight():
            matrix = self.result_dict[0]['matrix']
            weight = self.last_weight()
            new_weight = matrix @ weight
            return new_weight

        new_matrix = calculate_new_matrix()
        new_weight = calculate_new_weight()
        self.result_dict[deepcopy(self.current_step)] = {
            'matrix': deepcopy(new_matrix),
            'weight': deepcopy(new_weight)
        }
        self.current_step += 1

    def run(self):
        while self.is_converged(self.last_matrix()) is False:
            self.run_step()
            print(self.last_matrix())

    def is_converged(self, matrix):
        result = False
        average_distance = self.average_distance(matrix)
        overall_distance = self.overall_distance(average_distance)
        if overall_distance < self.threashold:
            result = True
        return result

    def average_distance(self, matrix):

        def distance(val, mean):
            return np.abs(val-mean)

        result = []
        for i in range(self.len):
            row = matrix[i]
            row_average = sum(row) / self.len
            distance_list = []
            for j in range(self.len):
                dist = distance(row[j], row_average)
                distance_list.append(dist)
            dist_average = sum(distance_list) / self.len
            result.append(dist_average)
        return result

    def overall_distance(self, average_distance):
        return sum(average_distance) / self.len


if __name__ == "__main__":
    matrix = [[0.8, 0.6], [0.2, 0.4]]
    threashold = 0.1
    pm = PowerMethod(matrix, threashold)
    print(pm.default_weight)