from piperabm.actions.action import Action
from piperabm.actions.move.tracks import Tracks
from piperabm.time import Date


class Move(Action):

    type = 'move'

    def __init__(
        self,
        date_start: Date = None
    ):
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
    
    def update(self, date):
        """
        Update status of action
        """
        pos = self.pos(date)
        self.agent.pos = pos
        if date > self.date_end:
            self.done = True
    
    def pos(self, date):
        """
        Calcualte position based on date
        """
        delta_time = date - self.date_start
        return self.tracks.pos(delta_time, self.transportation)

    def serialize(self) -> dict:
        dictionary = super().serialize()
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
