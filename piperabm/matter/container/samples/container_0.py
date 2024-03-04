from piperabm.matter import Container
from piperabm.matter.matter.samples import matter_0


container = Container(
    matter=matter_0,
    max=100,
)


if __name__ == '__main__':
    print(container)