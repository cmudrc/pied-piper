from copy import deepcopy

from piperabm.society.dynamics.friedkin import Friedkin


influence = [
    [0.8, 0.1, 0.1],
    [0.25, 0.5, 0.25],
    [0.2, 0.4, 0.4],
]
opinions_initial = deepcopy(influence)

solver = Friedkin(influence, opinions_initial)
solver.solve(report=True)
print(solver.opinions)