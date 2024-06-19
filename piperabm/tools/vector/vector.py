from piperabm.tools.vector.magnitude import magnitude
from piperabm.tools.vector.normalize import normalize


class vector:
    """
    A module to work with vectors
    """
    
    @staticmethod
    def magnitude(vector):
        return magnitude(vector)
    
    @staticmethod
    def normalize(vector, ndarray=False):
        return normalize(vector, ndarray)
    

if __name__ == "__main__":
    v = [1, 2 ,3]
    v_normalized = vector.normalize(v)
    v_normalized_magnitude = vector.magnitude(v_normalized)
    print(v_normalized_magnitude)