from piperabm.resource.container import Container
from piperabm.resource.matter.samples import matter_0


container = Container(max=10)
container.add_matter_object(matter_0)


if __name__ == "__main__":
    print(container)