from piperabm.society.actions.action.move.move import Move
from piperabm.society.actions.action.stay.stay import Stay


def action_deserialize(dictionary, queue):
    if dictionary["type"] == "move":
        object = Move()
    elif dictionary["type"] == "stay":
        object = Stay()
    object.deserialize(dictionary)
    object.queue = queue
    return object


if __name__ == "__main__":

    from piperabm.society.samples.society_1 import model

    agent_id = model.society.agents[0]
    destination_id = 2
    action_queue = model.society.actions[agent_id]
    current_node = model.society.get_current_node(agent_id)
    path = model.infrastructure.path(id_start=current_node, id_end=destination_id)
    move = Move(
        action_queue=action_queue,
        path=path,
        usage=1
    )
    action_queue.add(move)
    action_serialized = move.serialize()
    action_deserialized = action_deserialize(action_serialized, action_queue)
    
    print(action_deserialized.serialize() == move.serialize())