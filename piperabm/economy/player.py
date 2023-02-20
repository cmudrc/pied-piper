class Player:

    def __init__(self, agent, source, demand, wallet):
        self.index = agent
        self.source = source
        self.demand = demand
        self.wallet = wallet

    def sell(self, volume, cost):
        self.source -= volume
        self.demand += volume
        self.wallet += cost

    def buy(self, volume, cost):
        self.source += volume
        self.demand -= volume
        self.wallet -= cost