try: from .market import Market, Player
except: from market import Market, Player


class Economy:

    def __init__(self, agents: list, exchange):
        self.agents = agents
        self.exchange = exchange
        self.markets = None

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
    
    def size(self):
        if self.markets is None:
            self.create_markets()
        size = 0
        for market_index in self.markets:
            size += self.markets[market_index].size()
        return size
    
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
        self.markets = markets
    
    def sort_markets(self):
        """
        Sort markets based on their sizes
        """
        market_sizes = {} # {market_index: market_size}
        markets = self.markets
        for key in markets:
            market = markets[key]
            market_sizes[key] = market.size()
        #print(market_sizes)
        sorted_markets = sorted(market_sizes.items(), key=lambda x:x[1], reverse=True)
        sorted_markets = list(list(zip(*sorted_markets))[0])
        return sorted_markets

    def biggest_market(self):
        sorted_markets = self.sort_markets()
        biggest_market = self.markets[sorted_markets[0]]
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
        stat = []
        size = self.size()
        delta = None
        while delta is None or delta != 0:
            market_stat = self.solve_biggest_market()
            stat.append(market_stat)
            new_size = self.size()
            delta = new_size - size
            size = new_size
        return stat
        #for _ in range(5):
        #    self.create_markets()
        #    stat = self.solve_biggest_market()

    def update_agents(self, market):
        """
        Update agents info based on the final result of the solution
        """
        for player in market.players:
            delta_source, delta_demand, delta_wallet = player.to_delta()
            index = player.index
            agent = self.find_agent(index)
            new_resource, remaining = agent.resource - delta_source
            agent.resource = new_resource
            new_resource, remaining = agent.resource + delta_demand
            agent.resource = new_resource
            new_balance = agent.balance - delta_wallet
            agent.balance = new_balance

    def __str__(self):
        txt = ''
        for agent in self.agents:
            txt += str(agent) + ': '
            txt += str(agent.resource) + ' '
            txt += str(agent.balance) + '\n'
        return txt


if __name__ == "__main__":
    from piperabm.society.agent.sample import agent_0, agent_1
    from piperabm.economy.exchange.sample import exchange_0 as exchange

    agent_1.current_node = agent_0.current_node # 0
    agents = [agent_0, agent_1]
    eco = Economy(agents, exchange)
    #print(eco.all_nodes())
    #markets = eco.create_markets()
    #sorted_markets = eco.sort_markets(markets)
    #print(sorted_markets)
    stat = eco.solve()
    print(stat)
    print(eco)

