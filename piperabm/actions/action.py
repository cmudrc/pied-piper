from piperabm.object import PureObject
from piperabm.time import Date, DeltaTime, date_serialize, date_deserialize


class Action(PureObject):

    type = 'action'

    def __init__(
        self,
        date_start: Date = None,
        duration = 0
    ):
        super().__init__()
        if date_start is None:
            date_start = Date(2000, 1, 1)  # default
        if duration is None:
            duration = 0
        if isinstance(duration, (float, int)):
            duration = DeltaTime(seconds=duration)
        self.date_start = date_start
        self.date_end = self.date_start + duration
        #self.done = False
        self.agent = None  # Bilding

    @property
    def duration(self):
        return self.date_end - self.date_start
    
    def get(self, index):
        self.agent.model.get(index)

    def is_current(self, date):
        result = None
        progress = self.progress(date)
        if progress > 0 and progress < 1:
            result = True
        else:
            result = False
        return result
    
    def progress(self, date: Date):
        result = None
        passed = date - self.date_start
        result = passed.total_seconds() / self.duration.total_seconds()
        if result > 1:
            result = 1
        elif result < 0:
            result = 0
        return result

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['date_start'] = date_serialize(self.date_start)
        dictionary['date_end'] = date_serialize(self.date_end)
        dictionary['done'] = self.done
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        self.date_start = date_deserialize(dictionary['date_start'])
        self.date_end = date_deserialize(dictionary['date_end'])
        self.done = dictionary['done']
        self.type = dictionary['type']


if __name__ == "__main__":
    action = Action()
    action.print