import networkx as nx
import matplotlib.pyplot as plt

from piperabm.infrastructure.style import infrastructure_style


class Graphics:

    def to_plt(self):
        # Nodes
        pos_dict = {}
        node_color_list = []
        node_size_list = []
        node_label_dict = {}
        nodes = self.nodes_id
        for node_id in nodes:
            # Position
            pos_dict[node_id] = self.pos(node_id)
            # Color
            color = infrastructure_style['node'][self.node_type(node_id)]['color']
            node_color_list.append(color)
            # Size
            size = infrastructure_style['node'][self.node_type(node_id)]['radius']
            node_size_list.append(size)
            # Label
            node_label_dict[node_id] = self.node_name(node_id)

        # Edges
        edge_color_list = []
        edges_ids = self.edges_ids
        for edge_ids in edges_ids:
            # Color
            color = infrastructure_style['edge'][self.edge_type(ids=edge_ids)]['color']
            edge_color_list.append(color)

        # Draw
        nx.draw_networkx(
            self.G,
            nodelist=nodes,
            pos=pos_dict,
            node_color=node_color_list,
            node_size=node_size_list,
            labels=node_label_dict,
            font_size=infrastructure_style['font'],
            edgelist=edges_ids,
            edge_color=edge_color_list
        )

    def show(self):
        ax = plt.gca()
        ax.set_aspect("equal")
        #mng = plt.get_current_fig_manager()
        #mng.full_screen_toggle()
        self.to_plt()
        plt.show()