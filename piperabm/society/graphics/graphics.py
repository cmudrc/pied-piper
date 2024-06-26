import networkx as nx
import matplotlib.pyplot as plt

from piperabm.society.graphics.style import society_style


class Graphics:
    """
    Handle graphics
    """

    def to_fig(
            self,
            ax,
            relationships=False
        ):
        """
        Add society elements to plt fig ax
        """
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
            colors = society_style["node"]["agent"]["color"]
            if self.get_alive(id=node_id) is True:
                color = colors['alive']
            else:
                color = colors['dead']
            node_color_list.append(color)
            # Size
            size = society_style["node"]["agent"]["size"]
            node_size_list.append(size)
            # Label
            node_label_dict[node_id] = self.get_node_name(id=node_id)

        # Edges
        edge_color_list = []
        edges = []
        if relationships is not False:
            for u, v, key, data in self.G.edges(keys=True, data=True):
                type = data['type']
                if (isinstance(relationships, list) and type in relationships) or \
                (relationships is True):
                    # Add edge to list
                    edges.append([u, v, key])
                    # Color
                    color = society_style['edge'][type]['color']
                    edge_color_list.append(color)

        # Draw
        nx.draw_networkx(
            self.G,
            nodelist=nodes,
            pos=pos_dict,
            node_color=node_color_list,
            node_size=node_size_list,
            labels=node_label_dict,
            font_size=society_style['font'],
            edgelist=edges,
            edge_color=edge_color_list,
            ax=ax
        )

    def show(self, relationships=True):
        """
        Show society elements
        """
        fig, ax = plt.subplots()
        self.to_fig(ax, relationships)
        plt.show()


if __name__ == "__main__":

    from piperabm.society.samples import model_2 as model

    model.society.show(relationships=['family'])