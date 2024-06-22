from copy import deepcopy

from piperabm.tools.print.serialized import Print


class Stay(Print):

    type = 'stay'

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
        dictionary = {}
        dictionary['type'] = self.type
        dictionary['total_duration'] = self.total_duration
        dictionary['remaining'] = self.remaining
        dictionary['elapsed'] = self.elapsed
        dictionary['done'] = self.done
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.total_duration = dictionary['total_duration']
        self.elapsed = dictionary['elapsed']
        self.remaining = dictionary['remaining']
        self.done = dictionary['done'] 


if __name__ == '__main__':

    from piperabm.society.samples import model_1 as model
    from piperabm.society.actions import Move

    agent_id = 1
    destination_id = 2
    action_queue = model.society.actions[agent_id]

    stay = Stay(
        action_queue=action_queue,
        duration=5
    )
    action_queue.add(stay)

    path = model.society.path(agent_id, destination_id)
    move = Move(
        action_queue=action_queue,
        path=path,
        usage=1
    )
    action_queue.add(move)

    print(model.society.pos(agent_id))
    model.update(duration=4)
    print(model.society.pos(agent_id))
    model.update(duration=14)
    print(model.society.pos(agent_id))