from copy import deepcopy

from piperabm.object import PureObject
from piperabm.resources import Resources
from piperabm.resources.samples import resources_0 as default_fuel_rate
from piperabm.time import DeltaTime
from piperabm.tools.symbols import SYMBOLS


class Transportation(PureObject):

    def __init__(
            self,
            name: str = None,
            speed: float = None,
            fuels_rate: Resources = None
    ):
        self.name = name

        if speed is None:
            speed = SYMBOLS['inf']
        self.speed = speed

        if fuels_rate is None:
            fuels_rate = deepcopy(default_fuel_rate)
        self.fuels_rate = fuels_rate

    def how_long(self, length):
        """
        Calculate how long does it take to move by length amount.
        """
        result = None
        if self.speed != 0:
            result = length / self.speed
        else:
            result = SYMBOLS['inf']
        result = DeltaTime(seconds=result)
        return result

    def how_much_fuel(self, length):
        """
        Calculate the amount of required fuel
        """
        fuels_rate = deepcopy(self.fuels_rate)
        time = self.how_long(length)
        fuels_rate.mul(time.total_seconds())
        return fuels_rate

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['name'] = self.name
        dictionary['speed'] = self.speed
        dictionary['fuels_rate'] = self.fuels_rate.serialize()
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        self.name = dictionary['name']
        self.speed = float(dictionary['speed'])
        self.fuels_rate = Resources()
        self.fuels_rate.deserialize(dictionary['fuels_rate'])


if __name__ == '__main__':
    from piperabm.transporation.samples import transportation_0 as walk

    fuels_rate = walk.how_much_fuel(1000)
    fuels_rate.print
