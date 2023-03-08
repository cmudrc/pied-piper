def resource_value(resource, exchange_rate):
    """
    Calculate the value of each resource in unit of currency
    """
    result = {}
    for name in resource.current_resource:
        er = exchange_rate.rate(
            source=name,
            target='wealth'
        )
        amount = resource(name)
        result[name] = er * amount
    return result

def total_resource_value(resource_value_dict: dict):
    """
    Calculate the total value of resources in unit of currency
    """
    total_value = 0
    for key in resource_value_dict:
        total_value += resource_value_dict[key]
    return total_value