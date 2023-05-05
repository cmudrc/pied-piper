from piperabm.resource.container import Container
from piperabm.resource.matter.samples import matter_2


container = Container(max=25)
container.add_matter_object(matter_2)


if __name__ == "__main__":
    print(container)