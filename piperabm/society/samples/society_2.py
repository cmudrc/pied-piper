from piperabm.infrastructure.samples.infrastructure_2 import model


model.set_seed(2)
model.society.neighbor_radius = 270
model.society.generate(
    num=10,
    gini_index=0.45,
    average_food=10,
    average_water=10,
    average_energy=10,
    average_balance=1000
)
model.set_seed(None)


if __name__ == "__main__":
    print(model.society)