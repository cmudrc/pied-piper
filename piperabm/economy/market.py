from copy import deepcopy

from piperabm.log import Log

try: from .pool import Pool, Bid
except: from pool import Pool, Bid
try: from .player import Player
except: from player import Player
try: from .exchange import Exchange
except: from exchange import Exchange
try: from .log import Log
except: from .log import Log


class Market:

    def __init__(self, exchange):
        self.players = []
        self.exchange = exchange
        self.log = Log()

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
                demand = player.new_demand[resource]
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
            source = player.new_source[resource]
            ls.append(source)
        result = sum(ls)
        return result

    def all_resources(self):
        result = []
        for player in self.players:
            for name in player.new_source:
                if name not in result: result.append(name)
            for name in player.new_demand:
                if name not in result: result.append(name)
        return result

    def solve(self):
        """
        Solve the resource allocation problem for the pool of players
        """
        def create_pools():
            """
            Create a dictionary in form of {resource: Pool()} of current state
            """
            pools = {}
            for resource in self.all_resources():
                p = Pool()
                for player in self.players:
                    t_s = self.total_source(resource)
                    #t_d = self.total_demand(resource)
                    t_d_a = self.total_actual_demand(resource)
                    player_source = player.new_source[resource]
                    player_actual_demand = player.actual_demand(self.exchange)
                    player_demand = player_actual_demand[resource]
                    others_source = t_s - player_source
                    others_demand = t_d_a - player_demand
                    seller_score = others_demand * player_source
                    buyer_score = others_source * player_demand
                    if seller_score >= buyer_score:
                        mode = 'seller'
                        bid = Bid(agent=player.index, amount=player_source)
                        p.add_source(bid)
                    else:
                        mode = 'buyer'
                        bid = Bid(agent=player.index, amount=player_demand)
                        p.add_demand(bid)
                    txt = 'agent ' + str(player.index) + ' is a ' + mode
                    self.log.add(txt)
                pools[resource] = p
            return pools

        def sort_pools(pools):
            pools_score = {}
            result = None
            for resource_name in pools:
                pool = pools[resource_name]
                size_source, size_demand = pool.size()
                pools_score[resource_name] = size_source + size_demand
                sorted_pools = sorted(pools_score.items(), key=lambda x:x[1], reverse=True)
                sorted_pools = list(list(zip(*sorted_pools))[0])
                result = sorted_pools
            #print(pools_score)
            return result
        
        def solve_single(pools, resource):
            p = pools[resource]
            p.solve()
            #print(p)
            for player in self.players:
                bid, bid_type = p.find_bid(player.index)
                delta_wallet = bid.delta_wallet(self.exchange.rate(resource, 'wealth'))
                if bid_type == 'source':
                    #mode = 'sold'
                    delta_wallet = -delta_wallet
                    player.new_source[resource] = bid.new_amount
                else:
                    #mode = 'baught'
                    player.new_demand[resource] = bid.new_amount
                player.new_wallet = player.new_wallet + delta_wallet
                #print(player.index, player.new_source[resource], player.new_demand[resource])

        #for resource in sorted_pools:
        #    solve_single(pools, resource)
        #for i in range(len(self.all_resources())):
        #    pass
        
        def check_stagnation(previous_pools, current_pools):
            result = True
            for resource_name in previous_pools:
                if previous_pools[resource_name] != current_pools[resource_name]:
                    result = False
            print(result)
            return result

        def solve_step():
            pools = create_pools()
            #print(len(pools))
            sorted_pools = sort_pools(pools)
            if sorted_pools is not None:
                resource = sorted_pools[0]
                solve_single(pools, resource)
            return pools

        #previous_pools = solve_step()
        #current_pools = solve_step()
        solve_step()
        solve_step()
        solve_step()
        #while not check_stagnation(previous_pools, current_pools):
        #    previous_pools = deepcopy(current_pools)
        #    current_pools = solve_step()
        
        
        

                


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