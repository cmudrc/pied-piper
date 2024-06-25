def accessibility(resource: float, enough_resource: float) -> float:
    return min(resource / enough_resource, 1)


if __name__ == "__main__":
    resource = 5
    enough_resource = 10
    print(
        accessibility(
            resource=resource,
            enough_resource=enough_resource
        )
    )