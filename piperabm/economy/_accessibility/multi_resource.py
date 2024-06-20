from piperabm.tools import average as avg


def multi_resource_accessibility(accessibilities: list) -> float:
    return avg.geometric(values=accessibilities)


if __name__ == "__main__":
    food = 0.2
    water = 0.5
    energy = 0.8
    accessibilities = [food, water, energy]
    print(multi_resource_accessibility(accessibilities))