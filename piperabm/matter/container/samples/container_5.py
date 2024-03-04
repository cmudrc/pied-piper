from piperabm.matter import Container
from piperabm.matter.matter.samples import matter_5


container = Container(
    matter=matter_5,
    max=20,
)


if __name__ == '__main__':
    print(container)