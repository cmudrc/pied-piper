from piperabm.object import Object


class Shape(Object):
    
    def __init__(self):
        super().__init__()
        self.type = 'shape'

    def to_dict(self) -> dict:
        return {
            'type': self.type,
        }

    def from_dict(self, dictionary: dict):
        self.type = dictionary['type']


if __name__ == "__main__":
    shape = Shape()
    print(shape)