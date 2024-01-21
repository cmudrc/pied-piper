from copy import deepcopy

from piperabm.object import PureObject
from piperabm.matter import Containers, Matters
from piperabm.time import DeltaTime, Date
from piperabm.transportation import Transportation
from piperabm.actions.queue import Queue
from piperabm.time import date_serialize, date_deserialize
#from piperabm.agent.brain import Brain
from piperabm.tools.coordinate import distance as ds
from piperabm.society.agent.config import *


class Agent(PureObject):

    def __init__(
        self,
        index = None,
        name: str = '',
        home: int = None,
        transportation: Transportation = None,
        resources: Containers = None,
        fuels_rate_idle: Matters = None,
        balance: float = 0,
        income: float = 0,
        socioeconomic_status: float = 1,
    ):
        super().__init__()
        """ Binding to the model """
        self.model = None

        """ Decision making """
        #self.brain = Brain()
        self.brain = None

        """ Identity """
        self.index = index
        self.name = name
        self.alive = True
        self.death_reason = None
        self.home = home
        self.last_time_home = None
        self.socioeconomic_status = socioeconomic_status
        
        self.section = 'society'
        self.category = 'node'
        self.type = 'agent'

        """ Transporation """
        if transportation is None: transportation = WALK
        self.transportation = transportation
        self.pos = None

        """ Queue """
        self.queue = Queue()
        self.queue.agent = self  # Bilding

        """ Resources """
        if resources is None:
            resources = deepcopy(RESOURCES_DEFAULT)
        self.resources = resources

        if fuels_rate_idle is None:
            fuels_rate_idle = deepcopy(FUELS_RATE_HUMAN_IDLE)
        self.fuels_rate_idle = fuels_rate_idle

        if income < 0: raise ValueError
        self.income = income

        if balance < 0: raise ValueError
        self.balance = balance

    def check_alive(self) -> bool:
        """
        Check whether agent is alive
        """
        if self.alive is True:
            resources_zero = self.resources.check_empty(RESOURCES_VITAL)
            if len(resources_zero) > 0:  # died
                self.alive = False
                self.death_reason = resources_zero[0]  # one reason is enough
        return self.alive

    def is_home(self) -> bool:
        """
        Check whether agent is alive
        """
        result = None
        if self.home is None:
            print('home index not defined')
        else:
            home = self.model.get(self.home)
            distance = ds.point_to_point(home.pos, self.pos)
            if distance <= self.model.proximity_distance:
                result = True
            else:
                result = False
        return result
            
    '''
    @property
    def source(self):
        return self.resources.source
    
    @property
    def demand(self):
        return self.resources.demand
    '''
    def utility(self, resource_name):
        return self.resources(name=resource_name)

    def update(self, date_start: Date, date_end: Date) -> None:
        """
        Update agent
        """
        if self.alive is True:
            duration = date_end - date_start
            """ Income """
            self.balance += self.income * duration.total_seconds()
            """ Consume resources """
            other_rates = [] ###### from action in queue
            self.consume_resources(duration) # , other_rates
            self.queue.update(date_start, date_end)
            self.check_alive()

        """ decide """
        if self.alive is True:
            pass 
        #    self.brain.observe(self.index, self.environment, self.society)
        #    actions = self.brain.decide()
        #    self.queue.add(actions)

    def consume_resources(self, duration):
        """
        Create ResourceDelta object based on duration and fuel_rate(s)
        , other_rates: list = []
        """
        if isinstance(duration, DeltaTime):
            duration = duration.total_seconds()
        fuels = self.fuels_rate_idle * duration
        #for other_rate in other_rates:
        #    total_consumption.add(other_rate)
        remainder = self.resources - fuels
        return remainder

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'alive': self.alive,
            'death_reason': self.death_reason,
            'home': self.home,
            'last_time_home': date_serialize(self.last_time_home),
            'transportation': self.transportation.serialize(),
            'pos': self.pos,
            'queue': self.queue.serialize(),
            'resources': self.resources.serialize(),
            'fuels_rate_idle': self.fuels_rate_idle.serialize(),
            'balance': self.balance,
            'income': self.income,
            'type': self.type
        }

    def deserialize(self, dictionary: dict) -> None:
        self.name = dictionary['name']
        self.alive = dictionary['alive']
        self.death_reason = dictionary['death_reason']
        self.home = dictionary['home']
        self.last_time_home = date_deserialize(dictionary['last_time_home'])
        self.transportation = Transportation()
        self.transportation.deserialize(dictionary['transportation'])
        self.pos = dictionary['pos']
        self.queue = Queue()
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
