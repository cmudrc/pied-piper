from piperabm.environment.elements.element import Element
from piperabm.unit import Date


class Link(Element):

    def __init__(
        self,
        name: str = '',
        actual_length: float = None,
        start_date: Date = None,
        end_date: Date = None,
        structure=None
    ):
        ''' Element-specific variables '''
        super().__init__(
            name=name,
            start_date=start_date,
            end_date=end_date,
            structure=structure
        )
        self.type = 'link'
        ''' Link-specific variables '''
        self.actual_length = actual_length

    def length(self) -> float:
        """
        Return length
            return *self.actual_length* if provided,
            else, return euclediean distance (if provided)
        """
        result = None
        if self.actual_length is None:
            structure = self.structure
            if structure is not None:
                boundary = structure.boundary
                if boundary is not None:
                    shape = boundary.shape
                    if shape is not None:
                        result = shape.width
        else:
            result = self.actual_length
        return result
    
    def angle(self) -> float:
        """
        Return angle
        """
        result = None
        structure = self.structure
        if structure is not None:
            boundary = structure.boundary
            if boundary is not None:
                shape = boundary.shape
                if shape is not None:
                    result = shape.angle
        return result

    def to_dict(self) -> dict:
        ''' Element-specific variables '''
        dictionary = super().to_dict()
        ''' Link-specific variables '''
        dictionary['actual_length'] = self.actual_length
        return dictionary

    def from_dict(self, dictionary: dict) -> None:
        ''' Element-specific variables '''
        super().from_dict(dictionary)
        ''' Link-specific variables '''
        self.actual_length = dictionary['actual_length']


if __name__ == "__main__":
    link = Link(start_date=Date(2020, 1, 1))
    print(link)
