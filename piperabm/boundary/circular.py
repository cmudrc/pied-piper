from random import uniform #########
from piperabm.tools import euclidean_distance
from piperabm.boundary.boundary import Boundary


class Circular(Boundary):
    """
    Define an enclosed area in space.
    """

    def __init__(self, radius=1):
        super().__init__()
        self.center = None # position of center of boundery in [x, y] form
        self.radius = radius
        self.type = 'circular'

    def is_in(self, other):
        """
        Check whether *other* is within the boundary
        """
        distance = self.distance(other, mode='center')
        result = False
        if distance <= self.radius:
            result = True
        return result

    def _distance_from_center(self, other):
        """
        Calculate the distance from center.
        """
        x_0 = self.center[0]
        y_0 = self.center[1]
        pos_0 = [x_0, y_0]
        if isinstance(other, list):
            x_1 = other[0]
            y_1 = other[1]
        else:
            x_1 = other.center[0]
            y_1 = other.center[1]
        pos_1 = [x_1, y_1]
        return euclidean_distance(*pos_0, *pos_1)

    def _distance_from_boundary(self, other):
        return self._distance_from_center(other) - self.radius

    def distance(self, other, mode='center'):
        """
        Calculate the distance.
        """
        if mode == 'center':
            return self._distance_from_center(other)
        elif mode == 'boundary':
            return self._distance_from_boundary(other)

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
        return {
            'type': self.type,
            'center': self.center,
            'radius': self.radius,
        }

    def from_dict(self, dictionary: dict):
        self.center = dictionary['center']
        self.radius = dictionary['radius']


if __name__ == "__main__":
    boundary = Circular(radius=2)
    boundary.center = [-2, -2]
    print(boundary)