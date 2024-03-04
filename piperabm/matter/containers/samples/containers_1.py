from piperabm.matter import Containers
from piperabm.matter.container.samples import container_3 as food
from piperabm.matter.container.samples import container_4 as water
from piperabm.matter.container.samples import container_5 as energy


containers = Containers(food, water, energy)


if __name__ == '__main__':
    print(containers)