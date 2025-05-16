from copy import deepcopy

from piperabm.tools.print.serialized import Print


class Stay(Print):
    """
    Stay action
    """

    type = "stay"

    def __init__(self, action_queue, duration: float = 0):
        super().__init__()
        self.action_queue = action_queue  # Binding
        self.total_duration = duration
        self.elapsed = 0
        self.remaining = deepcopy(duration)
        self.done = False

    def update(self, duration: float, measure: bool = False):
        """
        Update status of action
        """
        if duration <= self.remaining:
            self.remaining -= duration
            self.elapsed += duration
            duration = 0
        else:
            duration -= self.remaining
            self.remaining = 0
            self.elapsed = self.total_duration
            self.done = True
        return duration
    
    def serialize(self) -> dict:
        """
        Serialize
        """
        data = {}
        data["type"] = self.type
        data["total_duration"] = self.total_duration
        data["remaining"] = self.remaining
        data["elapsed"] = self.elapsed
        data["done"] = self.done
        return data

    def deserialize(self, data: dict) -> None:
        """
        Deserialize
        """
        self.total_duration = data["total_duration"]
        self.elapsed = data["elapsed"]
        self.remaining = data["remaining"]
        self.done = data["done"] 


if __name__ == "__main__":

    from piperabm.society.samples.society_1 import model
    from piperabm.society.actions.action import Move

    agent_id = 1
    destination_id = 2
    action_queue = model.society.actions[agent_id]

    stay = Stay(
        action_queue=action_queue,
        duration=5
    )
    action_queue.add(stay)

    path = model.infrastructure.path(
        id_start=model.society.get_current_node(id=agent_id),
        id_end=destination_id
    )
    move = Move(
        action_queue=action_queue,
        path=path,
        usage=1
    )
    action_queue.add(move)

    print(f"time: {model.time}, pos: {model.society.get_pos(agent_id)}")

    model.update(duration=4)

    print(f"time: {model.time}, pos: {model.society.get_pos(agent_id)}")

    model.update(duration=14)

    print(f"time: {model.time}, pos: {model.society.get_pos(agent_id)}")