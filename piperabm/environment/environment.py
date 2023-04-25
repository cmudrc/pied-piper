import networkx as nx

from piperabm.object import Object
from piperabm.unit import DT, Date
from piperabm.environment.add import Add
from piperabm.environment.search import Search
from piperabm.environment.query import Query
from piperabm.environment.update import Update
from piperabm.environment.current_graph import CurrentGraph
from piperabm.environment.structures.load import load_structure


class Environment(Object, Add, Search, Query, Update):
    """
    Represent physical environment
    Manage settlements and their connecting links
    """

    def __init__(self):
        self.G = nx.Graph()
        self.current = None # last link_graph
        #self.log = Log(prefix='ENVIRONMENT', indentation_depth=1)
        super().__init__()
        self.type = 'environment'

    def to_current_graph(self, start_date=None, end_date=None):
        """
        Convert the environment to "link_graph" object
        """
        current_graph = CurrentGraph(env=self, start_date=start_date, end_date=end_date)
        self.current_graph = current_graph
        return current_graph
    
    def node_to_dict(self, index) -> dict:
        dictionary = {}
        dictionary['index'] = index
        dictionary['pos'] = self.get_node_pos(index)
        structure = self.get_node_object(index)
        if structure is None:
            dictionary['structure'] = None
        else:
            dictionary['structure'] = structure.to_dict()
        return dictionary
    
    def node_from_dict(self, dictionary: dict) -> None:
        index = dictionary['index']
        pos = dictionary['pos']
        structure = load_structure(dictionary['structure'])
        self.add_node(index, pos, structure)

    def edge_to_dict(self, index_start, index_end) -> dict:
        dictionary = {}
        dictionary['index_start'] = index_start
        dictionary['index_end'] = index_end
        structure = self.get_edge_object(index_start, index_end)
        if structure is None:
            dictionary['structure'] = None
        else:
            dictionary['structure'] = structure.to_dict()
        return dictionary
    
    def edge_from_dict(self, dictionary: dict) -> None:
        index_start = dictionary['index_start']
        index_end = dictionary['index_end']
        structure = load_structure(dictionary['structure'])
        self.add_edge(index_start, index_end, structure)
    
    def to_dict(self) -> dict:
        dictionary = {
            'type': self.type,
            'nodes': [],
            'edges': []
        }
        indexes = self.all_indexes()    
        for index in indexes:
            node_dictionary = self.node_to_dict(index)
            dictionary['nodes'].append(node_dictionary)
        edges = self.all_edges()
        for edge in edges:
            structure_dict = self.edge_to_dict(edge[0], edge[1])
            dictionary['edges'].append(structure_dict)     
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        self.type = dictionary['type']
        nodes = dictionary['nodes']
        for node_dictionary in nodes:
            self.node_from_dict(node_dictionary)
        edges = dictionary['edges']
        for edge_dictionary in edges:
            self.edge_from_dict(edge_dictionary)

    def show(self):
        if self.current is not None:
            self.current.show()
   

if __name__ == "__main__":
    from piperabm.environment.samples import environment_1 as environment
    from piperabm.unit import Date

    start_date = Date(2020, 1, 5)
    end_date = Date(2020, 1, 10)
    environment.update(start_date, end_date)
    environment.show()
