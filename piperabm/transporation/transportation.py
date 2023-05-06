from copy import deepcopy

from piperabm.object import Object
from piperabm.resource import ResourceDelta
from piperabm.unit import DT
from piperabm.tools.symbols import SYMBOLS


class Transportation(Object):

    def __init__(
            self,
            name: str = None,
            speed: float = None,
            fuel_rate=None
    ):
        self.name = name

        if speed is None:
            speed = SYMBOLS['inf']
        self.speed = speed

        if fuel_rate is None:
            fuel_rate = ResourceDelta()
            fuel_rate.create_zeros(['food', 'water', 'energy'])
        if isinstance(fuel_rate, dict):
            fuel_rate = ResourceDelta(fuel_rate)
        if isinstance(fuel_rate, ResourceDelta):
            self.fuel_rate = fuel_rate  # resource used for the transport

    def how_long(self, length):
        """
        Calculate how long does it take to move by length amount.
        """
        result = None
        speed = self.speed
        if speed != 0:
            result = length / self.speed
        else:
            result = SYMBOLS['inf']
        result = DT(seconds=result)
        return result

    def how_much_fuel(self, length):
        """
        Calculate the amount of required fuel
        """
        t = self.how_long(length)
        rate = deepcopy(self.fuel_rate)
        rate * t.total_seconds()
        return rate

    def to_dict(self) -> dict:
        dictionary = {}
        dictionary['name'] = self.name
        dictionary['speed'] = self.speed
        dictionary['fuel_rate'] = self.fuel_rate.to_dict()
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        self.name = dictionary['name']
        self.speed = float(dictionary['speed'])
        fuel_rate = ResourceDelta()
        fuel_rate.from_dict(dictionary['fuel_rate'])
        self.fuel_rate = fuel_rate


if __name__ == "__main__":
    transportation = Transportation()
    print(transportation)
