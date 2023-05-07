from copy import deepcopy

from piperabm.society import Society
from piperabm.environment.samples import environment_0
from piperabm.economy.exchange_rate.samples import exchange_rate_0
from piperabm.society.agent.samples import agent_0, agent_1


society = Society(
    environment=deepcopy(environment_0),
    exchange_rate=deepcopy(exchange_rate_0)
)

agent_0 = deepcopy(agent_0)
society.add_agent_object(agent_0)

agent_1 = deepcopy(agent_1)
agent_1.origin = agent_0.origin # to become family
society.add_agent_object(agent_1)


if __name__ == "__main__":
    society.print()
