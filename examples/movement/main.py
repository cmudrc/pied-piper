import os

from piperabm.model.samples import model_2 as model
from piperabm.society import Agent
from piperabm.actions import Move
from piperabm.time import Date, DeltaTime
from piperabm.matter import Containers, Matter
#from piperabm.society.agent.samples import agent_0 as agent
from piperabm.graphics import Animation


""" Setup model """
food = Matter('food', 0.2)
water = Matter('water', 0.2)
energy = Matter('energy', 0.2)
average_resources = Containers(food, water, energy)
model.average_resources = average_resources
model.average_income = 100
model.gini_index = 0
model.set_step_size(DeltaTime(seconds=10))  # seconds

""" Create move action """
infrastructure = model.infrastructure
nodes = infrastructure.all_nodes(type='settlement')
pos_start = [-60, 40]
pos_end = [200, 20]
index_start, _ = infrastructure.find_nearest_node(pos_start, items=nodes)
index_end, _ = infrastructure.find_nearest_node(pos_end, items=nodes)
path = infrastructure.find_path(index_start, index_end)
action = Move(path)

""" Add agent to model """
agent = Agent()
agent.home = index_start
model.add(agent)

""" Add move action to agent within model """
agents = model.all_agents
agent = model.get(agents[0])
agent.queue.add(action)

""" Run model """
path = os.path.dirname(os.path.realpath(__file__))
animation = Animation(path)
#agent.resources.print
for _ in range(30):
    fig = model.fig()
    animation.add_figure(fig)
    model.update()
#agent.resources.print
animation.render(framerate=15)

#model.show()