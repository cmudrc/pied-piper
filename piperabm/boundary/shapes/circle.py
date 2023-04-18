from random import uniform #######

from piperabm.tools.symbols import SYMBOLS
from piperabm.boundary.shapes.shape import Shape


class Circle(Shape):

    def __init__(self, radius: float=None):
        if radius is None:
            radius = SYMBOLS['eps']
        super().__init__()
        self.radius = radius
        self.type = 'circle'

    def is_in(self, point: list=[0, 0]):
        """
        Check whether *point* is located within the shape
        """
        distance = self.distance(point, mode='center')
        result = False
        if distance <= self.radius:
            result = True
        return result

    def point_distance_from_body(self, point: list=[0, 0]):
        """
        Calculate distance from body, negative when located inside
        """
        return self.point_distance_from_center(point) - self.radius

    def rand_pos(self) -> list:
        result = None
        while True:
            pos = [uniform(-self.radius, self.radius),
                   uniform(-self.radius, self.radius)]
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
