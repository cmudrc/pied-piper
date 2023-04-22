from piperabm.object import Object
from piperabm.boundary.shapes import Dot, Circle, Rectangle


class Boundary(Object):

    def __init__(self, shape=None):
        if shape is None:
            shape = Dot()
        self.shape = shape

    def distance(self, pos, center, mode='center'):
        relative_pos = self.relative_pos(pos, center)
        return self.shape.distance(relative_pos, mode)

    def relative_pos(self, point, center):
        """
        Calculate pos after moving origin to center
        """
        x = point[0] - center[0]
        y = point[1] - center[1]
        return [x, y]

    def rand_pos(self, center) -> list:
        pos_local = self.shape.rand_pos()
        return [
            pos_local[0] + center[0],
            pos_local[1] + center[1],
        ]

    def is_in(self, point, center):
        """
        Check whether *point* is located within the boundary
        """
        local_pos = self.relative_pos(point, center)
        return self.shape.is_in(local_pos)

    def to_dict(self) -> dict:
        return {
            'shape': self.shape.to_dict(),
        }

    def from_dict(self, dictionary: dict):
        shape_dict = dictionary['shape']
        type = shape_dict['type']
        if type == 'dot':
            shape = Dot()
        elif type == 'circle':
            shape = Circle()
        elif type == 'rectangle':
            shape = Rectangle()
        shape.from_dict(shape_dict)
        self.shape = shape


if __name__ == "__main__":
    boundary = Boundary()
    print(boundary)
