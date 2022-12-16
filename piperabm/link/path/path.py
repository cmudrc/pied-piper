import matplotlib.pyplot as plt
from copy import deepcopy

try:
    from .track import Linear
except:
    from track import Linear
from piperabm.graphics.plt.path import path_to_plt


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
                track = Linear()
                track.from_dict(track_dict)
                tracks.append(track)
        self.tracks = tracks
        self.temp = d['temp']

    def to_plt(self, ax=None):
        """
        Add the required elements to plt
        """
        path_to_plt(self.to_dict(), ax)

    def xylim(self):
        x_min, x_max = 0, 0
        y_min, y_max = 0, 0
        for track in self.tracks:
            x_s = track.pos_start[0]
            y_s = track.pos_start[1]
            if x_s < x_min: x_min = x_s
            elif x_s > x_max: x_max = x_s
            if y_s < y_min: y_min = y_s
            elif y_s > y_max: y_max = y_s
            x_e = track.pos_end[0]
            y_e = track.pos_end[1]
            if x_e < x_min: x_min = x_e
            elif x_e > x_max: x_max = x_e
            if y_e < y_min: y_min = y_e
            elif y_e > y_max: y_max = y_e
        offset_x = (x_max - x_min) / 8
        offset_y = (y_max - y_min) / 8
        xlim, ylim = [x_min-offset_x, x_max+offset_x], [y_min-offset_y, y_max+offset_y]
        return xlim, ylim

    def show(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.axis('equal')
        xlim, ylim = self.xylim()
        plt.xlim(xlim)
        plt.ylim(ylim)
        self.to_plt(ax)
        plt.show()


if __name__ == "__main__":
    p = Path()
    p.add(pos=[0, 0])
    p.add(pos=[0, 3], difficulty=2)
    p.add(pos=[4, 3])
    print(p.total_length())
    print(p.pos(8))
    #p.show()