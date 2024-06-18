from piperabm.tools.vector.magnitude import magnitude
from piperabm.tools.vector.normalize import normalize


class vector:
    
    @staticmethod
    def magnitude(vector):
        return magnitude(vector)
    
    @staticmethod
    def normalize(vector, ndarray=False):
        return normalize(vector, ndarray)