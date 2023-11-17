import networkx as nx
import matplotlib.pyplot as plt

from piperabm.model.graphics.style import style


class Graphics:
    """
    Add graphical representation, extends another class
    """

    def __init__(self, infrastructure=None, society=None):
        self.infrastructure = infrastructure
        self.society = society

    def infrastructure_to_plt(self):
        """
        Draw infrastructure
        """
        """ Nodes """
        nodes = self.infrastructure.all_nodes()
        pos_dict = {}
        node_color_list = []
        node_label_dict = {}
        for node_index in nodes:
            item = self.infrastructure.get(node_index)
            """ pos """
            pos_dict[node_index] = item.pos
            """ color """
            color = style['node'][item.type]['color']
            node_color_list.append(color)
            """ label """
            node_label_dict[node_index] = item.name

        edges = self.infrastructure.all_edges()
        edge_color_list = []
        for edge_indexes in edges:
            edge_index = self.infrastructure.find_edge_index(*edge_indexes)
            item = self.infrastructure.get(edge_index)
            """ color """
            color = style['edge'][item.type]['color']
            edge_color_list.append(color)

        nx.draw_networkx(
            self.infrastructure.G,
            nodelist=nodes,
            pos=pos_dict,
            node_color=node_color_list,
            labels=node_label_dict,
            edgelist=edges,
            edge_color=edge_color_list
        )

    def show(self):
        """
        Show the graph using matplotlib
        """
        plt.gca().set_aspect("equal")
        self.infrastructure_to_plt()
        plt.show()
