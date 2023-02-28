from piperabm.unit import DT

try: from .track import Track
except: from track import Track


class Path:

    def __init__(self, path, env):
        self.path = path
        self.env = env
        self.tracks = self.path_to_tracks()

    def path_to_tracks(self):
        tracks = []
        for i, _ in enumerate(self.path):
            if i >= 1:
                start_index = self.path[i-1]
                start_pos = self.env.node_info(start_index, 'pos')
                end_index = self.path[i]
                end_pos = self.env.node_info(end_index, 'pos')
                adjusted_length = self.env.adjusted_length(start_index, end_index)
                new_track = Track(start_index, start_pos, end_index, end_pos, adjusted_length)
                tracks.append(new_track)
        return tracks

    def start_pos(self):
        return self.path[0]

    def end_pos(self):
        return self.path[-1]

    def adjusted_length(self):
        total = 0
        for track in self.tracks:
            total += track.adjusted_length
        return total

    def duration(self, transportation):
        duration = 0
        for track in self.tracks:
            duration += track.duration(transportation)
        return duration

    def progress(self, delta_time, transportation):
        progress = None
        duration = self.duration(transportation)
        result = delta_time / duration
        if result < 0:
            progress = 0
        elif result > 1:
            progress = 1
        else:
            progress = result
        return progress

    def find_active_track(self, delta_time, transportation):
        active_track = None
        if delta_time <= 0:
            active_track = self.tracks[0]
            track_index = 0
        elif delta_time >= self.duration(transportation):
            active_track = self.tracks[-1]
            track_index = len(self.tracks) - 1
        else:
            val = delta_time
            for track_index, track in enumerate(self.tracks):
                val -= track.duration(transportation)
                if val <= 0:
                    active_track = track
                    break
        return active_track, track_index

    def pos(self, delta_time, transportation):
        track, index = self.find_active_track(delta_time, transportation)
        delta_time_0 = 0
        for i in range(index):
            delta_time_0 += self.tracks[i].duration(transportation)
        delta_time_track = delta_time - delta_time_0
        return track.pos(delta_time_track, transportation)

    def refine_delta_time(self, delta_time):
        if isinstance(delta_time, (int, float)):
            delta_time = delta_time
        elif isinstance(delta_time, DT):
            delta_time = delta_time.total_seconds()
        else: raise ValueError
        return delta_time

    def __str__(self):
        txt = '"path" from '
        txt += str(self.start_pos())
        txt += ' to '
        txt += str(self.end_pos()) + '\n'
        for track in self.tracks:
            txt += str(track) + '\n'
        return txt