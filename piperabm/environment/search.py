class Search:
    """
    *** Extends Environment Class ***
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

    def _find_node_by_pos(self, pos: list):
        """
        Find and return node index by its position
        """
        result = None
        index_list = self.all_indexes()
        for index in index_list:
            center_pos = self.get_node_pos(index)
            structure = self.get_node_object(index)
            if center_pos is not None and center_pos == pos:
                result = index
                break
            if structure is not None and structure.is_in(pos, center=center_pos, local=False) is True:
                result = index
                break
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
        elif isinstance(input, list):
            result = self._find_node_by_pos(input)
        return result
