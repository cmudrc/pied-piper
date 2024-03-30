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


def nash_product(params, agent_1, agent_2):
    amount, price = params
    # Calculate new resource and currency levels after trade
    new_resource1 = agent_1['resource'] + amount
    new_currency1 = agent_1['currency'] - amount * price
    new_resource2 = agent_2['resource'] - amount
    new_currency2 = agent_2['currency'] + amount * price
    
    # Utility gains
    gain1 = utility(new_resource1, new_currency1) - utility(agent_1['resource'], agent_1['currency'])
    gain2 = utility(new_resource2, new_currency2) - utility(agent_2['resource'], agent_2['currency'])
    
    # Nash product (negative for minimization)
    return -gain1 * gain2


if __name__ == "__main__":
    from scipy.optimize import minimize

    
    price = 1
    agent_1 = {
        'resource': 0.7,
        'currency': 1.5
    }
    agent_2 = {
        'resource': 1.5,
        'currency': 0.7
    }
    # YOUR CODE GOES HERE
    # Initial guesses for amount and price
    initial_guess = [(agent_1['resource'] + agent_2['resource']) / 2, price]  # 1 unit of resource, 1 unit of currency per resource
    
    # Bounds for amount and price (amount cannot be negative, price must be reasonable)
    bounds = [(0, min(agent_1['resource'], agent_2['currency'])), (0.01, 10)]
    
    # Perform the optimization
    res = minimize(nash_product, initial_guess, args=(agent_1, agent_2), bounds=bounds)
    
    if res.success:
        optimal_amount, optimal_price = res.x
        print(f"Optimal trade amount: {optimal_amount:.2f} units, Optimal price: {optimal_price:.2f} currency/unit")
    else:
        print("Optimization was not successful.")