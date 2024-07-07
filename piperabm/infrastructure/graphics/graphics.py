import networkx as nx
import matplotlib.pyplot as plt

from piperabm.infrastructure.graphics.style import infrastructure_style


class Graphics:
    """
    Handle graphics
    """

    def fig(
            self,
            clf: bool = False
        ):
        """
        Add infrastructure elements to plt fig ax
        """
        if clf is True:
            plt.clf()
        ax = plt.gca()
        ax.set_aspect("equal")

        # Nodes
        pos_dict = {}
        node_color_list = []
        node_size_list = []
        node_label_dict = {}
        nodes = self.nodes
        for node_id in nodes:
            # Position
            pos_dict[node_id] = self.get_pos(id=node_id)
            # Color
            color = infrastructure_style['node'][self.get_node_type(node_id)]['color']
            node_color_list.append(color)
            # Size
            size = infrastructure_style['node'][self.get_node_type(node_id)]['radius']
            node_size_list.append(size)
            # Label
            node_label_dict[node_id] = self.get_node_name(id=node_id)

        # Edges
        edge_color_list = []
        edges = self.edges
        for edge_ids in edges:
            # Color
            color = infrastructure_style['edge'][self.get_edge_type(ids=edge_ids)]['color']
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
            edgelist=edges,
            edge_color=edge_color_list,
            ax=ax
        )
        return plt.gcf()

    def show(self):
        """
        Show infrastructure elements
        """
        fig = self.fig()
        plt.show()


if __name__ == "__main__":

    from piperabm.infrastructure.samples.infrastructure_2 import model

    model.infrastructure.show()