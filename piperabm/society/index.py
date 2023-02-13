class Index:
    
    def __init__(self):
        self.index_list = []

    def find_next_index(self):
        """
        Check self.index_list (indexes) and suggest a new index
        """
        index_list = self.index_list
        if len(index_list) > 0:
            max_index = max(index_list)
            new_index = max_index + 1
        else:
            new_index = 0
        return new_index

    def agent_info(self, agent, property):
        index = self.find_agent(agent)
        node = self.G.nodes[index]
        return node[property]