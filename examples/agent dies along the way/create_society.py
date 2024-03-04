from piperabm.society import Agent
from piperabm.actions import Move
from load import model


id_agent = 0
id_start = 1
id_end = 2

""" Create agent """
agent = Agent()
agent.home = id_start
agent.id = id_agent

""" Create move action """
infrastructure = model.infrastructure
path = infrastructure.find_path(id_start, id_end)
action = Move(path)
agent.queue.add(action)

""" Add agent to model """
model.add(agent)

model.save_initial()