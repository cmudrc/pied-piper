from piperabm.unit import Unit


class Transporation:
    def __init__(self, speed, fuel_consumption=None):
        self.speed = speed
        self.fuel_consumption = None
        

class Walk(Transporation):
    def __init__(self):
        super().__init__(
            speed=Unit(1, 'm/second').to_SI(),
            fuel_consumption=None
            )