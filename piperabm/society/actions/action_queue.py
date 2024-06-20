from piperabm.society.actions.move import Move
from piperabm.society.actions.stay import Stay


class ActionQueue:

    type = 'queue'

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
        self.library = []

    @property
    def undones(self):
        """
        Find undone actions from end
        """
        undone_actions = []
        for action in reversed(self.library):
            if action.done:
                break  # Stop the iteration if an action is done, as per the list's structure.
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
        total = 0
        for action in self.library:
            duration = action.total_duration
            total += duration
        return total

    def update(self, duration, measure: bool = False):
        for action in self.undones:
            duration = action.update(duration, measure=measure)
            if duration == 0:
                break

    def serialize(self):
        dictionary = {}
        library_serialized = []
        for action in self.library:
            action_serialized = action.serialize()
            library_serialized.append(action_serialized)
        dictionary['library'] = library_serialized
        dictionary['agent_id'] = self.agent_id
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        if dictionary['type'] != self.type:
            raise ValueError
        library_serialized = dictionary['library']
        for action_serialized in library_serialized:
            if 'type' in action_serialized:
                if action_serialized['type'] == 'move':
                    action = Move(action_queue=self)
                elif action_serialized['type'] == 'stay':
                    action = Stay(action_queue=self)
                action.deserialize(action_serialized)
                self.library.append(action)
    

if __name__ == "__main__":

    from piperabm.society.samples import model_1 as model

    agent_id = 1
    destination_id = 2
    model.society.go_and_comeback(agent_id, destination_id)
    
    print(model.society.pos(agent_id))
    model.update(duration=30)
    print(model.society.pos(agent_id))
    model.update(duration=30)
    print(model.society.pos(agent_id))
    model.update(duration=28700)
    print(model.society.pos(agent_id))
    model.update(duration=300)
    print(model.society.pos(agent_id))