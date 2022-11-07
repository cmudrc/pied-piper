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
    if ax is None:
        ax = plt.gca()
    d = dictionary
    pos = d['pos']
    radius = 5
    element = Circle(
        pos,
        radius,
        **style
    )
    plt.gca().add_patch(element)