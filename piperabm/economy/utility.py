from piperabm.economy.accessibility import accessibility


def utility(resource, enough_resource, price, balance):
    resource_utility = accessibility(
        resource=resource*price,
        enough_resource=enough_resource*price
    )
    money_utility_coeff = 0.2
    money_utility = (1 / enough_resource*price) * money_utility_coeff * balance
    return resource_utility + money_utility


if __name__ == "__main__":
    u = utility(
        resource=5,
        enough_resource=10,
        price=10,
        balance=100
    )
    print(u)
    
    u = utility(
        resource=4,
        enough_resource=10,
        price=10,
        balance=110
    )
    print(u)