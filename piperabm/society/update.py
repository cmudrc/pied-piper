from piperabm.unit import Date
from piperabm.economy import Economy


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
            agent.is_alive()
            #if agent.alive is False:
            #    ''' log '''
                #msg = self.log.message__agent_died(agent)
                #print(msg)

        ''' calculate new position and reduce movement energy expenditure '''   
        agents_indexes = self.all_agents(type='active&alive')
        agents = self.get_agents(agents_indexes)
        for agent in agents:
            queue = agent.queue
            if queue.is_empty() is True:
                # decide
                path_graph = self.env.path_graph
                agent.observe(path_graph=path_graph, society=self)
                agent.decide_action(start_date, end_date)
            if queue.is_empty() is False:
                actions = queue.find_actions(type='move')
                move = actions[0]
                ## new resource
                fuel_consumption = move.how_much_fuel(start_date, end_date)
                new_resource, remaining = agent.resource - fuel_consumption
                agent.resource = new_resource
                ## new pos
                new_pos = move.pos(date=end_date)
                agent.pos = new_pos
                new_settlement = self.env.find_node(new_pos, report=False)
                if new_settlement is None:
                    agent.current_node = None
                else:
                    agent.current_node = new_settlement
                if new_resource.has_zero(): #####
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
            agents=participants,
            exchange=self.exchange
        )
        economy.solve()

        ## finalize
        agents_indexes = self.all_agents(type='active&alive')
        agents = self.get_agents(agents_indexes)
        for agent in agents:
            if agent.queue.done():
                agent.queue.reset()
