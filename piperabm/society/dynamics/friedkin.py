import numpy as np
from copy import deepcopy


class Friedkin:

    def __init__(self, influence, opinions_initial, threashold=0.01):
        influence = np.array(influence)
        W, A = self.split_influence(influence)
        self.W = W # interpersonal influence matrix
        self.A = A # self-weights matrix
        self.len = len(influence)
        self.opinions_initial = opinions_initial
        self.threashold = threashold
        
        self.opinions = deepcopy(opinions_initial)

    def split_influence(self, influence):
        # Create a diagonal matrix from the diagonal elements of the influence matrix
        diagonal_matrix = np.diag(np.diag(influence))
        # Create the off-diagonal matrix by subtracting the diagonal matrix from the influence matrix
        off_diagonal_matrix = influence - diagonal_matrix
        return off_diagonal_matrix, diagonal_matrix

    def solve(self, report=False):
        #for _ in range(1000):
        i = 0
        while True:
            i += 1
            opinions_new = self.formula()
            distance = self.average_columnwise_euclidean_distance(self.opinions, opinions_new)
            if report is True:
                txt = "step: " + str(i) + " / " + "error: " + str(distance)
                print(txt)
            if distance > self.threashold:
                self.opinions = opinions_new
            else:
                self.opinions = opinions_new
                break
        return self.opinions

    def formula(self):
        I = np.eye(self.len)
        interpersonal_part = (I - self.A) @ self.W @ self.opinions
        self_part = self.A @ self.opinions_initial
        return interpersonal_part + self_part
    
    def average_columnwise_euclidean_distance(self, matrix1, matrix2):
        matrix1 = np.array(matrix1)
        matrix2 = np.array(matrix2)
        distances = np.sqrt(((matrix1 - matrix2) ** 2).sum(axis=0))
        avg_distance = distances.mean()
        return avg_distance
    

if __name__ == "__main__":
    influence = [
        [0.8, 0.1, 0.1],
        [0.25, 0.5, 0.25],
        [0.2, 0.4, 0.4],
    ]
    opinions_initial = [
        [0.8, 0.1],
        [0.2, 0.3],
        [0.9, 0.8]
    ]
    solver = Friedkin(influence, opinions_initial)
    solver.solve(report=True)
    print(solver.opinions)
    '''
    opinions_final = [
        [0.65482265, 0.09180668],
        [0.24399502, 0.20912674],
        [0.49713752, 0.38120722]
    ]
    print(solver.average_columnwise_euclidean_distance(opinions_initial, opinions_final))
    '''