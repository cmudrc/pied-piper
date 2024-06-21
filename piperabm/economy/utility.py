from piperabm.economy.accessibility import accessibility


def utility(
        resource: float,
        enough_resource: float,
        price: float,
        balance: float,
        coeff: float = 0
    ):
    """
    Represent utility which is a combination of utility from money and resources
    :coeff: determines the effect of moeny on utility
    """
    if coeff > 1 or coeff < 0:
        raise ValueError("coeff should have a value between 0 and 1")
    resource_value = resource * price
    enough_resource_value = enough_resource * price
    resource_utility = accessibility(
        resource=resource_value,
        enough_resource=enough_resource_value
    )
    resource_utility_slope = 1 / enough_resource_value
    money_utility = (resource_utility_slope * coeff) * balance
    return resource_utility + money_utility


if __name__ == "__main__":
    coeff = 0.1

    resource = 7
    enough_resource = 10
    price = 10
    balance = 100

    delta_resource = 2
    delta_balance = delta_resource * price

    resource_final = resource - delta_resource
    balance_final = balance + delta_balance

    u_initial = utility(
        resource=resource,
        enough_resource=enough_resource,
        price=price,
        balance=balance,
        coeff=coeff
    )
    u_final = utility(
        resource=resource_final,
        enough_resource=enough_resource,
        price=price,
        balance=balance_final,
        coeff=coeff
    )

    print("initial: ", u_initial)
    print("final: ", u_final)