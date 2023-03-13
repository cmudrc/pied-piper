try: from .resource import Resource
except: from resource import Resource


def resource_sum(resources: list):
    """
    Calculate sum of *resources* list
    """
    all_resource_names = []
    if len(resources) > 0:
        for resource in resources:
            resource_names = resource.all_resource_names()
            for name in resource_names:
                if name not in all_resource_names:
                    all_resource_names.append(name)
    sum = Resource()
    sum.create_zeros(all_resource_names)
    #print(sum.max_resource, sum.min_resource) bugggg!
    for resource in resources:
        sum, r = sum + resource
    return sum


if __name__ == "__main__":
    r1 = Resource({
        'food': 1,
        'water': 2,
        'energy': 3
    })
    r2 = Resource({
        'food': 4,
        'water': 5,
        'energy': 6
    })
    resources = [r1, r2]
    print(resource_sum(resources))