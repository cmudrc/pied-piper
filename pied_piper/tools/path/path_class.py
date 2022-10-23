from copy import deepcopy

try:
    from .track import Linear
except:
    from track import Linear


class Path:
    def __init__(self, tracks:list):
        self.tracks = tracks

    def total_length(self):
        result = 0
        for track in self.tracks:
            result = result + track.length
        return result

    def progress(self, current_length:float):
        result = None
        result = current_length / self.total_length()
        if result > 1: result = 1
        elif result < 0: result = 0
        return result

    def find_active_track(self, current_length:float):
        current_length_input = deepcopy(current_length)
        result = None
        remainder_val = None
        total_val = 0
        for track in self.tracks:
            current_length -= track.length
            total_val += track.length
            if current_length < 0:
                result = track
                total_val -= track.length
                remainder_val = current_length_input - total_val
                break
        return result, remainder_val

    def pos(self, current_length:float):
        """
        Calculate position based on path length (current) from start to end.
        """
        p = self.progress(current_length)
        if p == 0:
            result = self.tracks[0].pos_start
        elif p == 1:
            result = self.tracks[-1].pos_end
        else:
            track, remainder_val = self.find_active_track(current_length)
            result = track.pos(current_length=remainder_val)
        return result


if __name__ == "__main__":
    tracks = [
        Linear(pos_start=[0, 0], pos_end=[1, 1]),
        Linear(pos_start=[1, 1], pos_end=[1, 2])
    ]
    path = Path(tracks)
    print(path.total_length())
    '''
    path = Path(
        'place_1',
        [0, 0],
        'place_2',
        [2, 3]
    )
    '''

        