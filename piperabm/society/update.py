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
        queue = self.agent_info(index, 'queue')
        # reduce idle energy expenditure
        for index in self.all_agents():
            if queue.is_done(start_date, end_date):
                pass

        duration = end_date - start_date
        for index in self.all_agents():
            resource = self.agent_info(index, 'resource')
            fuel_rate = self.agent_info(index, 'idle_fuel_rate')
            new_resource = resource - (fuel_rate * duration)
            self.set_agent_info(index, 'resource', new_resource)

        # calculate new position
        # reduce movement energy expenditure
        for index in self.all_agents():
            new_pos = None####
            self.set_agent_info(index, 'pos', new_pos)
        # mark agents who are ready for participating in trade
        for index in self.all_agents():
            queue = self.agent_info(index, 'queue')

            pos = queue.pos(end_date)
            self.set_agent_info(index, 'pos', pos)
            
            ready_for_trade = queue.is_done(end_date)
            if ready_for_trade:
                self.set_agent_info(index, 'ready_for_trade', ready_for_trade)
                queue.reset()

        # do the trade for each settlement

        # decide for new actions to be added to their queue
