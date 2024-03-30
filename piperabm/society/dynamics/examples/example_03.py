from piperabm.society.dynamics.friedkin import Friedkin


influence = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
opinions_initial = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
solver = Friedkin(influence, opinions_initial)
solver.solve(report=True)
print(solver.opinions)