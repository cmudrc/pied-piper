from piperabm.object import PureObject
from piperabm.matter_new import Matter
from piperabm.time import DeltaTime
from piperabm.tools.symbols import SYMBOLS


class Transportation(PureObject):

    type = 'transportation'

    def __init__(
            self,
            name: str = None,
            speed: float = SYMBOLS['inf'],
            fuels_rate: Matter = Matter({'food': 0, 'water': 0, 'energy': 0}),
            wear: float = 0,
    ):
        self.name = name
        self.speed = speed
        self.fuels_rate = fuels_rate
        self.wear = wear

    def length_by_duration(self, duration):
        """
        Calculate length based on duration
        """
        if isinstance(duration, DeltaTime):
            duration = duration.total_seconds()
        length = self.speed * duration
        return length

    def duration_by_length(self, length):
        """
        Calculate how long does it take to move by length amount.
        """
        if self.speed != 0:
            duration = length / self.speed
        else:
            duration = SYMBOLS['inf']
        duration = DeltaTime(seconds=duration)
        return duration
    
    def fuels_by_duration(self, duration):
        """
        Calculate the amount of required fuel based on duration
        """
        if isinstance(duration, DeltaTime):
            duration = duration.total_seconds()
        fuels = self.fuels_rate * duration
        return fuels

    def fuels_by_length(self, length):
        """
        Calculate the amount of required fuel based on length
        """
        time = self.duration_by_length(length)
        fuels = self.fuels_by_duration(time)
        return fuels
    
    def duration_by_fuels(self, fuels):
        """
        How long can one move having *fuels*
        """
        if isinstance(fuels, dict):
            fuels = Matter(fuels)
        if not isinstance(fuels, Matter):
            raise ValueError
        ratios = fuels / self.fuels_rate
        ratios = ratios.library
        min_key = min(ratios, key=ratios.get)
        duration = ratios[min_key]
        return duration

    def length_by_fuels(self, fuels):
        """
        How much can one move having *fuels*
        """
        duration = self.duration_by_fuels(fuels)
        length = self.length_by_duration(duration)
        return length

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['type'] = self.type
        dictionary['name'] = self.name
        dictionary['speed'] = self.speed
        dictionary['fuels_rate'] = self.fuels_rate.serialize()
        dictionary['wear'] = self.wear
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        if dictionary['type'] != self.type:
            raise ValueError
        self.name = dictionary['name']
        self.speed = float(dictionary['speed'])
        self.fuels_rate = Matter(dictionary['fuels_rate'])
        self.wear = dictionary['wear']


if __name__ == '__main__':

    from piperabm.transportation.samples import transportation_0 as walk

    fuels_rate = walk.fuels_by_length(1000)
    print(fuels_rate)
    duration = walk.duration_by_fuels({'food': 1, 'water': 1, 'energy': 1})
    print(duration)
