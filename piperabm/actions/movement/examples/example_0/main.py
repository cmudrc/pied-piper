from piperabm.model.samples import model_1 as model
from piperabm.society import Agent
from piperabm.actions import Move, Stay
from piperabm.time import DeltaTime


""" Setup model """
id_agent = 0
id_start = 1
id_end = 2
model.set_step_size(DeltaTime(seconds=1))

""" Create move action """
action_1 = Stay(duration=DeltaTime(seconds=5))
infrastructure = model.infrastructure
paths = infrastructure.paths
path_1 = paths.path(id_start, id_end)
action_2 = Move(path_1)
path_2 = paths.path(id_end, id_start)
action_3 = Move(path_2)

""" Add agent to model """
agent = Agent()
agent.home = id_start
agent.id = id_agent
model.add(agent)

""" Add move action to agent within model """
agent = model.get(id_agent)
agent.queue.add(action_1, action_2, action_1, action_3)
#agent.queue.add(action_1)

if __name__ == "__main__":
    """ Run model """
    print(agent.pos)
    model.run(n=6)
    print(agent.pos)