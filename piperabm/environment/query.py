import uuid


class Query:

    def all_nodes(self, type=None) -> list:
        """ Return a list of all nodes """
        all = list(self.G.nodes())
        if type is not None:
            result = []
            for index in all:
                item = self.get_node_object(index)
                if item.type == type:
                    result.append(index)
            all = result
        return all
    
    def all_edges(self) -> list:
        """ Return a list of all edges """
        all = list(self.G.edges())
        return all
    
    def get_node_object(self, index: int):
        """ Return node object by its index """
        result = None
        if self.G.has_node(index):
            node = self.G.nodes[index] 
            result = node['object']
        return result
    
    def get_edge_object(self, index_1: int, index_2: int):
        """ Return edge object by its index_1 and index_2 """
        result = None
        if self.G.has_edge(index_1, index_2):
            edge = self.G.edges[index_1, index_2]
            result = edge['object']
        return result
    
    def new_id(self) -> int:
        """ Generate a new unique integer as id for graph items """
        return uuid.uuid4().int
    
    def sort_distances(self, distances: list):
        """ Sort elements based on their distance """
        # remove None values in distance part
        distances = [[distance, index] for distance, index in distances if distance is not None]
        return [[distance, index] for distance, index in sorted(distances)]
    
    def filter_distances(self, distances: list):
        """ Filter and sort elements closer than *self.proximity_radius* """
        result = []
        for element in distances:
            distance = element[0]
            index = element[1]
            if distance is not None:
                if distance < self.proximity_radius:
                    result.append([distance, index])
        return self.sort_distances(result)