from copy import deepcopy

try:
    from .track import Linear
except:
    from track import Linear


class Path:
    def __init__(self):
        self.tracks = []
        self.temp = None

    def total_length(self):
        result = 0
        for track in self.tracks:
            result = result + track.length
        return result

    def progress(self, current_length: float):
        result = None
        result = current_length / self.total_length()
        if result > 1:
            result = 1
        elif result < 0:
            result = 0
        return result

    def find_active_track(self, current_length: float):
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

    def pos(self, current_length: float):
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

    def add(self, pos, name=None, mode='linear', length=None):
        pos_start, name_start = None, None
        if len(self.tracks) == 0:
            if self.temp is None:
                self.temp = [pos, name]
            else:
                pos_start = self.temp[0]
                name_start = self.temp[1]
        else:
            pos_start = self.tracks[-1].pos_end
            name_start = self.tracks[-1].name_end

        new = None
        if pos_start is not None:
            if mode == 'linear':
                new = Linear(
                    pos_start=pos_start,
                    pos_end=pos,
                    name_start=name_start,
                    name_end=name,
                    length=length
                )
            else:
                pass

        if new is not None:
            self.tracks.append(new)

    def __str__(self):
        txt = ''
        for track in self.tracks:
            txt += track.__str__()
            txt += '\n'
        return txt


if __name__ == "__main__":
    p = Path()
    p.add(pos=[0, 0])
    p.add(pos=[0, 3])
    p.add(pos=[4, 3])
    print(p.total_length())
