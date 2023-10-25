from copy import deepcopy

from piperabm.society.agent.samples import agent_0, agent_1
from piperabm.model.samples import model_0


model = deepcopy(model_0)
agent_0 = deepcopy(agent_0)
agent_1 = deepcopy(agent_1)
model.add(agent_0)
model.add(agent_1)


if __name__ == "__main__":
    #model.print
    model.run(100)
    print(model.all_alive_agents)
    model.run(900)
    print(model.all_alive_agents)
