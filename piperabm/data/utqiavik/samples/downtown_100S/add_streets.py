from piperabm.data.utqiavik.streets.add import add_streets_to_model
from piperabm.data.utqiavik.samples.downtown_100S.permitted_labels import streets_permitted_labels


def add_streets(model):
    model = add_streets_to_model(
        model,
        streets_permitted_labels=streets_permitted_labels
    )
    model.save_initial()


if __name__ == "__main__":
    from load_initial import model

    add_streets(model)