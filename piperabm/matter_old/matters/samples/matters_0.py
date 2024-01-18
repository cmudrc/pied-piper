from piperabm.matter import Matters
from piperabm.matter.matter.samples import matter_0 as food
from piperabm.matter.matter.samples import matter_1 as water
from piperabm.matter.matter.samples import matter_2 as energy


matters = Matters(food, water, energy)


if __name__ == '__main__':
    matters.print