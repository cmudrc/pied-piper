import matplotlib.pyplot as plt
from matplotlib.patches import Circle


style = {
    'fill': True,
    'linestyle': '--',
    'linewidth': None,
    'color': 'blue',
    'alpha': 0.5,
}

def agent_to_plt(dictionary: dict, ax=None):
    d = dictionary
    pos = d['pos']
    radius = 5
    circle = Circle(
        pos,
        radius,
        **style
    )
    if ax is None:
        plt.gca().add_patch(circle)
    else:
        ax.add_patch(circle)
    