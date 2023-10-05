from piperabm.time import Date


class Query:

    def get_item(self, index: int):
        """
        Return the item as object based on its index
        """
        return self.library[index]
    
    def has_item(self, index: int):
        return index in self.library

    @property
    def all_items(self) -> list:
        """
        Return all item indexes
        """
        return list(self.library.keys())
    
    @property
    def all_nodes(self) -> list:
        """
        Return all nodes indexes
        """
        items = self.all_items
        return self.filter_category(items, 'node')
    
    @property
    def all_edges(self) -> list:
        """
        Return all nodes indexes
        """
        items = self.all_items
        return self.filter_category(items, 'edge')

    def remove_item(self, index: int):
        """
        Remove the item object based on its index
        """
        del self.library[index]
    
    def current_items(self, date_start: Date, date_end: Date, items: list=None) -> list:
        """
        Return a list of current items index
        """
        if items is None:
            items = self.all_items
        current_items = []
        for index in items:
            item = self.library[index]
            if item.exists(date_start, date_end):
                current_items.append(index)
        return current_items

    def sort_distances(self, distances: list) -> list:
        """
        Sort *distances* based on distance value
        """
        ''' remove None values in distance part '''
        distances = [[distance, index] for distance, index in distances if distance is not None]
        ''' sort elements based on distance '''
        sorted_distances = [[distance, index] for distance, index in sorted(distances)]
        return sorted_distances
    
    def filter_category(self, items: list, category: str):
        """
        Return a list of nodes from *items* that based on *category* value (node/edge)
        """
        result = []
        for index in items:
            item = self.get_item(index)
            if item.category == category:
                result.append(index)
        return result
    
    def filter_type(self, items: list, type: str):
        """
        Return a list of nodes from *items* that based on *type* value (junction, road, etc.)
        """
        result = []
        for index in items:
            item = self.get_item(index)
            if item.type == type:
                result.append(index)
        return result