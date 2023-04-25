import matplotlib.pyplot as plt
import networkx as nx


class Graphics:
    """
    *** Extends CurrentGraph Class ***
    Add graphical representation
    """

    def to_plt(self, ax=None):
        """
        Add elements to plt
        """
        if ax is None:
            ax = plt.gca()

        node_size_dict = {
            'settlement': 300,
            'settlement_currently_inactive': 0,
            'cross': 0,
            'market': 500,
        }
        color = 'b'

        pos_dict = {}
        node_list = []
        node_size_list = []
        node_color_list = []
        label_dict = {}
        edge_list = []
        edge_color_list = []

        #print(self.all_nodes())

        for index in self.all_nodes():
            node_list.append(index)
            node_color_list.append(color)
            pos = self.node_info(index, 'pos')
            pos_dict[index] = pos
            label = self.node_info(index, 'name')
            node_type = self.node_info(index, 'type')
            if node_type == 'settlement':
                if self.node_info(index, 'currently_active'):
                    node_size = node_size_dict['settlement']
                    label_dict[index] = label
                else:
                    node_size = node_size_dict['settlement_currently_inactive']
                    label_dict[index] = ''
            elif node_type == 'cross':
                node_size = node_size_dict['cross']
                label_dict[index] = label
            elif node_type == 'market':
                node_size = node_size_dict['market']
                label_dict[index] = label
            node_size_list.append(node_size)

        for start, end in self.G.edges(data=False):
            edge_list.append([start, end])
            edge_color_list.append(color)

        nx.draw_networkx(
            self.G,
            pos=pos_dict,
            nodelist=node_list,
            node_size=node_size_list,
            labels=label_dict,
            edgelist=edge_list,
            edge_color=edge_color_list
        )

    def show(self):
        """
        Show the graph using matplotlib
        """
        self.to_plt()
        plt.show()
