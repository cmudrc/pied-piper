from scipy.optimize import minimize
from copy import deepcopy


def trade(agent_1, agent_2, resource_name, price):

    def extract_info(agent):
        return {
            'index': agent.index,
            'resource': agent.resources(resource_name),
            'resource_max': agent.resources.max(resource_name),
            'cash': agent.balance,
        }
    
    # Calculate utilities
    def utility(agent, resource_name, final_resource):
        """ Calculate utility of agent """
        agent_copy = deepcopy(agent)
        resource = agent_copy.resources.get(resource_name)
        resource.amount = final_resource
        return agent_copy.utility(resource_name)

    def nash_product(x):
        """ Nash product to maximize """
        # Update resources and cash after trade
        final_resource_agent_1 = a_1['resource'] + x
        final_resource_agent_2 = a_2['resource'] - x
        #final_cash_agent_1 = agent_1['cash'] - price * x
        #final_cash_agent_2 = agent_2['cash'] + price * x
        
        utility_agent_1 = utility(agent_1, resource_name, final_resource_agent_1)
        utility_agent_2 = utility(agent_2, resource_name, final_resource_agent_2)

        # Nash product (negative for minimization)
        return -(utility_agent_1 * utility_agent_2)


    trade_quantity = None

    a_1 = extract_info(agent_1)
    a_2 = extract_info(agent_2)

    # Constraints: Non-negative final quantities, non-negative cash, and not exceeding maximum capacities
    constraints = [
        {'type': 'ineq', 'fun': lambda x: a_1['resource'] + x},  # Agent 1's final resource >= 0
        {'type': 'ineq', 'fun': lambda x: a_2['resource'] - x},  # Agent 2's final resource >= 0
        {'type': 'ineq', 'fun': lambda x: a_1['cash'] - price * x},  # Agent 1's final cash >= 0
        {'type': 'ineq', 'fun': lambda x: a_2['cash'] + price * x},  # Agent 2's final cash >= 0
        {'type': 'ineq', 'fun': lambda x: a_1['resource_max'] - (a_1['resource'] + x)},  # Agent 1's final resource <= max
        {'type': 'ineq', 'fun': lambda x: a_2['resource_max'] - (a_2['resource'] - x)}  # Agent 2's final resource <= max
    ]

    # Initial guess (no trade)
    x0 = [0]

    # Find the Nash bargaining solution
    result = minimize(nash_product, x0, constraints=constraints)

    if result.success:
        trade_quantity = result.x[0]
        #print("Equilibrium trade quantity:", trade_quantity)
    else:
        pass
        #print("No solution found")
    return trade_quantity


if __name__ == '__main__':
    from piperabm.society.agent.samples import agent_0, agent_1

    trade_quantity = trade(agent_0, agent_1, 'energy', price=1)
    print(trade_quantity)