from copy import deepcopy

from piperabm.unit import Date
from piperabm.actions import Stay
from piperabm.environment.samples import environment_1


env = deepcopy(environment_1)
action_start_date = Date(2020, 1, 5)
env.update(
    start_date=Date(2020, 1, 1),
    end_date=action_start_date
)

action = Stay(
    start_date=action_start_date,
    environment=env,
    agent_index=0
)


if __name__ == "__main__":
    print(action)