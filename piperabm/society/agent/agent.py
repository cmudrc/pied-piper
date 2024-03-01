from copy import deepcopy

from piperabm.object import PureObject
from piperabm.matter import Containers, Matters
from piperabm.time import DeltaTime
from piperabm.transportation import Transportation
from piperabm.actions import ActionQueue
from piperabm.society.agent.brain import Brain
from piperabm.society.agent.config import *


class Agent(PureObject):

    section = 'society'
    category = 'node'
    type = 'agent'

    def __init__(
        self,
        name: str = '',
        transportation: Transportation = deepcopy(WALK),
        fuels_rate_idle: Matters = deepcopy(FUELS_RATE_HUMAN_IDLE),
        socioeconomic_status: float = 1,
        average_balance: float = deepcopy(BALANCE_DEFUALT),
        average_resources: Containers = deepcopy(RESOURCES_DEFAULT)
    ):
        super().__init__()
        """ Binding to the model """
        self.model = None

        """ Decision making """
        self.brain = Brain(agent=self)

        """ Identity """
        self.id = None
        self.name = name
        self.home = None
        self.current_node = None
        self.time_outside = DeltaTime(seconds=0)
        self.socioeconomic_status = socioeconomic_status

        """ Transporation """
        self.transportation = transportation
        self.pos = None  # Will be defined based on home

        """ Queue """
        self.queue = ActionQueue()
        self.queue.agent = self  # Binding

        """ Resources """
        self.fuels_rate_idle = fuels_rate_idle
        self.set_resources(average_resources)
        self.set_balance(average_balance)
        self.alive = True
        self.death_reasons = None
    
    def set_resources(self, average_resources: Containers):
        self.resources = average_resources * self.socioeconomic_status

    def set_balance(self, average_balance: float):
        balance = average_balance * self.socioeconomic_status
        if balance < 0: raise ValueError
        self.balance = balance

    @property
    def income(self):  # Currency / seconds
        income_per_month = self.model.average_income # Monthly
        income_per_seconds = income_per_month / (30 * 24 * 3600)
        return income_per_seconds * self.socioeconomic_status

    def check_alive(self) -> bool:
        """
        Check whether agent is alive
        """
        if self.alive is True:
            resources_zero = self.resources.check_empty(RESOURCES_VITAL)
            if len(resources_zero) > 0:  # Died
                self.alive = False
                self.death_reasons = resources_zero
        return self.alive

    def is_home(self) -> bool:
        """
        Check whether agent is in home
        """
        result = None
        if self.home is None:
            print('home index is not defined.')
        else:
            if self.current_node == self.home:
                result = True
            else:
                result = False
        return result
    
    '''
    def utility(self, resource_name):
        return self.resources(name=resource_name)
    '''

    def update(self, duration: DeltaTime) -> None:
        """
        Update agent
        """
        """ Check being alive """
        self.check_alive()
        """ Update assets """
        if self.alive is True:
            """ Income """
            self.balance += self.income * duration.total_seconds()
            """ Consume resources """
            fuels = self.fuels_rate_idle * duration.total_seconds()
            self.resources - fuels
            self.queue.update(duration)
            """ How long it has been out of home? """
            if self.is_home():
                self.time_outside = DeltaTime(seconds=0)
            else:
                self.time_outside += duration
        """ Decide """
        if self.alive is True:
            self.brain.decide()

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['name'] = self.name
        dictionary['id'] = self.id
        dictionary['alive'] = self.alive
        dictionary['death_reasons'] = self.death_reasons
        dictionary['home'] = self.home
        dictionary['time_outside'] = self.time_outside.total_seconds()
        dictionary['transportation'] = self.transportation.serialize()
        dictionary['pos'] = self.pos
        dictionary['queue'] = self.queue.serialize()
        dictionary['resources'] = self.resources.serialize()
        dictionary['fuels_rate_idle'] = self.fuels_rate_idle.serialize()
        dictionary['balance'] = self.balance
        dictionary['type'] = self.type
        dictionary['section'] = self.section
        dictionary['category'] = self.category
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        if dictionary['type'] != self.type:
            raise ValueError
        self.name = dictionary['name']
        self.id = int(dictionary["id"])
        self.alive = dictionary['alive']
        self.death_reasons = dictionary['death_reasons']
        self.home = dictionary['home']
        self.time_outside = DeltaTime(seconds=dictionary['time_outside'])
        self.transportation = Transportation()
        self.transportation.deserialize(dictionary['transportation'])
        self.pos = dictionary['pos']
        self.queue = ActionQueue()
        self.queue.deserialize(dictionary['queue'])
        self.resources = Containers()
        self.resources.deserialize(dictionary['resources'])
        self.fuels_rate_idle = Matters()
        self.fuels_rate_idle.deserialize(dictionary['fuels_rate_idle'])
        self.balance = dictionary['balance']


if __name__ == '__main__':

    from piperabm.matter.containers.samples import containers_0 as resources

    agent = Agent(
        name='Sample',
        average_resources=resources,
        average_balance=1000,
        socioeconomic_status=1,
    )
    agent.print()
