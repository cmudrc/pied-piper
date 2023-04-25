from piperabm.object import Object
from piperabm.unit import Date, date_to_dict, date_from_dict
from piperabm.unit import Date, DT


class Action(Object):

    def __init__(
            self,
            start_date: Date,
            end_date: Date=None,
            duration=None
        ):
        self.start_date = start_date
        if end_date is None and \
            duration is not None:
            if isinstance(duration, (float, int)):
                duration = DT(seconds=duration)
            elif isinstance(duration, DT):
                pass
            self.duration = duration
            self.end_date = self.start_date + self.duration
        elif end_date is not None and \
            duration is None:
            self.end_date = end_date
            self.duration = self.end_date - self.start_date
        elif end_date is None and \
            duration is None:
            raise ValueError
        elif end_date is not None and \
            duration is not None:
            raise ValueError
        self.done = False
        self.type = 'action'

        ''' temporary variables '''
        #self.started = None
        #self.finished = None
        #self.current_progress = None

    def is_finished(self, date: Date):
        result = None
        if date >= self.end_date:
            result = True
        else:
            result = False
        #self.finished = result
        return result
    
    def is_started(self, date: Date):
        result = None
        if date < self.start_date:
            result = False
        else:
            result = True
        #self.started = result
        return result
    
    def progress(self, date: Date):
        result = None
        if self.is_started(date) is True:
            if self.is_finished(date) is False:
                duration_SI = self.duration.total_seconds()
                current = date - self.start_date
                current_SI = current.total_seconds()
                result = current_SI / duration_SI
            else:
                result = 1
        else:
            result = 0
        #self.current_progress = result
        return result
    
    def to_dict(self) -> dict:
        dictionary = {}
        dictionary['start_date'] = date_to_dict(self.start_date)
        dictionary['end_date'] = date_to_dict(self.end_date)
        dictionary['duration'] = self.duration.total_seconds()
        dictionary['done'] = self.done
        dictionary['type'] = self.type
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        self.start_date = date_from_dict(dictionary['start_date'])
        self.end_date = date_from_dict(dictionary['end_date'])
        self.duration = DT(seconds=dictionary['duration'])
        self.done = dictionary['done']
        self.type = dictionary['type']
        

if __name__ == "__main__":
    action = Action(
        start_date=Date(2020, 1, 1),
        duration=500000
    )
    print(action)