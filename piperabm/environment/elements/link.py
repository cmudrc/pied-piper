from piperabm.environment.elements.element import Element
from piperabm.unit import Date


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
        return super().to_dict()
    
    def from_dict(self, dictionary: dict) -> None:
        super().from_dict(dictionary)


if __name__ == "__main__":
    link = Link(start_date=Date(2020,1,1))
    print(link)