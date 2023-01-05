import numpy as np
import matplotlib.pyplot as plt


class DiracDelta():
    """
    Dirac Delta distribution.
    """
    
    def __init__(self, main):
        self.main = main

    def probability(self, time_start, time_end):
        return self.CDF(time_end) - self.CDF(time_start)

    def CDF(self, point):
        result = 0
        if self.main <= point:
            result = 1
        return result

    def show(self):
        pass

    def to_dict(self) -> dict:
        dictionary = {
            'type': 'dirac delta',
            'main': self.main,
        }
        return dictionary
    
    def from_dict(self, dictionary: dict):
        d = dictionary
        self.main = d['main']


if __name__ == "__main__":
    time_start=0
    time_end=90

    d = DiracDelta(
        main=100
    )
    print(
        d.probability(
            time_start=time_start,
            time_end=time_end
        )
    )