import networkx as nx

from piperabm.degradation import ProgressiveDegradation
from piperabm.degradation import SuddenDegradation
from piperabm.unit import DT, Date

from piperabm.log import Log

try: from .search import Search
except: from search import Search
try: from .add import Add
except: from add import Add
try: from .index import Index
except: from index import Index
try: from .update import Update
except: from update import Update
try: from .graphics import Graphics
except: from graphics import Graphics
try: from .path import Path
except: from path import Path


class Environment(SuddenDegradation, ProgressiveDegradation, Search, Add, Index, Graphics, Update):
    """
    Manage settlements and their connecting links
    """

    def __init__(self, G=None, log=None, links_unit_length=None):
        """
            G: create instance from another graph
            log: logging instance
            unit_length: unit_length for the degradation distribution
        """
        if G is None:
            self.G = nx.Graph()
        else:
            self.G = G
        
        self.links_unit_length = links_unit_length
        
        if log is None:
            self.log = Log()
        else:
            self.log = log
        super().__init__()

    def adjusted_length(self, start_node, end_node):
        """
        Calculate adjusted_length between *start_node* and *end_node*
        """
        edge = self.G[start_node][end_node]
        difficulty = edge['difficulty']
        current_axels = edge['current_axels']
        total_axels = edge['total_axels']
        pd = self.progressive_degradation_factor(current_axels, total_axels)
        length = edge['length']
        return difficulty * pd * length

    def size(self):
        """
        Resturn size of environment based on elemets pos
        """
        x_min, x_max = None, None
        y_min, y_max = None, None
        for index in self.all_index():
            boundary = self.node_info(index, 'boundary')
            pos = boundary.center
            x = pos[0]
            y = pos[1]
            if x_max is None: x_max = x
            elif x > x_max: x_max = x
            if x_min is None: x_min = x
            elif x < x_min: x_min = x
            if y_max is None: y_max = y
            elif y > y_max: y_max = y
            if y_min is None: y_min = y
            elif y < y_min: y_min = y
        y_lim = [y_min, y_max]
        x_lim = [x_min, x_max]
        return x_lim, y_lim

    def to_path(self, start_date=None, end_date=None):
        return Path(env=self, start_date=start_date, end_date=end_date)

    def __str__(self):
        return str(self.G)


if __name__ == "__main__":
    from piperabm.boundary import Circular
    from piperabm.degradation import DiracDelta
    from piperabm.unit import Date, DT


    env = Environment()

    env.add_settlement(
        name="John's Home",
        pos=[-2, -2],
        boundary=Circular(radius=5),
        initiation_date=Date(2020, 1, 1),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )
    env.add_settlement(
        name="Peter's Home",
        pos=[20, 20],
        boundary=Circular(radius=5),
        initiation_date=Date(2020, 1, 3),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )

    env.add_link(
        "John's Home",
        [20, 0],
        initiation_date=Date(2020, 1, 1),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )
    env.add_link(
        [20.3, 0.3],
        "Peter's Home",
        initiation_date=Date(2020, 1, 3),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )

    #env.show(start_date=Date(2020, 1, 1), end_date=Date(2020, 1, 2))
    from path import Path
    p = Path(env, start_date=Date(2020, 1, 3), end_date=Date(2020, 1, 4))
    print(p.from_node_perspective(1))
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
