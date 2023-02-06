import networkx as nx
import matplotlib.pyplot as plt

from piperabm import Environment
from piperabm.unit import DT, Date
from piperabm.asset import Asset, Resource
from piperabm.actions import Queue, Move


class Society:
    def __init__(self, env: Environment):
        self.env = env
        self.G = nx.Graph()
        self.index_list = []

    def find_next_index(self):
        """
        Check self.index_list (indexes) and suggest a new index
        """
        index_list = self.index_list
        if len(index_list) > 0:
            max_index = max(index_list)
            new_index = max_index + 1
        else:
            new_index = 0
        return new_index

    def add_agent(self, name='', settlement=None, queue=Queue(), asset=None):
        """
        Add a new agent to the society
        """
        index = self.find_next_index()
        self.index_list.append(index)
        if settlement is None:
            settlement_index = self.env.random_settlement()
        else:
            settlement_index = self.env.find_node(settlement)
        settlement_node = self.env.G.nodes[settlement_index]
        pos = settlement_node['boundary'].center
        self.G.add_node(
            index,
            name=name,
            settlement=settlement_index,
            pos=pos,
            active=True,
            queue=queue,
            asset=asset
            )

    def update_elements(self, start_date, end_date):
        """
        Update all elements
        """
        self._update_all_nodes(start_date, end_date)

    def _update_all_nodes(self, start_date, end_date):
        """
        Update all agents
            start_date: starting date of the time duration
            end_date: ending date of the time duration
        """
        for index in self.G.nodes():
            node = self.G.nodes[index]
            queue = node['queue']
            result, action_type = queue.execute(end_date)
            if action_type == "pos":
                node['pos'] = result

    def add_agents(self, n):
        for _ in range(n):
            self.add_agent()

    def path_to_pos(self, path: list):
        """
        Convert edge path data to a list of pos
        """
        pos_list = []
        for index in path:
            node = self.env.G.nodes[index]
            pos = node['boundary'].center
            pos_list.append(pos)
        return pos_list

    def path_real_length_list(self, path: list):
        """
        Convert edge path data to a list of real length
        """
        real_length_list = []
        for index in path:
            node = self.env.G.nodes[index]
            length = node['length']
            real_length_list.append(length)
        return real_length_list

    def to_plt(self, ax=None):
        """
        Add elements to plt
        """
        if ax is None:
            ax = plt.gca()
        pos_dict = {}
        node_list = []
        node_size_list = []
        node_color_list = []
        label_dict = {}
        node_size = 200
        color_dict = {
            'active': 'green',
            'inactive': 'black',
        }

        for index in self.index_list:
            node = self.G.nodes[index]
            node_list.append(index)
            pos = node['pos']
            pos_dict[index] = pos
            node_size_list.append(node_size)
            label_dict[index] = node['name']
            if node['active'] == True:
                node_color_list.append(color_dict['active'])
            else:
                node_color_list.append(color_dict['inactive'])

        nx.draw_networkx(
            self.G,
            pos=pos_dict,
            nodelist=node_list,
            node_size=node_size_list,
            labels=label_dict
        )

    def show(self, start_date, end_date):
        """
        Show current state of Environment graph
        """
        self.to_plt(start_date=start_date, end_date=end_date)
        plt.show()

if __name__ == "__main__":
    from piperabm.unit import Unit, Date
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
