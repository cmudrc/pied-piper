from piperabm.matter import Container
from piperabm.matter.matter.samples import matter_4


container = Container(
    matter=matter_4,
    max=100,
)


if __name__ == '__main__':
    container.print