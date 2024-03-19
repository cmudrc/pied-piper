from piperabm.economy.trade.multi_solver import MultiSolver


class Solver:
    """
    Solve a trade between multiple agents for multiple resources in a fixed price
    """
    def __init__(self, prices, resource_names=None):
        self.prices = prices
        if resource_names is None:
            resource_names = list(self.prices.keys())
        self.resource_names = resource_names
        self.library = {}
        self.log = []

    def add(self, agent):
        """
        Add agent to solver
        """
        self.library[agent['id']] = agent

    @property
    def agents(self):
        """
        Return a list of agents
        """
        return list(self.library.keys())

    def solve_step(self):
        """
        Solve one step
        """
        possible_trades = {}
        for resource_name in self.resource_names:
            price = self.prices[resource_name]
            solver = MultiSolver(price)
            for id in self.agents:
                agent = self.library[id]
                solver.add(
                    id=id,
                    resource=agent['resources'][resource_name],
                    currency=agent['currency'],
                    critical=agent['critical'][resource_name],
                )
            transaction = solver.solve()
            possible_trades[resource_name] = transaction
        # Find transaction with highest value
        max_value = None
        max_resource_name = None
        for resource_name in possible_trades:
            amount = possible_trades[resource_name]['amount']
            price = possible_trades[resource_name]['price']
            value = amount * price
            if max_value is None or \
            value > max_value:
                max_value = value
                max_resource_name = resource_name
        transaction = {
            'resource': max_resource_name,
            'amount': possible_trades[max_resource_name]['amount'],
            'price': possible_trades[max_resource_name]['price'],
            'seller': possible_trades[max_resource_name]['seller'],
            'buyer': possible_trades[max_resource_name]['buyer']
        }
        return transaction

    def apply(self, transaction):
        """
        Apply a transaction to agents
        """
        # Update seller
        seller = self.library[transaction['seller']]
        seller['currency'] += transaction['amount']
        seller['resources'][transaction['resource']] -= transaction['amount'] / self.prices[transaction['resource']]
        # Update buyer
        buyer = self.library[transaction['buyer']]
        buyer['currency'] -= transaction['amount']
        buyer['resources'][transaction['resource']] += transaction['amount'] / self.prices[transaction['resource']]        

    def solve(self):
        """
        Solve until convergence
        """
        while True:
            transaction = self.solve_step()
            if transaction['amount'] == 0:
                break
            else:
                self.log.append(transaction)
                self.apply(transaction)
        return self.log


if __name__ == "__main__":
    solver = Solver(
        prices={
            'food': 1,
            'water': 1,
            'energy': 1,
        },
        #resource_names=['food']
        resource_names=None
    )
    agent_1 = {
        'id': 1,
        'resources': {
            'food': 8,
            'water': 3,
            'energy': 4,
        },
        'currency': 10,
        'critical': {
            'food': 2,
            'water': 4,
            'energy': 6,
        },
    }
    agent_2 = {
        'id': 2,
        'resources': {
            'food': 2,
            'water': 4,
            'energy': 6,
        },
        'currency': 10,
        'critical': {
            'food': 6,
            'water': 4,
            'energy': 2,
        },
    }
    agent_3 = {
        'id': 3,
        'resources': {
            'food': 2,
            'water': 9,
            'energy': 2,
        },
        'currency': 10,
        'critical': {
            'food': 6,
            'water': 4,
            'energy': 2,
        },
    }
    solver.add(agent_1)
    solver.add(agent_2)
    solver.add(agent_3)

    # Initial
    print(">>> Agents initial:")
    for id in solver.agents:
        agent = solver.library[id]
        print(agent)

    # Transations
    print(">>> Transations:")
    result = solver.solve()
    for transaction in result:
        print(transaction)

    # Final
    print(">>> Agents final:")
    for id in solver.agents:
        agent = solver.library[id]
        print(agent)