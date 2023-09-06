from copy import deepcopy

from piperabm.unit import Date
from piperabm.actions import Move
from piperabm.agent.config import Walk
from piperabm.environment_old.samples import environment_1


env = deepcopy(environment_1)
action_start_date = Date(2020, 1, 5)
env.update(
    start_date=Date(2020, 1, 1),
    end_date=action_start_date
)

action = Move(
    start_date=action_start_date,
    path=[(0, 2), (2, 1)],
    transportation=Walk(),
    environment=env,
    agent_index=0
)


if __name__ == "__main__":
    print(action)