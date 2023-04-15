from piperabm.object import Object
from piperabm.boundary.shapes import Dot, Circle


class Boundary(Object):

    def __init__(self, shape=None):
        if shape is None:
            shape = Dot()
        self.shape = shape

    def relative_pos(self, point, center):
        x = point[0]-center[0]
        y = point[1]-center[1]
        return [x, y]

    def is_in(self, point, center):
        relative_pos = self.relative_pos(point, center)
        return self.shape.is_in(relative_pos)

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
        shape.from_dict(shape_dict)
        self.shape = shape


if __name__ == "__main__":
    boundary = Boundary()
    print(boundary)