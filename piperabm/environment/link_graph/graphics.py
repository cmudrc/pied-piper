import matplotlib.pyplot as plt
import networkx as nx


class Graphics:
    """
    Contains methods for LinkGraph class
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

        for index in self.env.all_nodes():
            node_list.append(index)
            boundary = self.env.node_info(index, 'boundary')
            pos = boundary.center
            pos_dict[index] = pos
            label = self.env.node_info(index, 'name')
            label_dict[index] = label
            node_color_list.append(color)
            node_type = self.env.node_type(index)
            if node_type == 'settlement':
                node_size_list.append(node_size_dict['settlement'])
            elif node_type == 'cross':
                node_size_list.append(node_size_dict['cross'])
            elif node_type == 'market':
                node_size_list.append(node_size_dict['market'])

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
