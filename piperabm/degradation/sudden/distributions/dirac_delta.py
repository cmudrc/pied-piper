from piperabm.degradation.sudden.distributions.distribution import Distribution


class DiracDelta(Distribution):
    """
    Dirac Delta distribution.
    """
    
    def __init__(self, main=0):
        super().__init__()
        self.main = self.refine_input(main)

    def CDF(self, point) -> float:
        result = None
        point = self.refine_input(point)
        if self.main <= point:
            result = 1
        else:
            result = 0
        return result

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