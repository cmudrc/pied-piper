from piperabm.tools.eigenvector_centrality import PowerMethod


matrix = [
    [1, 0],
    [0, 1]
]
pm = PowerMethod(matrix, threashold=0.05)


pm.run(10)
print(pm)