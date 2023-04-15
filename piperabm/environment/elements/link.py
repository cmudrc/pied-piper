from piperabm.environment.elements.element import Element
from piperabm.environment.structures.load import load_structure
from piperabm.unit import Date, date_to_dict, date_from_dict


class Link(Element):

    def __init__(
        self,
        name: str = '',
        start_date: Date = None,
        end_date: Date = None,
        structure = None
    ):
        super().__init__(
            name=name,
            start_date=start_date,
            end_date=end_date,
            structure=structure
        )
        self.type = 'link'

    def to_dict(self) -> dict:
        structure_dict = None
        if self.structure is not None:
            structure_dict = self.structure.to_dict()
        return {
            'name': self.name,
            'start_date': date_to_dict(self.start_date),
            'end_date': date_to_dict(self.end_date),
            'structure': structure_dict
        }
    
    def from_dict(self, dictionary: dict) -> None:
        self.name = dictionary['name']
        self.start_date = date_from_dict(dictionary['start_date'])
        self.end_date = date_from_dict(dictionary['end_date'])
        self.structure = load_structure(dictionary['structure'])


if __name__ == "__main__":
    hub = Link(start_date=Date(2020,1,1))
    dictionary = hub.to_dict()
    print(dictionary['start_date'])