from piperabm.unit import Date, date_to_dict, date_from_dict


class Hub:

    def __init__(
        self,
        name: str = '',
        pos: list = [0, 0],
        start_date: Date = None,
        end_date: Date = None,
        element = None
    ):
        self.name = name
        self.pos = pos
        self.start_date = start_date
        self.end_date = end_date
        self.element = element

    def type(self):
        result = None
        if self.element is None:
            result = 'hub'
        else:
            result = self.element.type
        return result

    def to_dict(self) -> dict:
        start_date_dict = date_to_dict(self.start_date)
        end_date_dict = date_to_dict(self.end_date)
        element_dict = None
        if self.element is not None:
            element_dict = self.element.to_dict()
        return {
            'name': self.name,
            'pos': self.pos,
            'start_date': start_date_dict,
            'end_date': end_date_dict,
            'element': element_dict
        }
    
    def from_dict(self, dictionary: dict) -> None:
        self.name = dictionary['name']
        self.pos = dictionary['pos']
        start_date_dict = dictionary['start_date']
        self.start_date = date_from_dict(start_date_dict)
        end_date_dict = dictionary['end_date']
        self.end_date = date_from_dict(end_date_dict)
        #element_dict = dictionary['element'] ########


if __name__ == "__main__":
    hub = Hub(start_date=Date(2020,1,1))
    dictionary = hub.to_dict()
    print(dictionary['start_date'])