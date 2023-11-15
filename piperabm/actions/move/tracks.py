from piperabm.object import PureObject
from piperabm.actions.move.track import Track
from piperabm.time import DeltaTime


class Tracks(PureObject):

    def __init__(
        self,
        library: list = [],
    ):
        super().__init__()
        self.library = library
    
    def add(self, tracks):
        if isinstance(tracks, Track):
            self.library.append(tracks)
        elif isinstance(tracks, list):
            for track in tracks:
                self.add(track)

    @property
    def duration(self):
        total = 0
        for track in self.library:
            total += track.duration.total_seconds()
        return DeltaTime(seconds=total)

    def find_active_track(self, delta_time) -> Track:
        if isinstance(delta_time, DeltaTime):
            delta_time = delta_time.total_seconds()
        active_track = None
        if delta_time >= self.duration.total_seconds():
            active_track = self.library[-1]
            remainder_time = active_track.duration
        else:
            for track in self.library:
                duration = track.duration.total_seconds()
                delta_time -= duration
                if delta_time < 0:
                    active_track = track
                    remainder_time = delta_time + duration
                    break
        return active_track, remainder_time

    def pos(self, delta_time) -> list:
        active_track, remainder_time = self.find_active_track(delta_time)
        return active_track.pos(remainder_time)


if __name__ == "__main__":

    from piperabm.transporation.samples import transportation_0 as transportation
    from piperabm.actions.move.track import Track

    track_0 = Track(
        pos_start=[0, 0],
        pos_end=[40, 0],
        transportation=transportation
    )
    track_1 = Track(
        pos_start=[40, 0],
        pos_end=[40, 30],
        transportation=transportation
    )
    tracks = Tracks([track_0, track_1])
    print(tracks.duration)
    #pos = tracks.pos(100)
    #print(pos)
