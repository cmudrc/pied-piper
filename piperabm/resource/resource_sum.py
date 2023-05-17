from piperabm.resource import Resource, ResourceDelta


def resource_sum(resources: list):
    """
    Calculate sum of *resources* list
    """
    all_resource_names = []
    ''' aggregate all resource names in the list '''
    if len(resources) > 0:
        for resource in resources:
            resource_names = resource.all_names()
            for name in resource_names:
                if name not in all_resource_names:
                    all_resource_names.append(name)
    ''' summation '''
    sum = Resource()
    sum.create_zeros(all_resource_names)
    for resource in resources:
        if isinstance(resource, Resource):
            sum + resource.to_resource_delta()
        elif isinstance(resource, ResourceDelta):
            sum + resource
    return sum.to_resource_delta()


if __name__ == "__main__":
    from copy import deepcopy
    from piperabm.resource.samples import resource_0
    
    r1 = deepcopy(resource_0)
    r2 = deepcopy(resource_0)
    sum = resource_sum([r1, r2])
    print(sum)