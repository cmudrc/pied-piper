from copy import deepcopy

from piperabm.boundary.circular import Circular
from piperabm.tools.shapes.circle.samples import circle_0


circular = Circular()
circular.shape = deepcopy(circle_0)


if __name__ == "__main__":
    print(circular)