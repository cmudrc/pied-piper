import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from copy import deepcopy


style_active = {
    'fill': True,
    'linestyle': '--',
    'linewidth': None,
    'color': 'green',
    'alpha': 0.5,
}
style_inactive = deepcopy(style_active)
style_inactive['color'] = 'black'

def agent_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    pos = d['pos']
    active = d['active']
    size = 10
    if active is True:
        color = style_active['color']
        ax.scatter(*pos, c=color, s=size)
    else:
        color = style_inactive['color']
        ax.scatter(*pos, c=color, s=size)