from piperabm.tools.shapes.circle import Circle
from piperabm.boundary.boundary import Boundary
from piperabm.tools.symbols import SYMBOLS


class Circular(Boundary):

    def __init__(self, radius=None):
        super().__init__(
            shape=Circle(radius)
        )


if __name__ == "__main__":
    boundary = Circular(radius=5)
    print(boundary)