import uuid

from piperabm.tools.coordinate import distance_point_to_point


class Query:

    @property
    def new_index(self) -> int:
        """
        Generate a new unique integer as id for graph items
        """
        return uuid.uuid4().int
    
    @property
    def infrastructure_types(self):
        result = self.valid_types["infrastructure"]["node"] + \
        self.valid_types["infrastructure"]["edge"]
        return result
    
    @property
    def society_types(self):
        result = self.valid_types["society"]["node"] + \
        self.valid_types["society"]["edge"]
        return result

    def remove(self, index: int):
        """
        Remove the item object based on its index
        """
        del self.library[index]

    def get(self, index: int):
        """
        Return the item as object based on its index
        """
        return self.library[index]
    
    def has(self, index: int, items=None):
        """
        Check if an item having *index* exists in *items*
        """
        if items is None:
            items = self.library.keys()
        return index in items
    
    def filter(self, items=None, types=None):
        """
        Filter *items* based on their *types* and *category*
        """
        result = []
        if items is None:
            items = self.all
        if isinstance(types, str):
            types = [types]
        for index in items:
            item = self.get(index)
            if types is None or \
                item.type in types:
                result.append(index)
        return result
    
    def find_agents_in_same_home(self, home_index):
        result = []
        all = self.all_agents
        for index in all:
            agent = self.get(index)
            if agent.home == home_index:
                result.append(index)
        return result

    @property
    def all_environment_nodes(self):
        types = self.valid_types["infrastructure"]["node"]
        items = self.filter(types=types)
        return items
    
    @property
    def all_environment_edges(self):
        types = self.valid_types["infrastructure"]["edge"]
        items = self.filter(types=types)
        return items
    
    @property
    def all_alive_agents(self):
        result = []
        items = self.all_agents
        for index in items:
            item = self.get(index)
            if item.alive is True:
                result.append(index)
        return result

    @property
    def all_dead_agents(self):
        result = []
        items = self.all_agents
        for index in items:
            item = self.get(index)
            if item.alive is False:
                result.append(index)
        return result

    @property
    def all_agents(self):
        types = self.valid_types["society"]["node"]
        items = self.filter(types=types)
        return items

    @property
    def all(self):
        return self.library.keys()
    
    def distances(self, pos: list, items: list) -> list:
        """
        Calculate nodes distance from *pos*
        """
        result = []  # list of [distance, index]
        for index in items:
            item = self.get(index)
            if item.category == "node":
                distance = distance_point_to_point(pos, item.pos)
                result.append([distance, index])
        return result

    def sort_distances(self, distances: list) -> list:
        """
        Sort *distances* based on distance value
        """
        # Remove None distance values
        distances = [[distance, index]
                     for distance, index in distances if distance is not None]
        # Sort elements based on distance
        sorted_distances = [[distance, index]
                            for distance, index in sorted(distances)]
        return sorted_distances
    
    def find_nearest_node(self, pos: list, items: list = None) -> int:
        """
        Find the nearst node index to the *pos*
        """
        if items is None:
            raise ValueError
        distances = self.distances(pos, items)
        distances = self.sort_distances(distances)
        nearest_node_index = distances[0][1]
        nearest_node_distance = distances[0][0]
        return nearest_node_index, nearest_node_distance