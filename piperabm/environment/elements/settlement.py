from piperabm.environment.elements.element import Element
from piperabm.boundary.load import load_boundary
from piperabm.unit import Date, date_to_dict, date_from_dict
from piperabm.degradation.sudden.distributions.load import load_sudden_degradation


class Settlement(Element):

    def __init__(
        self,
        boundary=None,
        active=True,
        start_date: Date = None,
        end_date: Date = None,
        sudden_degradation=None,
        progressive_degradation=None
    ):
        super().__init__(
            boundary=boundary,
            active=active,
            start_date=start_date,
            end_date=end_date,
            sudden_degradation=sudden_degradation,
            progressive_degradation=progressive_degradation
        )
        self.type = 'settlement'

    def to_dict(self) -> dict:
        start_date_dict = date_to_dict(self.start_date)
        end_date_dict = date_to_dict(self.end_date)
        return {
            'boundary': self.boundary.to_dict(),
            'active': self.active,
            'start_date': start_date_dict,
            'end_date': end_date_dict,
            'sudden_degradation': self.sudden_degradation.to_dict(),
            'type': self.type
        }
    
    def from_dict(self, dictionary: dict) -> None:
        self.boundary = load_boundary(dictionary['boundary'])
        self.active = dictionary['active']
        start_date_dict = dictionary['start_date']
        self.start_date = date_from_dict(start_date_dict)
        end_date_dict = dictionary['end_date']
        self.end_date = date_from_dict(end_date_dict)
        self.sudden_degradation = load_sudden_degradation(dictionary=['sudden_degradation'])
        self.type = dictionary['type']


if __name__ == "__main__":
    settlement = Settlement()