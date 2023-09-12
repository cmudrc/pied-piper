from piperabm.tools.coordinate.distance import distance_point_to_line


def intersect_line_circle(
        line_point_1: list,
        line_point_2: list,
        circle_center: list,
        circle_radius: float
    ):
    """
    Check whether the line intersecs the circle
    """
    distance = distance_point_to_line(
        point=circle_center,
        line_point_1=line_point_1,
        line_point_2=line_point_2
    )
    if distance is None: result = False
    else:
        if distance <= circle_radius:
            result = True
        else:
            result = False
    return result


if __name__ == '__main__':
    point_1 = [0, 0]
    point_2 = [2, 2]
    circle_center = [1.4, 0.6]
    circle_radius = 0.6
    result = intersect_line_circle(point_1, point_2, circle_center, circle_radius)
    print(result)
