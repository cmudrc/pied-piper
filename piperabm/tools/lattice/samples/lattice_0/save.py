"""
Create and save a simple lattice structure with imperfections
"""

import os

from piperabm.tools.lattice import Lattice


lattice = Lattice(3, 4)

# Horizontal removals:
lattice.remove_edge((0, 0), (1, 0))
lattice.remove_edge((1, 0), (2, 0))
lattice.remove_edge((0, 1), (1, 1))
lattice.remove_edge((1, 1), (2, 1))
lattice.remove_edge((1, 3), (2, 3))

# Vertical removals:
lattice.remove_edge((0, 0), (0, 1))
lattice.remove_edge((0, 1), (0, 2))
lattice.remove_edge((1, 0), (1, 1))

path = os.path.dirname(os.path.realpath(__file__))
lattice.save(path, filename='lattice_0')