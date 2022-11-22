import matplotlib.pyplot as plt
import matplotlib.lines as lines

try:
    from .track import track_to_plt
except:
    from track import track_to_plt


def path_to_plt(dictionary: dict, ax=None):
    if ax is None:
        ax = plt.gca()
    d = dictionary
    tracks = d['tracks']
    for track_dict in tracks:
        track_to_plt(track_dict, ax)