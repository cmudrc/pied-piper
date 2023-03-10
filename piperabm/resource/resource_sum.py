try: from .resource import Resource
except: from resource import Resource


def resource_sum(resources: list):
    sum = Resource(
        current_resource={
            'food': 0,
            'water': 0,
            'energy': 0
        },
        max_resource={
            'food': None,
            'water': None,
            'energy': None
        },
        min_resource={
            'food': 0,
            'water': 0,
            'energy': 0
        }
    )
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