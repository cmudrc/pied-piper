from piperabm.matter import Matters
from piperabm.matter.matter.samples import matter_3 as food
from piperabm.matter.matter.samples import matter_4 as water
from piperabm.matter.matter.samples import matter_5 as energy


matters = Matters(food, water, energy)


if __name__ == '__main__':
    print(matters)