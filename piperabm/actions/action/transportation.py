from piperabm.unit import Unit


class Transporation:
    def __init__(self, speed, fuel_rate={}):
        self.speed = speed
        self.fuel_rate = fuel_rate # dictionary: {resource_name: consumption_rate}

    def fuel_consumption(self, duration):
        """
        Calculate fuel consumption in the desired duration of time
        """
        consumption = {} # dictionary: {resource_name: consumption}
        for key in self.fuel_rate:
            consumption[key] = self.fuel_rate[key] * duration
        return consumption
        

class Walk(Transporation):
    def __init__(self):
        super().__init__(
            speed=Unit(1, 'm/second').to_SI(),
            fuel_rate={
                'food': 0.01,
                'water': 0.02,
            }
            )