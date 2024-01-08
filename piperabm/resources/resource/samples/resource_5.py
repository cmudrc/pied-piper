from piperabm.resources.resource import Resource


resource = Resource(
    name='energy',
    amount=0.5
)


if __name__ == '__main__':
    resource.print