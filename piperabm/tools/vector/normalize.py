import numpy as np


def normalize(vector, ndarray=False):
    """
    Normalize a vector to have a magnitude of 1.
    
    :param v: A numpy array representing a vector.
    :return: Normalized vector.
    """
    result = None
    magnitude = np.linalg.norm(vector)
    if magnitude == 0:
        raise ValueError("Cannot normalize a zero vector")
    result = vector / magnitude
    if ndarray is False:
        result = [float(num) for num in result]  # Convert np.float64 to float explicitly
    return result


if __name__ == "__main__":
    vector = [1, 2 ,3]
    vector_normalized = normalize(vector)
    print(vector_normalized)