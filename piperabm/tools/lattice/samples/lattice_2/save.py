"""
Generate a lattice structure based on a target lattice (lattice_1)
"""

import os
import random

from piperabm.tools.lattice.samples import lattice_1 as target_lattice


random.seed(10)
lattice = target_lattice.generate(30, 40, threashold=0.1)
path = os.path.dirname(os.path.realpath(__file__))
lattice.save(path, filename='lattice_2')