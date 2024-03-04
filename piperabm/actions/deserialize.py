from piperabm.actions.move import Move
from piperabm.actions.stay import Stay


def action_deserialize(dictionary, queue):
    if dictionary["type"] == "move":
        object = Move()
    elif dictionary["type"] == "stay":
        object = Stay()
    object.deserialize(dictionary)
    object.queue = queue
    return object