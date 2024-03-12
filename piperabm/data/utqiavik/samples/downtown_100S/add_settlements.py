from piperabm.data.utqiavik.settlements.add import add_settlements_to_model
from piperabm.data.utqiavik.samples.downtown_100S.permitted_labels import settlement_meshes_permitted_labels
from piperabm.data.utqiavik.samples.downtown_100S.info import settlements_num


def add_settlements(model):
    model = add_settlements_to_model(
        model,
        settlements_num=settlements_num,
        settlement_meshes_permitted_labels=settlement_meshes_permitted_labels
    )
    model.save_initial()


if __name__ == "__main__":
    from load_initial import model

    add_settlements(model)