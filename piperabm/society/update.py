from piperabm.unit import Date


class Update:

    def update_elements(self, start_date: Date, end_date: Date):
        """
        Update all elements
        """
        self._update_all_agents(start_date, end_date)

    def _update_all_agents(self, start_date: Date, end_date: Date):
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
            ## action is done
            current_action.done = True
            if new_resource.has_zero():
                self.set_agent_info(index, 'active', False) ## dead

        ## mark agents who are ready for participating in trade
        for index in self.all_agents():
            queue = self.agent_info(index, 'queue')
            
            
            ready_for_trade = queue.is_done(end_date)
            if ready_for_trade:
                self.set_agent_info(index, 'ready_for_trade', ready_for_trade)
                queue.reset()
        ## do the trade for each settlement

        ## finalize
        for index in self.all_agents(type='active'):
            if queue.done():
                queue.reset()