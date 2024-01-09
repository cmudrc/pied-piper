from piperabm.actions.action import Action
from piperabm.transporation import Transportation
from piperabm.time import Date


class Move(Action):

    def __init__(
        self,
        agent=None,
        date_start: Date = None,
        tracks: list = None
    ):
        self.agent = agent
        duration = None
        duration = agent.transportation.how_long(total_adjusted_length)
        #self.fuels = transportation.how_much_fuel(total_adjusted_length)
        super().__init__(
            date_start=date_start,
            duration=duration
        )
        self.type = "move"

    def serialize(self) -> dict:
        dictionary = super().serialize()
        dictionary['fuels'] = self.fuels.serialize()
        dictionary['type'] = self.type


if __name__ == "__main__":
    move = Move()
    move.print
