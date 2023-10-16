from copy import deepcopy

from piperabm.resources import Resources
from piperabm.resources.resource.samples import resource_3, resource_4, resource_5


resource_3 = deepcopy(resource_3)
resource_4 = deepcopy(resource_4)
resource_5 = deepcopy(resource_5)
resources = Resources(resource_3, resource_4, resource_5)


if __name__ == "__main__":
    resources.print