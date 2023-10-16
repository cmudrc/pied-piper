from piperabm.resources.resource import Resource


resource = Resource(
    name='food',
    amount=0.2
)


if __name__ == "__main__":
    resource.print