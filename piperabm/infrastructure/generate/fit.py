import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

from piperabm.model.samples import model_6 as model

def vectors_to_xy(vectors):
    if isinstance(vectors, list):
        vectors = np.array(vectors)
    transposed = np.array(vectors).T
    xs = transposed[0]
    ys = transposed[1]
    return xs, ys

def xy_to_data(xs, ys):
    return np.column_stack((xs, ys))

def data_to_xy(data):
    xs = data[:, 0]
    ys = data[:, 1]
    return xs, ys

def show(xs, ys):
    plt.scatter(xs, ys)
    plt.show()

def pca_fit(data):
    data = np.column_stack((xs, ys))
    pca = PCA(n_components=2)
    pca.fit(data)
    return pca

infrastructure = model.infrastructure
#infrastructure.show()
vectors = infrastructure.principal_vectors(4)
xs, ys = vectors_to_xy(vectors)
show(xs, ys)
data = xy_to_data(xs, ys)
pca = pca_fit(data)
#print(pca.components_)
transformed_data = pca.transform(data)
transformed_xs, transformed_ys = data_to_xy(transformed_data)
show(transformed_xs, transformed_ys)


def grid_fit(grid_x, grid_y, data):
    def find_minmax(data):
        min_x = None
        max_x = None
        min_y = None
        max_y = None
        for entry in data:
            x = entry[0]
            y = entry[1]
    #xs = np.linspace(grid_x_min, grid_x_max, grid_x_num)
    #ys = np.linspace(grid_y_min, grid_y_max, grid_y_num)
