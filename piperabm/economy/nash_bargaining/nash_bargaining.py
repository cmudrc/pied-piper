from scipy.optimize import minimize
import numpy as np

# Initial endowments and prices
agent_1 = {
    'resources': {'food': 10, 'water': 15, 'energy': 20},
    'cash': 100
}
agent_2 = {
    'resources': {'food': 5, 'water': 5, 'energy': 5},
    'cash': 100
}
prices = {'food': 1, 'water': 1, 'energy': 2}

# Utility function
def utility(agent):
    return agent['resources']['food'] * agent['resources']['water'] * agent['resources']['energy']

# Nash product to maximize
def nash_product(x):
    # Update resources after trade
    final_agent_1_resources = {key: agent_1['resources'][key] + x[i] for i, key in enumerate(prices)}
    final_agent_2_resources = {key: agent_2['resources'][key] - x[i] for i, key in enumerate(prices)}
    
    # Update cash after trade
    cost = sum(prices[key] * x[i] for i, key in enumerate(prices))
    final_agent_1_cash = agent_1['cash'] - cost
    final_agent_2_cash = agent_2['cash'] + cost

    return -(utility({'resources': final_agent_1_resources, 'cash': final_agent_1_cash}) *
             utility({'resources': final_agent_2_resources, 'cash': final_agent_2_cash}))

# Constraints: Non-negative final quantities and non-negative cash
constraints = [{'type': 'ineq', 'fun': lambda x, key=key: agent_1['resources'][key] + x[i]}
               for i, key in enumerate(prices)] + \
              [{'type': 'ineq', 'fun': lambda x, key=key: agent_2['resources'][key] - x[i]}
               for i, key in enumerate(prices)] + \
              [{'type': 'ineq', 'fun': lambda x: agent_1['cash'] - sum(prices[key] * x[i] for i, key in enumerate(prices))},
               {'type': 'ineq', 'fun': lambda x: agent_2['cash'] + sum(prices[key] * x[i] for i, key in enumerate(prices))}]

# Initial guess (no trade)
x0 = np.zeros(len(prices))

# Find the Nash bargaining solution
result = minimize(nash_product, x0, constraints=constraints)

if result.success:
    trade_quantities = result.x
    print("Equilibrium trade quantities (food, water, energy):", trade_quantities)
else:
    print("No solution found")
