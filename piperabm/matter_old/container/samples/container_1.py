from piperabm.matter import Container
from piperabm.matter.matter.samples import matter_1


container = Container(
    matter=matter_1,
    max=100,
)


if __name__ == '__main__':
    print(container)