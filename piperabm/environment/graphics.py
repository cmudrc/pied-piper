import matplotlib.pyplot as plt
import networkx as nx

from piperabm.tools import ElementExists


class Graphics:
    """
    Contains methods for Environment class
    """
    pass
    '''
    def to_plt(self, ax=None, start_date=None, end_date=None):
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
        node_size_dict = {
            'settlement': 300,
            'cross': 0,
            'market': 500,
        }
        color_dict = {
            'active': 'b',
            'inactive': 'r',
        }
        edge_list = []
        edge_color_list = []

        def node_exists(node, start_date=None, end_date=None):
            """
            Check if node exists in the stated date
            """
            initiation_date = node['initiation_date']
            return check_existance(initiation_date, start_date, end_date)

        def edge_exists(data, start_date=None, end_date=None):
            """
            Check if edge exists in the stated date
            """
            initiation_date = data['initiation_date']
            return check_existance(initiation_date, start_date, end_date)

        for index in self.node_types['settlement']:
            node = self.G.nodes[index]
            if node_exists(node, start_date, end_date):
                node_list.append(index)
                pos = node['boundary'].center
                pos_dict[index] = pos
                label = node['name']
                label_dict[index] = label
                if node['active'] is True:
                    node_color_list.append(color_dict['active'])
                elif node['active'] is False:
                    node_color_list.append(color_dict['inactive'])
                node_size_list.append(node_size_dict['settlement'])

        for index in self.node_types['cross']:
            node = self.G.nodes[index]
            node_list.append(index)
            pos = node['boundary'].center
            pos_dict[index] = pos
            label = node['name']
            label_dict[index] = label
            node_color_list.append(color_dict['active'])
            node_size_list.append(node_size_dict['cross'])

        for index in self.node_types['market']:
            node = self.G.nodes[index]
            if node_exists(node, start_date, end_date):
                node_list.append(index)
                pos = node['boundary'].center
                pos_dict[index] = pos
                label = node['name']
                label_dict[index] = label
                if node['active'] is True:
                    node_color_list.append(color_dict['active'])
                elif node['active'] is False:
                    node_color_list.append(color_dict['inactive'])
                node_size_list.append(node_size_dict['market'])

        for start, end, data in self.G.edges(data=True):
            if edge_exists(data, start_date, end_date):
                edge_list.append([start, end])
                if data['active'] is True:
                    edge_color_list.append(color_dict['active'])
                elif data['active'] is False:
                    edge_color_list.append(color_dict['inactive'])

        nx.draw_networkx(
            self.G,
            pos=pos_dict,
            nodelist=node_list,
            node_size=node_size_list,
            labels=label_dict,
            edgelist=edge_list,
            edge_color=edge_color_list
        )

    def show(self, start_date, end_date):
        """
        Show current state of Environment graph
        """
        self.to_plt(start_date=start_date, end_date=end_date)
        plt.show()
    '''
