import matplotlib.pyplot as plt


style = {
    'width': 0.25,
    'color_good': 'b',
    'color_bad': 'r',
}

def use_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    footer = ['use']
    ax.bar(
        footer,
        d['current_amount'],
        style['width'],
        color=style['color_bad']
    )

def produce_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    footer = ['produce']
    ax.bar(
        footer,
        d['current_amount'],
        style['width'],
        color=style['color_good']
    )

def storage_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    footer = ['storage']
    ax.bar(
        footer,
        d['max_amount'],
        style['width'],
        color=style['color_good'],
        fill=False
    )
    ax.bar(
        footer,
        d['current_amount'],
        style['width'],
        color=style['color_good']
    )

def deficiency_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    footer = ['deficiency']
    ax.bar(
        footer,
        d['max_amount'],
        style['width'],
        color=style['color_bad'],
        fill=False
    )
    ax.bar(
        footer,
        d['current_amount'],
        style['width'],
        color=style['color_bad']
    )

def resource_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    if d['use'] is not None:
        use_to_plt(d['use'], ax)
    if d['produce'] is not None:
        produce_to_plt(d['produce'], ax)
    if d['storage'] is not None:
        storage_to_plt(d['storage'], ax)
    if d['deficiency'] is not None:
        deficiency_to_plt(d['deficiency'], ax)