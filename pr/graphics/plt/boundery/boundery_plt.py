import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

from pr.tools.unit import Unit


style = {
    'fill': False,
    'linestyle': '--',
    'linewidth': None,
    'color': 'blue',
    'alpha': 0.5,
}


def circular_boundery_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    center = d['center']
    radius = d['radius']
    element = Circle(
        center,
        radius,
        **style
    )
    ax.add_patch(element)


def rectangular_boundery_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    center = d['center']
    width = d['width']
    height = d['height']
    theta = d['theta']
    element = Rectangle(
        center,
        width,
        height,
        angle=Unit(theta, 'rad').to('degree').val,
        **style
    )
    ax.add_patch(element)


def boundery_to_plt(dictionary: dict, ax=None):
    d = dictionary
    if d['type'] == 'circular':
        circular_boundery_to_plt(d, ax)
    elif d['type'] == 'rectangular':
        rectangular_boundery_to_plt(d, ax)
