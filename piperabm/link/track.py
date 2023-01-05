import  numpy as np
import matplotlib.pyplot as plt

from piperabm.degradation import DegradationProperty, degradation_kwargs, Eternal
from piperabm.graphics.plt.path import track_to_plt


class Track(DegradationProperty):

    def __init__(self, start_name, end_name, length=None, difficulty=1):
        super().__init__(
            **degradation_kwargs
        )
        self.start_name = start_name
        self.end_name = end_name
        self.length = length
        self.difficulty = difficulty
        #self.coeff = self.length / 1000  # for degradation


if __name__ == "__main__":
    from piperabm.unit import Date
    from piperabm.degradation import DiracDelta

    t = Track('here', 'there', length=1000, difficulty=1)
    t.initiation_date = Date(2020,1,1)
    t.add_distribution(DiracDelta(main=5*24*3600))
    t.is_working
    p = t.probability_of_working(Date(2020,1,1), Date(2020,1,10))
    #active = t.is_active(Date(2020,1,1), Date(2020,1,10))
    print(p)
    

    

    