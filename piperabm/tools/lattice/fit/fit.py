from load import model

'''
nodes = model.all_environment_nodes
nodes = model.filter(nodes, types=['junction'])

positions = []
for node in nodes:
    item = model.get(node)
    positions.append(item.pos)

print(positions)
'''

import numpy as np
import matplotlib.pyplot as plt
infrastrucure = model.infrastructure
vectors = np.array(infrastrucure.principal_vectors())
transposed = vectors.T
xs = transposed[0]
ys = transposed[1]

#plt.scatter(xs, ys)
#plt.show()

from sklearn.decomposition import PCA


pca = PCA(n_components=2)
data = np.column_stack((xs, ys))
pca.fit(data)
#vec = pca.components_[0]
#print(np.degrees(np.arctan(vec[1]/vec[0])))
transformed_data = pca.transform(data)
transformed_data_T = transformed_data.T
#plt.gca().set_aspect('equal')
#plt.scatter(transformed_data_T[0], transformed_data_T[1])
#plt.show()


