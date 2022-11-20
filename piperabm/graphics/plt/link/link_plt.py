import matplotlib.pyplot as plt
import matplotlib.lines as lines
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

def link_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    pos = d['pos']
    active = d['active']
    size = 10
    if active is True:
        color = style_active['color']
        line = lines.Line2D([0*cm, 1.5*cm], [0*cm, 2.5*cm],
                    lw=2, color='black', axes=ax)
        ax.add_line(line)
    else:
        color = style_inactive['color']
        ax.add_line(line)

def track_to_plt(dictionary: dict, ax=None):
    pass