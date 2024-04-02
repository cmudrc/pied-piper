import matplotlib.pyplot as plt

from piperabm.society_new.style import society_style


class Graphics:

    def to_plt(self, agents_only=True):
        if agents_only is True:
            agents = self.agents
            xs = []
            ys = []
            agent_color_list = []
            for id in agents:
                agent = self.get(id)
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