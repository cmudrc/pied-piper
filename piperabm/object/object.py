import pprint

from piperabm.object.delta import Delta


class PureObject:
    """
    Pure object for the program
    """

    type = 'pure object'

    def __init__(self):
        pass

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

    def __str__(self) -> str:
        """
        Show serialized format of object
        """
        return str(self.serialize())

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

    def create_delta(self, old) -> dict:
        """
        Create delta between the *self* and *other*
        """
        if not isinstance(old, (dict, list, int, float, bool, str)):
            old = old.serialize()
        new = self.serialize()
        delta = Delta.create(old, new)
        return delta

    def apply_delta_to_object(self, delta: dict) -> None:
        """
        Apply the *delta* to the *self*
        """
        dictionary = self.serialize()
        dictionary_new = Delta.apply(dictionary, delta)
        self.deserialize(dictionary_new)

    def apply_deltas_to_object(self, deltas: list) -> None:
        """
        Apply the *delta* to the *self*
        """
        for delta in deltas:
            self.apply_delta(delta)


if __name__ == '__main__':

    class Sample(PureObject):

        def __init__(self, value):
            super().__init__()
            self.value = value

        def serialize(self) -> dict:
            return {'value': self.value}

        def deserialize(self, dictionary: dict) -> None:
            self.value = dictionary['value']

    s_1 = Sample(value=3)
    s_2 = Sample(value=5)
    delta = s_2.create_delta(s_1)
    print(delta)
    s_1.apply_delta(delta)
    s_1.print()
