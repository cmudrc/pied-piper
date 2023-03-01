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
        # reduce idle energy expenditure

        # calculate new position
        # reduce movement energy expenditure
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
