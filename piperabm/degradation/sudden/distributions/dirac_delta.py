from piperabm.unit import DT


class DiracDelta:
    """
    Dirac Delta distribution.
    """
    
    def __init__(self, main):
        self.main = self.refine_input(main)

    def refine_input(self, dt_object):
        if isinstance(dt_object, DT):
            dt = dt_object.total_seconds()
        else:
            dt = dt_object
        return dt

    def probability(self, time_start, time_end):
        time_start = self.refine_input(time_start)
        time_end = self.refine_input(time_end)
        return self.CDF(time_end) - self.CDF(time_start)

    def CDF(self, point):
        point = self.refine_input(point)
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