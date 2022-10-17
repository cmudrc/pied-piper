import matplotlib.pyplot as plt


def draw_agent(agent):
    ''' Draw agent '''
    circle = plt.Circle(
        xy=agent.pos,
        radius=0.05,
        color='red',
        fill=True,
    )
    plt.gca().add_patch(circle)
    
    ''' Draw agent's name '''
    plt.text(
        x=agent.pos[0],
        y=agent.pos[1]-0.05,
        s=agent.name,
        verticalalignment='center',
        horizontalalignment='center',
        fontsize=8
    )
