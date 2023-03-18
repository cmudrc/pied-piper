class Search:
    """
    Contains methods for Society class
    Methods for searching for agent index
    """

    def _find_agent_index_by_name(self, name: str, report=True):
        result = None
        if len(name) > 0:
            for index in self.G.nodes():
                agent = self.G.nodes[index]['agent']
                if agent.name == name:
                    result = index
        if result is None and report is True:
            txt = name + ' not found.'
            print(txt)
        return result

    def _find_agent_index_by_index(self, index: int, report=True):
        """
        Find and return node index (Check if it exists)
        """
        result = None
        index_list = self.index_list
        if index in index_list:
            result = index
        if result is None and report is True:
            txt = 'node_index ' + str(index) + ' not found.'
            print(txt)
        return result

    def find_agent_index(self, input, report=False):
        """
        Find and return node index based on input (name, position, or index)
        """
        result = None
        if isinstance(input, str):
            result = self._find_agent_index_by_name(input, report=report)
        elif isinstance(input, int):
            result = self._find_agent_index_by_index(input, report=report)
        return result
    
    def find_agent(self, agent):
        result = None
        index = self.find_agent_index(agent)
        if index is not None:
            result = self.G.nodes[index]['agent']
        return result