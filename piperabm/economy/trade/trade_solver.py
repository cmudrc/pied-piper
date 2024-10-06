"""
Solves multi-resources for multiple players at fixed price
"""

from piperabm.economy.trade.nash_bargaining import NashBargaining as nb


class MultiResourceTrade:

    def resource_names(players: list):
        return players[0]['resources'].keys()

    def balance_allocations(players: list, prices: dict) -> list:
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
                if all_needs != 0:
                    balance_allocation[resource_name] = needs[resource_name] / all_needs
                else:
                    balance_allocation[resource_name] = 0
            result.append(balance_allocation)
        return result
    
    def prepare(players: list, balance_allocations: list, resource_name: str):
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
    '''
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
    '''

    def sorted_markets(players, prices):
        """
        Sorted name of markets based on their size
        """
        market_sizes = {}
        for resource_name in MultiResourceTrade.resource_names(players):
            market_sizes[resource_name] = 0
        for player in players:
            resources = player['resources']
            for resource_name in resources:
                market_sizes[resource_name] += resources[resource_name]
        for resource_name in market_sizes:
            market_sizes[resource_name] *= prices[resource_name]
        return sorted(market_sizes, key=market_sizes.get, reverse=True)
    
    def transactions(players: list, prices: dict) -> dict:
        """
        Calculate the proper transactions
        """
        markets = MultiResourceTrade.sorted_markets(players=players, prices=prices)
        all_transactions = {}
        for market in markets:
            balance_allocations = MultiResourceTrade.balance_allocations(players=players, prices=prices)
            market_players = MultiResourceTrade.prepare(
                players=players,
                balance_allocations=balance_allocations,
                resource_name=market
            )
            transactions = nb.transactions(players=market_players, price=prices[market])
            all_transactions[market] = transactions
        return all_transactions
    
    def apply(players, transactions) -> list:
        """
        Apply transactions to players
        """
        num_players = len(players)
        resource_names = MultiResourceTrade.resource_names(players=players)
        for resource_name in resource_names:
            resource_transactions = transactions[resource_name]
            for i in range(num_players):
                players[i]['balance'] = players[i]['balance'] + resource_transactions['money'][i]
                players[i]['resources'][resource_name] = players[i]['resources'][resource_name] + resource_transactions['resource'][i]
        return players

    def solve(players: list, prices: dict) -> list:
        """
        Solve until convergence
        """
        i = 0
        #max_itteration = 1
        max_itteration = len(players) ** 2
        while i < max_itteration:
            transactions = MultiResourceTrade.transactions(players=players, prices=prices)
            #print(transactions)
            if MultiResourceTrade.check_empty(transactions) is True:
                break
            else:
                players = MultiResourceTrade.apply(players=players, transactions=transactions)
            i += 1
        '''
        transactions = MultiResourceTrade.transactions(players=players, prices=prices)
        players = MultiResourceTrade.apply(players=players, transactions=transactions)
        '''
        return players

    def check_empty(transactions: dict) -> bool:
        result = None
        threashold = 0
        transfers = 0
        for resource_name in transactions:
            transfers += sum(transactions[resource_name]['money'])
        if transfers <= threashold:
            result = True
        else:
            result = False
        return result


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
    players = MultiResourceTrade.solve(players=players, prices=prices)

    # Final
    print("\n" + ">>> " + "Final: ")
    for player in players:
        print(player['resources'], ', balance:', player['balance'])