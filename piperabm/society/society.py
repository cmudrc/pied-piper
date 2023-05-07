import networkx as nx

from piperabm.object import Object
from piperabm.society.add import Add
from piperabm.society.search import Search
from piperabm.society.query import Query
#from piperabm.environment import Environment
from piperabm.society.agent import Agent
from piperabm.society.relationship.load import load_relationship
from piperabm.economy import GiniGenerator, ExchangeRate


class Society(Object, Add, Search, Query):
    """
    Represent society
    Manage agents and their relationships
    """

    def __init__(self, environment = None, gini: float = 0, exchange_rate: ExchangeRate = None):
        super().__init__()
        self.environment = environment
        self.gini = gini
        #self.gini_gen = GiniGenerator(gini, 1)
        self.exchange = exchange_rate
        self.G = nx.Graph()
        self.type = 'society'
        #self.log = Log(prefix='SOCIETY', indentation_depth=1)

    def node_to_dict(self, index) -> dict:
        dictionary = {}
        dictionary['pos'] = self.get_node_pos(index)
        agent = self.get_node_object(index)
        dictionary['agent'] = agent.to_dict()
        return dictionary
    
    def node_from_dict(self, index, dictionary: dict) -> None:
        pos = dictionary['pos']
        agent = Agent()
        agent.from_dict(dictionary['agent'])
        self.add_node(index, pos, agent)

    def edge_to_dict(self, index_start, index_end) -> dict:
        dictionary = {}
        dictionary['index_end'] = index_end
        relationships = self.get_edge_object(index_start, index_end)
        relationships_dictionary = {}
        for relation in relationships:
            relationships_dictionary[relation] = relationships[relation].to_dict()
        dictionary['relationships'] = relationships_dictionary
        return dictionary
    
    def edge_from_dict(self, index_start, dictionary: dict) -> None:
        index_end = dictionary['index_end']
        relationships_dictionary = dictionary['relationships']
        relationships = {}
        for key in relationships_dictionary:
            relationships[key] = load_relationship(relationships_dictionary[key])
        self.add_edge(index_start, index_end, relationships)

    def to_dict(self) -> dict:
        dictionary = {
            'type': self.type,
            'exchange_rate': None, ####
            'nodes': {},
            'edges': {}
        }
        indexes = self.all_indexes()    
        for index in indexes:
            node_dictionary = self.node_to_dict(index)
            dictionary['nodes'][index] = node_dictionary
        edges = self.all_edges()
        for edge in edges:
            index_start = edge[0]
            index_end = edge[1]
            edge_dictionary = self.edge_to_dict(index_start, index_end)
            dictionary['edges'][index_start] = edge_dictionary
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        self.type = dictionary['type']
        nodes = dictionary['nodes']
        for index in nodes:
            self.node_from_dict(index, nodes[index])
        edges = dictionary['edges']
        for index_start in edges:
            self.edge_from_dict(index_start, edges[index_start])
        

if __name__ == "__main__":
    society = Society()
    print(society)
