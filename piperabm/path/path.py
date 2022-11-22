from copy import deepcopy

try:
    from .track import Linear
except:
    from track import Linear


class Path:
    def __init__(
        self,
        tracks=[]
    ):
        self.tracks = tracks
        self.temp = None

    def add(self, pos, length=None, difficulty=1):
        """
        Add a new track to the path.
        """
        track = None
        if len(self.tracks) > 0:
            track = Linear(
                pos_start=self.tracks[-1].pos_end,
                pos_end=pos,
                length=length,
                difficulty=difficulty
            )
        else:
            if self.temp is None:
                self.temp = pos
            else:
                track = Linear(
                    pos_start=deepcopy(self.temp),
                    pos_end=pos,
                    length=length,
                    difficulty=difficulty
                )
                self.temp = None
        if track is not None:
            self.tracks.append(track)

    def total_length(self):
        """
        Length of all tracks within the path combined.
        """
        result = 0
        for track in self.tracks:
            result = result + track.length
        return result

    def progress(self, current_length: float):
        """
        Calculate the progress

        Returns:
            float value between 0 and 1
        """
        result = None
        result = current_length / self.total_length()
        if result > 1:
            result = 1
        elif result < 0:
            result = 0
        return result

    def find_active_track(self, current_length: float):
        """
        Find the track in tracks list that is active at the moment.
        """
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

    def __str__(self):
        txt = ''
        for track in self.tracks:
            txt += track.__str__()
            txt += '\n'
        return txt

    def to_dict(self) -> dict:
        tracks_list = []
        for track in self.tracks:
            track_dict = track.to_dict()
            tracks_list.append(track_dict)
        dictionary = {
            'temp': self.temp,
            'tracks': tracks_list
        }
        return dictionary

    def from_dict(self, dictionary: dict):
        d = dictionary
        tracks = []
        tracks_list = d['tracks']
        for track_dict in tracks_list:
            if track_dict['type'] == 'linear':
                print(track_dict)
                track = Linear()
                track.from_dict(track_dict)
                tracks.append(track)
        self.tracks = tracks
        self.temp = d['temp']


if __name__ == "__main__":
    p = Path()
    p.add(pos=[0, 0])
    p.add(pos=[0, 3], difficulty=2)
    p.add(pos=[4, 3])
    #print(p.total_length())

    dictionary = p.to_dict()
    print(dictionary)
    p_new = Path()
    p_new.from_dict(dictionary)
    #print(p_new.tracks)
    dictionary_new = p_new.to_dict()
    print(dictionary_new)