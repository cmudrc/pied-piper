from piperabm.model import Model
from piperabm.infrastructure import Road

from piperabm.tools.lattice.samples import lattice_1 as lattice


#lattice.show()
poses = lattice.to_pos(
    x_size=10,
    y_size=12,
    rotation=0.2,
    vector_zero=[3, 5]
)

roads = []
for edge in poses:
    road = Road(*edge)
    roads.append(road)

model = Model(proximity_radius=0.1)
for road in roads:
    model.add(road)


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from random import uniform
    from sklearn.decomposition import PCA

    infrastrucure = model.infrastrucure
    vectors = np.array(infrastrucure.principal_vectors())
    transposed = vectors.T
    xs = transposed[0]
    ys = transposed[1]

    new_xs = []
    for x in xs:
        new_x = x + uniform(-1, 1)
        new_xs.append(new_x)

    new_ys = []
    for y in ys:
        new_y = y + uniform(-2, 2)
        new_ys.append(new_y)

    def unit_vectors(x_values, y_values):
        data = np.column_stack((x_values, y_values))
        pca = PCA(n_components=2)
        pca.fit(data)
        principal_components = pca.components_
        print(principal_components)


        transformed_data = pca.transform(data)
        #print("Transformed Data:\n", transformed_data)
        data = transformed_data.T
        plt.gca().set_aspect("equal")
        plt.scatter(data[0], data[1])
        plt.show()

        # Print the variance explained by each component
        #print("Variance explained by each component:", pca.explained_variance_ratio_)

    unit_vectors(new_xs, new_ys)

    #plt.scatter(new_xs, new_ys)
    #plt.show()

    #_, log = model.infrastructure_grammar_rule_1()
    #print(log)
    #_, log = model.infrastructure_grammar_rule_2()
    #model.infrastructure_grammar_rule_1()
    #print(log)
    #print(len(model.all_environment_nodes))
    #print(len(model.all_environment_edges))
    #model.infrastructure_grammar_rule_3()
    #infrastrucure = model.infrastrucure
    #print(infrastrucure.all_nodes())
    
    #infrastrucure.show
    #print(len(model.all_environment_nodes))
    #print(len(model.all_environment_edges))
    #model.print
    #model.show()
