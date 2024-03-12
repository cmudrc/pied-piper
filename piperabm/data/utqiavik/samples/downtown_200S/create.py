import os

from piperabm.model import Model
from piperabm.data.utqiavik.samples.downtown_200S.info import *


def create():
    model = Model(
        name=name,
        proximity_radius=proximity_radius,
    )
    model.path = os.path.dirname(os.path.realpath(__file__))

    model.save_initial()


if __name__ == "__main__":
    model = create()