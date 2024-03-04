import os

from piperabm.model import Model


model = Model(name='Sample Model')
model.path = os.path.dirname(os.path.realpath(__file__))
model.load_initial()


if __name__ == "__main__":
    print("infrastructure nodes: " + str(len(model.infrastructure_nodes)))
    print("infrastructure edges: " + str(len(model.infrastructure_edges)))
    print("society nodes: " + str(len(model.society_nodes)))
    print("society edges: " + str(len(model.society_edges)))

    #print(model)
    model.show()
