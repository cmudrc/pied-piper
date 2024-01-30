from copy import deepcopy

from piperabm.object import PureObject
from piperabm.matter import Containers, Matters
from piperabm.time import DeltaTime
from piperabm.transportation import Transportation
from piperabm.actions import ActionQueue
#from piperabm.agent.brain import Brain
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
        #self.brain = Brain()
        self.brain = None

        """ Identity """
        self.index = None
        self.name = name
        self.home = None
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

    @property
    def alive(self) -> bool:
        """
        Check whether agent is alive
        """
        result = True
        resources_zero = self.resources.check_empty(RESOURCES_VITAL)
        if len(resources_zero) > 0:  # Died
            result = False
        return result
    
    @property
    def death_reason(self):
        result = None
        resources_zero = self.resources.check_empty(RESOURCES_VITAL)
        if len(resources_zero) > 0:  # Died
            result = resources_zero[0]
        return result

    def is_home(self) -> bool:
        """
        Check whether agent is in home
        """
        result = None
        if self.home is None:
            print('home index not defined')
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
    @property
    def current_node(self):
        """
        Return current node id based on current pos
        """
        result = None
        infrastructure = self.model.infrastructure
        items = infrastructure.all_nodes()
        node_index, distance = infrastructure.find_nearest_node(self.pos, items)
        if distance <= self.model.proximity_radius:
            result = node_index
        return result

    def update(self) -> None:
        """
        Update agent
        """
        if self.alive is True:
            duration_object = self.model.step_size
            duration = duration_object.total_seconds()
            """ Income """
            self.balance += self.income * duration
            """ Consume resources """
            fuels = self.fuels_rate_idle * duration
            self.resources - fuels
            self.queue.update()
            """ How long it has been out of home? """
            if self.is_home():
                self.time_outside = DeltaTime(seconds=0)
            else:
                self.time_outside += duration_object

        """ Decide """
        if self.alive is True:
            #self.brain.observe(self)
            #actions = self.brain.decide()
            actions = []
            self.queue.add(actions)

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'home': self.home,
            'time_outside': self.time_outside.total_seconds(),
            'transportation': self.transportation.serialize(),
            'pos': self.pos,
            'queue': self.queue.serialize(),
            'resources': self.resources.serialize(),
            'fuels_rate_idle': self.fuels_rate_idle.serialize(),
            'balance': self.balance,
            'type': self.type
        }

    def deserialize(self, dictionary: dict) -> None:
        self.name = dictionary['name']
        self.alive = dictionary['alive']
        self.death_reason = dictionary['death_reason']
        self.home = dictionary['home']
        self.time_outside = DeltaTime(seconds=dictionary['time_outside'])
        self.transportation = Transportation()
        self.transportation.deserialize(dictionary['transportation'])
        self.pos = dictionary['pos']
        self.queue = ActionQueue()
        self.queue.deserialize(dictionary['queue'])
        self.resources = Containers()
        self.resources.deserialize(dictionary['resource'])
        self.fuels_rate_idle = Matters()
        self.fuels_rate_idle.deserialize(dictionary['fuels_rate_idle'])
        self.balance = dictionary['balance']
        self.income = dictionary['income']
        self.type = dictionary['type']


if __name__ == '__main__':

    from piperabm.matter.containers.samples import containers_0 as resources

    agent = Agent(
        name='Sample',
        resources=resources
    )
    agent.print
