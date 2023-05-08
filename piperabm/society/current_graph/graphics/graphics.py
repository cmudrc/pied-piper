import matplotlib.pyplot as plt
import networkx as nx

from piperabm.society.current_graph.graphics.style import style


class Graphics:
    """
    *** Extends CurrentGraph Class ***
    Add graphical representation
    """

    def to_plt(self, ax=None, relationships='all'):
        """
        Add elements to plt
        """
        if ax is None:
            ax = plt.gca()

        def create_multi_graph(self):
            G = nx.MultiGraph()
            for edge in self.all_edges():
                start_index = edge[0]
                end_index = edge[1]
                relationships = self.society.get_edge_object(start_index, end_index)
                for relationship in relationships:
                    G.add_edge(edge[0], edge[1], type=relationship)
            return G
            
        G = create_multi_graph(self)

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
    
                ''' label, color '''
                label = agent.name
                if agent.alive is True:
                    node_color = style['nodes']['agent']['color']['active']
                else:
                    node_color = style['nodes']['agent']['color']['inactive']
                node_color_list.append(node_color)
                label_dict[index] = label
   
        ''' draw edges '''
        for start, end, relationship in G.edges(data=True):
            if relationship is not None:
                edge_list.append([start, end])
                relationship_type = relationship['type']
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

    def show(self):
        """
        Show the graph using matplotlib
        """
        self.to_plt()
        plt.show()
