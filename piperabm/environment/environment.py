import networkx as nx
import uuid

from piperabm.object import PureObject
from piperabm.environment.infrastructure import Infrastructure
from piperabm.environment.items import Junction
from piperabm.tools.coordinate import distance_point_to_point, distance_point_to_line, intersect_line_line


class Environment(PureObject):

    def __init__(
            self,
            proximity_radius: float = 0.1    
        ):
        super().__init__()
        self.society = None  # used for binding
        self.library = {}  # {index: item} pairs
        self.proximity_radius = proximity_radius  # distance less than this amount is equivalent to zero

    @property
    def new_index(self) -> int:
        """ Generate a new unique integer as id for graph items """
        return uuid.uuid4().int
    
    def add(self, item) -> None:
        """
        Add new item to library
        """
        if item.category == 'node':
            item.index = self.new_index
            self.library[item.index] = item
        elif item.category == 'edge':
            junction_1 = Junction(pos=item.pos_1)
            junction_2 = Junction(pos=item.pos_2)
            self.add(junction_1)
            self.add(junction_2)
            item.index = self.new_index
            self.library[item.index] = item
        else:
            raise ValueError

    def item(self, index: int):
        """
        Return items as object based on its index
        """
        return self.library[index]
    
    def current_items(self, date_start, date_end) -> list:
        """
        Return a list of current items index
        """
        current_items = []
        for index in self.library:
            item = self.library[index]
            if item.exists(date_start, date_end):
                current_items.append(index)
        return current_items
    
    def to_infrastrucure_graph(self, date_start, date_end):
        items = self.current_items(date_start, date_end)
        infrastructure = Infrastructure(environment=self)
        for item_index in items:
            item = self.item(item_index)
            if item.category == 'node':
                infrastructure.add_node(item.index)
            elif item.category == 'edge':
                index_1 = self.find_nearest_node(item.pos_1, items)
                index_2 = self.find_nearest_node(item.pos_2, items)
                infrastructure.add_edge(index_1, index_2, item.index)
        #infrastructure.apply_grammars()
        return infrastructure
    
    def find_nearest_node(self, pos: list, items: list) -> int:
        distances = self.nodes_distance(pos, items)
        distances = self.sort_distances(distances)
        nearest_node_index = distances[0][1]
        return nearest_node_index

    def nodes_distance(self, pos: list, items: list) -> list:
        """
        Calculate nodes distance from *pos*
        """
        result = []  # list of [distance, index]
        items = self.filter_category(items, category='node')
        for index in items:
            item = self.item(index)
            distance = distance_point_to_point(pos, item.pos)
            result.append([distance, index])
        return result
    
    def sort_distances(self, distances: list) -> list:
        # remove None values in distance part
        #distances = [[distance, index] for distance, index in distances if distance is not None]
        # sort elements based on distance
        sorted_distances = [[distance, index] for distance, index in sorted(distances)]
        return sorted_distances
    
    def filter_category(self, items: list, category: str):
        """
        Return a list of nodes from *items* that based on *category* value (node/edge)
        """
        result = []
        for index in items:
            item = self.item(index)
            if item.category == category:
                result.append(index)
        return result
    
    def serialize(self) -> dict:
        dictionary = {}
        # serialize library items
        library_serialized = {}
        for index in self.library:
            item = self.item(index)
            library_serialized[index] = item.serialize()
        dictionary['library'] = library_serialized
        dictionary['proximity radius'] = self.proximity_radius
        return dictionary


if __name__ == '__main__':
    from items import Junction

    env = Environment()
    item = Junction(name='sample', pos=[0, 0])
    env.add(item)
    env.print
    