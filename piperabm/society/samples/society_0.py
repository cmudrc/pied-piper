from piperabm.infrastructure.samples.infrastructure_0 import model


model.society.generate_agents(
    num=100,
    gini_index=0.45,
    average_balance=1000
)


if __name__ == "__main__":
    print(model.society.gini_index)