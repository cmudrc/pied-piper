from copy import deepcopy

#from piperabm.resources.resource import Resource


class Market:

    def __init__(
        self,
        players: list,
        model = None
    ):
        self.model = model  # binding 
        self.players = players
        self.history = []
    
    def get(self, index):
        """
        Get object from model based on its index
        """
        return self.model.get(index)

    def resources(self, index):
        """
        Return resources object of an agent based on agent"s index
        """
        agent = self.get(index)
        return agent.resources
    
    def balance(self, index):
        """
        Return *balance* of an agent based on agent"s index
        """
        agent = self.get(index)
        return agent.balance
    
    @property
    def exchange_rate(self):
        """
        Return exchange_rate from model
        """
        return self.model.exchange_rate
    
    def agent_demands(self, index):
        """
        Return actual demand of an agent based on its index
        """
        resources = self.resources(index)
        demands = resources.demands_actual(
            exchange_rate=self.exchange_rate,
            balance=self.balance(index)
        )
        return demands
        
    def agent_sources(self, index):
        """
        Return source of an agent based on its index
        """
        resources = self.resources(index)
        return resources.source

    def find_biggest_source(self, buyer_index, resource_name):
        players = deepcopy(self.players)
        players.remove(buyer_index)
        seller_index = None
        selling_amount = None
        biggest_resource_value = None  # used for comparison (in terms of money)
        if buyer_index is not None and \
        resource_name is not None:
            for index in players:
                sources = self.agent_sources(index)
                values = sources.value(self.exchange_rate)
                value = values(resource_name)
                if biggest_resource_value is None or \
                value > biggest_resource_value:
                    biggest_resource_value = value
                    seller_index = index
                    selling_amount = sources(resource_name)
        return seller_index, selling_amount
    
    def find_biggest_demand(self):
        buyer_index = None
        biggest_resource_name = None
        buying_amount = None
        biggest_resource_value = None  # used for comparison (in terms of money)
        for index in self.players:
            demands = self.agent_demands(index)
            values = demands.value(self.exchange_rate)
            resource_name = values.biggest
            value = values(resource_name)
            if biggest_resource_value is None or \
            value > biggest_resource_value:
                biggest_resource_value = value  # biggest in terms of money
                buyer_index = index
                biggest_resource_name = resource_name
                buying_amount = demands(biggest_resource_name)
        return buyer_index, biggest_resource_name, buying_amount

    def run_step(self):
        """
        Solve the market for one step
        """
        # biggest demand actual
        buyer_index, biggest_resource_name, buying_amount = self.find_biggest_demand()
        # biggest corresponding source
        seller_index, selling_amount = self.find_biggest_source(buyer_index, biggest_resource_name)
        # transaction
        transaction_amount = min(buying_amount, selling_amount)
        transaction_value = transaction_amount * self.exchange_rate(biggest_resource_name, "wealth")
        # update seller
        agent = self.get(seller_index)
        resource = agent.resources.get(biggest_resource_name)
        remainder = resource.sub(transaction_amount)
        if remainder.amount != 0:  # transaction failed
            raise ValueError
        agent.balance += transaction_value
        # update buyer
        agent = self.get(buyer_index)
        resource = agent.resources.get(biggest_resource_name)
        remainder = resource.add(transaction_amount)
        if remainder.amount != 0:  # transaction failed
            raise ValueError
        agent.balance -= transaction_value
        log = {
            "buyer": buyer_index,
            "seller": seller_index,
            "resource": biggest_resource_name,
            "amount": transaction_amount,
            "value": transaction_value
        }
        self.history.append(log)

    def solve(self):
        count = len(self.players)
        for _ in range(count ** 2):
            self.run_step()


if __name__ == "__main__":
    from piperabm.model.samples import model_3
    
    players = model_3.all_alive_agents
    market = Market(players, model_3)
    market.solve()
    print(market.history)
    