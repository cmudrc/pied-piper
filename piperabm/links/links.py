import networkx as nx
from datetime import datetime as Date

from piperabm.boundary import Point
from piperabm.degradation import Eternal
from piperabm.unit import Unit


class Links:
    """
    Manage settlements and their connecting links
    """
    def __init__(self):
        """
            index_dict: {index:type} pairs, types: s => settlement, c => cross
        """
        self.G = nx.MultiDiGraph()
        self.index_dict = {}

    def find_next_index(self):
        """
        Check self.index_dict dictionary keys (indexes) and suggest a new index
        """
        index_dict = self.index_dict
        if len(index_dict) > 0:
            key_list = index_dict.keys()
            max_index = max(key_list)
            new_index = max_index + 1
        else:
            new_index = 0
        return new_index

    def add_settlement(
        self,
        name='',
        pos=[0, 0],
        boundary=None,
        active=True,
        initiation_date=None,
        degradation_dist=None
    ):
        """
        Add a new settlement
            name: name of settlement, optional
            pos: position of the settlement
            boundary: shape of settlement
            active: is it still active? (True/False)
            initiation_date: the built date of settlement
            degradation_dist: the distribution for degradation of the settlement
        """
        index = self.find_next_index()
        if boundary is None:
            boundary = Point()
        boundary.center = pos
        if degradation_dist is None:
            degradation_dist = Eternal()
        if initiation_date is None:
            initiation_date = Date.today()
        self.G.add_node(
            index,
            name=name,
            active=active,
            boundary=boundary,
            initiation_date=initiation_date,
            degradation_dist=degradation_dist
        )
        self.index_dict[index] = 's'

    def add_cross(
        self,
        pos=[0, 0]
    ):
        """
        Add a new cross point
        """
        index = self.find_next_index()
        boundary = Point()
        boundary.center = pos
        self.G.add_node(
            index,
            boundary=boundary
        )
        self.index_dict[index] = 'c'

    def add_link(
        self,
        start,
        end,
        double_sided=True
    ):
        """
        Add a link between *start* and *end*
            start: starting point in the form of either index (as int), name (as str), or pos (as a [x,y] list)
            end: ending point in the form of either index (as int), name (as str), or pos (as a [x,y] list)
            double_sided: whether it is two way connection or not (True/False)
        """
        start_index = self.find_node(start)
        end_index = self.find_node(end)

    def _find_node_by_name(self, name:str):
        """
        Find and return settlement node index by its name property
        """
        result = None
        for node_index in self.index_dict.keys():
            if self.index_dict[node_index] == 's':
                if self.G.nodes[node_index]['name'] == name:
                    result = node_index
        return result

    def _find_node_by_index(self, index:int):
        """
        Find and return node index (Check if it exists)
        """
        result = None
        if index in self.index_dict.keys():
            result = index
        return result

    def _find_node_by_pos(self, pos:list):
        result = None
        for node_index in self.G.nodes():
            boundary = self.G.nodes[node_index]['boundary']
            if boundary.is_in(pos):
                result = node_index
                break
        return result


    def find_node(self, input):
        result = None
        if isinstance(input, str):
            result = self._find_node_by_name(input)
        elif isinstance(input, int):
            result = self._find_node_by_index(input)
        elif isinstance(input, list):
            result = self._find_node_by_pos(input)
        return result


if __name__ == "__main__":
    from piperabm.boundary import Circular
    from piperabm.degradation import DiracDelta

    L = Links()
    L.add_settlement(
        name="John's Home",
        pos=[0, 0],
        boundary=Circular(radius=10),
        initiation_date=Date(2020, 1, 1),
        degradation_dist=DiracDelta(main=Unit(10,'day').to('second').val)
    )
    print(L.find_node("John's Home"))
    print(L.find_node([1, 1]))
    print(L.find_node(0))