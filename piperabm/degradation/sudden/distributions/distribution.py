from piperabm.object import Object
from piperabm.unit import DT


class Distribution(Object):

    def __init__(self):
        super().__init__()
        self.type = 'distribution'

    def probability(self, time_start, time_end) -> float:
        time_start = self.refine_input(time_start)
        time_end = self.refine_input(time_end)
        probability_numerator = self.CDF(time_end) - self.CDF(time_start)
        probability_denominator = 1 - self.CDF(time_start)
        probability = probability_numerator / probability_denominator
        return probability

    def refine_input(self, dt_object) -> float:
        if isinstance(dt_object, DT):
            dt = dt_object.total_seconds()
        else:
            dt = dt_object
        return dt