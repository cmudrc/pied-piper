from piperabm.infrastructure.samples.infrastructure_0 import model


model.society.generate_agents(num=3, gini_index=0.45)


if __name__ == "__main__":
    print(model.society.gini_index)