from piperabm.object import Object
from piperabm.resource import Resource
from piperabm.unit import DT


class Transportation(Object):

    def __init__(
            self,
            name: str = None,
            speed: float = None,
            fuel_rate=None
    ):
        self.name = name
        self.speed = speed # None means Infinity
        if fuel_rate is None:
            fuel_rate ={
                'food': 0,
                'water': 0,
                'energy': 0,
            }
        if isinstance(fuel_rate, dict):
            self.fuel_rate = Resource(fuel_rate)
        elif isinstance(fuel_rate, Resource):
            self.fuel_rate = fuel_rate  # resource used for the transport

    def how_long(self, length, object: bool=True):
        """
        Calculate how long does it take to move by length amount.
        """
        result = None
        speed = self.speed
        if speed is None:
            result = 0
        else:
            result = length / self.speed
        if object is True:
            result = DT(seconds=result)
        return result

    def how_much_fuel(self, length):
        """
        Calculate the amount of required fuel
        """
        t = self.how_long(length)
        return self.fuel_rate * t.total_seconds()

    def to_dict(self) -> dict:
        dictionary = {}
        dictionary['name'] = self.name
        dictionary['speed'] = self.speed
        dictionary['fuel_rate'] = None ####
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        self.name = dictionary['name']
        self.speed = dictionary['speed']
        self.fuel_rate = None ####


if __name__ == "__main__":
    transportation = Transportation()
    print(transportation)
