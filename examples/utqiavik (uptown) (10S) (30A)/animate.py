import os

from load_initial import model
from piperabm.graphics import Animation


""" Aniamte model """
animation = Animation(path=os.path.dirname(os.path.realpath(__file__)))
deltas = model.load_deltas()
for delta in deltas:
    fig = model.fig()
    animation.add_figure(fig)
    model.apply_delta(delta)
animation.render(framerate=15)
'''
ids = model.infrastructure_edges
degs = []
for id in ids:
    object = model.get(id)
    deg = object.degradation.factor
    degs.append(deg)
print(max(degs))
'''
