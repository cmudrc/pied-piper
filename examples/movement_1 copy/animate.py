from load import model
from piperabm.graphics import Animation


""" Aniamte model """

deltas = model.load_deltas()
#agent = model.get(0)
#print(agent.pos)
model.apply_delta(deltas[0])
model.apply_delta(deltas[1])
#print(deltas[0])
#print(deltas[1])
##agent = model.get(0)
#print(agent.pos)
#for delta in deltas:
#    model.apply_delta(delta)
#model.show()
'''
animation = Animation(path=model.path)
for delta in deltas:
    fig = model.fig()
    animation.add_figure(fig)
    model.apply_delta(delta)
animation.render(framerate=15)
'''