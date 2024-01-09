import numpy as np

from piperabm.object import PureObject
from piperabm.tools.coordinate.distance import point_to_point
from piperabm.tools.linear_algebra import vector
from piperabm.transporation import Transportation
from piperabm.time import DeltaTime


class Track(PureObject):

    type = 'track'

    def __init__(
        self,
        pos_start: list = None,
        pos_end: list = None,
        adjustment_factor: float = 1
    ):
        super().__init__()
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.length_real = point_to_point(self.pos_start, self.pos_end)
        if adjustment_factor < 0:
            raise ValueError
        self.length_adjusted = self.length_real * adjustment_factor
    
    @property
    def vector(self):
        """
        Movement vector
        """
        return vector(self.pos_start, self.pos_end)
    
    @property
    def unit_vector(self):
        """
        Unit vector showing the direction of movement
        """
        return self.vector / self.length_real
    
    def duration(self, transportation: Transportation):
        """
        Duration of movement on the track
        """
        return transportation.how_long(length=self.length_adjusted)
    
    def total_fuel(self, transportation: Transportation):
        """
        Total amount of fuel of movement on the track
        """
        return transportation.how_much_fuel(length=self.length_adjusted)
    
    def pos(self, delta_time, transportation):
        if isinstance(delta_time, DeltaTime):
            delta_time = delta_time.total_seconds()
        progress = delta_time / self.duration(transportation).total_seconds()
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
        
        result = np.array(self.pos_start) + self.unit_vector * progress * self.length_real
        return list(result)

    def serialize(self):
        dictionary = {}
        dictionary['pos_start'] = self.pos_start
        dictionary['pos_end'] = self.pos_end
        dictionary['length_real'] = self.length_real
        dictionary['length_adjusted'] = self.length_adjusted
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        self.pos_start = dictionary['pos_start']
        self.pos_end = dictionary['pos_end']
        self.length_real = dictionary['length_real']
        self.length_adjusted = dictionary['length_adjusted']


if __name__ == '__main__':

    from piperabm.transporation.samples import transportation_0 as transportation

    track = Track(
        pos_start=[0, 0],
        pos_end=[100, 100],
        adjustment_factor=1
    )
    delta_time = 60
    pos = track.pos(delta_time, transportation)
    print(pos)
    #track.print