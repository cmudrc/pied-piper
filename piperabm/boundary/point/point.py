from piperabm.tools.shapes.dot import Dot
from piperabm.boundary.boundary import Boundary


class Point(Boundary):

    def __init__(self):
        super().__init__(
            shape=Dot()
        )


if __name__ == "__main__":
    boundary = Point()
    print(boundary)