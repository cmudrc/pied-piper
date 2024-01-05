import numpy as np

from piperabm.tools.coordinate.distance.point_to_point import point_to_point as distance_point_to_point


class distance:

    def point_to_point(point_1, point_2):
        return distance_point_to_point(point_1, point_2)
    
    def point_to_line(point, line, segment=True, perpendicular_only=True, vector=False):
        pass
    

if __name__ == "__main__":
    point_1 = [0, 0]
    point_2 = [3, 4]
    d = distance.point_to_point(point_1, point_2)
    print(d)