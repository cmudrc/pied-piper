class Eternal:
    """
    Eternal distribution.
    """

    def __init__(self):
        pass

    def probability(self, time_start, time_end):
        return 0

    def show(self):
        pass

    def to_dict(self) -> dict:
        dictionary = {
            'type': 'eternal'
        }
        return dictionary
    
    def from_dict(self, dictionary: dict):
        pass