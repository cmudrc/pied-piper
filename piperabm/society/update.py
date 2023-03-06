from piperabm.unit import Date
from piperabm.economy import Market, Player


class Update:

    def update_elements(self, start_date: Date, end_date: Date):
        """
        Update all agents
            start_date: starting date of the time duration
            end_date: ending date of the time duration
        """            
        ## reduce idle energy expenditure
        duration = end_date - start_date
        for index in self.all_agents(type='active'):
            resource = self.agent_info(index, 'resource')
            idle_fuel_rate = self.agent_info(index, 'idle_fuel_rate')
            new_resource, remaining = resource - (idle_fuel_rate * duration)
            self.set_agent_info(index, 'resource', new_resource)
            if new_resource.has_zero():
                self.set_agent_info(index, 'active', False) ## dead
        ## calculate new position
        ## reduce movement energy expenditure     
        for index in self.all_agents(type='active'):
            queue = self.agent_info(index, 'queue')
            if queue.is_empty() is True:
                # decide
                pass
            current_action = queue.current_action()
            ## new resource
            fuel_consumption = current_action.how_much_fuel(start_date, end_date)
            resource = self.agent_info(index, 'resource')
            new_resource, remaining = resource - fuel_consumption
            self.set_agent_info(index, 'resource', new_resource)
            ## new pos
            new_pos = current_action.pos(start_date, end_date)
            self.set_agent_info(index, 'pos', new_pos)
            if new_resource.has_zero():
                self.set_agent_info(index, 'active', False) ## dead

        ## mark agents who are ready for participating in trade
        participants = []
        for index in self.all_agents():
            queue = self.agent_info(index, 'queue')
            trade = queue.find_actions('trade')
            if trade.done is False:
                participants.append(index)

        ## do the trade for each settlement
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
                player = Player(player_index, source, demand, wallet)
                players_list.append(player)
            market.add(players_list)
            markets[index] = market
        

        ## finalize
        for index in self.all_agents(type='active'):
            if queue.done():
                queue.reset()