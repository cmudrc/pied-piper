from piperabm.BASEMENT.array_arg_minmax import array_argmax


class Trade:

    def __init__(
        self,
        players: list,
        model = None
    ):
        self.model = model  # binding 
        self.players = players
        self.resource_names = ["food", "water", "energy"]
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

    def best_transaction(self):
        """
        Find the best suitable transaction for each step
        """
        transactions = {}
        for name in self.resource_names:
            transactions[name] = None
            
        # Load all players sources and demands
        players_sources = []
        players_sources_values = []
        players_demands = []
        players_demands_values = []
        for player in self.players:
            sources = self.agent_sources(player)
            players_sources.append(sources)
            sources_values = sources.value(self.exchange_rate)
            players_sources_values.append(sources_values)
            demands = self.agent_demands(player)
            players_demands.append(demands)
            demands_values = demands.value(self.exchange_rate)
            players_demands_values.append(demands_values)

        def total_resources(all_resources):
            result = {
                "food": 0,
                "water": 0,
                "energy": 0,
            }
            for resources in all_resources:
                for resource_name in result:
                    result[resource_name] += resources(resource_name)
            return result

        total_sources = total_resources(players_sources_values)
        total_demands = total_resources(players_demands_values)
        #print(total_sources, total_demands)

        # Create possible transactions
        for name in self.resource_names:
            resource_transactions = []
            for i in range(len(self.players)):
                row = []
                sources = players_sources[i]
                source = sources(name)
                source_value = source * self.exchange_rate(name, 'currency')
                for j in range(len(self.players)):
                    if i == j:  # One cannot trade with themself
                        transaction_value = 0
                    else:
                        demands = players_demands[j]
                        demand = demands(name)
                        demand_value = demand * self.exchange_rate(name, 'currency')
                        transaction_value = source_value * demand_value
                    row.append(transaction_value)
                resource_transactions.append(row)
            transactions[name] = resource_transactions
        
        # Select the best transaction
        argmax_index = {}
        argmax_value = {}
        for key in transactions:
            argmax_index[key] = array_argmax(transactions[key])
            argmax_value[key] = transactions[key][argmax_index[key][0]][argmax_index[key][1]]
        max_key = max(argmax_value, key=argmax_value.get)
        best_transaction = argmax_index[max_key]

        # Calculate best transaction info
        sources = players_sources[best_transaction[0]]
        source = sources(max_key)
        seller_index = self.players[best_transaction[0]]
        demands = players_demands[best_transaction[1]]
        demand = demands(max_key)
        buyer_index = self.players[best_transaction[1]]
        amount = min(source, demand)
        value = amount * self.exchange_rate(max_key, 'currency')
        transaction = {
            "buyer": buyer_index,
            "seller": seller_index,
            "resource": max_key,
            "amount": amount,
            "value": value,
        }
        return transaction

    def run_step(self):
        """
        Solve the market for one step
        """
        transaction = self.best_transaction()

        # Update seller
        agent = self.get(transaction["seller"])
        resource = agent.resources.get(transaction["resource"])
        remainder = resource.sub(transaction["amount"])
        if remainder.amount != 0:  # Transaction failed
            raise ValueError
        agent.balance += transaction["value"]

        # Update buyer
        agent = self.get(transaction["buyer"])
        resource = agent.resources.get(transaction["resource"])
        remainder = resource.add(transaction["amount"])
        if remainder.amount != 0:  # Transaction failed
            raise ValueError
        agent.balance -= transaction["value"]

        # Log
        self.history.append(transaction)

    def solve(self):
        """
        Solve market
        """
        count = (len(self.players) ** 2) * len(self.resource_names)
        for _ in range(count):
            self.run_step()


if __name__ == "__main__":
    from piperabm.model.samples import model_3
    
    players = model_3.all_alive_agents
    trade = Trade(players, model_3)
    trade.solve()

    for entry in trade.history:
        print(entry)
