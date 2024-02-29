from piperabm.object import PureObject
from piperabm.actions import Move


class ActionQueue(PureObject):

    type = 'queue'

    def __init__(self):
        super().__init__()
        self.library = []
        self.agent = None  # Binding

    def add(self, actions):
        if isinstance(actions, list):
            for action in actions:
                self.add(action)
        else:
            action = actions
            action.queue = self  # Binding
            self.library.append(action)

    def update(self, duration):
        if len(self.library) > 0:
            last_move = self.library[-1]
            last_move.update(duration)

    def serialize(self):
        dictionary = {}
        library_serialized = []
        for action in self.library:
            action_serialized = action.serialize()
            library_serialized.append(action_serialized)
        dictionary['library'] = library_serialized
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        library_serialized = dictionary['library']
        for action_dictionary in library_serialized:
            if action_dictionary['type'] == 'move':
                action = Move()
            action.queue = self  # Binding
            action.deserialize(action_dictionary)
    

if __name__ == "__main__":
    queue = ActionQueue()
    queue.print