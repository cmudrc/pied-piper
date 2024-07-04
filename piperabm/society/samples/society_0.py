from piperabm.infrastructure.samples.infrastructure_0 import model


model.set_seed(2)
model.society.generate(
    num=100,
    gini_index=0.45,
    average_balance=1000
)
model.set_seed(None)


if __name__ == "__main__":
    print(model.society.gini_index)