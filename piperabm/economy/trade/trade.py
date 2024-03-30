from piperabm.economy.trade.solver import Solver


class Trade:

    def __init__(self, model, agents, resource_names=None):
        self.model = model
        self.agents = agents
        self.resource_names = resource_names

    @property
    def prices(self):
        return self.model.exchange_rate.prices

    def run(self):
        solver = Solver(
            prices=self.prices,
            resource_names=self.resource_names
        )
        for id in self.agents:
            object = self.model.get(id)
            agent = {
                'id': object.id,
                'resources': object.resources.to_matters().amounts(),
                'currency': object.balance,
                ###############
                'critical': {
                    'food': 100,
                    'water': 100,
                    'energy': 100,
                },
            }
            solver.add(agent)
        transactions = solver.solve()
        self.apply(transactions)
        return transactions
    
    def apply(self, transactions):
        for transaction in transactions:
            resource_name = transaction['resource']
            amount = transaction['amount']
            value = amount * transaction['price']
            seller_id = transaction['seller']
            buyer_id = transaction['buyer']
            seller = self.model.get(seller_id)
            seller.balance += value
            resource = seller.resources.get(resource_name)
            resource - amount
            buyer = self.model.get(buyer_id)
            buyer.balance -= value
            resource = buyer.resources.get(resource_name)
            resource + amount


if __name__ == "__main__":

    from piperabm.model.samples import model_0 as model

    model.gini_index = 0.8
    model.generate_agents(num=20)
    agents = model.agents
    
    #total = 1
    #for id in agents:
        #object = model.get(id)
        #total *= object.balance
        #total *= object.resources.value(model.exchange_rate)
    #print(total)

    trade = Trade(model, agents)
    transactions = trade.run()
    print(len(transactions))

    #total = 1
    #for id in agents:
        #object = model.get(id)
        #total *= object.balance
        #total *= object.resources.value(model.exchange_rate)
    #print(total)