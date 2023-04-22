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
        ''' Element-specific variables '''
        super().__init__(
            name=name,
            start_date=start_date,
            end_date=end_date,
            structure=structure
        )
        self.type = 'hub'
        ''' Hub-specific variables '''
        self.pos = pos

    def to_dict(self) -> dict:
        ''' Element-specific variables '''
        dictionary = super().to_dict()
        ''' Hub-specific variables '''
        # pass
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        ''' Element-specific variables '''
        super().from_dict(dictionary)
        ''' Hub-specific variables '''
        # pass


if __name__ == "__main__":
    hub = Hub(start_date=Date(2020,1,1))
    print(hub)