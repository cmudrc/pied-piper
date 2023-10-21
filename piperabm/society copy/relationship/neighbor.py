from piperabm.society.relationship.relationship import Relationship
from piperabm.unit import Date


class Neighbor(Relationship):

    def __init__(
        self,
        start_date: Date = None,
        end_date: Date = None,
        distance: float = None
    ):
        super().__init__(
            start_date=start_date,
            end_date=end_date,
            distance=distance
        )
        self.type = 'neighbor'


if __name__ == "__main__":
    relationship = Neighbor()
    print(relationship)