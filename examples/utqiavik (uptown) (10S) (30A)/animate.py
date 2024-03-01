import os

from create_society import model
from piperabm.graphics import Animation


""" Run model """
model.set_step_size(10)

animation = Animation(path=os.path.dirname(os.path.realpath(__file__)))
for _ in range(100):
    fig = model.fig()
    animation.add_figure(fig)
    model.update()
animation.render(framerate=15)
