import os

from piperabm.model import Model
from piperabm.tools.lattice import Lattice


path = os.path.dirname(os.path.realpath(__file__))
filename = 'utqiavik_small'

model = Model()
model.load(path, filename)


if __name__ == '__main__':
    model.show()
