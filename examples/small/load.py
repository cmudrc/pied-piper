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
    model.show()
    #paths = model.infrastructure.paths()
    #print(paths.G)