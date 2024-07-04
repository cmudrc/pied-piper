import numpy as np
from scipy.optimize import minimize

from piperabm.economy.utility import utility


def solve(agents, prices):
    def initial_utilities(agents, prices):
        return [sum(utility(agents[i]['resources'][res], agents[i]['enough_resources'][res], prices[res], agents[i]['balance']) for res in prices) for i in range(len(agents))]

    initial_utils = initial_utilities(agents, prices)

    def total_utility(variables):
        price_food, price_water, price_energy = variables[:3]
        trade_food_1_2, trade_food_1_3, trade_water_1_2, trade_water_1_3, trade_energy_1_2, trade_energy_1_3 = variables[3:]
        new_prices = {'food': price_food, 'water': price_water, 'energy': price_energy}
        
        trades = {
            'food': [trade_food_1_2, trade_food_1_3],
            'water': [trade_water_1_2, trade_water_1_3],
            'energy': [trade_energy_1_2, trade_energy_1_3]
        }
        
        new_resources = []
        for i, agent in enumerate(agents):
            new_agent_resources = agent['resources'].copy()
            if i == 0:  # Agent 1
                new_agent_resources['food'] += trade_food_1_2 + trade_food_1_3
                new_agent_resources['water'] += trade_water_1_2 + trade_water_1_3
                new_agent_resources['energy'] += trade_energy_1_2 + trade_energy_1_3
            elif i == 1:  # Agent 2
                new_agent_resources['food'] -= trade_food_1_2
                new_agent_resources['water'] -= trade_water_1_2
                new_agent_resources['energy'] -= trade_energy_1_2
            elif i == 2:  # Agent 3
                new_agent_resources['food'] -= trade_food_1_3
                new_agent_resources['water'] -= trade_water_1_3
                new_agent_resources['energy'] -= trade_energy_1_3
            new_resources.append(new_agent_resources)
        
        total_utils = []
        for i, agent in enumerate(agents):
            total_util = sum(
                utility(new_resources[i][res], agent['enough_resources'][res], new_prices[res], agent['balance'])
                for res in new_prices
            )
            total_utils.append(total_util)
        return -np.prod([total_utils[i] - initial_utils[i] for i in range(len(agents))])

    initial_guess = [prices['food'], prices['water'], prices['energy'], 0, 0, 0, 0, 0, 0]
    bounds = [(1, 20), (1, 20), (1, 20), -10, 10, -10, 10, -10, 10, -10, 10, -10, 10]  # Assumed bounds for prices and trade amounts

    result = minimize(total_utility, initial_guess, bounds=bounds)

    optimal_values = result.x
    optimal_prices = optimal_values[:3]
    optimal_trades = optimal_values[3:]

    print(f"Optimal Prices: Food: {optimal_prices[0]}, Water: {optimal_prices[1]}, Energy: {optimal_prices[2]}")
    print(f"Optimal Trades:")
    print(f"  Food: Agent 1 -> Agent 2: {optimal_trades[0]}")
    print(f"  Food: Agent 1 -> Agent 3: {optimal_trades[1]}")
    print(f"  Water: Agent 1 -> Agent 2: {optimal_trades[2]}")
    print(f"  Water: Agent 1 -> Agent 3: {optimal_trades[3]}")
    print(f"  Energy: Agent 1 -> Agent 2: {optimal_trades[4]}")
    print(f"  Energy: Agent 1 -> Agent 3: {optimal_trades[5]}")


if __name__ == "__main__":
    prices = {
        'food': 10,
        'water': 12,
        'energy': 8
    }

    agents = [
        {
            'id': 1,
            'resources': {'food': 9, 'water': 2, 'energy': 3},
            'enough_resources': {'food': 10, 'water': 12, 'energy': 8},
            'balance': 100,
        },
        {
            'id': 2,
            'resources': {'food': 12, 'water': 3, 'energy': 10},
            'enough_resources': {'food': 10, 'water': 12, 'energy': 8},
            'balance': 100,
        },
        {
            'id': 3,
            'resources': {'food': 3, 'water': 10, 'energy': 7},
            'enough_resources': {'food': 10, 'water': 12, 'energy': 8},
            'balance': 10,
        }
    ]

    result = solve(agents, prices)
    #print(result)
