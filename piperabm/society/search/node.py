class Node:
    """
    *** Extends Search Class ***
    Methods for searching for node index
    """

    def _find_node_by_name(self, name: str):
        """
        Find and return settlement node index by its name property
        """
        result = None
        if len(name) > 0: # to avoid: (name='')
            index_list = self.all_indexes()
            for index in index_list:
                structure = self.get_node_object(index)
                if structure is not None and structure.name == name:
                    result = index
                    break
        return result

    def _find_node_by_index(self, index: int):
        """
        Find and return node index (Check if it exists)
        """
        result = None
        index_list = self.all_indexes()
        if index in index_list:
            result = index
        return result

    def find_node(self, input):
        """
        Find and return node index based on input (name, position, or index)
        """
        result = None
        if isinstance(input, str):
            result = self._find_node_by_name(input)
        elif isinstance(input, int):
            result = self._find_node_by_index(input)
        return result