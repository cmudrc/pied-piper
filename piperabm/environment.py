import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from piperabm.boundary import Point
from piperabm.degradation import DegradationProperty, Eternal, DiracDelta
from piperabm.unit import Unit, DT, Date
from piperabm.tools import euclidean_distance



class Environment(DegradationProperty):
    """
    Manage settlements and their connecting links
    """

    def __init__(self):
        """
            node_types: node indexes gathered as list inside a dictionary based on their type
        """
        super().__init__()
        self.G = nx.Graph()
        self.node_types = {
            'settlement': [],
            'cross': [],
        }

    def all_index(self):
        """
        Aggregate all lists of nodes in self.node_types
        """
        all_index = []
        for key in self.node_types:
            all_index += self.node_types[key]
        return all_index

    def node_type(self, index):
        """
        Find node type based on its index
        """
        result = None
        for key in self.node_types:
            if index in self.node_types[key]:
                result = key
                break
        return result

    def find_next_index(self):
        """
        Check all indexes in self.node_types dictionary and suggest a new index
        """
        all = self.all_index()
        if len(all) > 0:
            max_index = max(all)
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
            pos: position of the settlement, [x, y]
            boundary: shape of settlement
            active: is it cuurently active? (True/False)
            initiation_date: the built date of settlement
            degradation_dist: the distribution for degradation of the settlement
        """
        create_node = True
        if self.find_node(pos, report=False) is not None:
            create_node = False
        if self.find_node(name, report=False) is not None:
            create_node = False

        if create_node is True:
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
            self.node_types['settlement'].append(index)
        else:
            print('duplicate settlement node data, node not created')

    def add_cross(
        self,
        name='',
        pos=[0, 0]
    ):
        """
        Add a new cross point
            name: name of the cross point, optional
            pos: position of the settlement, [x, y]
        """
        create_node = True
        if self.find_node(pos, report=False) is not None:
            create_node = False
        if self.find_node(name, report=False) is not None:
            create_node = False

        if create_node is True:
            index = self.find_next_index()
            boundary = Point()
            boundary.center = pos
            self.G.add_node(
                index,
                name=name,
                boundary=boundary
            )
            self.node_types['cross'].append(index)
            return index
        else:
            print('duplicate cross node data, node not created')
            return None

    def add_link(
        self,
        start,
        end,
        active=True,
        initiation_date=Date.today(),
        degradation_dist=Eternal(),
        length=None,
        difficulty=1
    ):
        """
        Add a link between *start* and *end*

        Args:
            start: starting point in the form of either index (as int), name (as str), or pos (as a [x,y] list)
            end: ending point in the form of either index (as int), name (as str), or pos (as a [x,y] list)
            active: is it still active? (True/False)
            initiation_date: the built date of settlement
            degradation_dist: the distribution for degradation of the settlement
            length: the length of the link, eucledian distance is used as default
            difficulty: difficulty of the link (unrelated to slope), default is 1
        """
        create_node = True
        start_index = self.find_node(start, report=False)
        if start_index is None:
            if isinstance(start, list):
                start_index = self.add_cross(pos=start)
            else:
                create_node = False
        end_index = self.find_node(end, report=False)
        if end_index is None:
            if isinstance(end, list):
                end_index = self.add_cross(pos=end)
            else:
                create_node = False

        if create_node is True:
            start_pos = self.G.nodes[start_index]['boundary'].center
            end_pos = self.G.nodes[end_index]['boundary'].center
            euclidean_length = euclidean_distance(*start_pos, *end_pos)
            if length is None or length < euclidean_length:
                length = euclidean_length  # default value
            self.G.add_edge(
                start_index,
                end_index,
                active=active,
                initiation_date=initiation_date,
                degradation_dist=degradation_dist,
                length=length,
                difficulty=difficulty
            )
        else:
            print('link creation failed.')

    def _update_all_edges(self, start_date, end_date, unit_length):
        """
        Check all edges to see whether they are active in the duration of time or not
            start_date: starting date of the time duration
            end_date: ending date of the time duration
            unit_length: unit_length for the degradation distribution
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
                active = self.is_active(
                    initiation_date, distribution, start_date, end_date, coeff)
                if active is False:
                    data['active'] = False

    def _update_all_nodes(self, start_date, end_date):
        """
        Check all nodes to see whether they are active in the duration of time or not
            start_date: starting date of the time duration
            end_date: ending date of the time duration
        """
        settlement_nodes = self.node_types['settlement']

    def update_elements(self, start_date, end_date, unit_length):
        """
        Update all elements during the *start_date* until *end_date*
        """
        self._update_all_edges(start_date, end_date, unit_length)
        self._update_all_nodes(start_date, end_date)

    def _find_node_by_name(self, name: str, report=True):
        """
        Find and return settlement node index by its name property
        """
        result = None
        if len(name) > 0:
            for index in self.G.nodes():
                if self.G.nodes[index]['name'] == name:
                    result = index
        if result is None and report is True:
            txt = name + ' not found.'
            print(txt)
        return result

    def _find_node_by_index(self, index: int, report=True):
        """
        Find and return node index (Check if it exists)
        """
        result = None
        if index in self.node_types.keys():
            result = index
        if result is None and report is True:
            txt = 'node_index ' + str(index) + ' not found.'
            print(txt)
        return result

    def _find_node_by_pos(self, pos: list, report=True):
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
        if result is None and report is True:
            txt = 'node position ' + str(pos) + ' not found.'
            print(txt)
        return result

    def find_node(self, input, report=True):
        """
        Find and return node index based on input (name, position, or index)
        """
        result = None
        if isinstance(input, str):
            result = self._find_node_by_name(input, report=report)
        elif isinstance(input, int):
            result = self._find_node_by_index(input, report=report)
        elif isinstance(input, list):
            result = self._find_node_by_pos(input, report=report)
        return result

    def random_settlement(self):
        settlement_list = self.node_types['settlement']
        rnd = np.random.choice(settlement_list, size=1)
        return rnd[0]

    def to_path(self):
        return Path(env=self)

    def show(self):
        """
        Show current state of Environment graph
        """
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
            node_type = self.node_type(index)
            if node_type == 'settlement':
                node_size.append(node_size_s)
            elif node_type == 'cross':
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
    def __init__(self, env: Environment):
        self.G = nx.DiGraph()
        self.to_path(env)

    def to_path(self, env: Environment):
        """
        Convert environment (current) information to path as a graph
        """

        def check_path_active(path, env: Environment):
            """
            Check all environment within a path to see if they are all active
            """
            path_active = True
            for i, _ in enumerate(path):
                if i > 0:
                    start = path[i-1]
                    end = path[i]
                    active = env.G[start][end]['active']
                    if active is False:
                        path_active = False
                        break
            return path_active

        def calculate_path_length(path, env: Environment):
            """
            Calculate the equivalent length of path
            """
            total_length = 0
            for i, _ in enumerate(path):
                if i > 0:
                    start = path[i-1]
                    end = path[i]
                    length = env.G[start][end]['length']
                    difficulty = env.G[start][end]['difficulty']
                    adjusted_length = length * difficulty
                    total_length += adjusted_length
            return total_length

        settlement_list = env.node_types['settlement']
        for index in settlement_list:
            node = env.G.nodes[index]
            name = node['name']
            pos = node['boundary'].center
            self.G.add_node(index, name=name, pos=pos)
            for other in settlement_list:
                if other != index and nx.has_path(env.G, source=index, target=other):
                    path = nx.shortest_path(env.G, source=index, target=other)
                    path_active = check_path_active(path, env)
                    if path_active is True:
                        length = calculate_path_length(path, env)
                        self.G.add_edge(index, other, path=path, length=length)

    def show(self):
        pos_dict = {}
        label_dict = {}
        for index in self.G.nodes():
            node = self.G.nodes[index]
            pos = node['pos']
            pos_dict[index] = pos
            label = node['name']
            label_dict[index] = label
        nx.draw_networkx(
            self.G,
            pos=pos_dict,
            labels=label_dict
        )
        plt.show()


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
        degradation_dist=DiracDelta(main=Unit(10, 'day').to('second').val)
    )
    env.add_settlement(
        name="Peter's Home",
        pos=[20, 20],
        boundary=Circular(radius=5),
        initiation_date=Date(2020, 1, 1),
        degradation_dist=DiracDelta(main=Unit(10, 'day').to('second').val)
    )
    # print(L.find_node("John's Home"))
    # print(L.find_node([2, 2]))
    # print(L.find_node(0))

    # L.add_link("John's Home", "Peter's Home")

    env.add_link(
        "John's Home",
        [20, 0],
        initiation_date=Date(2020, 1, 1),
        degradation_dist=DiracDelta(main=Unit(10, 'day').to('second').val)
    )
    env.add_link(
        [20.3, 0.3],
        "Peter's Home",
        initiation_date=Date(2020, 1, 1),
        degradation_dist=DiracDelta(main=Unit(10, 'day').to('second').val)
    )
    # L.add_link([2, 2], [22, 22])
    # L.add_link(0, 1)
    # print(L.G.edges())
    # L.show()

    # P = Path(L)
    # P.show()

    i = 0
    current_date = Date(2020, 1, 1)
    while i < 20:
        start_date = current_date
        end_date = current_date + DT(days=3)
        env.update_elements(start_date, end_date, unit_length=10)
        current_date += DT(days=1)
        i = i+1

    P = env.to_path()
    P.show()
    # L.show()
