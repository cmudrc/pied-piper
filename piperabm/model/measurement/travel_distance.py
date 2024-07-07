import matplotlib.pyplot as plt


class TravelDistance:
    """
    Manage travel distance measurement
    """

    type = 'travel distance'

    def __init__(self, measurement):
        self.measurement = measurement
        self.values = []

    def add(self, value: float) -> None:
        """
        Add new travel distance value
        """
        self.values.append(value)

    def filter(self, _from=None, _to=None):
        """
        Filter values in a specific range
        """
        if _from is None:
            _from = 0
        if _to is None:
            _to = len(self.values)
        return self.values[_from: _to]
    
    def __call__(self, _from=None, _to=None):
        return self.filter(_from=_from, _to=_to)
    
    def show(self, _from=None, _to=None):
        """
        Draw plot
        """
        plt.title("Travel Distance")
        xs = self.measurement.filter_times(_from=_from, _to=_to)
        yx = self.filter(_from=_from, _to=_to)
        plt.plot(xs, yx, color='blue')
        plt.xlabel("Time")
        plt.ylabel("Travel Distance")
        plt.show()

    def serialize(self) -> dict:
        """
        Serialize
        """
        return {
            'values': self.values,
            'type': self.type
        }
    
    def deserialize(self, data: dict) -> None:
        """
        Deserialize
        """
        self.values = data['values']


if __name__ == "__main__":
    
    from piperabm.model.measurement import Measurement

    measure = Measurement()
    hour = 3600
    measure.add_time(0 * hour) # Base

    # 1
    measure.add_time(value=1*hour)
    measure.travel_distance.add(value=1.1)
    # 2
    measure.add_time(value=2*hour)
    measure.travel_distance.add(value=0.9)
    # 3
    measure.add_time(value=3*hour)
    measure.travel_distance.add(value=0.3)
    # 4
    measure.add_time(value=4*hour)
    measure.travel_distance.add(value=0.46)
    # 5
    measure.add_time(value=5*hour)
    measure.travel_distance.add(value=0.2)

    _from = None
    _to = None
    print("travel distances: ", measure.travel_distance(_from=_from, _to=_to))
    measure.travel_distance.show(_from=_from, _to=_to)