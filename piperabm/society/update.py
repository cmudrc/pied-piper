from piperabm.unit import Date
from piperabm.economy import Economy
from piperabm.actions import Trade, Move, Walk

try: from .decision import Decision
except: from decision import Decision


class Update:
    """
    Contains methods for Society class
    Methods for updating agents in each step
    """

    def update_elements(self, start_date: Date, end_date: Date):
        """
        Update all agents between *start_date* and *end_date*
        """

        ''' reduce idle energy expenditure '''
        agents_indexes = self.all_agents(type='active&alive')
        agents = self.get_agents(agents_indexes)
        duration = end_date - start_date
        for agent in agents:
            agent.idle_time_pass(duration)
        for index in self.all_agents(type='alive'): ###### index or agent
            agent = self.find_agent(index)
            agent.idle_time_pass(duration)
            if agent.alive is False:
                ''' log '''
                #msg = self.log.message__agent_died(agent)
                #print(msg)

        ''' calculate new position and reduce movement energy expenditure '''   
        agents_indexes = self.all_agents(type='active&alive')
        agents = self.get_agents(agents_indexes)
        for agent in agents:
            queue = agent.queue
            if queue.is_empty() is True:
                agent.decide() ##########
                # decide
                path_graph = self.env.to_path_graph(start_date, end_date)
                decision = Decision(
                    path_graph=path_graph,
                    society=self,
                    agent=agent.index
                )
                route = decision.select_best_route()
                if route is not None:
                    path = path_graph.edge_info(*route, 'path')
                    move = Move(
                        start_date=start_date,
                        path=path,
                        transportation=Walk()
                    )
                    queue.add(move)
                    trade = Trade(start_date=start_date)
                    queue.add(trade)
                    ''' log '''
                    msg = self.log.message__agent_decided(
                        route=route,
                        agent_index=index,
                        agent_name=self.agent_info(index, 'name'),
                        agent_pos=self.agent_info(index, 'pos')
                    )
                    #print(msg)
            if queue.is_empty() is False:
                actions = queue.find_actions(type='move')
                move = actions[0]
                ## new resource
                fuel_consumption = move.how_much_fuel(start_date, end_date)
                resource = self.agent_info(index, 'resource')
                new_resource, remaining = resource - fuel_consumption
                self.set_agent_info(index, 'resource', new_resource)
                ## new pos
                new_pos = move.pos(date=end_date)
                self.set_agent_info(index, 'pos', new_pos)
                new_settlement = self.env.find_node(new_pos)
                if new_settlement is not None:
                    self.set_agent_info(index, 'settlement', new_settlement)
                if new_resource.has_zero():
                    self.set_agent_info(index, 'active', False) ## dead

        ## mark agents who are ready for participating in trade
        participants = [] # active and alive
        for index in self.all_agents():
            queue = self.agent_info(index, 'queue')
            if queue.is_empty() is False:
                actions = queue.find_actions('trade')
                trade = actions[0]
                if trade.done is False:
                    participants.append(index)

        ## do the trade for all settlements
        economy = Economy(
            agents=agents,
            exchange=self.exchange
        )

        ## finalize
        for index in self.all_agents(type='active'):
            if queue.done():
                queue.reset()


        '''
        markets = {} # {market_index: market instance}
        for index in self.env.all_nodes('settlement'):
            market = Market(self.exchange)
            player_index_list = self.all_agents_from(index, participants)
            players_list = []
            for player_index in player_index_list:
                resource = self.agent_info(player_index, 'resource')
                source = resource.source()
                demand = resource.demand()
                wallet = self.agent_info(player_index, 'wealth')
                player = Player(
                    agent=player_index,
                    source=source.current_resource,
                    demand=demand.current_resource,
                    wallet=wallet
                )
                players_list.append(player)
            market.add(players_list)
            markets[index] = market
        
        ## sort markets based on their size
        market_sizes = {} # {market_index: market_sze}
        for key in markets:
            market = markets[key]
            market_sizes[key] = market.size()
        sorted_markets = sorted(market_sizes.items(), key=lambda x:x[1], reverse=True)
        sorted_markets = list(list(zip(*sorted_markets))[0])
        
        ## solve markets
        for key in sorted_markets:
            markets[key].solve()

        ## update agent properties
        for key in markets:
            for player in markets[key].players:
                delta_source, delta_demand, delta_wallet = player.to_delta()
                index = player.index
                resource = self.agent_info(index, 'resource')
                new_resource, remaining = resource - delta_source
                self.set_agent_info(index, 'resource', new_resource)
                wealth = self.agent_info(index, 'wealth')
                new_wealth = wealth - delta_wallet
                self.set_agent_info(index, 'wealth', new_wealth)
        '''