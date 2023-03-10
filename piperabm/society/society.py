import networkx as nx

from piperabm import Environment
from piperabm.unit import DT, Date
#from piperabm.resource import Resource
from piperabm.actions import Queue, Move

try: from .search import Search
except: from search import Search
try: from .add import Add
except: from add import Add
try: from .index import Index
except: from index import Index
try: from .graphics import Graphics
except: from graphics import Graphics
try: from .update import Update
except: from update import Update


class Society(Add, Index, Graphics, Update, Search):

    def __init__(self, env: Environment, gini, average_income, exchange_rate):
        self.env = env
        self.gini = gini
        self.average_income = average_income
        self.exchange = exchange_rate
        self.G = nx.Graph()
        super().__init__()

    def __str__(self):
        return str(self.G)


if __name__ == "__main__":
    from piperabm.unit import Date
    from piperabm.actions import Move, Walk

    m = Move(
        start_date=Date(2020, 1, 1),
        start_pos=[0, 0],
        end_pos=[10000, 10000],
        adjusted_length=20000,
        transportation=Walk()
        )
    print(m.end_date)
    print(m.pos(date=Date(2020, 1, 1)+DT(hours=1)))
