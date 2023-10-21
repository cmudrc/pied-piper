from copy import deepcopy

from piperabm.environment.samples import environment_0 as environment
from piperabm.society import Society


society = Society(
    gini = 0.5,
    gdp_per_capita=200
)
society.environment = environment


if __name__ == '__main__':
    society.print