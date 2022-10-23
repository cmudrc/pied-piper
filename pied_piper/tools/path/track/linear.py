import numpy as np

try:
    from .distance import euclidean_distance
except:
    from distance import euclidean_distance


class Linear:
    def __init__(
        self,
        pos_start,
        pos_end,
        name_start=None,
        name_end=None,
        length=None
    ):
        self.pos_start, self.pos_end = pos_start, pos_end
        self.name_start, self.name_end = name_start, name_end
        self.distance = euclidean_distance(*pos_start, *pos_end)
        if length is None:
            self.length = self.distance
        else:
            if length >= self.distance:
                self.length = length
            else:
                raise ValueError
    
    def pos(self, current_length:float):
        """
        Calculate the position based on path length (current) from start to end.
        """
        result = None
        progress = self.progress(current_length)
        if progress == 0:
            result = self.pos_start
        elif progress == 1:
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

    def progress(self, current_length:float):
        """
        Calculate the progress based on path length (current) from start to end.
        """
        result = None
        result = current_length / self.length
        if result > 1: result = 1
        elif result < 0: result = 0
        return result

    def status(self, progress:float):
        """
        Calculate the status based on path length (current) from start to end.
        """
        result = None
        if progress == 0:
            result = 'not started'
        elif progress == 1:
            result = 'done'
        else:
            result = 'in progress'
        return result


if __name__ == "__main__":
    track = Linear([0, 0], [1, 1], length=3)
    #print(track.distance, track.length)
    print(track.pos(current_length=1.5))