import numpy as np
from piperabm.tools.coordinate.inverse_function import inverse_function


def rotate(
        point: list=[0, 0],
        angle: float=0,
        inverse: bool=False
    ) -> list:
    rot_mat = rotate_matrix(angle, inverse)
    new_point = np.matmul(rot_mat, np.array(point))
    return list(new_point)

def rotate_coordinate(point, angle) -> list:
    return rotate(point, angle, inverse=False)

def rotate_point(point, angle) -> list:
    return rotate(point, angle, inverse=True)

def rotate_matrix(angle, inverse: bool=False):
    inverse_factor = inverse_function(inverse)
    rot_mat = np.array(
        [
            [
                np.cos(angle),
                np.sin(angle) * inverse_factor
            ],
            [
                -np.sin(angle) * inverse_factor,
                np.cos(angle)
            ]
        ]
    )
    return rot_mat


if __name__ == "__main__":
    point = [1, 0]
    angle = (np.pi / 180) * 90
    new_point = rotate_coordinate(point, angle)
    print(new_point)