from piperabm.matter import Container
from piperabm.matter.matter.samples import matter_3


container = Container(
    matter=matter_3,
    max=20,
)


if __name__ == '__main__':
    print(container)