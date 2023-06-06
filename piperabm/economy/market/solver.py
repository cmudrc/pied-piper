from piperabm.economy.market.pool import Pool, Bid


class Solver:
    """
    Solve the resource allocation problem for the pool of players
    """
    def __init__(self):
        self.pools = {}
        self.stat = {
            'food': {
                'transactions': [],
                'total_volume': 0,
            },
            'water': {
                'transactions': [],
                'total_volume': 0,
            },
            'energy': {
                'transactions': [],
                'total_volume': 0,
            },
            'size': []
        }

    def solve(self):
        #self.solve_biggest_pool()
        stat = []
        size = self.size()
        delta = None
        while delta is None or delta != 0:
            #print(size)
            pool_stat = self.solve_biggest_pool()
            stat.append(pool_stat)
            new_size = self.size()
            delta = new_size - size
            size = new_size
        return stat

    def score(self, player, resource_name):
        """
        Calculate the score which will used for deciding between being a seller or a buyer
        """
        player_source, player_demand, others_source, others_demand = \
            self.extract_resource_info(player, resource_name)
        seller_score = others_demand * player_source
        buyer_score = others_source * player_demand
        return buyer_score, seller_score
    
    def extract_resource_info(self, player, resource_name):
        """
        Extract player and other players source and demand info
        """
        t_s = self.total_source(resource_name)
        #t_d = self.total_demand(resource)
        t_d_a = self.total_actual_demand(resource_name)
        player_source = player.new_source[resource_name]
        player_actual_demand = player.actual_demand(self.exchange)
        player_demand = player_actual_demand[resource_name]
        others_source = t_s - player_source
        others_demand = t_d_a - player_demand
        return player_source, player_demand, others_source, others_demand

    def create_bid(self, player, resource_name):
        """
        Create a *player* bid for a certain *resource*
        """
        buyer_score, seller_score = self.score(player, resource_name)
        if seller_score >= buyer_score:
            amount = player.new_source[resource_name]
            bid = Bid(agent=player.index, amount=amount)
            type = 'source'
        else:
            amount = player.actual_demand(self.exchange)[resource_name]
            bid = Bid(agent=player.index, amount=amount)
            type = 'demand'
        #print(player.index, bid, type)
        return bid, type

    def create_pool(self, resource_name):
        """
        Create pool for a certain *resource*
        """
        pool = Pool()
        for player in self.players:
            bid, type = self.create_bid(player, resource_name)
            if type == 'source':
                pool.add_source(bid)
            elif type == 'demand':
                pool.add_demand(bid)
        return pool

    def create_pools(self):
        """
        Create all possible pools
        """
        pools = {}
        for resource_name in self.all_resources():
            pool = self.create_pool(resource_name)
            pools[resource_name] = pool
        self.pools = pools
    
    def sort_pools(self):
        """
        Sort pools based on their sizes
        """
        pools_score = {}
        result = []
        pools = self.pools
        for resource_name in pools:
            pool = pools[resource_name]
            size_source, size_demand = pool.size()
            score = size_source * size_demand
            pools_score[resource_name] = score
            sorted_pools = sorted(pools_score.items(), key=lambda x:x[1], reverse=True)
            sorted_pools = list(list(zip(*sorted_pools))[0])
            result = sorted_pools
        #print(pools_score)
        return result
    
    def biggest_pool(self):
        """
        Return biggest pool
        """
        resource_name = None
        self.create_pools()
        sorted_pools = self.sort_pools()
        if len(sorted_pools) > 0:
            resource_name = sorted_pools[0]
        return resource_name

    def solve_biggest_pool(self):
        """
        Solve the biggest pool
        """
        stat = {}
        resource_name = self.biggest_pool()
        stat = self.solve_pool(resource_name)
        return stat

    def update_players(self, resource_name, pool):
        for player in self.players:
            bid, bid_type = pool.find_bid(player.index)
            delta_amount, delta_wallet = bid.to_delta(self.exchange.rate(resource_name, 'wealth'))
            #delta_wallet = bid.delta_wallet(self.exchange.rate(resource_name, 'wealth'))
            if bid_type == 'source':
                player.new_source[resource_name] += delta_amount
                #player.new_demand[resource_name] -= bid.delta_amount()
                player.new_wallet -= delta_wallet
            else:
                player.new_demand[resource_name] += delta_amount
                #player.new_source[resource_name] -= bid.delta_amount()
                player.new_wallet += delta_wallet

    def solve_pool(self, resource_name):
        if resource_name is not None:
            pool = self.pools[resource_name]
            """
            sellers, buyers = pool.all_participants()
            ''' log '''
            stat = {
                'sellers': sellers,
                'buyers': buyers
            }
            msg = self.log.message__pool_started(resource_name, stat)
            #print(msg)
            """
            pool_stat = pool.solve()
            #print(resource_name, pool)
            ''' update self.stat '''
            if len(self.stat['size']) == 0:
                self.stat['size'].append(self.size())
            new_transactions = pool_stat['transactions']
            for new_transaction in new_transactions:
                self.stat[resource_name]['transactions'].append(new_transaction)
            self.stat[resource_name]['total_volume'] += pool_stat['total_volume']
            ''' update players '''
            self.update_players(resource_name, pool)
            self.stat['size'].append(self.size())
            # log 
            #msg = self.log.message__pool_complete(resource_name, stat)
            #print(msg)
        return self.stat