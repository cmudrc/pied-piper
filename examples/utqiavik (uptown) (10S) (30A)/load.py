import os

from piperabm.model import Model
from data.info import name


model = Model(name=name)
model.path = os.path.dirname(os.path.realpath(__file__))
model.load_initial()


if __name__ == "__main__":
    print("nodes: " + str(len(model.infrastructure_nodes)))
    print("edges: " + str(len(model.infrastructure_edges)))
    #model.print()
    model.show()