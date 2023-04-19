from piperabm.environment.elements.element import Element
from piperabm.unit import Date


class Hub(Element):

    def __init__(
        self,
        name: str = '',
        pos: list = [0, 0],
        start_date: Date = None,
        end_date: Date = None,
        structure = None
    ):
        super().__init__(
            name=name,
            pos=pos,
            start_date=start_date,
            end_date=end_date,
            structure=structure
        )
        self.type = 'hub'

    def is_in(self, pos: list) -> bool:
        result = None
        if self.structure is not None:
            result = self.structure.boundary.is_in(
                point=pos,
                center=self.pos
            )
        elif pos == self.pos:
            result = True
        return result

    def to_dict(self) -> dict:
        dictionary = super().to_dict()
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        super().from_dict(dictionary)


if __name__ == "__main__":
    hub = Hub(start_date=Date(2020,1,1))
    print(hub)