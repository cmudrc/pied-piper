from piperabm.object import PureObject
from piperabm.actions.movement import Move, Stay


class ActionQueue(PureObject):

    type = 'queue'

    def __init__(self):
        super().__init__()
        self.library = []
        self.agent = None  # Binding

    def add(self, actions):
        """
        Add new action(s) to the queue
        """
        if isinstance(actions, list):
            for action in actions:
                self.add(action)
        else:
            action = actions
            action.queue = self  # Binding
            self.library.append(action)

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
            elif action_dictionary['type'] == 'stay':
                action = Stay()
            action.queue = self  # Binding
            action.deserialize(action_dictionary)
    

if __name__ == "__main__":
    queue = ActionQueue()
    queue.print()
