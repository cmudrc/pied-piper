import pprint


class Print:

    def __str__(self) -> str:
        """
        To print serialized format of object
        """
        data = self.serialize()
        txt = pprint.pformat(
            data,
            depth=5,
            compact=True,
            width=100,
        )
        return txt