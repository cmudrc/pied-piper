from piperabm.environment.elements.element import Element
from piperabm.unit import Date


class Link(Element):

    def __init__(
        self,
        name: str = '',
        pos: list = [0, 0],
        angle: float = 0,
        start_date: Date = None,
        end_date: Date = None,
        structure=None
    ):
        super().__init__(
            name=name,
            pos=pos,
            start_date=start_date,
            end_date=end_date,
            structure=structure
        )
        self.angle = angle
        self.type = 'link'

    def to_dict(self) -> dict:
        dictionary = super().to_dict()
        dictionary['angle'] = self.angle
        return dictionary

    def from_dict(self, dictionary: dict) -> None:
        super().from_dict(dictionary)
        self.angle = dictionary['angle']


if __name__ == "__main__":
    link = Link(start_date=Date(2020, 1, 1))
    print(link)
