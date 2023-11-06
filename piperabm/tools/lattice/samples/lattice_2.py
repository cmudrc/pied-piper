import random

from piperabm.tools.lattice.samples import lattice_0 as target_lattice


random.seed(10)
lattice = target_lattice.generate(30, 40, threashold=0.1)


if __name__ == "__main__":
    lattice.show()
    #print(lattice.distribution)
    #print(lattice.length_ratio)

