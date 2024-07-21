"""
Grid world without access to market
"""

from copy import deepcopy

from piperabm.infrastructure.samples.infrastructure_3 import model as model_infrastructure


model = deepcopy(model_infrastructure)
model.set_seed(2)
model.society.generate(num=10)
model.set_seed(None)


if __name__ == "__main__":
    print(model.society)
    #model.show()