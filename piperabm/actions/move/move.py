from piperabm.object import PureObject
from piperabm.actions.move.track import Track


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
    
    def update(self, duration):
        """
        Update status of action
        """
        delta_time = duration
        while delta_time.total_seconds() > 0:
            track = self.active_track
            if track is not None:
                delta_time = track.update(delta_time, self.transportation)
            else:
                break

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
            track.queue = self.queue
            self.tracks.append(track)


if __name__ == '__main__':
    move = Move()
    move.print
