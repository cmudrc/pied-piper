import os

from piperabm.model import Model
from piperabm.data.utqiavik.samples.downtown_100S.info import name


model = Model(name=name)
model.path = os.path.dirname(os.path.realpath(__file__))
model.load_initial()


if __name__ == "__main__":
    print(">>> infrastructure nodes:")
    print("# junctions: " + str(len(model.junctions)))
    print("# settlements: " + str(len(model.settlements)))
    print("# markets: " + str(len(model.markets)))

    print(">>> infrastructure edges:")
    print("# roads: " + str(len(model.roads)))

    print(">>> society nodes:")
    print("# agents: " + str(len(model.agents)))

    print(">>> society edges:")
    print("# family: " + str(len(model.family_edges)))
    
    #model.print()
    model.show()