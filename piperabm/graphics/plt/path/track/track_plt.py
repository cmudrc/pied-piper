import matplotlib.pyplot as plt
import matplotlib.lines as lines
from copy import deepcopy


def track_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    if d['type'] == 'linear':
        linear_to_plt(d, ax)

def linear_to_plt(dictionary: dict, ax=None):
    d = dictionary
    pos_start = d['pos_start']
    pos_end = d['pos_end']
    x_list = [pos_start[0], pos_end[0]]
    y_list = [pos_start[1], pos_end[1]]
    active = d['active']
    size = 10
    if active is True:
        color = 'blue'
    else:
        color = 'red'
    #ax.scatter(*pos_start, c=color, s=size)
    #ax.scatter(*pos_end, c=color, s=size)
    line = lines.Line2D(
        x_list,
        y_list,
        lw=1,
        color=color,
        axes=ax,
        linestyle='--',
    )
    ax.add_line(line)