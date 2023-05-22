from piperabm.tools.eigenvector_centrality import PowerMethod


matrix = [
    [1/3, 1/3, 1/3],
    [0.02, 0.96, 0.02],
    [0.02, 0.02, 0.96]
]
pm = PowerMethod(matrix, threashold=0.05)


pm.run(10)
print(pm)