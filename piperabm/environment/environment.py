import networkx as nx
import uuid

from piperabm.object import PureObject
from piperabm.environment.query import Query
from piperabm.environment.grammar import Grammar
from piperabm.environment.infrastructure import Infrastructure
from piperabm.environment.items import Junction
from piperabm.tools.coordinate import distance_point_to_point, distance_point_to_line, intersect_line_line


class Environment(PureObject, Query, Grammar):

    def __init__(
            self,
            proximity_radius: float  
        ):
        super().__init__()
        self.society = None  # used for binding
        self.library = {}  # {index: item} pairs
        self.proximity_radius = proximity_radius  # distance less than this amount is equivalent to zero

    @property
    def new_index(self) -> int:
        """
        Generate a new unique integer as id for graph items
        """
        return uuid.uuid4().int
    
    def add(self, item) -> None:
        """
        Add new item to library
        """
        if item.category == 'node':
            item.index = self.new_index
            self.library[item.index] = item
            self.apply_grammars()
        elif item.category == 'edge':
            junction_1 = Junction(pos=item.pos_1)
            junction_2 = Junction(pos=item.pos_2)
            self.add(junction_1)
            self.add(junction_2)
            item.index = self.new_index
            self.library[item.index] = item
            self.apply_grammars()
        else:
            raise ValueError
    
    def to_infrastrucure_graph(self):
        return Infrastructure(environment=self)
    
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
            item = self.get_item(index)
            distance = distance_point_to_point(pos, item.pos)
            result.append([distance, index])
        return result
    
    def show(self):
        infrastructure = self.to_infrastrucure_graph()
        infrastructure.show()
    
    def serialize(self) -> dict:
        dictionary = {}
        ''' serialize library items '''
        library_serialized = {}
        for index in self.library:
            item = self.get_item(index)
            library_serialized[index] = item.serialize()
        dictionary['library'] = library_serialized
        dictionary['proximity radius'] = self.proximity_radius
        return dictionary


if __name__ == '__main__':
    from items import Junction

    env = Environment(proximity_radius=0.1)
    item = Junction(name='sample', pos=[0, 0])
    env.add(item)
    other = Junction(pos=[0.05, 0])
    env.add(other)
    env.show()
    