import os


# Create:
'''
import random

from piperabm.tools.lattice.samples import lattice_0 as target_lattice


random.seed(10)
lattice = target_lattice.generate(9, 12, threashold=0.07)

path = os.path.dirname(os.path.realpath(__file__))
lattice.save(path, filename="lattice_1")
'''

# Load:
from piperabm.tools.lattice import Lattice

lattice = Lattice()
path = os.path.dirname(os.path.realpath(__file__))
lattice.load(path, filename="lattice_1")


if __name__ == "__main__":
    lattice.show()

