import numpy as np
from piperabm.unit import DT


class Track:

    def duration(self, transportation):
        """
        Calculate how long does it take to finish the track 
        """
        return transportation.how_long(self.length('adjusted'))
    
    def fuel(self, transportation):
        """
        Calculate how much fuel does it take to finish the track 
        """
        return transportation.how_much_fuel(self.length('adjusted'))
    
    def refine_delta_time(self, delta_time) -> DT:
        if isinstance(delta_time, DT):
            delta_time = delta_time
        elif isinstance(delta_time, (int, float)):
            delta_time = DT(seconds=delta_time)
        else: raise ValueError
        return delta_time
    
    def progress(self, elapsed_time, transportation):
        delta_time = self.refine_delta_time(elapsed_time)
        delta_time = delta_time.total_seconds()
        duration = self.duration(transportation)
        duration = duration.total_seconds()
        progress = delta_time / duration
        if progress < 0:
            progress = 0
        elif progress > 1:
            progress = 1
        return progress

