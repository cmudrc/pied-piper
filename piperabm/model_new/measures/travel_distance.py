from copy import deepcopy


class TravelDistanceMeasure:

    def __init__(self):
        self.library = []
        self.per_step = 0

    def add(self):
        self.library.append(deepcopy(self.per_step))
        self.per_step = 0

    def measure(self, value):
        self.per_step += value

    @property
    def total(self):
        return sum(self.library)


if __name__ == '__main__':
    measure = TravelDistanceMeasure()
    measure.measure(5)
    measure.measure(2)
    measure.add()
    measure.measure(3)
    measure.add()
    #print(measure.library)
    print(measure.total)
