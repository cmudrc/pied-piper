import sys

from piperabm.boundary.shapes.circle import Circle


class Dot(Circle):

    def __init__(self):
        epsilon = sys.float_info.epsilon
        super().__init__(radius=epsilon)
        self.type = 'dot'


if __name__ == "__main__":
    shape = Dot()
    print(shape)