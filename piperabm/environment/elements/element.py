from piperabm.object import Object
from piperabm.environment.structures.load import load_structure
from piperabm.unit import Date, date_to_dict, date_from_dict
from piperabm.tools import ElementExists


class Element(Object):

    def __init__(
        self,
        name: str = '',
        start_date: Date = None,
        end_date: Date = None,
        structure = None
    ):
        self.name = name
        if start_date is None:
            start_date = Date.today()
        self.start_date = start_date
        self.end_date = end_date
        self.structure = structure
        self.type = 'element'

    def add_structure(self, structure):
        if self.start_date > structure.start_date:
            self.start_date = structure.start_date
        if self.end_date < structure.end_date:
            self.end_date = structure.end_date
        self.structure = structure

    def get_type(self):
        """
        Return type of element
        """
        result = None
        if self.structure is None:
            result = self.type
        else:
            result = self.structure.type
        return result
    
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
        structure_dict = None
        if self.structure is not None:
            structure_dict = self.structure.to_dict()
        return {
            'name': self.name,
            'start_date': date_to_dict(self.start_date),
            'end_date': date_to_dict(self.end_date),
            'structure': structure_dict,
            'type': self.type,
        }
    
    def from_dict(self, dictionary: dict) -> None:
        self.name = dictionary['name']
        self.start_date = date_from_dict(dictionary['start_date'])
        self.end_date = date_from_dict(dictionary['end_date'])
        self.structure = load_structure(dictionary['structure'])
        self.type = dictionary['type']


if __name__ == "__main__":
    element = Element()
    print(element)