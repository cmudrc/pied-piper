"""
A single home standing in the middle of nowhere with
two agents living inside it as family
"""

from copy import deepcopy

from piperabm.infrastructure.samples.infrastructure_0 import model as model_infrastructure


model = deepcopy(model_infrastructure)
model.set_seed(2)
model.society.generate(
    num=2,
    gini_index=0.45,
    average_balance=1000
)
model.set_seed(None)


if __name__ == "__main__":
    print("gini index: ", model.society.gini_index)
    #model.show()