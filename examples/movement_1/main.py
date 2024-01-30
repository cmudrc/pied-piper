import os

from piperabm.model import Model
from piperabm.infrastructure import Road, Settlement
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
model = Model(
    proximity_radius=1,  # Meters
    step_size=DeltaTime(seconds=100),  # Seconds
    current_date=Date(2000, 1, 1),
    average_income=100,  # Dollars per month
    average_resources=average_resources,
    gini_index=0,
    name="Sample Model"
)
pos_start = [0, 0]
pos_end = [5000, 0]
road = Road(
    pos_1=pos_start,
    pos_2=pos_end,
    roughness=2
)
settlement_1 = Settlement(pos=pos_start, name="start")
settlement_2 = Settlement(pos=pos_end, name="end")
model.add(road, settlement_1, settlement_2)
model.apply_grammars()

""" Create move action """
infrastructure = model.infrastructure
nodes = infrastructure.all_nodes(type='settlement')
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
for _ in range(80):
    fig = model.fig()
    animation.add_figure(fig)
    model.update()
#agent.resources.print
animation.render(framerate=15)

#model.show()