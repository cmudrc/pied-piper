from piperabm.actions.action import Action
from piperabm.actions.move.tracks import Tracks
from piperabm.time import Date


class MoveNew(Action):

    type = 'move'

    def __init__(
        self,
        transportation = None,
        date_start: Date = None
    ):
        self.current_progress = 0
        self.tracks = Tracks()
        self.transportation = transportation
        super().__init__(
            date_start=date_start,
            duration=0
        )

    def add_tracks(self, tracks):
        self.tracks = tracks
        duration = self.tracks.duration(self.transportation)
        self.date_end = self.date_start + duration

    def get(self, index):
        self.agent.model.get(index)
    #@property
    #def transportation(self):
    #    return self.agent.transportation
    
    @property
    def done(self):
        result = False
        if self.current_progress == 1:
            result = True
        return result
    
    def update(self, date):
        """
        Update status of action
        """
        new_progress = self.progress(date)
        if new_progress < self.current_progress:
            raise ValueError
        delta_progress = new_progress - self.current_progress
        duration = self.duration * delta_progress
        fuels = self.transportation.fuels_by_duration(duration)
        self.agent.resources - fuels
        pos = self.pos(date)
        self.agent.pos = pos
        self.current_progress = new_progress
        #return {'pos': pos, 'consumption': fuels}

        
        #if date > self.date_end:
        #    self.done = True
        
    
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
