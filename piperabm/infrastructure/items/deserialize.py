from piperabm.infrastructure.items.junction import Junction
from piperabm.infrastructure.items.settlement import Settlement
from piperabm.infrastructure.items.road import Road


def infrastructure_deserialize(dictionary, model):
    if dictionary["type"] == "junction":
        object = Junction()
    elif dictionary["type"] == "settlement":
        object = Settlement()
    elif dictionary["type"] == "road":
        object = Road()
    object.deserialize(dictionary)
    object.model = model
    return object