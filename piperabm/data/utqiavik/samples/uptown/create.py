import os

from piperabm.model import Model
from piperabm.data.utqiavik.streets.add import add_streets_to_model
from piperabm.data.utqiavik.settlements.add import add_settlements_to_model
from piperabm.data.utqiavik.samples.uptown.permitted_labels import streets_permitted_labels, settlement_meshes_permitted_labels
from piperabm.data.utqiavik.samples.uptown.info import *


def create():
    model = Model(
        name=name,
        proximity_radius=proximity_radius,
    )
    model.path = os.path.dirname(os.path.realpath(__file__))

    model = add_streets_to_model(
        model,
        streets_permitted_labels=streets_permitted_labels
    )
    model = add_settlements_to_model(
        model,
        settlements_num=settlements_num,
        settlement_meshes_permitted_labels=settlement_meshes_permitted_labels
    )
    
    return model


if __name__ == "__main__":
    model = create()
    model.bake(save=True)