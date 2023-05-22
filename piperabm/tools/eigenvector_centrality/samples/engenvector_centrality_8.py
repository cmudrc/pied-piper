from piperabm.tools.eigenvector_centrality import PowerMethod


matrix = [
    [0.48, 0.48, 0.02],
    [0.48, 0.48, 0.02],
    [0.02, 0.02, 0.96]
]
pm = PowerMethod(matrix, threashold=0.05)


pm.run(10)
print(pm)