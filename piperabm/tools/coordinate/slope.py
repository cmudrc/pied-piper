import numpy as np
from piperabm.tools.symbols import SYMBOLS


def slope(start_pos: list, end_pos: list):
    angle = None
    vector_unit = np.array([1, 0])
    start_x = start_pos[0]
    start_y = start_pos[1]
    end_x = end_pos[0]
    end_y = end_pos[1]
    vector = np.array(
        [
            end_x - start_x,
            end_y - start_y
        ]
    )
    dot_product = np.dot(vector, vector_unit)
    angle = np.arccos(dot_product)
    if vector[1] < 0:
        angle += np.pi
    return angle


if __name__ == "__main__":
    start_pos = [0, 0]
    end_pos = [-1, 0]
    angle = slope(start_pos, end_pos)
    print(angle)