from piperabm.resources.resource import Resource


resource = Resource(
    name='food',
    amount=30,
    max=100,
)


if __name__ == "__main__":
    resource.print