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
        """
            G: create instance from another graph
            log: logging instance
        """
        self.G = nx.Graph()
        self.current_graph = None # last link_graph
        self.path_graph = None # last path_graph
        #self.log = Log(prefix='ENVIRONMENT', indentation_depth=1)
        super().__init__()
        self.type = 'environment'

    '''
    def to_path_graph(self, start_date=None, end_date=None):
        """
        Convert the environment to "path_graph" object
        """
        link_graph = self.to_link_graph(start_date, end_date)
        path_graph = PathGraph(link_graph)
        self.path_graph = path_graph
        return path_graph
    '''
    def current(self, start_date=None, end_date=None):
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


if __name__ == "__main__":
    from piperabm.boundary import Circular
    from piperabm.degradation.sudden.distributions import DiracDelta
    from piperabm.unit import Date, DT


    env = Environment()

    env.add_settlement(
        name="John's Home",
        pos=[-2, -2],
        boundary=Circular(radius=5),
        start_date=Date(2020, 1, 1),
        sudden_degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )
    env.add_settlement(
        name="Peter's Home",
        pos=[20, 20],
        boundary=Circular(radius=5),
        start_date=Date(2020, 1, 3),
        sudden_degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )
    #print(env.all_indexes(type='settlement'))
    #print(env.find_node(1))
    
    env.add_road(
        _from="John's Home",
        _to=[20, 0],
        start_date=Date(2020, 1, 1),
        sudden_degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )
    env.add_road(
        _from=[20, 0],
        _to="Peter's Home",
        start_date=Date(2020, 1, 3),
        sudden_degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )
    print(env)
    
    #env.show(start_date=Date(2020, 1, 1), end_date=Date(2020, 1, 2))
    #from path import Path
    #p = Path(env, start_date=Date(2020, 1, 3), end_date=Date(2020, 1, 4))
    #print(p.from_node_perspective(1))
    #p.show()
    # L.add_link([2, 2], [22, 22])
    # L.add_link(0, 1)
    # print(L.G.edges())
    # L.show()

    # P = Path(L)
    # P.show()

    '''
    i = 0
    current_date = Date(2020, 1, 1)
    while i < 20:
        start_date = current_date
        end_date = current_date + DT(days=3)
        env.update_elements(start_date, end_date)
        current_date += DT(days=1)
        i = i+1

    P = env.to_path()
    P.show()
    # L.show()
    '''
