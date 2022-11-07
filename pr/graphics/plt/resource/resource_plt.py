import matplotlib.pyplot as plt


style = {
    'width': 0.3,
    'color_good': 'b',
    'color_bad': 'r',
}

def use_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary

def produce_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary

def storage_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    footer = ['storage']
    ax.bar(
        footer,
        d['current_amount'],
        style['width'],
        color=style['color_good']
    )
    ax.bar(
        footer,
        d['max_amount'],
        style['width'],
        color=style['color_bad']
    )

def deficiency_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    footer = ['deficiency']
    ax.bar(
        footer,
        d['current_amount'],
        style['width'],
        color=style['color_bad']
    )
    ax.bar(
        footer,
        d['max_amount'],
        style['width'],
        color=style['color_good']
    )

def resource_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    if d['use'] is not None:
        pass
    if d['produce'] is not None:
        pass
    if d['storage'] is not None:
        pass
    if d['deficiency'] is not None:
        pass