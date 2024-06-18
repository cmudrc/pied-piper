from piperabm.tools.coordinate.distance.point_to_point import point_to_point
from piperabm.tools.coordinate.distance.point_to_line import point_to_line
from piperabm.tools.coordinate.distance.point_to_line_segment import point_to_line_segment


class distance:

    @staticmethod
    def point_to_point(point_1, point_2, vector=False, ndarray=False):
        return point_to_point(point_1, point_2, vector, ndarray)

    @staticmethod
    def point_to_line(point, line, segment=False, perpendicular_only=False, vector=False, ndarray=False):
        result = None

        line_point_1 = line[0]
        line_point_2 = line[1]

        if segment is False:
            result = point_to_line(point, line_point_1, line_point_2, vector, ndarray)
        elif segment is True:
            result = point_to_line_segment(point, line_point_1, line_point_2, perpendicular_only, vector, ndarray)

        return result
