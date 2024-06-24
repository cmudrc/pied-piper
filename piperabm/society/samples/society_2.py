from piperabm.infrastructure.samples import model_2 as model


model.society.neighbor_radius = 270
model.society.generate_agents(
    num=10,
    gini_index=0.45,
    average_food=10,
    average_water=10,
    average_energy=10,
    average_balance=1000
)


if __name__ == "__main__":
    print(model.society)