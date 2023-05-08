import matplotlib.pyplot as plt
import networkx as nx

from piperabm.environment.current_graph.graphics.style import style


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

        pos_dict = {}
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

            ''' pos '''
            pos = self.get_node_pos(index)
            pos_dict[index] = pos
 
            ''' label, color, size '''
            structure = self.get_node_object(index)           
            if structure is not None:
                node_type = structure.type
                if node_type == 'settlement':
                    settlement_style = style['nodes']['settlement']
                    label = structure.name
                    if structure.active is True:
                        node_size = settlement_style['radius']['active']
                        node_color = settlement_style['color']['active']
                    else:
                        node_size = settlement_style['radius']['inactive']
                        node_color = settlement_style['color']['active']
            else: # hub
                hub_style = style['nodes']['hub']
                node_size = hub_style['radius']
                label = ''
                node_color = hub_style['color']
            node_size_list.append(node_size)
            node_color_list.append(node_color)
            label_dict[index] = label

        ''' draw edges '''
        for edge in self.all_edges():
            edge_list.append(edge)
            structure = self.get_edge_object(edge[0], edge[1])
            edge_type = structure.type
            if edge_type == 'road':
                road_style = style['edges']['road']
                if structure.active is True:
                    color = road_style['color']['active']
                else:
                    color = road_style['color']['inactive']
            edge_color_list.append(color)

        ''' add to plt '''
        nx.draw_networkx(
            self.G,
            pos=pos_dict,
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
