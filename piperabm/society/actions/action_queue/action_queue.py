from piperabm.society.actions.action import Move
from piperabm.society.actions.action.stay.stay import Stay
from piperabm.tools.print.serialized import Print


class ActionQueue(Print):
    """
    Action queue to manage the to-do list
    """

    type = "queue"

    def __init__(
            self,
            agent_id: int = None
        ):
        super().__init__()
        self.society = None  # Binding
        self.library = []
        self.agent_id = agent_id
        
    def add(self, *actions):
        """
        Add new action(s) to the queue
        """
        for element in actions:
            if isinstance(element, list):
                for action in element:
                    self.add(action)
            else:
                action = element
                action.action_queue = self  # Binding
                self.library.append(action)

    def reset(self):
        """
        Reset the queue
        """
        self.library = []

    @property
    def undones(self):
        """
        Find undone actions from end
        """
        undone_actions = []
        for action in reversed(self.library):
            if action.done:
                break  # Stop the iteration if an action is done, as per the list"s structure.
            undone_actions.append(action)
        return list(reversed(undone_actions))
    
    @property
    def done(self):
        """
        Whether all actions are done or not
        """
        result = None
        if len(self.undones) > 0:
            result = False
        else:
            result = True
        return result
    
    @property
    def remaining(self):
        """
        Estimate the remaining time to complete undone tasks
        """
        total = 0
        undone_actions = self.undones
        for action in undone_actions:
            remaining = action.remaining
            total += remaining
        return total
    
    @property
    def elapsed(self):
        """
        Estimate the remaining time to complete undone tasks
        """
        total = 0
        for action in self.library:
            remaining = action.elapsed
            total += remaining
        return total
    
    @property
    def total_duration(self):
        """
        Return how long all the actions will take
        """
        total = 0
        for action in self.library:
            duration = action.total_duration
            total += duration
        return total

    def update(self, duration, measure: bool = False):
        """
        Update the queue
        """
        for action in self.undones:
            duration = action.update(duration, measure=measure)
            if duration == 0:
                break

    def serialize(self):
        """
        Serialize
        """
        data = {}
        library_serialized = []
        for action in self.library:
            action_serialized = action.serialize()
            library_serialized.append(action_serialized)
        data["library"] = library_serialized
        data["agent_id"] = self.agent_id
        data["type"] = self.type
        return data
    
    def deserialize(self, data: dict) -> None:
        """
        Deserialize
        """
        if data["type"] != self.type:
            raise ValueError
        library_serialized = data["library"]
        for action_serialized in library_serialized:
            if "type" in action_serialized:
                if action_serialized["type"] == "move":
                    action = Move(action_queue=self)
                elif action_serialized["type"] == "stay":
                    action = Stay(action_queue=self)
                action.deserialize(action_serialized)
                self.library.append(action)
    

if __name__ == "__main__":

    from piperabm.society.samples.society_1 import model

    agent_id = model.society.agents[0]
    destination_id = 2
    action_queue = model.society.actions[agent_id]
    path = model.infrastructure.path(
        id_start=model.society.get_current_node(id=agent_id),
        id_end=destination_id
    )
    move = Move(
        action_queue=action_queue,
        path=path,
        usage=1
    )

    agent_id = model.society.agents[0]
    destination_id = 2
    action_queue = model.society.actions[agent_id]
    model.society.go_and_comeback_and_stay(
        action_queue=action_queue,
        move_go=move,
        stay_length=100,
    )
    
    #print(model.society.actions[agent_id])
    print(f"time: {model.time}, pos: {model.society.get_pos(agent_id)}")

    model.update(duration=30)

    print(f"time: {model.time}, pos: {model.society.get_pos(agent_id)}")

    model.update(duration=30)

    print(f"time: {model.time}, pos: {model.society.get_pos(agent_id)}")

    model.update(duration=120)

    print(f"time: {model.time}, pos: {model.society.get_pos(agent_id)}")

    model.update(duration=60)

    print(f"time: {model.time}, pos: {model.society.get_pos(agent_id)}")
    