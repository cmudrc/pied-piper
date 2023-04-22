from piperabm.boundary.rectangular import Rectangular
from piperabm.tools.shapes.rectangle.samples import rectangle_1


rectangular = Rectangular()
rectangular.shape = rectangle_1


if __name__ == "__main__":
    print(rectangular)