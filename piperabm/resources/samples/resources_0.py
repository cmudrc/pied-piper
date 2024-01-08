from copy import deepcopy

from piperabm.resources import Resources
from piperabm.resources.resource.samples import resource_0, resource_1, resource_2


resource_0 = deepcopy(resource_0)
resource_1 = deepcopy(resource_1)
resource_2 = deepcopy(resource_2)
resources = Resources(resource_0, resource_1, resource_2)


if __name__ == '__main__':
    resources.print