import matplotlib.pyplot as plt
from matplotlib.patches import Circle


style = {
    'fill': True,
    'linestyle': '--',
    'linewidth': None,
    'color': 'blue',
    'alpha': 0.5,
}

def agent_to_plt(dictionary: dict):
    d = dictionary
    pos = d['pos']
    radius = 5
    circle = Circle(
        pos,
        radius,
        **style
    )
    plt.gca().add_patch(circle)
    