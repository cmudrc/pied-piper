import os

from load import model
from piperabm.graphics import Animation


""" Aniamte model """
animation = Animation(path=os.path.dirname(os.path.realpath(__file__)))
deltas = model.load_deltas()
for delta in deltas:
    fig = model.fig()
    animation.add_figure(fig)
    model.apply_delta(delta)
animation.render(framerate=15)
