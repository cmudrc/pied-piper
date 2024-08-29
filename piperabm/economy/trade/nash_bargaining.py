"""
Solves a single resource for multiple players at fixed price
"""

from scipy.optimize import minimize
import warnings

from piperabm.economy.accessibility import accessibility


warnings.filterwarnings('ignore', message="Values in x were outside bounds during a minimize step, clipping to bounds")


class NashBargaining:

    def transactions(players: list, price: float) -> dict:
        """
        Calculate the list of transfers for proper resource allocation
        """
        num_players = len(players)

        if num_players == 0:
            return {
                'resource': [],
                'money': []
            }
        
        def objective(resource_transafers):
            """
            Optimization objective function
            """
            accessibilities = [
                accessibility(
                    players[i]['resource'] + resource_transafers[i],
                    players[i]['enough_resource']
                )
                for i in range(num_players)
            ]
            result = 1
            for a in accessibilities:
                result *= a
            return -result
        
        initial_guess = []
        bounds = []
        for i in range(num_players):
            need = max(0, players[i]['enough_resource'] - players[i]['resource'])
            possible = players[i]['balance'] / price
            upper_bound = min(need, possible)
            lower_bound = -players[i]['resource']
            bound = (lower_bound, upper_bound)
            bounds.append(bound)
            initial_guess.append((upper_bound + lower_bound) / 2)
        constraints = [
            {'type': 'eq', 'fun': lambda resource_transafers: sum(resource_transafers)},
        ]
        result = minimize(
            objective,
            initial_guess,
            bounds=bounds,
            constraints=constraints,
        )
        resource_transfers = [float(resource_transfer) for resource_transfer in result.x]
        money_transfers = [float(-resource_transfer * price) for resource_transfer in resource_transfers]
        return {
            'resource': resource_transfers,
            'money': money_transfers
        }
    
    def apply(players: list, transactions: dict) -> list:
        """
        Apply transfers to players
        """
        num_players = len(players)
        for i in range(num_players):
            players[i]['balance'] = players[i]['balance'] + transactions['money'][i]
            players[i]['resource'] = players[i]['resource'] + transactions['resource'][i]
        return players


if __name__ == "__main__":
    price = 10
    player_1 = {
        'id': 1,
        'type': 'agent',
        'resource': 9,
        'enough_resource': 10,
        'balance': 100,
    }
    player_2 = {
        'id': 2,
        'type': 'agent',
        'resource': 6,
        'enough_resource': 10,
        'balance': 100,
    }
    player_3 = {
        'id': 3,
        'type': 'agent',
        'resource': 3,
        'enough_resource': 10,
        'balance': 10,
    }
    players = [player_1, player_2, player_3]

    # Initial
    print("\n" + ">>> " + "Initial: ")
    for player in players:
        print(player)

    # Solve
    transactions = NashBargaining.transactions(players, price)
    players = NashBargaining.apply(players, transactions)

    # Final
    print("\n" + ">>> " + "Final: ")
    for player in players:
        print(player)
