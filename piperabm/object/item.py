from piperabm.object import PureObject
from piperabm.time import Date, date_serialize, date_deserialize


class Item(PureObject):
    """
    Used as super class for items in graph and has defition of time
    """

    def __init__(
        self,
        date_start: Date = None,
        date_end: Date = None,
        index: int = None,
        name: str = ''
    ):
        super().__init__()
        self.date_start = date_start
        self.date_end = date_end
        self.index = index
        self.name = name
        self.type = "item"

    def exists(
        self,
        start: Date,
        end: Date = None
    ) -> bool:
        """
        Check whether an item exists in a window of time between *start* and *end*
        """

        date_start = self.date_start
        date_end = self.date_end

        if end is None:
            end = start

        # Ensuring the item start and end dates are valid if they are not None
        if date_start is not None and date_end is not None:
            if date_start >= date_end:
                raise ValueError(
                    "Item start date must be earlier than item end date")

        # Ensuring the window start and end dates are valid
        if start > end:
            raise ValueError(
                "Window start date must be earlier than or equal to window end date")

        # Checking if the item exists in the specified window
        if date_start is None and date_end is None:
            # Item has always existed and will exist forever
            return True
        elif date_start is None:
            # Item has always existed until date_end
            return date_end >= start
        elif date_end is None:
            # Item exists from date_start and will exist forever
            return date_start <= end
        else:
            # Item exists between date_start and date_end
            return date_start <= end and date_end >= start

    def serialize(self) -> dict:
        dictionary = {}
        dictionary["date_start"] = date_serialize(self.date_start)
        dictionary["date_end"] = date_serialize(self.date_end)
        dictionary["index"] = self.index
        dictionary["name"] = self.name
        dictionary["type"] = self.type
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.date_start = date_deserialize(dictionary["date_start"])
        self.date_end = date_deserialize(dictionary["date_end"])
        self.index = dictionary["index"]
        self.name = dictionary["name"]
        self.type = dictionary["type"]


if __name__ == "__main__":
    item = Item(
        date_start=Date(2020, 1, 1),
        date_end=Date(2021, 1, 1)
    )
    result = item.exists(
        start=Date(2020, 11, 11),
        end=Date(2020, 12, 12),
    )
    print(result)
