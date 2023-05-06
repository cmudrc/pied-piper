from piperabm.object import Object
from piperabm.unit import Date, date_to_dict, date_from_dict
from piperabm.tools import ElementExists


class Relationship(Object):

    def __init__(
            self,
            start_date: Date = None,
            end_date: Date = None
        ):
        super().__init__()
        self.start_date = start_date
        self.end_date = end_date
        self.type = 'relationship'

    def exists(self, start_date: Date, end_date: Date):
        """
        Check whether element exists in the time range
        """
        ee = ElementExists()
        return ee.check(
            item_start=self.start_date,
            item_end=self.end_date,
            time_start=start_date,
            time_end=end_date
        )

    def to_dict(self) -> dict:
        return {
            'type': self.type,
            'start_date': date_to_dict(self.start_date),
            'end_date': date_to_dict(self.end_date),
        }
    
    def from_dict(self, dictionary: dict) -> None:
        self.type = dictionary['type']
        self.start_date = date_from_dict(dictionary['start_date'])
        self.end_date = date_from_dict(dictionary['end_date'])


if __name__ == "__main__":
    relationship = Relationship()
    print(relationship)