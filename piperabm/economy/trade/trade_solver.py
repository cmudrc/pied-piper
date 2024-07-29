"""
Solves multi-resources for multiple players at fixed price
"""

from piperabm.economy.trade.nash_bargaining import NashBargaining as nb


class MultiResourceTrade:

    def resource_names(players: list):
        return players[0]['resources'].keys()

    def balance_allocations(players: list):
        # Balance allocation
        resource_names = MultiResourceTrade.resource_names(players=players)
        result = []
        for player in players:
            balance_allocation = {}
            needs = {}
            for resource_name in resource_names:
                need = max(0, (player['enough_resources'][resource_name] - player['resources'][resource_name]) * prices[resource_name])
                needs[resource_name] = need
            all_needs = sum(needs.values())
            for resource_name in resource_names:
                balance_allocation[resource_name] = needs[resource_name] / all_needs
            result.append(balance_allocation)
        return result
    
    def prepare(players, balance_allocations, resource_name):
        """
        Extract the player info
        """
        result = []
        for i, player in enumerate(players):
            new = {}
            new['id'] = player['id']
            new['resource'] = player['resources'][resource_name]
            new['enough_resource'] = player['enough_resources'][resource_name]
            new['balance'] = player['balance'] * balance_allocations[i][resource_name]
            result.append(new)
        return result
    
    def transactions(players: list, prices: dict):
        balance_allocations = MultiResourceTrade.balance_allocations(players)
        resource_names = MultiResourceTrade.resource_names(players=players)
        all_transactions = {}
        for resource_name in resource_names:
            market_players = MultiResourceTrade.prepare(
                players=players,
                balance_allocations=balance_allocations,
                resource_name=resource_name
            )
            transactions = nb.transactions(players=market_players, price=prices[resource_name])
            all_transactions[resource_name] = transactions
            #players = nb.apply(players, transactions)
        return all_transactions
    
    def apply(players, transactions):
        num_players = len(players)
        resource_names = MultiResourceTrade.resource_names(players=players)
        for resource_name in resource_names:
            resource_transactions = transactions[resource_name]
            for i in range(num_players):
                players[i]['balance'] = players[i]['balance'] + resource_transactions['money'][i]
                players[i]['resources'][resource_name] = players[i]['resources'][resource_name] + resource_transactions['resource'][i]
        return players


if __name__ == "__main__":
    prices = {
        'food': 10,
        'water': 10,
        'energy': 10
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
            'water': 10,
            'energy': 10
        },
        'balance': 100,
    }
    player_2 = {
        'id': 2,
        'type': 'agent',
        'resources': {
            'food': 10,
            'water': 3,
            'energy': 10
        },
        'enough_resources': {
            'food': 10,
            'water': 10,
            'energy': 10
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
            'water': 10,
            'energy': 10
        },
        'balance': 10,
    }
    players = [player_1, player_2, player_3]

    print("Solves multi-resources for multiple players at fixed price.")

    # Initial
    print("\n" + ">>> " + "Initial: ")
    for player in players:
        print(player['resources'], ', balance:', player['balance'])

    # Solve
    transactions = MultiResourceTrade.transactions(players=players, prices=prices)
    players = MultiResourceTrade.apply(players=players, transactions=transactions)

    # Final
    print("\n" + ">>> " + "Final: ")
    for player in players:
        print(player['resources'], ', balance:', player['balance'])