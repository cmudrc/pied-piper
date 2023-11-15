from piperabm.object import PureObject
from piperabm.actions.move.track import Track
from piperabm.transporation import Transportation


class Move(PureObject):

    def __init__(
        self,
        tracks: list = [],
        transportation: Transportation = None
    ):
        super().__init__()
        self.tracks = tracks
        self.transportation = transportation
    
    @property
    def duration(self):
        total = 0
        for track in self.tracks:
            total += track.duration(self.transportation)
        return total

    def find_active_track(self, delta_time: float) -> Track:
        active_track = None
        for track in self.tracks:
            duration = track.duration(self.transportation).total_seconds()
            delta_time -= duration
            if delta_time < 0:
                active_track = track
                remainder_time = delta_time + duration
                break
        return active_track, remainder_time

    def pos(self, delta_time: float) -> list:
        track, remainder_time = self.find_active_track(delta_time)
        return track.pos(remainder_time, self.transportation)


if __name__ == "__main__":

    from piperabm.transporation.samples import transportation_0 as transportation
    from piperabm.actions.move.track import Track

    track_0 = Track(
        pos_start=[0, 0],
        pos_end=[40, 0]
    )
    track_1 = Track(
        pos_start=[40, 0],
        pos_end=[40, 30]
    )
    tracks = [track_0, track_1]
    move = Move(tracks, transportation)
    #print(move.duration)
    pos = move.pos(100)
    print(pos)
