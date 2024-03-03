from piperabm.object import PureObject
from piperabm.actions.movement.track import Track
from piperabm.time import DeltaTime


class Move(PureObject):

    type = 'move'

    def __init__(self, path: list = []):
        super().__init__()
        self.tracks = self.path_to_tracks(path)
        self.usage = 1
        self.queue = None  # Binding

    def path_to_tracks(self, path):
        tracks = []
        for i, _ in enumerate(path):
            if i != 0:
                index_start = path[i-1]
                index_end = path[i]
                track = Track(index_start, index_end)
                track.action = self
                tracks.append(track)
        return tracks

    def get(self, index):
        self.model.get(index)

    @property
    def transportation(self):
        return self.agent.transportation

    @property
    def agent(self):
        return self.queue.agent
    
    @property
    def model(self):
        return self.agent.model
    
    @property
    def transportation(self):
        return self.agent.transportation
    
    @property
    def destination(self):
        last_track = self.tracks[-1]
        return last_track.id_end
    
    @property
    def active_track(self):
        result = None
        for track in self.tracks:
            #print(track.done)
            if track.done is False:
                result = track
                break
        return result
    
    @property
    def done(self):
        result = True
        for track in self.tracks:
            status = track.done
            if status is False:
                result = False
                break
        return result
    
    @property
    def remaining_time(self):
        """
        Estimate the remaining time to complete action
        """
        remainings = []
        for track in self.tracks:
            remainings.append(track.remaining_time)
        return sum(remainings, start=DeltaTime(seconds=0))

    def update(self, duration):
        """
        Update status of action
        """
        self.agent.current_node = None
        excess_delta_time = duration
        while excess_delta_time.total_seconds() > 0:
            track = self.active_track
            if track is not None:
                excess_delta_time = track.update(excess_delta_time, self.transportation)
            else: # Action ended
                self.agent.current_node = self.destination
                break
            #print(excess_delta_time.total_seconds())
        return excess_delta_time

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['type'] = self.type
        tracks_serialized = []
        for track in self.tracks:
            track_serialized = track.serialize()
            tracks_serialized.append(track_serialized)
        dictionary['tracks'] = tracks_serialized
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        if dictionary['type'] != self.type:
            raise ValueError
        tracks_serialized = dictionary['tracks']
        for track_serialized in tracks_serialized:
            track = Track()
            track.deserialize(track_serialized)
            track.action = self  # Binding
            self.tracks.append(track)


if __name__ == '__main__':
    move = Move()
    move.print()
