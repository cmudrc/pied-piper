from piperabm.boundary.rectangular import Rectangular
from piperabm.boundary.shapes.samples.rectangle import rectangle_1


rectangular = Rectangular()
rectangular.shape = rectangle_1


if __name__ == "__main__":
    print(rectangular)