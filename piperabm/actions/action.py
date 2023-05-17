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
            else:
                raise ValueError
            self.duration = duration
            self.end_date = self.calculate_end_date(
                self.start_date,
                self.duration
            )
        elif end_date is not None and \
            duration is None:
            self.end_date = end_date
            self.duration = self.calculate_duration(
                self.start_date,
                self.end_date
            )
        elif end_date is None and \
            duration is None:
            raise ValueError
        elif end_date is not None and \
            duration is not None:
            raise ValueError
        self.done = False
        self.type = 'action'

    def calculate_duration(self, start_date: Date, end_date: Date):
        return end_date - start_date
    
    def calculate_end_date(self, start_date: Date, duration: DT):
        return start_date + duration

    def is_current(self, date: Date):
        result = False
        if self.is_started(date) is True and \
            self.is_finished(date) is False:
            result = True
        return result

    def is_finished(self, date: Date):
        result = None
        if date >= self.end_date:
            result = True
        else:
            result = False
        return result
    
    def is_started(self, date: Date):
        result = None
        if date < self.start_date:
            result = False
        else:
            result = True
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