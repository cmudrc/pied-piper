from piperabm.model import Model
from piperabm.infrastructure import Road
from piperabm.tools.lattice.samples import lattice_0 as lattice

#lattice.show()
poses = lattice.to_pos(
    x_size=10,
    y_size=10,
    rotation=0.2,
    vector_zero=[5, 5]
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
    infrastrucure = model.infrastructure
    vectors = np.array(infrastrucure.principal_vectors())
    transposed = vectors.T
    x = transposed[0]
    y = transposed[1]

    plt.scatter(x, y)
    plt.show()

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
