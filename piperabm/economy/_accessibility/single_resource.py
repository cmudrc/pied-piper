def single_resource_accessibility(resource: float, enough_resource: float) -> float:
    return min(resource / enough_resource, 1)


if __name__ == "__main__":
    resource = 5
    enough_resource = 10
    print(single_resource_accessibility(resource, enough_resource))