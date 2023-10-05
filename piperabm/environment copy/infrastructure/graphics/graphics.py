import networkx as nx
import matplotlib.pyplot as plt

from piperabm.environment.infrastructure.graphics.style import style


class Graphics:
    """
    Add graphical representation, extends another class
    """

    def to_plt(self, ax=None):
        """
        Add elements to plt
        """

        if ax is None:
            ax = plt.gca()

        ''' draw nodes '''
        node_list = []
        pos_dict = {}
        node_color_list = []
        node_label_dict = {}

        for node_index in self.all_nodes():
            item = self.get_node_item(node_index)

            ''' index '''
            node_list.append(item.index)

            ''' pos '''
            pos_dict[node_index] = item.pos
 
            ''' color '''
            color = style['node'][item.type]['color']
            node_color_list.append(color)

            ''' label '''
            node_label_dict[node_index] = item.name

        ''' draw edges '''
        edge_list = []
        edge_color_list = []

        for edge_indexes in self.all_edges():
            item = self.get_edge_item(*edge_indexes)

            ''' indexes '''
            edge_list.append(edge_indexes)

            ''' color '''
            color = style['edge'][item.type]['color']
            edge_color_list.append(color)

        ''' add to plt '''
        nx.draw_networkx(
            self.G,
            nodelist=node_list,
            pos=pos_dict,
            node_color=node_color_list,
            labels=node_label_dict,
            edgelist=edge_list,
            edge_color=edge_color_list
        )

    def show(self):
        """
        Show the graph using matplotlib
        """
        self.to_plt()
        plt.show()