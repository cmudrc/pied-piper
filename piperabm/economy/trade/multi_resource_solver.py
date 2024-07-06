"""
Solves multi-resources for multiple players at fixed price
"""

from piperabm.economy.trade.single_resource_solver import solver as single_resource_solver


def solver(players, prices):
    """
    Solve the optimal trade between players
    """

    def extract(players, resource_name):
        """
        Extract the player info
        """
        result = []
        for player in players:
            new = {}
            new['id'] = player['id']
            new['resource'] = player['resources'][resource_name]
            new['enough_resource'] = player['enough_resources'][resource_name]
            new['balance'] = player['balance']
            result.append(new)
        return result
    
    def update(players, result, resource_name):
        """
        Update the player info
        """
        for i, player in enumerate(players):
            player['resources'][resource_name] = result[i]['resource']
            player['balance'] = result[i]['balance']
        return players
    
    # Sort market for the resources based on size
    market_sizes = {
        'food': 0,
        'water': 0,
        'energy': 0
    }
    for player in players:
        resources = player['resources']
        for resource_name in resources:
            market_sizes[resource_name] += resources[resource_name]
    for resource_name in market_sizes:
        market_sizes[resource_name] *= prices[resource_name]
    markets = sorted(market_sizes, key=market_sizes.get, reverse=True)
    #print(markets)
    for resource_name in markets:
        result = single_resource_solver(players=extract(players, resource_name), price=prices[resource_name])
        #print(result)
        players = update(players, result, resource_name)
    return players


if __name__ == "__main__":
    prices = {
        'food': 10,
        'water': 12,
        'energy': 8
    }
    player_1 = {
        'id': 1,
        'type': 'agent',
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
    player_2 = {
        'id': 2,
        'type': 'agent',
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
    player_3 = {
        'id': 3,
        'type': 'agent',
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
    players = [player_1, player_2, player_3]

    print("Solves multi-resources for multiple players at fixed price.")

    # Initial
    print(">>> Initial: ")
    for player in players:
        print(player['resources'], ', balance:', player['balance'])

    # Solve
    players = solver(players, prices)

    # Final
    print(">>> Final: ")
    for player in players:
        print(player['resources'], ', balance:', player['balance'])