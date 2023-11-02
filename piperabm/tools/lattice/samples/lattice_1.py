from piperabm.tools.lattice.samples import lattice_0


lattice = lattice_0.generate(9, 12, threashold=0.07)


if __name__ == "__main__":
    lattice.show()
