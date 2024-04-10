import os

from load_infrastructure import infrastructure
from piperabm.society_new import Society
from piperabm.model_new import Model


society = Society()
society.path = os.path.dirname(os.path.realpath(__file__))
society.load()
model = Model(
    infrastructure=infrastructure,
    society=society
)


if __name__ == "__main__":
    #ids = model.society.agents
    #a_1 = model.society.get(ids[0])
    #a_2 = model.society.get(ids[5])
    #print(a_1.accessibility, a_2.accessibility)
    model.show()
    #paths = model.infrastructure.paths()
    #print(paths.G)