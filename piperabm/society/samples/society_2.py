from copy import deepcopy

from piperabm.infrastructure.samples.infrastructure_2 import model as model_infrastructure


model = deepcopy(model_infrastructure)
model.set_seed(2)
model.society.neighbor_radius = 270
model.society.generate(
    num=10,
    gini_index=0.45,
    average_resources={
        'food': 10,
        'water': 10,
        'energy': 10,
    },
    average_balance=100
)
model.set_seed(None)


if __name__ == "__main__":
    print(model.society)
    print("society serialized: ", model.society.serialize())
    #model.show()