class Search:
    """
    Contains methods for Environment class
    """

    def _find_node_by_name(self, name: str, report=True):
        """
        Find and return settlement node index by its name property
        """
        result = None
        if len(name) > 0:
            for index in self.G.nodes():
                if self.G.nodes[index]['name'] == name:
                    result = index
        if result is None and report is True:
            txt = name + ' not found.'
            print(txt)
        return result

    def _find_node_by_index(self, index: int, report=True):
        """
        Find and return node index (Check if it exists)
        """
        result = None
        index_list = self.all_nodes()
        if index in index_list:
            result = index
        if result is None and report is True:
            txt = 'node_index ' + str(index) + ' not found.'
            print(txt)
        return result

    def _find_node_by_pos(self, pos: list, report=True):
        """
        Find and return node index by its position
        """
        result = None
        for index in self.G.nodes():
            node = self.G.nodes[index]
            boundary = node['boundary']
            if boundary.is_in(pos):
                result = index
                break
        if result is None and report is True:
            txt = 'node position ' + str(pos) + ' not found.'
            print(txt)
        return result

    def find_node(self, input, report=True):
        """
        Find and return node index based on input (name, position, or index)
        """
        result = None
        if isinstance(input, str):
            result = self._find_node_by_name(input, report=report)
        elif isinstance(input, int):
            result = self._find_node_by_index(input, report=report)
        elif isinstance(input, list):
            result = self._find_node_by_pos(input, report=report)
        return result
