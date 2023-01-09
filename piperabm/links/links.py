import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from piperabm.boundary import Point
from piperabm.degradation import Eternal
from piperabm.unit import Unit, DT, Date
from piperabm.tools import euclidean_distance


class Links:
    """
    Manage settlements and their connecting links
    """
    def __init__(self):
        """
            index_dict: {index:type} pairs, types: s => settlement, c => cross
        """
        self.G = nx.DiGraph()
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
        boundary=Point(),
        active=True,
        initiation_date=Date.today(),
        degradation_dist=Eternal()
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
        boundary.center = pos
        self.G.add_node(
            index,
            name=name,
            active=active,
            initiation_date=initiation_date,
            degradation_dist=degradation_dist,
            boundary=boundary
        )
        self.index_dict[index] = 's'

    def add_cross(
        self,
        name='',
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
            name=name,
            boundary=boundary
        )
        self.index_dict[index] = 'c'
        return index

    def add_link(
        self,
        start,
        end,
        double_sided=True,
        active=True,
        initiation_date=Date.today(),
        degradation_dist=Eternal(),
        length=None,
        difficulty=1,
        slope_ratio=1
    ):
        """
        Add a link between *start* and *end*

        Args:
            start: starting point in the form of either index (as int), name (as str), or pos (as a [x,y] list)
            end: ending point in the form of either index (as int), name (as str), or pos (as a [x,y] list)
            double_sided: whether it is two way connection or not (True/False)
            active: is it still active? (True/False)
            initiation_date: the built date of settlement
            degradation_dist: the distribution for degradation of the settlement
            length: the length of the link, eucledian distance is used as default
            difficulty: difficulty of the link (unrelated to slope), default is 1
            slope_ratio: difficulty of the link due to slope, default is 1
        """
        create_node = True
        start_index = self.find_node(start)
        if start_index is None:
            if isinstance(start, list): start_index = self.add_cross(pos=start)
            else: create_node = False
        end_index = self.find_node(end)
        if end_index is None:
            if isinstance(end, list): end_index = self.add_cross(pos=end)
            else: create_node = False
        
        start_pos = self.G.nodes[start_index]['boundary'].center
        end_pos = self.G.nodes[end_index]['boundary'].center
        euclidean_length = euclidean_distance(*start_pos, *end_pos)
        if length is None or length < euclidean_length:
            length = euclidean_length

        if create_node is True:
            self.G.add_edge(
                start_index,
                end_index,
                active=active,
                initiation_date=initiation_date,
                degradation_dist=degradation_dist,
                length=length,
                difficulty=difficulty,
                slope_ratio=slope_ratio
                )
            if double_sided:
                self.G.add_edge(
                    end_index,
                    start_index,
                    active=active,
                    initiation_date=initiation_date,
                    degradation_dist=degradation_dist,
                    length=length,
                    difficulty=difficulty,
                    slope_ratio=1/slope_ratio
                    )
        else:
            txt = 'link creation failed.'
            print(txt)

    def probability_of_working(self, initiation_date, distribution, start_date, end_date, coeff=1):
        """
        Probability of remaining active during the desired duration of time.
        
        Args:
            start_date: start of duration of time, datetime object
            end_date: end of duration of time, datetime object
        
        """
        time_start = (start_date - initiation_date).total_seconds()
        time_end = (end_date - initiation_date).total_seconds()
        Q = distribution.probability(time_start, time_end)
        Q *= coeff
        if Q > 1: Q = 1
        elif Q < 0: Q = 1
        print(Q)
        return 1 - Q

    def is_working(self, probability):
        """
        Check if the structure survived based on weighted random and returns the result (True/False).
        
        Args:
            probability: probability of working (or remaining alive) at each step
        
        """
        if probability > 1: probability = 1
        elif probability < 0: probability = 0
        sequence = [True, False]  # set of possible outcomes
        weights = [probability, 1-probability]
        index = np.random.choice(
            2, # np.arange(1)
            1, # return one element
            p=weights
        )
        return sequence[int(index)]

    def is_active(self, initiation_date, distribution, start_date, end_date, coeff=1):
        """
        Check if the element is going to survive the desired duration of time or not.

        Args:
            start_date: start of duration of time, datetime object
            end_date: end of duration of time, datetime object
        
        Returns:
            active (True/False)
        """
        probability = self.probability_of_working(initiation_date, distribution, start_date, end_date, coeff)
        active = self.is_working(probability)
        return active

    def update_all_edges(self, start_date, end_date, unit_length=None):
        """
        Check all elements whether they are active in the duration of time or not.
        """
        for start, end, data in self.G.edges(data=True):
            if data['active'] is True:
                distribution = data['degradation_dist']
                initiation_date = data['initiation_date']
                length = data['length']
                if isinstance(distribution, (Eternal, DiracDelta)):
                    coeff = 1
                else:
                    coeff = length / unit_length
                print(initiation_date, start_date, end_date)
                active = self.is_active(initiation_date, distribution, start_date, end_date, coeff)
                data['active'] = active # update

    def _find_node_by_name(self, name:str):
        """
        Find and return settlement node index by its name property
        """
        result = None
        for index in self.G.nodes():
            if self.G.nodes[index]['name'] == name and len(name) > 0:
                result = index
        if result is None:
            txt = name + ' not found.'
            print(txt)
        return result

    def _find_node_by_index(self, index:int):
        """
        Find and return node index (Check if it exists)
        """
        result = None
        if index in self.index_dict.keys():
            result = index
        if result is None:
            txt = 'node_index ' + str(index) + ' not found.'
            print(txt)
        return result

    def _find_node_by_pos(self, pos:list):
        """
        Find and return node index by its position
        """
        result = None
        for index in self.G.nodes():
            node = self.G.nodes[index]
            boundary = node['boundary']
            if boundary.is_in(pos):
                result = index
                break
        return result

    def find_node(self, input):
        """
        Find and return node index based on input (name, position, or index)
        """
        result = None
        if isinstance(input, str):
            result = self._find_node_by_name(input)
        elif isinstance(input, int):
            result = self._find_node_by_index(input)
        elif isinstance(input, list):
            result = self._find_node_by_pos(input)
        return result

    def show(self):
        pos_dict = {}
        node_list = []
        node_size = []
        label_dict = {}
        node_size_s = 300
        node_size_c = 0
        edge_list = []
        edge_color = []
        edge_color_active = 'b'
        edge_color_inactive = 'r'

        for index in self.G.nodes():
            node = self.G.nodes[index]
            node_list.append(index)
            pos = node['boundary'].center
            pos_dict[index] = pos
            label = node['name']
            label_dict[index] = label
            node_type = self.index_dict[index]
            if node_type == 's':
                node_size.append(node_size_s)
            elif node_type == 'c':
                node_size.append(node_size_c)
        
        for start, end, data in self.G.edges(data=True):
            edge_list.append([start, end])
            if data['active'] is True:
                edge_color.append(edge_color_active)
            elif data['active'] is False:
                edge_color.append(edge_color_inactive)
        
        nx.draw_networkx(
            self.G,
            pos=pos_dict,
            nodelist=node_list,
            node_size=node_size,
            labels=label_dict,
            edgelist=edge_list,
            edge_color=edge_color
        )
        plt.show()


class Path:
    def __init__(self):
        self.G = nx.MultiDiGraph()

    def import_links(self, links):
        for node_index in links.G.nodes():
            if links.index_dict[node_index] == 's':
                self.G.add_node(links.G.nodes[node_index])


if __name__ == "__main__":
    from piperabm.boundary import Circular
    from piperabm.degradation import DiracDelta

    L = Links()
    L.add_settlement(
        name="John's Home",
        pos=[-2, -2],
        boundary=Circular(radius=5),
        initiation_date=Date(2020, 1, 1),
        degradation_dist=DiracDelta(main=Unit(10,'day').to('second').val)
    )
    L.add_settlement(
        name="Peter's Home",
        pos=[20, 20],
        boundary=Circular(radius=5),
        initiation_date=Date(2020, 1, 1),
        degradation_dist=DiracDelta(main=Unit(10,'day').to('second').val)
    )
    #print(L.find_node("John's Home"))
    #print(L.find_node([2, 2]))
    #print(L.find_node(0))

    #L.add_link("John's Home", "Peter's Home")
    L.add_link(
        "John's Home",
        [20, 0],
        initiation_date=Date(2020, 1, 1),
        degradation_dist=DiracDelta(main=Unit(10,'day').to('second').val)
        )
    L.add_link(
        [20.3, 0.3],
        "Peter's Home",
        initiation_date=Date(2020, 1, 1),
        degradation_dist=DiracDelta(main=Unit(10,'day').to('second').val)
        )
    #L.add_link([2, 2], [22, 22])
    #L.add_link(0, 1)
    #print(L.G.edges())
    #L.show()
    #P = Path()
    #P.import_links(L)
    #print(P.G)

    
    i = 0
    current_date = Date(2020, 1, 1)
    while i < 20:
        start_date = current_date
        end_date = current_date + DT(days=3)
        L.update_all_edges(start_date, end_date, unit_length=10)
        current_date += DT(days=1)
        i = i+1
    
    L.show()
