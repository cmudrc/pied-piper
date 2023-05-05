from piperabm.resource import ResourceRate


resource_rate = ResourceRate()
resource_rate.create('food', 6)
resource_rate.create('water', 4)
resource_rate.create('energy', 3)


if __name__ == "__main__":
    resource_rate.print()