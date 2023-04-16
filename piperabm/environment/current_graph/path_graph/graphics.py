import networkx as nx
import matplotlib.pyplot as plt


class Graphics:
    """
    Add graphical representation to the LinkGraph class
    """
    def show(self):
        """
        Show the graph using matplotlib
        """
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