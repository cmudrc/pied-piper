from piperabm.actions.action import Action
from piperabm.actions.move.tracks import Tracks
from piperabm.transporation import Transportation
from piperabm.time import Date


class Move(Action):

    type = 'move'

    def __init__(
        self,
        agent = None,
        date_start: Date = None
    ):
        self.agent = agent
        self.tracks = Tracks()
        super().__init__(
            date_start=date_start,
            duration=0
        )

    def add_tracks(self, tracks):
        self.tracks = tracks
        duration = self.tracks.duration(self.transportation)
        self.date_end = self.date_start + duration

    @property
    def transportation(self):
        return self.agent.transportation

    def serialize(self) -> dict:
        dictionary = super().serialize()
        dictionary['agent_index'] = self.agent
        dictionary['tracks'] = self.tracks.serialize()
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        super().deserialize(dictionary)
        self.tracks = Tracks()
        self.tracks.deserialize(dictionary['tracks'])


if __name__ == '__main__':
    move = Move()
    move.print
