from piperabm.resource.container import Container
from piperabm.resource.matter.samples import matter_1


container = Container(max=20)
container.add_matter_object(matter_1)


if __name__ == "__main__":
    print(container)