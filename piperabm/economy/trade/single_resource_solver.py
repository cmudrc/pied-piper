"""
Solves a single resource for multiple players at fixed price
"""

import numpy as np
from scipy.optimize import minimize

from piperabm.economy.accessibility import accessibility


def solver(players: list, price: float):
    """
    Solve the optimal trade between players
    """
    num_players = len(players)
    initial_resources = np.array([player['resource'] for player in players])
    enough_resources = np.array([player['enough_resource'] for player in players])
    balances = np.array([player['balance'] for player in players])

    def objective(resource_allocations):
        """
        Objective function to maximize the product of utility gains
        """
        utilities = np.array([accessibility(resource_allocations[i], enough_resources[i]) for i in range(num_players)])
        return -np.prod(utilities)  # Minimize the negative for maximization

    def resource_conservation(resource_allocations):
        """
        Constraint: sum of final resources must be equal to sum of initial resources
        """
        return np.sum(resource_allocations) - np.sum(initial_resources)

    def balance_constraints(resource_allocations):
        """
        Constraint: ensure no player spends more than they have
        """
        resource_changes = resource_allocations - initial_resources
        cost = resource_changes * price
        final_balances = balances - cost
        return final_balances

    # Constraints
    constraints = [
        {'type': 'eq', 'fun': resource_conservation},  # Resource conservation constraint
        {'type': 'ineq', 'fun': balance_constraints}   # Balance constraints for each player
    ]

    # Bounds for each variable (resource allocation cannot be negative and should not exceed the player's balance converted to resources)
    bounds = [(0, balances[i] / price + initial_resources[i]) for i in range(num_players)]

    # Initial guess: start with initial resources
    initial_guess = initial_resources

    # Optimize
    result = minimize(objective, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

    # Prepare results
    if result.success:
        final_resources = result.x
        #final_utilities = [utility(final_resources[i], enough_resources[i]) for i in range(num_players)]
        for i, player in enumerate(players):
            final_resource = final_resources[i]
            player['balance'] += float((player['resource'] - final_resource) * price)
            player['resource'] = float(final_resource)
        status = 'success'
    else:
        status = 'failed'
    #print(status)
    result = players
    return result


if __name__ == "__main__":
    price = 10
    player_1 = {
        'id': 1,
        'resource': 19,
        'enough_resource': 10,
        'balance': 100,
    }
    player_2 = {
        'id': 2,
        'resource': 8,
        'enough_resource': 10,
        'balance': 100,
    }
    player_3 = {
        'id': 3,
        'resource': 3,
        'enough_resource': 10,
        'balance': 10,
    }
    players = [player_1, player_2, player_3]

    print("Solves a single resource for multiple players at fixed price.")

    # Initial
    print(">>> Initial: ")
    for player in players:
        print(player)

    # Solve
    players = solver(players, price)

    # Final
    print(">>> Final: ")
    for player in players:
        print(player)
