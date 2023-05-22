import numpy as np
from copy import deepcopy


class PowerMethod:

    def __init__(self, matrix, threashold):
        if not isinstance(matrix, np.matrix):
            if isinstance(matrix, list):
                matrix = np.matrix(matrix)
        self.matrix = matrix
        self.threashold = threashold

        self.initial_values = {
            'matrix': deepcopy(self.matrix),
            'threashold': deepcopy(self.threashold)
        }
    
    def run_step(self):

        def calculate_new_matrix(matrix):
            return matrix @ matrix
        
        self.matrix = calculate_new_matrix(self.matrix)

    def run(self, n):
        for _ in range(n):
            self.run_step()

    def is_converged(self):
        return False ####
    
    def __str__(self):
        return str(self.matrix)
    

if __name__ == "__main__":
    matrix = [
        [0.4, 0.6],
        [0.2, 0.8]
    ]
    pm = PowerMethod(matrix, threashold=0.05)
    pm.run(10)
    print(pm)