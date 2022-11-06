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

def circular_boundery_to_plt(dictionary: dict):
    d = dictionary
    center = d['center']
    radius = d['radius']
    circle = Circle(
        center,
        radius,
        **style
    )
    plt.gca().add_patch(circle)

def rectangular_boundery_to_plt(dictionary: dict):
    d = dictionary
    center = d['center']
    width = d['width']
    height = d['height']
    theta = d['theta']
    rectangle = Rectangle(
        center,
        width,
        height,
        angle=Unit(theta, 'rad').to('degree').val,
        **style
    )
    plt.gca().add_patch(rectangle)

def boundery_to_plt(dictionary: dict):
    d = dictionary
    if d['type'] == 'circular':
        circular_boundery_to_plt(d)
    elif d['type'] == 'rectangular':
        rectangular_boundery_to_plt(d)