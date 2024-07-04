"""
Solves multi-resources for multiple agents at fixed price
"""

from piperabm.economy.trade.single_resource_solver import solver as single_resource_solver


def solver(agents, prices):
    """
    Solve the optimal trade between agents
    """

    def extract(agents, resource_name):
        """
        Extract the agent info
        """
        result = []
        for agent in agents:
            new = {}
            new['id'] = agent['id']
            new['resource'] = agent['resources'][resource_name]
            new['enough_resource'] = agent['enough_resources'][resource_name]
            new['balance'] = agent['balance']
            result.append(new)
        return result
    
    def update(agents, result, resource_name):
        """
        Update the agent info
        """
        for i, agent in enumerate(agents):
            agent['resources'][resource_name] = result[i]['resource']
            agent['balance'] = result[i]['balance']
        return agents
    
    # Sort market for the resources based on size
    market_sizes = {
        'food': 0,
        'water': 0,
        'energy': 0
    }
    for agent in agents:
        resources = agent['resources']
        for resource_name in resources:
            market_sizes[resource_name] += resources[resource_name]
    for resource_name in market_sizes:
        market_sizes[resource_name] *= prices[resource_name]
    markets = sorted(market_sizes, key=market_sizes.get, reverse=True)
    #print(markets)
    for resource_name in markets:
        result = single_resource_solver(agents=extract(agents, resource_name), price=prices[resource_name])
        #print(result)
        agents = update(agents, result, resource_name)
    return agents


if __name__ == "__main__":
    prices = {
        'food': 10,
        'water': 12,
        'energy': 8
    }
    agent_1 = {
        'id': 1,
        'resources': {
            'food': 9,
            'water': 2,
            'energy': 3
        },
        'enough_resources': {
            'food': 10,
            'water': 12,
            'energy': 8
        },
        'balance': 100,
    }
    agent_2 = {
        'id': 2,
        'resources': {
            'food': 12,
            'water': 3,
            'energy': 10
        },
        'enough_resources': {
            'food': 10,
            'water': 12,
            'energy': 8
        },
        'balance': 100,
    }
    agent_3 = {
        'id': 3,
        'resources': {
            'food': 3,
            'water': 10,
            'energy': 7
        },
        'enough_resources': {
            'food': 10,
            'water': 12,
            'energy': 8
        },
        'balance': 10,
    }
    agents = [agent_1, agent_2, agent_3]

    print("Solves multi-resources for multiple agents at fixed price.")

    # Initial
    print(">>> Initial: ")
    for agent in agents:
        print(agent['resources'], ', balance:', agent['balance'])

    # Solve
    agents = solver(agents, prices)

    # Final
    print(">>> Final: ")
    for agent in agents:
        print(agent['resources'], ', balance:', agent['balance'])