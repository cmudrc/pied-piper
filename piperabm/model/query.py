import uuid

from piperabm.tools.coordinate import distance as ds


class Query:

    def has_id(self, id) -> bool:
        """
        Check if the id already exists
        """
        result = False
        if id in self.all:
            result = True
        return result

    @property
    def new_id(self) -> int:
        """
        Generate a new unique integer as id for graph items
        """
        result = None
        while True:
            new_id = uuid.uuid4().int
            if self.has_id(new_id) is False:
                result = new_id
                break
        return result

    def add_object_to_library(self, object):
        """
        Add new object to library
        """
        # ID
        if object.id is None:
            object.id = self.new_id
        else:
            if self.has_id(object.id) is True:
                object.id = self.new_id
        # Binding
        object.model = self
        # Add to library
        self.library[object.id] = object
        return object.id
    
    def remove(self, id: int):
        """
        Remove the item object based on its index
        """
        del self.library[id]

    def get(self, id: int):
        """
        Return the item as object based on its index
        """
        return self.library[id]
    
    def has(self, id: int, items=None):
        """
        Check if an item having *index* exists in *items*
        """
        if items is None:
            items = self.library.keys()
        return id in items
    
    @property
    def all(self):
        """
        Return all items indexes
        """
        return self.library.keys()
    
    def filter(self, ids=None, type=None, section=None, category=None):
        """
        Filter *ids* based on their *type*, *section*, and *category*
        """
        result = []
        if ids is None:
            ids = self.all
        for id in ids:
            check = []
            object = self.get(id)
            if type is None or \
            object.type == type:
                check.append(True)
            else:
                check.append(False)
            if section is None or \
            object.section == section:
                check.append(True)
            else:
                check.append(False)
            if category is None or \
            object.category == category:
                check.append(True)
            else:
                check.append(False)
            if False not in check:
                result.append(id)
        return result
    
    @property
    def infrastructure_nodes(self):
        """
        Return id of all infrastructure nodes id
        """
        return self.filter(section="infrastructure", category="node")
    
    @property
    def infrastructure_edges(self):
        """
        Return id of all infrastructure edges id
        """
        return self.filter(section="infrastructure", category="edge")
    
    @property
    def society_nodes(self):
        """
        Return id of all society nodes id
        """
        return self.filter(section="society", category="node")
    
    @property
    def society_edges(self):
        """
        Return id of all society edges id
        """
        return self.filter(section="society", category="edge")

    def find_by_name(self, name: str, ids=None):
        """
        Find an item based on its name
        """
        result = []
        if ids is None:
            ids = self.all
        for id in ids:
            object = self.get(id)
            if object.name == name:
                result.append(id)
        return result
    
    def is_isolated(self, node_id: int):
        result = True
        for edge_id in self.infrastructure_edges:
            edge = self.get(edge_id)
            if node_id == edge.id_1 or \
            node_id == edge.id_2:
                result = False
                break
        return result
    '''
    def find_agents_in_same_home(self, home_index):
        """
        Return all agent indexes sharing the same home
        """
        result = []
        all = self.all_agents
        for index in all:
            agent = self.get(index)
            if agent.home == home_index:
                result.append(index)
        return result
    '''
    
    '''
    @property
    def all_alive_agents(self):
        """
        Return index of all alive agents
        """
        result = []
        items = self.all_agents
        for index in items:
            item = self.get(index)
            if item.alive is True:
                result.append(index)
        return result

    @property
    def all_dead_agents(self):
        """
        Return index of all dead agents
        """
        result = []
        items = self.all_agents
        for index in items:
            item = self.get(index)
            if item.alive is False:
                result.append(index)
        return result

    @property
    def all_agents(self):
        """
        Return index of all alive and dead agents combined
        """
        types = self.valid_types["society"]["node"]
        items = self.filter(types=types)
        return items
    
    @property
    def all_relationships(self):
        """
        Return index of all relationships between agents
        """
        types = self.valid_types["society"]["edge"]
        items = self.filter(types=types)
        return items
    
    def distances(self, pos: list, items: list) -> list:
        """
        Calculate nodes distance from *pos*
        """
        result = []  # list of [distance, index]
        for index in items:
            item = self.get(index)
            if item.category == "node":
                distance = ds.point_to_point(pos, item.pos)
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
            items = self.all
        distances = self.distances(pos, items)
        distances = self.sort_distances(distances)
        nearest_node_index = distances[0][1]
        nearest_node_distance = distances[0][0]
        return nearest_node_index, nearest_node_distance
    
    def find_nearest_nodes(self, pos: list, items: list = None, k: int = 1) -> int:
        """
        Find the *k* nearst node index to the *pos*
        """
        if items is None:
            raise ValueError
        distances = self.distances(pos, items)
        distances = self.sort_distances(distances)
        return distances[:k]
    '''