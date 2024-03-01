import os

from piperabm.graphics import Animation
from main import model


""" Run model """
animation = Animation(path=os.path.dirname(os.path.realpath(__file__)))
for _ in range(100):
    fig = model.fig()
    animation.add_figure(fig)
    model.update()
animation.render(framerate=15)
