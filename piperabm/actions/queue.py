from piperabm.object import PureObject


class Queue(PureObject):

    def __init__(self):
        super().__init__()
        self.library = []
        self.type = "queue"

    def add(self, actions):
        if isinstance(actions, list):
            for action in actions:
                self.library.append(action)
        else:
            self.library.append(actions)

    @property
    def current(self):
        self.library[-1]

    def serialize(self):
        dictionary = {}
        library_serialized = []
        for action in self.library:
            action_serialized = action.serialize()
            library_serialized.append(action_serialized)
        dictionary['library'] = library_serialized
        dictionary['type'] = self.type
        return dictionary


if __name__ == "__main__":
    queue = Queue()
    queue.print