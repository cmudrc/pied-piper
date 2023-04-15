from piperabm.boundary.shapes.circle import Circle
from piperabm.boundary.boundary import Boundary


class Circular(Boundary):

    def __init__(self, radius):
        super().__init__(
            shape=Circle(radius)
        )


if __name__ == "__main__":
    boundary = Circular(radius=5)
    print(boundary)