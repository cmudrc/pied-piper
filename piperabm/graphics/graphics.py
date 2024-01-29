import networkx as nx
import matplotlib.pyplot as plt

from piperabm.graphics.style import style


class Graphics:
    """
    Add graphical representation
    """

    def __init__(self, infrastructure=None, society=None):
        self.infrastructure = infrastructure
        self.society = society

    def infrastructure_to_plt(self):
        """
        Draw infrastructure
        """
        # Nodes
        infrastructure_style = style['infrastructure']
        nodes = self.infrastructure.all_nodes()
        pos_dict = {}
        node_color_list = []
        node_size_list = []
        node_label_dict = {}
        for node_index in nodes:
            item = self.infrastructure.get(node_index)
            # Position
            pos_dict[node_index] = item.pos
            # Color
            color = infrastructure_style['node'][item.type]['color']
            node_color_list.append(color)
            # Size
            size = infrastructure_style['node'][item.type]['radius']
            node_size_list.append(size)
            # Label
            node_label_dict[node_index] = item.name
        font_size = 8 #

        edges = self.infrastructure.all_edges()
        edge_color_list = []
        for edge_indexes in edges:
            edge_index = self.infrastructure.find_edge_index(*edge_indexes)
            item = self.infrastructure.get(edge_index)
            # Color
            color = infrastructure_style['edge'][item.type]['color']
            edge_color_list.append(color)

        nx.draw_networkx(
            self.infrastructure.G,
            nodelist=nodes,
            pos=pos_dict,
            node_color=node_color_list,
            node_size=node_size_list,
            labels=node_label_dict,
            font_size=font_size,
            edgelist=edges,
            edge_color=edge_color_list
        )

    def society_to_plt(self):
        society_style = style['society']
        agents = self.society.agents
        xs = []
        ys = []
        for index in agents:
            item = self.society.get(index)
            pos = item.pos
            xs.append(pos[0])
            ys.append(pos[1])

        agent_color = society_style["node"]["agent"]["color"]
        agent_shape = society_style["node"]["agent"]["shape"]
        agent_size = society_style["node"]["agent"]["size"]

        ax = plt.gca()
        ax.scatter(
            xs,
            ys,
            color=agent_color,
            s=agent_size,
            marker=agent_shape,
        )

    def fig(self):
        plt.clf()
        ax = plt.gca()
        ax.set_aspect("equal")
        xlim, ylim = self.infrastructure.xylim()
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        if self.infrastructure is not None:
            self.infrastructure_to_plt()
        if self.society is not None:
            self.society_to_plt()
        return plt.gcf()

    def show(self):
        """
        Show the graph using matplotlib
        """
        fig = self.fig()
        plt.show()
