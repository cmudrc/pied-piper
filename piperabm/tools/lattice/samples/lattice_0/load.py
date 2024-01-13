"""
Load the lattice structure
"""

import os

from piperabm.tools.lattice import Lattice


lattice = Lattice()
path = os.path.dirname(os.path.realpath(__file__))
lattice.load(path, filename='lattice_0')


if __name__ == '__main__':
    lattice.show()
