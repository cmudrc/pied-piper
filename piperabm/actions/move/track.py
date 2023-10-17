import numpy as np

from piperabm.object import PureObject
from piperabm.tools.coordinate import distance_point_to_point


class Track(PureObject):

    def __init__(
        self,
        pos_start: list = None,
        pos_end: list = None
    ):
        super().__init__()
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.length = distance_point_to_point(self.pos_start, self.pos_end)
    
    def pos(self, progress: float) -> list:
        """
        Calcualte position based on ratio of track
        """
        result = None
        if progress > 1 or progress < 0:
            raise ValueError
        
        vector_start = np.array(self.pos_start)
        vector_end = np.array(self.pos_end)
        vector = vector_end - vector_start
        vector_normalized = vector / np.linalg.norm(vector)
        result = vector_start + vector_normalized * self.length * progress
        return result
    
    def serialize(self):
        dictionary = {}
        dictionary['pos_start'] = self.pos_start
        dictionary['pos_end'] = self.pos_end
        dictionary['length'] = self.length
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        self.pos_start = dictionary['pos_start']
        self.pos_end = dictionary['pos_end']
        self.length = dictionary['length']


if __name__ == "__main__":
    track = Track(
        pos_start=[0, 0],
        pos_end=[10, 10]
    )
    pos = track.pos(progress=0.5)
    print(pos)
    track.print