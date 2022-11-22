import numpy as np

from piperabm.path import euclidean_distance

try:
    from .track import Track
except:
    from track import Track


class Linear(Track):
    def __init__(
        self,
        pos_start=None,
        pos_end=None,
        length=None,
        difficulty=1
    ):
        super().__init__()
        self.add_pos(pos_start, pos_end)
        self.add_length(length)
        self.difficulty = difficulty

    def add_pos(self, pos_start, pos_end):
        """
        Add position information to the instance
        """
        self.pos_start, self.pos_end = pos_start, pos_end
        if pos_start is not None and pos_end is not None:
            self.displacement = euclidean_distance(*pos_start, *pos_end)
        else:
            self.displacement = None

    def add_length(self, length: float):
        """
        Add custom length information to the instance
        """
        if self.displacement is not None:
            if length is None:
                self.length = self.displacement
            else:
                if length >= self.displacement:
                    self.length = length
                else:
                    raise ValueError
        else:
            self.length = None

    def pos(self, current_length: float):
        """
        Calculate the current position based on current displacement vector starting from *pos_start*
        """
        result = None
        progress = self.progress(current_length)
        if progress <= 0:
            result = self.pos_start
        elif progress >= 1:
            result = self.pos_end
        else:
            current_displacement_vector = progress * self.total_displacement_vector()
            result = self.pos_start + current_displacement_vector
        return list(result)

    def total_displacement_vector(self):
        """
        Total displacement vector between starting point and ending point
        """
        return np.array(self.pos_end) - np.array(self.pos_start)

    def progress(self, current_length: float):
        """
        Calculate the progress based on path length (current) from start to end.
        """
        result = None
        result = current_length / (self.length * self.difficulty)
        if result > 1:
            result = 1
        elif result < 0:
            result = 0
        return result

    def status(self, progress: float):
        """
        Calculate the status based on path length (current) from start to end.
        """
        result = None
        if progress <= 0:
            result = 'not started'
        elif progress >= 1:
            result = 'done'
        else:
            result = 'in progress'
        return result

    def __str__(self):
        txt = ''
        txt += 'from ' + str(self.pos_start)
        txt += ' to ' + str(self.pos_end)
        return txt

    def to_dict(self) -> dict:
        dictionary = {
            'type': 'linear',
            'pos_start': self.pos_start,
            'pos_end': self.pos_end,
            'length': self.length,
            'difficulty': self.difficulty
        }
        dictionary = {**dictionary, **self.degradation_to_dict()}
        return dictionary

    def from_dict(self, dictionary: dict):
        d = dictionary
        self.degradation_from_dict(dictionary)
        self.add_pos(d['pos_start'], d['pos_end'])
        self.add_length(d['length'])
        self.difficulty = d['difficulty']


if __name__ == "__main__":
    track = Linear([0, 0], [1, 1], length=3, difficulty=2)
    print(track.pos(current_length=1.5))
    track.show()
