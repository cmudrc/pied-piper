from piperabm.unit import Date


class Element:

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

    def get_type(self):
        result = None
        if self.structure is None:
            result = self.type
        else:
            result = self.structure.type
        return result
    
    def __str__(self) -> str:
        return str(self.to_dict())

    def __eq__(self, other) -> bool:
        result = False
        if self.to_dict() == other.to_dict():
            result = True
        return result


if __name__ == "__main__":
    element = Element()
    print(element.start_date)