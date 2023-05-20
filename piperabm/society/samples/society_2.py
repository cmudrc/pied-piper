from copy import deepcopy

from piperabm.society import Society
from piperabm.environment.samples import environment_1
from piperabm.economy.exchange_rate.samples import exchange_rate_0
from piperabm.agent.samples import agent_0


society = Society(
    environment=deepcopy(environment_1),
    exchange_rate=deepcopy(exchange_rate_0)
)

agent_0 = deepcopy(agent_0)
society.add_agent_object(agent_0)


if __name__ == "__main__":
    society.print()
