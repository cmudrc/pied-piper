class Update:

    def update_elements(self, start_date, end_date):
        """
        Update all elements
        """
        self._update_all_agents(start_date, end_date)

    def _update_all_agents(self, start_date, end_date):
        """
        Update all agents
            start_date: starting date of the time duration
            end_date: ending date of the time duration
        """
        for index in self.all_agents():
            queue = self.agent_info(index, 'queue')
            result, action_type = queue.execute(end_date)
            if action_type == "pos":
                pass
                #node['pos'] = result