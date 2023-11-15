import numpy as np

from piperabm.object import PureObject
from piperabm.tools.coordinate.distance import point_to_point
from piperabm.transporation import Transportation
from piperabm.time import DeltaTime


class Track(PureObject):

    def __init__(
        self,
        pos_start: list = None,
        pos_end: list = None,
        adjustment_factor: float = 1,
        transportation: Transportation = None
    ):
        super().__init__()
        self.pos_start = np.array(pos_start)
        self.pos_end = np.array(pos_end)
        if adjustment_factor < 0:
            raise ValueError
        self.adjustment_factor = adjustment_factor
        self.transportation = transportation
    
    @property
    def length(self):
        """
        Physical length of track
        """
        return point_to_point(self.pos_start, self.pos_end)

    @property
    def length_adjusted(self):
        """
        Adjusted length of track
        """
        return self.length * self.adjustment_factor
    
    @property
    def vector(self):
        """
        Movement vector
        """
        return self.pos_end - self.pos_start
    
    @property
    def unit_vector(self):
        """
        Unit vector showing the direction of movement
        """
        return self.vector / self.length
    
    @property
    def duration(self):
        """
        Duration of movement on the track
        """
        return self.transportation.how_long(length=self.length_adjusted)
    
    def pos(self, delta_time):
        if isinstance(delta_time, DeltaTime):
            delta_time = delta_time.total_seconds()
        progress = delta_time / self.duration.total_seconds()
        return self.pos_by_progress(progress)

    def pos_by_progress(self, progress: float) -> list:
        """
        Calcualte position based on ratio of track
        """
        result = None
        if progress > 1:
            progress = 1
        if progress < 0:
            progress = 0
        
        result = np.array(self.pos_start) + self.unit_vector * progress * self.length
        return list(result)

    def serialize(self):
        dictionary = {}
        dictionary["pos_start"] = self.pos_start
        dictionary["pos_end"] = self.pos_end
        dictionary["adjustment_factor"] = self.adjustment_factor
        dictionary["transportation"] = self.transportation.serialize()
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        self.pos_start = dictionary["pos_start"]
        self.pos_end = dictionary["pos_end"]
        self.adjustment_factor = dictionary["adjustment_factor"]
        self.transportation = Transportation()
        self.transportation.deserialize(dictionary["transportation"])


if __name__ == "__main__":

    from piperabm.transporation.samples import transportation_0 as transportation

    track = Track(
        pos_start=[0, 0],
        pos_end=[100, 100],
        transportation=transportation,
        adjustment_factor=1
    )
    delta_time = 60
    pos = track.pos(delta_time)
    print(pos)
    #track.print