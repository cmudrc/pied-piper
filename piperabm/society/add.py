from piperabm.actions import Queue


class Add:
    
    def add(self, name='', settlement=None, queue=Queue(), asset=None):
        """
        Add a new agent to the society
        """
        index = self.find_next_index()
        self.index_list.append(index)
        if settlement is None:
            settlement_index = self.env.random_settlement()
        else:
            settlement_index = self.env.find_node(settlement)
        settlement_node = self.env.G.nodes[settlement_index]
        pos = settlement_node['boundary'].center
        self.G.add_node(
            index,
            name=name,
            settlement=settlement_index,
            pos=pos,
            active=True,
            queue=queue,
            asset=asset
            )

    def add_agents(self, n):
        for _ in range(n):
            self.add_agent()