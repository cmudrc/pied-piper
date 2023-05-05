from piperabm.resource import Resource
from piperabm.resource.container.samples import container_0, container_1, container_2


resource = Resource()
resource.add_container_object('food', container_0)
resource.add_container_object('water', container_1)
resource.add_container_object('energy', container_2)


if __name__ == "__main__":
    resource.print()