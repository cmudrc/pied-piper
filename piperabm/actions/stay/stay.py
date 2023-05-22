from piperabm.actions.action import Action
from piperabm.unit import Date, DT


class Stay(Action):

    def __init__(
            self,
            start_date: Date = None,
            duration=None,
            environment=None,
            agent_index: int = None,
        ):
        self.environment = environment
        self.agent_index = agent_index

        if isinstance(duration, (float, int)):
            duration = DT(seconds=duration)
        super().__init__(
            start_date=start_date,
            duration=duration
        )
        self.done = False
        self.type = 'stay'

    def to_dict(self) -> dict:
        dictionary = super().to_dict()
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        super().from_dict(dictionary)

    
if __name__ == "__main__":
    from piperabm.actions.move.samples import move_0 as move

    print(move)