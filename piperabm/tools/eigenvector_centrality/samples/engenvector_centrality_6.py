from piperabm.tools.eigenvector_centrality import PowerMethod


matrix = [
    [0.5, 0.5],
    [0.05, 0.95]
]
pm = PowerMethod(matrix, threashold=0.05)


pm.run(10)
print(pm)