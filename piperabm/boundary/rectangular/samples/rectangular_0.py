from copy import deepcopy

from piperabm.boundary.rectangular import Rectangular
from piperabm.tools.shapes.rectangle.samples import rectangle_0


rectangular = Rectangular()
rectangular.shape = deepcopy(rectangle_0)


if __name__ == "__main__":
    print(rectangular)