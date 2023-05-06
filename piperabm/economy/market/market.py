try: from .player import Player
except: from player import Player
try: from .solver import Solver
except: from solver import Solver
try: from .log import Log
except: from log import Log


class Market(Solver):

    def __init__(self, exchange):
        self.players = []
        self.exchange = exchange
        self.log = Log(prefix='MARKET', indentation_depth=2)
        super().__init__()

    def add(self, players):
        """
        Add new player to the market
        """
        if not isinstance(players, list):
            players = [players]
        for player in players:
            self.players.append(player)

    def find_player(self, index):
        """
        Return player based on index
        """
        result = None
        for player in self.players:
            if player.index == index:
                result = player
                break
        return result

    def size(self):
        """
        Calculate the market total value in units of currency
        """
        size = 0
        for resource in self.all_resources():
            total_demand = self.total_actual_demand(resource)
            total_demand_value = total_demand * self.exchange.rate(resource, 'wealth')
            total_source = self.total_source(resource)
            total_source_value = total_source * self.exchange.rate(resource, 'wealth')
            size += total_source_value + total_demand_value
        return size

    def total_demand(self, resource_name=None):
        """
        Calculate overall demand
        """
        result = None
        if resource_name is not None:
            demand_list = []
            for player in self.players:
                demand = player.new_demand[resource_name]
                demand_list.append(demand)
            result = sum(demand_list)
        return result
    
    def total_actual_demand(self, resource_name=None):
        """
        Calculate overall demand when not possible to have more than budget
        """
        result = None
        if resource_name is not None:
            demand_list = []
            for player in self.players:
                demand = player.actual_demand(self.exchange)[resource_name]
                demand_list.append(demand)
            result = sum(demand_list)
        return result

    def total_source(self, resource_name=None):
        """
        Calculate overall source
        """
        result = None
        if resource_name is not None:
            source_list = []
            for player in self.players:
                source = player.new_source[resource_name]
                source_list.append(source)
            result = sum(source_list)
        return result

    def all_resources(self):
        """
        Return all resource names
        """
        result = []
        for player in self.players:
            for name in player.new_source:
                if name not in result: result.append(name)
            for name in player.new_demand:
                if name not in result: result.append(name)
        return result
                
    def __str__(self):
        txt = ''
        for player in self.players:
            txt += player.__str__() + '\n'
        return txt


if __name__ == "__main__":
    from piperabm.economy.exchange.sample import exchange_0 as exchange

    p1 = Player(
        index=1,
        source={'food': 8, 'water': 9, 'energy': 5},
        demand={'food': 6, 'water': 5, 'energy': 3},
        wallet=100
    )
    p2 = Player(
        index=2,
        source={'food': 8, 'water': 10, 'energy': 8},
        demand={'food': 8, 'water': 5, 'energy': 1},
        wallet=200
        )
    p3 = Player(
        index=3,
        source={'food': 5, 'water': 5, 'energy': 2},
        demand={'food': 5, 'water': 5, 'energy': 7},
        wallet=200
        )

    market = Market(exchange)
    market.add([p1, p2, p3])
    market.solve()
    print(market.stat['size'])
