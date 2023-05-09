import matplotlib.pyplot as plt
import networkx as nx

from piperabm.society.current_graph.graphics.style import style


class Graphics:
    """
    *** Extends CurrentGraph Class ***
    Add graphical representation
    """

    def to_plt(self, ax=None, filter='all'):
        """
        Add elements to plt
        """
        if ax is None:
            ax = plt.gca()
            
        G = self.to_multi_graph(filter)

        pos_dict = {}
        node_list = []
        node_color_list = []
        label_dict = {}
        edge_list = []
        edge_color_list = []
        
        ''' draw nodes '''
        for index in self.all_indexes():
            agent = self.get_node_object(index)           
            if agent is not None:
                ''' index '''
                node_list.append(index)

                ''' pos '''
                pos = self.get_node_pos(index)
                pos_dict[index] = pos
    
                ''' label '''
                label = agent.name
                label_dict[index] = label

                ''' color '''
                if agent.alive is True:
                    node_color = style['nodes']['agent']['color']['active']
                else:
                    node_color = style['nodes']['agent']['color']['inactive']
                node_color_list.append(node_color)
   
        ''' draw edges '''
        for start, end, relationship in G.edges(data=True):
            if relationship is not None:
                relationship_type = relationship['type']
                edge_list.append([start, end])
                color = style['edges'][relationship_type]['color']
                edge_color_list.append(color)

        nx.draw_networkx(
            G,
            #pos=pos_dict,
            nodelist=node_list,
            labels=label_dict,
            edgelist=edge_list,
            edge_color=edge_color_list,
            node_color=node_color_list
        )

    def show(self, filter='all'):
        """
        Show the graph using matplotlib
        """
        self.to_plt(filter=filter)
        plt.show()
