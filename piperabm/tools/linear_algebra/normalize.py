import numpy as np


def normalize(vector):
    """
    Normalize a vector to have a magnitude of 1.
    
    :param v: A numpy array representing a vector.
    :return: Normalized vector.
    """
    if isinstance(vector, list):
        vector = np.array(vector)
    magnitude = np.linalg.norm(vector)
    if magnitude == 0:
        raise ValueError("Cannot normalize a zero vector")
    return vector / magnitude


if __name__ == "__main__":
    vector = [1, 2 ,3]
    vector_normalized = normalize(vector)
    print(vector_normalized)