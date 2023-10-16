from piperabm.resources.resource import Resource


resource = Resource(
    name='water',
    amount=0.1
)


if __name__ == "__main__":
    resource.print