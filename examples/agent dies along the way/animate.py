from load import model
from piperabm.graphics import Animation


""" Aniamte model """

deltas = model.load_deltas()

animation = Animation(path=model.path)
for delta in deltas:
    fig = model.fig()
    animation.add_figure(fig)
    model.apply_delta(delta)
animation.render(framerate=15)
