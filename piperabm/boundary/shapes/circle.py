from random import uniform #######

from piperabm.setting import SETTING
from piperabm.boundary.shapes.shape import Shape
from piperabm.tools import euclidean_distance


class Circle(Shape):

    def __init__(self, radius: float=None):
        if radius is None:
            radius = SETTING['eps']
        super().__init__()
        self.radius = radius
        self.type = 'circle'

    def is_in(self, point: list=[0, 0]):
        """
        Check whether *point* is located within the boundary
        """
        distance = self.distance(point, mode='center')
        result = False
        if distance <= self.radius:
            result = True
        return result

    def point_distance_from_center(self, point: list=[0, 0]):
        """
        Calculate the distance from center.
        """
        center = [0, 0]
        return euclidean_distance(*center, *point)

    def point_distance_from_boundary(self, point: list=[0, 0]):
        """
        Calculate distance from boundary, negative when located inside
        """
        return self.point_distance_from_center(point) - self.radius

    def point_distance(self, point: list=[0, 0], mode='center'):
        """
        Calculate the distance.
        """
        if mode == 'center':
            return self.point_distance_from_center(point)
        elif mode == 'boundary':
            return self.point_distance_from_boundary(point)
        
    def distance(self, other, mode='center'):
        result = None
        if isinstance(other, list): # point
            result = self.point_distance(point=other, mode=mode)
        return result

    def rand_pos(self) -> list:
        result = None
        while True:
            pos = [uniform(-self.radius, self.radius),
                   uniform(-self.radius, self.radius)]
            pos = [(pos[0] + self.center[0]), (pos[1] + self.center[1])]
            if self.is_in(pos):
                result = pos
                break
        return list(result)

    def to_dict(self) -> dict:
        dictionary = super().to_dict()
        dictionary['radius'] = self.radius
        return dictionary

    def from_dict(self, dictionary: dict):
        super().from_dict(dictionary)
        self.radius = dictionary['radius']    

if __name__ == "__main__":
    shape = Circle(radius=5)
    print(shape)
