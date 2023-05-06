from piperabm.society.relationship.relationship import Relationship
from piperabm.unit import Date


class FellowCitizen(Relationship):

    def __init__(
        self,
        start_date: Date = None,
        end_date: Date = None
    ):
        super().__init__(
            start_date=start_date,
            end_date=end_date
        )
        self.type = 'fellow citizen'
        self.rank = None

    def to_dict(self) -> dict:
        dictionary = super().to_dict()
        dictionary['rank'] = self.rank

    def from_dict(self, dictionary: dict) -> None:
        super().from_dict(dictionary)
        self.rank = dictionary['rank']

if __name__ == "__main__":
    relationship = FellowCitizen(
        start_date=Date(2020, 1, 1),
        end_date=Date(2020, 1, 3),

    )
    print(relationship)