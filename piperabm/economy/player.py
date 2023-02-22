from copy import deepcopy


class Player:

    def __init__(self, agent, source, demand, wallet):
        self.index = agent
        self.source = source
        self.demand = demand
        self.wallet = wallet
        # will be calculated:
        self.new_source = deepcopy(source)
        self.new_demand = deepcopy(demand)
        self.new_wallet = deepcopy(wallet)

    '''
    def sell(self, resource, volume, cost):
        self.new_source[resource] -= volume
        self.new_demand[resource] += volume
        self.new_wallet += cost

    def buy(self, resource, volume, cost):
        self.new_source[resource] += volume
        self.new_demand[resource] -= volume
        self.new_wallet -= cost
    '''
    def delta(self):
        result = {}
        delta_source = {}
        for name in self.source:
            delta_source[name] = self.new_source[name] - self.source[name]
        result["source"] = delta_source
        delta_demand = {}
        for name in self.demand:
            delta_demand[name] = self.new_demand[name] - self.demand[name]
        result["demand"] = delta_demand
        delta_wallet = {}
        delta_wallet = self.new_wallet - self.wallet
        result["wallet"] = delta_wallet
        return result

    def actual_demand(self, exchange_rate):
        """
        When the agent does not have enough money, they can't have a demand more than a certain point
        """
        player_demand = deepcopy(self.new_demand)
        for name in self.demand:
            player_demand_max = self.wallet / exchange_rate.rate(name, 'wealth')
            if player_demand[name] > player_demand_max:
                player_demand[name] = player_demand_max
        return player_demand

    def value(self, exchange_rate):
        result = self.wallet
        #result += value(self.current, exchange_rate)
        return result

    def new_value(self, exchange_rate):
        result = self.wallet
        #result += value(self.new_current, exchange_rate)
        return result

    def __str__(self):
        txt_info = ">>> index: " + str(self.index)
        txt_start = "## start: "
        txt_start += str({
            "source": self.source,
            "demand": self.demand,
            "wallet": self.wallet
        })
        txt_end = "## end: "
        txt_end += str({
            "source": self.new_source,
            "demand": self.new_demand,
            "wallet": self.new_wallet
        })
        return txt_info + '\n' + txt_start + '\n' + txt_end