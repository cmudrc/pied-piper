"""
Solves a single resource for multiple agents at fixed price
"""

import numpy as np
from scipy.optimize import minimize

from piperabm.economy.accessibility import accessibility


def solver(agents: list, price: float):
    """
    Solve the optimal trade between agents
    """
    num_agents = len(agents)
    initial_resources = np.array([agent['resource'] for agent in agents])
    enough_resources = np.array([agent['enough_resource'] for agent in agents])
    balances = np.array([agent['balance'] for agent in agents])

    def objective(resource_allocations):
        """
        Objective function to maximize the product of utility gains
        """
        utilities = np.array([accessibility(resource_allocations[i], enough_resources[i]) for i in range(num_agents)])
        return -np.prod(utilities)  # Minimize the negative for maximization

    def resource_conservation(resource_allocations):
        """
        Constraint: sum of final resources must be equal to sum of initial resources
        """
        return np.sum(resource_allocations) - np.sum(initial_resources)

    def balance_constraints(resource_allocations):
        """
        Constraint: ensure no agent spends more than they have
        """
        resource_changes = resource_allocations - initial_resources
        cost = resource_changes * price
        final_balances = balances - cost
        return final_balances

    # Constraints
    constraints = [
        {'type': 'eq', 'fun': resource_conservation},  # Resource conservation constraint
        {'type': 'ineq', 'fun': balance_constraints}   # Balance constraints for each agent
    ]

    # Bounds for each variable (resource allocation cannot be negative and should not exceed the agent's balance converted to resources)
    bounds = [(0, balances[i] / price + initial_resources[i]) for i in range(num_agents)]

    # Initial guess: start with initial resources
    initial_guess = initial_resources

    # Optimize
    result = minimize(objective, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

    # Prepare results
    if result.success:
        final_resources = result.x
        #final_utilities = [utility(final_resources[i], enough_resources[i]) for i in range(num_agents)]
        for i, agent in enumerate(agents):
            final_resource = final_resources[i]
            agent['balance'] += float((agent['resource'] - final_resource) * price)
            agent['resource'] = float(final_resource)
        status = 'success'
    else:
        status = 'failed'
    #print(status)
    result = agents
    return result


if __name__ == "__main__":
    price = 10
    agent_1 = {
        'id': 1,
        'resource': 19,
        'enough_resource': 10,
        'balance': 100,
    }
    agent_2 = {
        'id': 2,
        'resource': 8,
        'enough_resource': 10,
        'balance': 100,
    }
    agent_3 = {
        'id': 3,
        'resource': 3,
        'enough_resource': 10,
        'balance': 10,
    }
    agents = [agent_1, agent_2, agent_3]

    print("Solves a single resource for multiple agents at fixed price.")

    # Initial
    print(">>> Initial: ")
    for agent in agents:
        print(agent)

    # Solve
    agents = solver(agents, price)

    # Final
    print(">>> Final: ")
    for agent in agents:
        print(agent)
