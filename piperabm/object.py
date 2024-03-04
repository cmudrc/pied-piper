import pprint


class PureObject:
    """
    Highset level super class
    """

    type = 'object'

    def __init__(self):
        pass

    '''
    def print(self):
        """
        "Pretty Print" the object
        """
        data = self.serialize()
        pprint.pprint(
            data,
            depth=5,
            compact=True,
            width=100,
        )
    '''

    def __str__(self) -> str:
        """
        Show serialized format of object
        """
        #return str(self.serialize())
        data = self.serialize()
        txt = pprint.pformat(
            data,
            depth=5,
            compact=True,
            width=100,
        )
        return txt

    def __eq__(self, other) -> bool:
        """
        Check equality for two objects
        """
        result = False
        if self.serialize() == other.serialize() and \
                self.serialize != {}:
            result = True
        return result

    def serialize(self) -> dict:
        """
        Serialize object into a dictionary
        """
        dictionary = {}
        print('NOT IMPLEMENTED YET')
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        """
        Deserialize object from a dictionary
        """
        print('NOT IMPLEMENTED YET')


if __name__ == '__main__':

    class Sample(PureObject):

        def __init__(self, value=None):
            super().__init__()
            self.value = value

        def serialize(self) -> dict:
            return {'value': self.value}

        def deserialize(self, dictionary: dict) -> None:
            self.value = dictionary['value']

    sample = Sample(value=3)
    data = sample.serialize()
    sample_new = Sample()
    sample_new.deserialize(data)
    print(sample == sample_new)