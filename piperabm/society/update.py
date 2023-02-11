class Update:

    def update_elements(self, start_date, end_date):
        """
        Update all elements
        """
        self._update_all_nodes(start_date, end_date)

    def _update_all_nodes(self, start_date, end_date):
        """
        Update all agents
            start_date: starting date of the time duration
            end_date: ending date of the time duration
        """
        for index in self.G.nodes():
            node = self.G.nodes[index]
            queue = node['queue']
            result, action_type = queue.execute(end_date)
            if action_type == "pos":
                node['pos'] = result