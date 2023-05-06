import networkx as nx

from piperabm.object import Object
from piperabm.society.add import Add
from piperabm.society.search import Search
from piperabm.society.query import Query
#from piperabm.environment import Environment
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
        self.G = nx.MultiGraph()
        self.type = 'society'
        #self.log = Log(prefix='SOCIETY', indentation_depth=1)
        


if __name__ == "__main__":
    society = Society()
    print(society)
