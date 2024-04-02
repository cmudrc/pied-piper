from piperabm.infrastructure_new.samples import infrastructure_1 as infrastructure
from piperabm.model_new import Model
from piperabm.society_new import Agent
from piperabm.actions import Stay, Move
from piperabm.time import DeltaTime


id_agent = 0
id_start = 1
id_end = 2

model = Model(
    infrastructure=infrastructure,
    step_size=1
)

# Actions
paths = model.infrastructure.paths()
path = paths.path(id_start, id_end)
action_1 = Stay(duration=DeltaTime(seconds=5))
path = paths.path(id_start, id_end)
action_2 = Move(path)
action_3 = Stay(duration=DeltaTime(seconds=5))
path = paths.path(id_end, id_start)
action_4 = Move(path)
action_5 = Stay(duration=DeltaTime(seconds=100))
actions = [action_1, action_2, action_3, action_4, action_5]

# Agent
agent = Agent()
agent.home = id_start
model.society.add(agent)
agent.queue.add(actions)


if __name__ == "__main__":
    import os

    model.path = os.path.dirname(os.path.realpath(__file__))
    
    # Run model
    #print(agent.pos)
    model.save()
    model.run(n=140, report=False, save=True)
    #print(agent.pos)
