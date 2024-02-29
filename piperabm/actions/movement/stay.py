from copy import deepcopy

from piperabm.object import PureObject
from piperabm.time import DeltaTime


class Stay(PureObject):

    def __init__(self, duration: DeltaTime = None):
        super().__init__()
        self.queue = None  # Binding
        self.duration = duration
        self.remaining = deepcopy(duration)
        self.done = False

    def update(self, duration: DeltaTime):
        """
        Update status of action
        """
        if duration >= self.remaining:
            self.remaining = DeltaTime(seconds=0)
            self.done = True
        else:
            self.remaining -= duration
        return self.remaining
    
    def serialize(self) -> dict:
        dictionary = {}
        dictionary['type'] = self.type
        dictionary['duration'] = self.duration.total_seconds()
        dictionary['remaining'] = self.remaining.total_seconds()
        dictionary['done'] = self.done
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        if dictionary['type'] != self.type:
            raise ValueError
        self.duration = DeltaTime(seconds=dictionary['duration'])
        self.remaining = DeltaTime(seconds=dictionary['remaining'])
        self.done = dictionary['done']