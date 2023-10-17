from piperabm.object import PureObject
from piperabm.actions.move.track import Track


class Tracks(PureObject):

    def __init__(
        self,
        positions: list = None
    ):
        super().__init__()
        self.library = self.positions_to_tracks(positions)

    def positions_to_tracks(self, positions) -> list:
        result = []
        for i in range(len(positions)-1):
            pos_start = positions[i]
            pos_end = positions[i+1]
            track = Track(pos_start, pos_end)
            result.append(track)
        return result

    @property
    def total_length(self):
        total = 0
        for track in self.library:
            total += track.length
        return total

    def find_active_track(self, progress: float) -> Track:
        active_track = None
        active_track_ratio = None
        current_length = progress * self.total_length
        for track in self.library:
            current_length -= track.length
            if current_length < 0:
                active_track = track
                remainder_length = current_length + active_track.length
                active_track_ratio = remainder_length / active_track.length
                break
        return active_track, active_track_ratio

    def pos(self, progress: float) -> list:
        track, track_ratio = self.find_active_track(progress)
        return track.pos(track_ratio)


if __name__ == "__main__":
    positions = [
        [0, 0],
        [4, 0],
        [4, 3]
    ]
    tracks = Tracks(positions)
    pos = tracks.pos(progress=0.5)
    print(pos)
