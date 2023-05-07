from piperabm.resource import ResourceDelta


resource_delta = ResourceDelta()
resource_delta.create('food', 6)
resource_delta.create('water', 4)
resource_delta.create('energy', 3)


if __name__ == "__main__":
    resource_delta.print()