try: from .market import Market, Player
except: from market import Market, Player


class Economy:

    def __init__(self, agents: list, exchange):
        self.agents = agents
        self.exchange = exchange

    def all_nodes(self):
        """
        Return all current and origin nodes of agents
        """
        result = []
        for agent in self.agents:
            if agent.current_node not in result:
                result.append(agent.current_node)
            if agent.origin_node not in result:
                result.append(agent.origin_node)
        return result
    
    def find_agent(self, index):
        """
        Find agent based on its index
        """
        result = None
        for agent in self.agents:
            if agent.index == index:
                result = agent
                break
        return result
    
    def create_markets(self):
        """
        Create markets between agents
        """
        markets = {} # {market_index: market instance}
        all_nodes = self.all_nodes()
        for index in all_nodes:
            market = Market(self.exchange)
            players_list = []
            for agent in self.agents:
                if agent.current_node == index or agent.origin_node == index:
                    resource = agent.resource
                    source = resource.source()
                    demand = resource.demand()
                    wallet = agent.balance
                    player = Player(
                        index=agent.index,
                        source=source.current_resource,
                        demand=demand.current_resource,
                        wallet=wallet
                    )
                    players_list.append(player)
            market.add(players_list)
            markets[index] = market
        return markets
    
    def sort_markets(self, markets):
        """
        Sort markets based on their sizes
        """
        market_sizes = {} # {market_index: market_size}
        for key in markets:
            market = markets[key]
            market_sizes[key] = market.size()
        #print(market_sizes)
        sorted_markets = sorted(market_sizes.items(), key=lambda x:x[1], reverse=True)
        sorted_markets = list(list(zip(*sorted_markets))[0])
        return sorted_markets

    def biggest_market(self):
        markets = self.create_markets()
        sorted_markets = self.sort_markets(markets)
        biggest_market = markets[sorted_markets[0]]
        return biggest_market

    def solve_biggest_market(self):
        """
        Solve and update the biggest market
        """
        biggest_market = self.biggest_market()
        stat = biggest_market.solve()
        #print(stat)
        self.update_agents(biggest_market)
        return stat

    def solve(self):
        """
        Solve until stagnation
        """
        for _ in range(5):
            stat = self.solve_biggest_market()

    def update_agents(self, biggest_market):
        """
        Update agents info based on the final result of the solution
        """
        for player in biggest_market.players:
            delta_source, delta_demand, delta_wallet = player.to_delta()
            index = player.index
            agent = self.find_agent(index)
            new_resource, remaining = agent.resource - delta_source
            agent.resource = new_resource
            new_resource, remaining = agent.resource + delta_demand
            agent.resource = new_resource
            new_balance = agent.balance - delta_wallet
            agent.balance = new_balance
        '''
        for market_index in markets:
            market = markets[market_index]
            for player in market.players:
                delta_source, delta_demand, delta_wallet = player.to_delta()
                index = player.index
                agent = self.find_agent(index)
                new_resource, remaining = agent.resource - delta_source
                agent.resource = new_resource
                new_balance = agent.balance - delta_wallet
                agent.balance = new_balance
        '''

    def __str__(self):
        txt = ''
        for agent in self.agents:
            txt += str(agent) + ': '
            txt += str(agent.resource) + '\n'
        return txt


if __name__ == "__main__":
    from piperabm.society.agent.sample import agent_0, agent_1
    from piperabm.economy.exchange.sample import exchange_0 as exchange

    agents = [agent_0, agent_1]
    eco = Economy(agents, exchange)
    #print(eco.all_nodes())
    #markets = eco.create_markets()
    #sorted_markets = eco.sort_markets(markets)
    #print(sorted_markets)
    eco.solve()
    print(eco)

