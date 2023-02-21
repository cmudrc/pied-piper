from copy import deepcopy

try:
    from .pool import Pool, Bid
except:
    from pool import Pool, Bid
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

    def size(self):
        """
        Calculate the economy total value
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
                demand = player.demand[resource]
                ls.append(demand)
            result = sum(ls)
        return result
    
    def total_actual_demand(self, resource=None):
        result = None
        if resource is None:
            pass
        else:
            ls = []
            for player in self.players:
                demand = player.actual_demand(self.exchange)[resource]
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
        pools = {}
        for resource in self.all_resources():
            p = Pool()
            for player in self.players:
                t_s = self.total_source(resource)
                #t_d = self.total_demand(resource)
                t_d_a = self.total_actual_demand(resource)
                player_source = player.source[resource]
                player_actual_demand = player.actual_demand(self.exchange)
                player_demand = player_actual_demand[resource]
                others_source = t_s - player_source
                others_demand = t_d_a - player_demand
                seller_score = others_demand * player_source
                buyer_score = others_source * player_demand
                if seller_score >= buyer_score:
                    #mode = 'seller'
                    bid = Bid(agent=player.index, amount=player_source)
                    p.add_source(bid)
                else:
                    #mode = 'buyer'
                    bid = Bid(agent=player.index, amount=player_demand)
                    p.add_demand(bid)
            pools[resource] = p
        pools_score = {}
        for resource_name in pools:
            pool = pools[resource_name]
            size_source, size_demand = pool.size()
            pools_score[resource_name] = size_source + size_demand
            sorted_pools = sorted(pools_score)
        for pool in sorted_pools:
            pools[pool].solve()
            print(pool)
            print(pools[pool])


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
            'water': 5,
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

    econ = Economy(exchange)
    econ.add([p1, p2, p3])
    econ.solve()
    #print(econ)

    #for player in econ.players:
    #    print(player)