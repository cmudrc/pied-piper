import os

from piperabm.model import Model
from piperabm.infrastructure import Road, Settlement
from piperabm.society import Agent
from piperabm.actions.movement import Move
from piperabm.matter import Containers, Matter
from piperabm.time import Date, DeltaTime
from piperabm.graphics import Animation


""" Setup model """
id_agent = 0
id_start = 1
id_end = 2
pos_start = [0, 0]
pos_end = [5000, 0]
average_resources = Containers(
    Matter('food', 0.2),
    Matter('water', 0.2),
    Matter('energy', 0.2)
)
model = Model(
    proximity_radius=1,  # Meters
    step_size=DeltaTime(seconds=100),  # Seconds
    current_date=Date(2000, 1, 1),
    average_income=100,  # Dollars per month
    average_resources=average_resources,
    name="Sample Model"
)
road = Road(
    pos_1=pos_start,
    pos_2=pos_end,
    roughness=2
)
settlement_1 = Settlement(pos=pos_start, name="start")
settlement_1.id = id_start
settlement_2 = Settlement(pos=pos_end, name="end")
settlement_2.id = id_end
model.add(road, settlement_1, settlement_2)
model.bake(save=False)

""" Create move action """
infrastructure = model.infrastructure
path = infrastructure.find_path(id_start, id_end)
action = Move(path)

""" Add agent to model """
agent = Agent()
agent.home = id_start
agent.id = id_agent
model.add(agent)

""" Add move action to agent within model """
agent = model.get(id_agent)
agent.queue.add(action)

""" Run model """
animation = Animation(path=os.path.dirname(os.path.realpath(__file__)))
for _ in range(80):
    fig = model.fig()
    animation.add_figure(fig)
    model.update()
animation.render(framerate=15)
