from copy import deepcopy

try:
    from .player import Player
except:
    from player import Player
try:
    from .exchange import Exchange
except:
    from exchange import Exchange


class Economy:

    def __init__(self, exchange):
        self.players = []
        self.exchange = exchange

    def add(self, players):
        if not isinstance(players, list):
            players = [players]
        for player in players:
            self.players.append(player)

    def find_player(self, index):
        for player in self.players:
            if player.index == index:
                return player

    def total_demand(self, resource=None):
        result = None
        if resource is None:
            pass
        else:
            ls = []
            for player in self.players:
                demand = player.demand[resource]
                ls.append(demand)
            result = sum(ls)
        return result

    def total_source(self, resource=None):
        ls = []
        for player in self.players:
            source = player.source[resource]
            ls.append(source)
        result = sum(ls)
        return result

    def all_resources(self):
        result = []
        for player in self.players:
            for name in player.source:
                if name not in result: result.append(name)
            for name in player.demand:
                if name not in result: result.append(name)
        return result

    def solve(self):
        """
        Solve the resource allocation problem for the pool of players
        """
        for player in self.players:

            for resource in self.all_resources():

                t_s = self.total_source(resource)
                t_d = self.total_demand(resource)
                diff = t_s - t_d

                player_source = player.source[resource]
                player_new_source = (player_source / t_s) * abs(diff)
                player.new_source[resource] = player_new_source

                player_demand = player.demand[resource]
                player_demand_max = player.wallet / self.exchange.rate(resource, 'wealth')
                if player_demand > player_demand_max:
                    player_demand = player_demand_max
                player_new_demand = (player_demand / t_d) * abs(diff)
                player.new_demand[resource] = player_new_demand
                
                delta_source = player_source - player_new_source
                player_new_wallet = player.wallet + (delta_source * self.exchange.rate(resource, 'wealth'))
                delta_demand = player_demand - player_new_demand
                player_new_wallet = player_new_wallet - (delta_demand * self.exchange.rate(resource, 'wealth'))
                player.new_wallet = player_new_wallet

    def __str__(self):
        txt = ''
        for player in self.players:
            txt += player.__str__() + '\n'
        return txt


if __name__ == "__main__":

    p1 = Player(
        1,
        source={
            'food': 4,
            'water': 5,
        },
        demand={
            'food': 6,
            'water': 5,
        },
        wallet=10
    )
    p2 = Player(
        2,
        source={
            'food': 2,
            'water': 5,
        },
        demand={
            'food': 8,
            'water': 5,
        },
        wallet=20
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
        wallet=20
        )

    exchange = Exchange()
    exchange.add('food', 'wealth', 10)
    exchange.add('water', 'wealth', 2)

    econ = Economy(exchange)
    econ.add([p1, p2, p3])
    econ.solve()

    for player in econ.players:
        print(player)