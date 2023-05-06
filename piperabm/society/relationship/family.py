from piperabm.society.relationship.relationship import Relationship
from piperabm.unit import Date


class Family(Relationship):

    def __init__(
        self,
        start_date: Date = None,
        end_date: Date = None
    ):
        super().__init__(
            start_date=start_date,
            end_date=end_date
        )
        self.type = 'family'


if __name__ == "__main__":
    relationship = Family(
        start_date=Date(2020, 1, 1),
        end_date=Date(2020, 1, 3)
    )
    print(relationship)