from piperabm.boundary.shapes.rectangle import Rectangle
from piperabm.boundary.boundary import Boundary


class Rectangular(Boundary):

    def __init__(
            self,
            width: float=None,
            height: float=None,
            angle: float=0
        ):
        super().__init__(
            shape=Rectangle(
                width=width,
                height=height,
                angle=angle
            )
        )


if __name__ == "__main__":
    boundary = Rectangular(width=4, height=3, angle=0)
    print(boundary)