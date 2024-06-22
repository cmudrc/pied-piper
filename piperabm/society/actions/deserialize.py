from piperabm.society.actions import Move
from piperabm.society.actions.action.stay.stay import Stay


def action_deserialize(dictionary, queue):
    if dictionary["type"] == "move":
        object = Move()
    elif dictionary["type"] == "stay":
        object = Stay()
    object.deserialize(dictionary)
    object.queue = queue
    return object