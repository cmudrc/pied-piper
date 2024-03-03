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
        self.font_size = 8

    def infrastructure_to_plt(self):
        """
        Draw infrastructure
        """
        # Nodes
        infrastructure_style = style['infrastructure']
        pos_dict = {}
        node_color_list = []
        node_size_list = []
        node_label_dict = {}
        nodes = self.infrastructure.nodes_id
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

        edge_color_list = []
        edges_ids = self.infrastructure.edges_ids
        edges_id = self.infrastructure.edges_id
        for edge_id in edges_id:
            item = self.infrastructure.get(edge_id)
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
            font_size=self.font_size,
            edgelist=edges_ids,
            edge_color=edge_color_list
        )

    def society_to_plt(self):
        society_style = style['society']
        agents = self.society.agents
        xs = []
        ys = []
        agent_color_list = []
        for id in agents:
            agent = self.society.get(id)
            pos = agent.pos
            xs.append(pos[0])
            ys.append(pos[1])
            colors = society_style["node"]["agent"]["color"]
            if agent.alive is True:
                color = colors['alive']
            else:
                color = colors['dead']
            agent_color_list.append(color)

        #agent_color = society_style["node"]["agent"]["color"]
        agent_shape = society_style["node"]["agent"]["shape"]
        agent_size = society_style["node"]["agent"]["size"]

        ax = plt.gca()
        ax.scatter(
            xs,
            ys,
            color=agent_color_list,
            s=agent_size,
            marker=agent_shape,
        )

    def fig(self):
        plt.clf()
        ax = plt.gca()
        ax.set_aspect("equal")
        if self.infrastructure is not None:
            margins = self.infrastructure.margins
            xlim = [margins['x']['min'], margins['x']['max']]
            ylim = [margins['y']['min'], margins['y']['max']]
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)
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
