import networkx as nx

from piperabm.environment import Environment
from piperabm.economy import GiniGenerator, Exchange

try: from .search import Search
except: from search import Search
try: from .add import Add
except: from add import Add
try: from .index import Index
except: from index import Index
try: from .query import Query
except: from query import Query
try: from .graphics import Graphics
except: from graphics import Graphics
try: from .update import Update
except: from update import Update
try: from .log import Log
except: from log import Log


class Society(Add, Index, Query, Graphics, Update, Search):
    """
    Represent society
    Manage agents
    """

    def __init__(self, env: Environment, gini: float, exchange_rate: Exchange):
        self.env = env
        self.gini = gini
        self.gini_gen = GiniGenerator(gini, 1)
        self.exchange = exchange_rate
        self.G = nx.Graph()
        self.log = Log(prefix='SOCIETY', indentation_depth=1)
        super().__init__()

    def __str__(self):
        return str(self.G)


if __name__ == "__main__":
    pass
