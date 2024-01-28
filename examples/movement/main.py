from piperabm.model.samples import model_2 as model
from piperabm.actions import Move
from piperabm.time import Date, DeltaTime
from piperabm.society.agent.samples import agent_0 as agent
from piperabm.graphics import Animation
import os


""" Setup model """
model.current_date = Date(2000, 1, 1)
model.set_step_size(DeltaTime(seconds=10))  # seconds


""" Create move action """
pos_start = [-60, 40]
pos_end = [200, 20]
infrastructure = model.infrastructure
nodes = infrastructure.all_nodes(type='settlement')
index_start, _ = infrastructure.find_nearest_node(pos_start, items=nodes)
index_end, _ = infrastructure.find_nearest_node(pos_end, items=nodes)
path = infrastructure.find_path(index_start, index_end)
action = Move(path)
#action.print

""" Add agent to model """
agent.home = index_start
model.add(agent)

#print(agent)
""" Add move action to agent within model """
agents = model.all_agents
agent = model.get(agents[0])
agent.queue.add(action)
#print(agent.queue)

print(agent.pos)

model.run(25)

print(agent.pos)

'''
""" Run model """
path = os.path.dirname(os.path.realpath(__file__))
animation = Animation(path)
#agent.resources.print
for _ in range(26):
    fig = model.fig()
    animation.add_figure(fig)
    model.update()
#agent.resources.print
animation.render()
'''