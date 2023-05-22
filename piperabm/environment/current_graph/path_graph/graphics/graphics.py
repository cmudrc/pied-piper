import matplotlib.pyplot as plt
import networkx as nx

from piperabm.environment.current_graph.path_graph.graphics.style import style


class Graphics:
    """
    *** Extends PathGraph Class ***
    Add graphical representation
    """

    def to_plt(self, ax=None):
        """
        Add elements to plt
        """
        if ax is None:
            ax = plt.gca()

        node_list = []
        node_size_list = []
        node_color_list = []
        label_dict = {}
        edge_list = []
        edge_color_list = []

        ''' draw nodes '''
        for index in self.all_indexes():
            ''' index '''
            node_list.append(index)

            ''' label, color, size '''
            object = self.get_node_object(index)
            node_type = object.type
            if node_type == 'settlement':
                settlement_style = style['nodes']['settlement']
                label = object.name
                node_size = settlement_style['radius']
                node_color = settlement_style['color']

            node_size_list.append(node_size)
            node_color_list.append(node_color)
            label_dict[index] = label

        ''' draw edges '''
        for edge in self.all_edges():
            edge_list.append(edge)
            color = style['edges']['color']
            edge_color_list.append(color)

        ''' add to plt '''
        nx.draw_networkx(
            self.G,
            nodelist=node_list,
            node_size=node_size_list,
            labels=label_dict,
            edgelist=edge_list,
            edge_color=edge_color_list,
            node_color=node_color_list
        )

    def show(self):
        """
        Show the graph using matplotlib
        """
        self.to_plt()
        plt.show()

        
