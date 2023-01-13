import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np
from copy import deepcopy

from piperabm.unit import Unit
from piperabm.tools import euclidean_distance


style_active = {
    'fill': False,
    'linestyle': '--',
    'linewidth': None,
    'color': 'blue',
    'alpha': 0.5,
}

style_inactive = deepcopy(style_active)
style_inactive['color'] = 'red'


def circular_boundery_to_plt(dictionary: dict, ax=None, active=True):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    center = d['center']
    radius = d['radius']
    if active is True:
        element = Circle(
            center,
            radius,
            **style_active
        )
    else:
        element = Circle(
            center,
            radius,
            **style_inactive
        )
    ax.add_patch(element)


def point_boundery_to_plt(dictionary: dict, ax=None, active=True):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    center = d['center']
    if active is True:
        color = style_active['color']
        ax.scatter(*center, c=color)
    else:
        color = style_inactive['color']
        ax.scatter(*center, c=color)


def rectangular_boundery_to_plt(dictionary: dict, ax=None, active=True):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    width = d['width']
    height = d['height']
    theta = d['theta']
    center_x = d['center'][0]
    center_y = d['center'][1]
    dist = euclidean_distance(height/2, width/2, 0, 0)
    phi = np.arctan(height/width)
    delta_x = dist * np.cos(theta + phi)
    delta_y = dist * np.sin(theta + phi)
    center = [0, 0]
    center[0] = center_x - delta_x
    center[1] = center_y - delta_y
    if active is True:
        element = Rectangle(
            center,
            width,
            height,
            angle=Unit(theta, 'rad').to('degree').val,
            **style_active
        )
    else:
        element = Rectangle(
            center,
            width,
            height,
            angle=Unit(theta, 'rad').to('degree').val,
            **style_inactive
        )
    ax.add_patch(element)


def boundery_to_plt(dictionary: dict, ax=None, active=True):
    d = dictionary
    if d['type'] == 'circular':
        circular_boundery_to_plt(d, ax, active)
    elif d['type'] == 'rectangular':
        rectangular_boundery_to_plt(d, ax, active)
    elif d['type'] == 'point':
        point_boundery_to_plt(d, ax, active)
