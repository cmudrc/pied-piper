from copy import deepcopy

from piperabm.object import Object
from piperabm.resource import Resource, ResourceDelta
from piperabm.transporation import Transportation
from piperabm.actions import Queue
from piperabm.unit import DT, Date, date_to_dict, date_from_dict
from piperabm.society.agent.config import *
from piperabm.tools import ElementExists


class Agent(Object):

    def __init__(
        self,
        name: str = '',
        active: bool = True,
        start_date: Date = None,
        end_date: Date = None,
        origin: int = None,
        transportation: Transportation = None,
        queue=None,
        resource: Resource = None,
        fuel_rate_idle: ResourceDelta = None,
        income: float = 0,
        balance: float = 0
    ):
        super().__init__()

        ''' identity '''
        self.name = name
        self.active = active
        self.death_reason = None
        self.origin = origin
        self.type = 'agent'

        ''' dates '''
        if start_date is None:
            start_date = Date.today()
        self.start_date = start_date
        self.end_date = end_date

        ''' transporation '''
        if transportation is None:
            self.transportation = Walk()
        else:
            self.transportation = transportation

        ''' queue '''
        if queue is None:
            self.queue = Queue()
        else:
            self.queue = queue

        ''' resource '''
        if resource is None:
            self.resource = deepcopy(DEFAULT_RESOURCE)
        else:
            self.resource = resource

        if fuel_rate_idle is None:
            self.fuel_rate_idle = deepcopy(HUMAN_IDLE_FUEL_RATE)
        else:
            self.fuel_rate_idle = fuel_rate_idle

        ''' wealth '''
        if income >= 0:
            self.income = income
        if balance >= 0:
            self.balance = balance

        ''' binding to the world '''
        self.environment = None
        self.society = None

    @property
    def alive(self) -> bool:
        return self.active

    def is_alive(self) -> bool:
        """
        Check whether agent is alive
        """
        result = None
        if self.alive is True:
            result = True
            resource_zeros = self.resource.find_zeros(VITAL_RESOURCES)
            if len(resource_zeros) > 0:  # died
                result = False
                self.death_reason = resource_zeros
                self.end_date = None  # deepcopy(self.current.start_date)
        else:
            result = False
        return result

    def update(self, start_date, end_date) -> None:
        """
        Reduce the idle_fuel_consumption from agent's resource
        """
        duration = end_date - start_date
        if self.alive is True:
            ''' income '''
            self.balance += self.income * duration
            ''' idle fuel consumption '''
            fuel_consumption = self.fuel_consumption_idle(duration)
            self.resource - fuel_consumption

        if self.alive is True:
            ''' decide '''
            pass

    def fuel_consumption_idle(self, duration) -> ResourceDelta:
        """
        Create ResourceDelta object based on duration and fuel_rate
        """
        if isinstance(duration, DT):
            duration = duration.total_seconds()
        rate = deepcopy(self.fuel_rate_idle)
        rate * duration
        return rate

    def exists(self, start_date: Date, end_date: Date):
        """
        Check whether element exists in the time range
        """
        ee = ElementExists()
        return ee.check(
            item_start=self.start_date,
            item_end=self.end_date,
            time_start=start_date,
            time_end=end_date
        )

    def __add__(self, other):
        if isinstance(other, ResourceDelta):  # resource arithmetic
            remaining = self.resource + other
            self.active = self.is_alive()
            return remaining
        else:
            super().__add__(other)  # delta arithmetic

    def __sub__(self, other):
        if isinstance(other, ResourceDelta):  # resource arithmetic
            remaining = self.resource - other
            self.active = self.is_alive()
            return remaining
        else:
            super().__sub__(other)  # delta arithmetic

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'active': self.active,
            'start_date': date_to_dict(self.start_date),
            'end_date': date_to_dict(self.end_date),
            'death_reason': self.death_reason,
            'origin': self.origin,
            'transportation': self.transportation.to_dict(),
            'queue': self.queue.to_dict(),
            'resource': self.resource.to_dict(),
            'fuel_rate_idle': self.fuel_rate_idle.to_dict(),
            'income': self.income,
            'balance': self.balance,
            'type': self.type
        }

    def from_dict(self, dictionary: dict) -> None:
        self.name = dictionary['name']
        self.active = dictionary['active']
        self.start_date = date_from_dict(dictionary['start_date'])
        self.end_date = date_from_dict(dictionary['end_date'])
        self.death_reason = dictionary['death_reason']
        self.origin = dictionary['origin']
        transportation = Transportation()
        transportation.from_dict(dictionary['transportation'])
        self.transportation = transportation
        queue = Queue()
        queue.from_dict(dictionary['queue'])
        self.queue = queue
        resource = Resource()
        resource.from_dict(dictionary['resource'])
        self.resource = resource
        fuel_rate_idle = ResourceDelta()
        fuel_rate_idle.from_dict(dictionary['fuel_rate_idle'])
        self.fuel_rate_idle = fuel_rate_idle
        self.income = dictionary['income']
        self.balance = dictionary['balance']
        self.type = dictionary['type']


if __name__ == "__main__":
    from piperabm.resource.samples import resource_0

    agent = Agent(
        name='John',
        resource=resource_0
    )
    print(agent)
