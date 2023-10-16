from piperabm.resources.resource import Resource


resource = Resource(
    name='energy',
    amount=40,
    max=100,
)


if __name__ == "__main__":
    resource.print