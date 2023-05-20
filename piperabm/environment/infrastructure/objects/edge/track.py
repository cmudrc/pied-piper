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
    