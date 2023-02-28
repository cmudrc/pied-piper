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
try: from .decision import Decision
except: from decision import Decision


class Society(Add, Index, Graphics, Update, Search, Decision):

    def __init__(self, env: Environment):
        self.env = env
        self.G = nx.Graph()
        super().__init__()


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
