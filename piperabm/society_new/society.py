import networkx as nx

from piperabm.object import PureObject
from piperabm.society_new.query import Query
from piperabm.society_new.graphics import Graphics
from piperabm.society_new.agent import Agent
from piperabm.matter_new import Matter
from piperabm.economy import ExchangeRate
from piperabm.economy.exchange_rate.samples import exchange_rate_0
from piperabm.tools.stats import gini
from piperabm.society_new.deserialize import society_deserialize
from piperabm.tools.file_manager import JsonFile


class Society(PureObject, Query, Graphics):

    type = "society"

    def __init__(
            self,
            exchange_rate: ExchangeRate = exchange_rate_0,
        ):
        super().__init__()
        self.G = nx.Graph()
        self.model = None # Bind
        self.library = {}
        self.exchange_rate = exchange_rate
        self.path = None

    @property
    def infrastructure(self):
        result = None
        if self.model is not None:
            result = self.model.infrastructure
        return result

    def generate_agents(
            self,
            num: int = 1,
            gini_index: float = 0,
            average_income: float = 0,
            average_balance: float = 0,
            average_resources = Matter({'food': 1, 'water': 1, 'energy': 1}),):
        """
        Generate agents
        """
        distribution = gini.lognorm(gini_index)
        if isinstance(average_resources, dict):
            average_resources = Matter(average_resources)
        for _ in range(num):
            socioeconomic_status = distribution.rvs()        
            resources = average_resources * socioeconomic_status
            enough_resources = average_resources * 10 ###
            balance = average_balance * socioeconomic_status
            income = average_income * socioeconomic_status
            agent = Agent(
                socioeconomic_status=socioeconomic_status,
                resources=resources,
                balance=balance,
                enough_resources=enough_resources,
                income=income,
            )
            self.add(agent)

    @property
    def gini_index(self):
        data = []
        for id in self.agents:
            agent = self.get(id)
            wealth = agent.balance + agent.resources.value(prices=self.exchange_rate.prices)
            data.append(wealth)
        return gini.coefficient(data)
    
    def edge_id(self, id_1: int, id_2: int):
        """
        Get edge id based on its id_1 and id_2 (both ends)
        """
        result = None
        if self.G.has_edge(id_1, id_2):
            edge = self.G.edges[id_1, id_2]
            result = edge['id']
        return result
    
    def edge_ids(self, id: int):
        """
        Get edge id_1 and id_2 (both ends) based on its id
        """
        result = None
        for id_1, id_2 in self.G.edges():
            if self.edge_id(id_1, id_2) == id:
                result = [id_1, id_2]
                break
        return result
    
    @property
    def edges_ids(self):
        """
        Return all edges ids
        """
        return list(self.G.edges())

    @property
    def edges_id(self):
        """
        Return all edges id
        """
        result = []
        edges = self.edges_ids
        for ids in edges:
            id = self.edge_id(*ids)
            result.append(id)
        return result
    
    @property
    def nodes_id(self):
        """
        Return all nodes id
        """
        return list(self.G.nodes())
    
    @property
    def agents(self):
        return self.nodes_id
    
    @property
    def dead_agents(self):
        return self.filter_alive(alive=False)
    
    @property
    def alive_agents(self):
        return self.filter_alive(alive=True)
    
    def agents_in(self, id: int):
        result = []
        for agent_id in self.alive_agents:
            object = self.get(agent_id)
            if object.current_node == id:
                result.append(agent_id)
        return result
    
    def node_alive(self, id: int):
        """
        Return node type
        """
        agent = self.get(id)
        return agent.alive
    
    def filter_alive(self, alive: bool, nodes_id: list = None):
        """
        Filter a list of nodes id based on their type
        """
        result = []
        if nodes_id is None:  # All nodes
            nodes_id = self.nodes_id
        for node_id in nodes_id:
            if self.node_alive(node_id) is alive:
                result.append(node_id)
        return result
    
    def save(self, name: str = 'society'):
        """
        Save society to file
        """
        if self.path is not None:
            path = self.path
        else:
            path = self.model.path
        data = self.serialize()
        file = JsonFile(path, filename=name)
        file.save(data)

    def load(self, name: str = 'society'):
        """
        Load society from file
        """
        if self.path is not None:
            path = self.path
        else:
            path = self.model.path
        file = JsonFile(path, filename=name)
        data = file.load()
        self.deserialize(data)

    def serialize(self) -> dict:
        dictionary = {}
        library_serialized = {}
        for id in self.all:
            object = self.get(id)
            library_serialized[id] = object.serialize()
        dictionary['library'] = library_serialized
        dictionary['G'] = nx.to_dict_of_dicts(self.G)
        dictionary['exchange_rate'] = self.exchange_rate.serialize()
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        library_serialized = dictionary['library']
        for id in library_serialized:
            object = society_deserialize(library_serialized[id], society=self)
            self.library[int(id)] = object
        converted_dict_of_dicts = {
            int(outer_key): {int(inner_key): values for inner_key, values in outer_dict.items()}
            for outer_key, outer_dict in dictionary['G'].items()
        }
        self.G = nx.from_dict_of_dicts(d=converted_dict_of_dicts)   
        self.exchange_rate = ExchangeRate()
        self.exchange_rate.deserialize(dictionary['exchange_rate'])


if __name__ == "__main__":

    society = Society()
    print(society)