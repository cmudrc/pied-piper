from piperabm.degradation.sudden.distributions.distribution import Distribution


class Eternal(Distribution):
    """
    Eternal distribution.
    """

    def __init__(self):
        super().__init__()
        self.type = 'eternal'
    
    def CDF(self, time) -> float:
        return 0

    def to_dict(self) -> dict:
        dictionary = {'type': self.type}
        return dictionary
    

if __name__ == "__main__":
    time_start=0
    time_end=90

    distribution = Eternal()
    print(
        distribution.probability(
            time_start=time_start,
            time_end=time_end
        )
    )