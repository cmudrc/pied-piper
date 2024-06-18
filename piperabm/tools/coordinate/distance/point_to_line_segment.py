import numpy as np

from piperabm.tools.vector import vector as vc


def point_to_line_segment(
        point,
        line_point_1,
        line_point_2,
        perpendicular_only: bool = False,
        vector: bool = False,
        ndarray: bool = False
    ):
    result = None

    x = point[0]
    y = point[1]
    x1 = line_point_1[0]
    y1 = line_point_1[1]
    x2 = line_point_2[0]
    y2 = line_point_2[1]

    A = x - x1
    B = y - y1
    C = x2 - x1
    D = y2 - y1

    dot = A * C + B * D
    len_sq = C * C + D * D
    param = -1
    if len_sq != 0:  # in case of 0 length line
        param = dot / len_sq

    xx = None
    yy = None
    if perpendicular_only is False:
        if param < 0:
            xx = x1
            yy = y1
        elif param > 1:
            xx = x2
            yy = y2
        else:
            xx = x1 + param * C
            yy = y1 + param * D
    elif perpendicular_only is True:
        if param <= 1 and \
            param >= 0:
            xx = x1 + param * C
            yy = y1 + param * D
        
    if xx is not None and \
        yy is not None:
        dx = xx - x
        dy = yy - y
        result = [dx, dy]
    
    if result is not None:
        if vector is True:
            if ndarray is True:
                result = np.array(result)
            else:
                pass
        else:
            result = vc.magnitude(result)

    return result


if __name__ == "__main__":
    point = [-3, 4]
    line_point_1 = [0, 0]
    line_point_2 = [2, 0]
    vector = point_to_line_segment(point, line_point_1, line_point_2, perpendicular_only=False)
    print(vector)
