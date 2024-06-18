import numpy as np

from piperabm.tools.vector import vector as vc


def point_to_point(point_1, point_2, vector=False, ndarray=False):
    result = None
    point_1 = np.array(point_1)
    point_2 = np.array(point_2)
    
    if vector is True:
        result = point_2 - point_1
        if ndarray is False:
            result = list(result)
    else:
        result = vc.magnitude(point_to_point(point_1, point_2, vector=True, ndarray=True))

    return result


if __name__ == '__main__':
    point_1 = [0, 0]
    point_2 = [3, 4]
    distance = point_to_point(point_1, point_2, vector=True)
    print(distance)