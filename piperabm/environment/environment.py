import networkx as nx

from piperabm.degradation import ProgressiveDegradation
from piperabm.degradation import SuddenDegradation, Eternal, DiracDelta
from piperabm.unit import DT, Date

from piperabm.log import Log

try: from .search import Search
except: from search import Search
try: from .add import Add
except: from add import Add
try: from .index import Index
except: from index import Index
try: from .graphics import Graphics
except: from graphics import Graphics


class Environment(SuddenDegradation, ProgressiveDegradation, Search, Add, Index, Graphics):
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

    def _update_all_edges(self, start_date, end_date):
        """
        Check all edges to see whether they are active in the duration of time or not
            start_date: starting date of the time duration
            end_date: ending date of the time duration
        """
        for start, end, data in self.G.edges(data=True):
            if data['active'] is True:
                distribution = data['degradation_dist']
                length = data['length']
                if self.links_unit_length is None:
                    coeff = 1
                else:
                    if isinstance(distribution, (Eternal, DiracDelta)):
                        coeff = 1
                    else:
                        coeff = length / self.links_unit_length
                initiation_date = data['initiation_date']
                if initiation_date < end_date:
                    if initiation_date > start_date:
                        kwargs = {
                            'initiation_date': initiation_date,
                            'distribution': distribution,
                            'start_date': initiation_date,
                            'end_date': end_date,
                            'coeff': coeff,
                        }
                    else:
                        kwargs = {
                            'initiation_date': initiation_date,
                            'distribution': distribution,
                            'start_date': start_date,
                            'end_date': end_date,
                            'coeff': coeff,
                        }
                    active = self.is_active(**kwargs)
                else:
                    active = True

                if active is False:
                    data['active'] = False
                    txt = str(start_date.strftime('%Y-%m-%d')) + \
                        ' -> ' + str(end_date.strftime('%Y-%m-%d'))
                    txt += ': link ' + str(start) + '-' + \
                        str(end) + ' degradaded.'
                    self.log.add(txt)

    def _update_all_nodes(self, start_date, end_date):
        """
        Check all nodes to see whether they are active in the duration of time or not
            start_date: starting date of the time duration
            end_date: ending date of the time duration
        """
        for index in self.G.nodes():
            if index in self.node_types['settlement'] or index in self.node_types['market']:
                node = self.G.nodes[index]
                distribution = node['degradation_dist']
                initiation_date = node['initiation_date']
                if initiation_date < end_date:
                    if initiation_date > start_date:
                        kwargs = {
                            'initiation_date': initiation_date,
                            'distribution': distribution,
                            'start_date': initiation_date,
                            'end_date': end_date,
                        }
                    else:
                        kwargs = {
                            'initiation_date': initiation_date,
                            'distribution': distribution,
                            'start_date': start_date,
                            'end_date': end_date,
                        }
                    active = self.is_active(**kwargs)
                else:
                    active = True

                if active is False:
                    node['active'] = False
                    txt = str(start_date.strftime('%Y-%m-%d')) + \
                        ' -> ' + str(end_date.strftime('%Y-%m-%d'))
                    txt += ': node ' + str(index) + ' degradaded.'
                    self.log.add(txt)

    def update_elements(self, start_date, end_date):
        """
        Update all elements during the *start_date* until *end_date*
        """
        self._update_all_edges(start_date, end_date)
        self._update_all_nodes(start_date, end_date)

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
    p = Path(env, start_date=Date(2020, 1, 1), end_date=Date(2020, 1, 2))
    p.show()
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
