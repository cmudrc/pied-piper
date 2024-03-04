from piperabm.matter import Containers
from piperabm.matter.container.samples import container_0 as food
from piperabm.matter.container.samples import container_1 as water
from piperabm.matter.container.samples import container_2 as energy


containers = Containers(food, water, energy)


if __name__ == '__main__':
    print(containers)