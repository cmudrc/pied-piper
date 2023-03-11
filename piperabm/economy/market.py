try: from .player import Player
except: from player import Player
try: from .exchange import Exchange
except: from exchange import Exchange
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
        if not isinstance(players, list):
            players = [players]
        for player in players:
            self.players.append(player)

    def find_player(self, index):
        for player in self.players:
            if player.index == index:
                return player

    def size(self):
        """
        Calculate the market total value
        """
        result = 0
        for player in self.players:
            pass
        return result

    def total_demand(self, resource=None):
        result = None
        if resource is None:
            pass
        else:
            ls = []
            for player in self.players:
                demand = player.new_demand[resource]
                ls.append(demand)
            result = sum(ls)
        return result
    
    def total_actual_demand(self, resource_name=None):
        result = None
        if resource_name is None:
            pass
        else:
            demand_list = []
            for player in self.players:
                demand = player.actual_demand(self.exchange)[resource_name]
                demand_list.append(demand)
            result = sum(demand_list)
        return result

    def total_source(self, resource_name=None):
        result = None
        if resource_name is None:
            pass
        else:
            source_list = []
            for player in self.players:
                source = player.new_source[resource_name]
                source_list.append(source)
            result = sum(source_list)
        return result

    def all_resources(self):
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

    p1 = Player(
        1,
        source={
            'food': 8,
            'water': 9,
        },
        demand={
            'food': 6,
            'water': 5,
        },
        wallet=100
    )
    p2 = Player(
        2,
        source={
            'food': 8,
            'water': 10,
        },
        demand={
            'food': 8,
            'water': 5,
        },
        wallet=200
        )
    p3 = Player(
        3,
        source={
            'food': 5,
            'water': 5,
        },
        demand={
            'food': 5,
            'water': 5,
        },
        wallet=200
        )

    exchange = Exchange()
    exchange.add('food', 'wealth', 10)
    exchange.add('water', 'wealth', 2)

    mk = Market(exchange)
    mk.add([p1, p2, p3])
    mk.solve()
    print(mk)

    #for player in econ.players:
    #    print(player)