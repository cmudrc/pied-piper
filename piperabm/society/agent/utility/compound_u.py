def resource_utility(x, x_critical=1, y_max=1):
    y = None
    if x < x_critical:
        slope = y_max / x_critical
        y = slope * x
    else:
        y = y_max
    return y


def currency_utility(currency, slope=1):
    return slope * currency


def utility(resource, currency):
    return resource_utility(x=resource, x_critical=1, y_max=1) + currency_utility(currency)


def total_utility_gain(resource1, currency1, resource2, currency2, price, amount):
    # Calculate the new amounts of resources and currency after trade
    new_resource1 = resource1 + amount
    new_currency1 = currency1 - price * amount
    new_resource2 = resource2 - amount
    new_currency2 = currency2 + price * amount
    
    # Calculate the utility for both agents after trade
    utility1_after = utility(new_resource1, new_currency1)
    utility2_after = utility(new_resource2, new_currency2)
    
    # Calculate the utility gain for both agents
    gain1 = utility1_after - utility(resource1, currency1)
    gain2 = utility2_after - utility(resource2, currency2)
    
    return gain1 * gain2  # Nash product


if __name__ == "__main__":
    from scipy.optimize import minimize_scalar

    
    price = 1
    agent_1 = {
        'resource': 2,
        'currency': 0
    }
    agent_2 = {
        'resource': 0,
        'currency': 2
    }
    # YOUR CODE GOES HERE
    def to_maximize(amount):
        return -total_utility_gain(agent_1['resource'], agent_1['currency'], agent_2['resource'], agent_2['currency'], price, amount)
    
    # Optimize trade amount for maximum utility gain
    res = minimize_scalar(to_maximize, bounds=(0, min(agent_1['resource'], agent_2['currency']/price)), method='bounded')
    
    if res.success:
        trade_amount = res.x
        print(f"Optimal trade amount: {trade_amount:.2f} units of resource")
    else:
        print("Optimization was not successful.")