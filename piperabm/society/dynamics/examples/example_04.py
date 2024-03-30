from piperabm.society.dynamics.friedkin import Friedkin


influence = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
opinions_initial = [
    [0.8, 0.1, 0.1],
    [0.25, 0.5, 0.25],
    [0.2, 0.4, 0.4],
]
solver = Friedkin(influence, opinions_initial)
solver.solve(report=True)
print(solver.opinions)