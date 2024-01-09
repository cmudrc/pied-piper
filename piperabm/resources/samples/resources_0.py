from copy import deepcopy

from piperabm.resources import Resource, Resources


resource_0 = Resource(name='food', amount=0)
resource_1 = Resource(name='water', amount=0)
resource_2 = Resource(name='energy', amount=0)
resources = Resources(resource_0, resource_1, resource_2)


if __name__ == '__main__':
    resources.print