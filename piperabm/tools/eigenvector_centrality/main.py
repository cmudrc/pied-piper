import numpy as np
from copy import deepcopy


class EC:

    def __init__(self):
        pass
        self.votes = []
        self.mat = None
        self.initial_vector = None
        self.vector = None
        self.step = 0

    @property
    def len(self):
        return len(self.votes)

    def add(self, vote):
        vote = np.array(vote)
        vote = self.normalize(vote)
        self.votes.append(vote)

    def to_matrix(self):
        mat = []
        i_length = self.len
        for vote in self.votes:
            j_length = len(vote)
            if j_length != i_length:
                raise ValueError
            mat.append(vote)
        mat = np.array(mat)
        #mat = mat.T
        self.mat = mat
        return mat
    
    def run_step(self):
        ''' initial vector assumptipn '''
        if self.vector is None:
            self.to_matrix()
            ones = np.ones(self.len)
            #ones = ones.T
            self.vector = ones / self.len
            self.initial_vector = deepcopy(self.vector)
        #new_vector = np.matmul(self.mat, self.vector)
        new_vector = self.mat.dot(self.vector)
        #print(new_vector)
        self.vector = new_vector
        self.step += 1

    def run(self, n=10):
        for _ in range(n):
            self.run_step()

    '''
    def normalize_0(self, array):
        """
        Normalize the vector length
        """
        array = np.array(array)
        return array / np.linalg.norm(array)
    '''
    
    def normalize(self, array):
        """
        Normalize the vector length
        """
        array = np.array(array)
        return array / sum(array)
    

if __name__ == "__main__":
    ec = EC()
    ec.add([1, 1, 1])
    ec.add([0, 2, 1])
    ec.add([0.5, 1, 1.5])
    #ec.mat
    #ec.to_matrix()
    #print(ec.mat)
    ec.run_step()
    ec.run_step()
    ec.run_step()
    #print(ec.vector)
    #print(ec.mat)
    mat = np.matrix(ec.mat)
    mat = mat @ mat
    mat = mat @ mat
    mat = mat @ mat
    print(mat)
    #arr = np.array([1, 1])
    #new_arr = ec.normalize(arr)
    #print(new_arr)

    
    #a = np.array([[0.5, 0.5], [0, 1]])
   # b = np.ones(2)
    #b = b / 2
    #r = a.dot(b)
    #r = np.matmul(a, b)
    #print(r)
    
