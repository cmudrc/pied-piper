from piperabm.environment.elements.element import Element
from piperabm.boundary.load import load_boundary
from piperabm.degradation.sudden.load import load_sudden_degradation


class Settlement(Element):

    def __init__(
        self,
        boundary=None,
        active=True,
        sudden_degradation=None
    ):
        super().__init__(
            boundary=boundary,
            active=active,
            sudden_degradation=sudden_degradation
        )
        self.type = 'settlement'

    def to_dict(self) -> dict:
        return {
            'boundary': self.boundary.to_dict(),
            'active': self.active,
            'sudden_degradation': self.sudden_degradation.to_dict(),
            'type': self.type
        }
    
    def from_dict(self, dictionary: dict) -> None:
        self.boundary = load_boundary(dictionary['boundary'])
        self.active = dictionary['active']
        self.sudden_degradation = load_sudden_degradation(dictionary=['sudden_degradation'])
        self.type = dictionary['type']


if __name__ == "__main__":
    settlement = Settlement()