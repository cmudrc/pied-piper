try: from .pool import Pool, Bid
except: from pool import Pool, Bid


class NewSolver:

    def solve(self):
        while True:
            self.solve

    def create_pools(self):

        def create_bid(player, resource_name):
            t_s = self.total_source(resource_name)
            #t_d = self.total_demand(resource)
            t_d_a = self.total_actual_demand(resource_name)
            player_source = player.new_source[resource_name]
            player_actual_demand = player.actual_demand(self.exchange)
            player_demand = player_actual_demand[resource_name]
            others_source = t_s - player_source
            others_demand = t_d_a - player_demand
            seller_score = others_demand * player_source
            buyer_score = others_source * player_demand
            if seller_score >= buyer_score:
                bid = Bid(agent=player.index, amount=player_source)
                type = 'source'
            else:
                bid = Bid(agent=player.index, amount=player_demand)
                type = 'demand'
            return bid, type
        
        pools = {}
        for resource_name in self.all_resources():
            pool = Pool()
            for player in self.players:
                bid, type = create_bid(player, resource_name)
                if type == 'source':
                    pool.add_source(bid)
                elif type == 'demand':
                    pool.add_demand(bid)
            pools[resource_name] = pool
        return pools
    
    def sort_pools(self, pools):
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
    
    def solve_biggest(self, pools):
        pools = self.create_pools()
        #print(len(pools))
        sorted_pools = self.sort_pools(pools)
        if sorted_pools is not None:
            resource = sorted_pools[0] # biggest pool
            self.solve_single(pools, resource) ######
        return pools




class Solver:

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
                        bid = Bid(agent=player.index, amount=player_source)
                        p.add_source(bid)
                    else:
                        bid = Bid(agent=player.index, amount=player_demand)
                        p.add_demand(bid)
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
            pool = pools[resource]
            sellers, buyers = pool.all_participants()
            ''' log '''
            stat = {
                'sellers': sellers,
                'buyers': buyers
            }
            msg = self.log.message__pool_started(resource, stat)
            #print(msg)
            stat = pool.solve()
            #print(pool)
            for player in self.players:
                bid, bid_type = pool.find_bid(player.index)
                delta_wallet = bid.delta_wallet(self.exchange.rate(resource, 'wealth'))
                if bid_type == 'source':
                    delta_wallet = -delta_wallet
                    player.new_source[resource] = bid.new_amount
                else:
                    player.new_demand[resource] = bid.new_amount
                player.new_wallet = player.new_wallet + delta_wallet
                #print(player.index, player.new_source[resource], player.new_demand[resource])
            ''' log '''
            msg = self.log.message__pool_complete(resource, stat)
            #print(msg)

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

        stat = {}
        return stat