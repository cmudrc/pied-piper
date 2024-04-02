from piperabm.matter import Container
from piperabm.matter.matter.samples import matter_2


container = Container(
    matter=matter_2,
    max=100,
)


if __name__ == '__main__':
    print(container)