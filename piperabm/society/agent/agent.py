from copy import deepcopy

from piperabm.object import Object
from piperabm.resource import Resource
from piperabm.transporation import Walk
from piperabm.transporation.load import load_transportation
from piperabm.actions import Queue
from piperabm.unit import DT, Date, date_to_dict, date_from_dict
#try: from .decision import Decision
#except: from decision import Decision
from piperabm.society.agent.config import *


class Agent(Object):

    def __init__(
            self,
            name: str = '',
            active: bool = True,
            start_date: Date = None,
            end_date: Date = None,
            origin: int = None,
            transportation=None,
            queue=None,
            resource: Resource = None,
            fuel_rate_idle: Resource = None,
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
        if queue is None or not isinstance(queue, Queue):
            self.queue = Queue()
        else:
            self.queue = queue

        ''' resource '''
        if resource is None or not isinstance(resource, Resource):
            self.resource = deepcopy(DEFAULT_RESOURCE)
        else:
            self.resource = resource
    
        if fuel_rate_idle is None or not isinstance(fuel_rate_idle, Resource):
            self.fuel_rate_idle = deepcopy(HUMAN_IDLE_FUEL_RATE)
        else:
            self.fuel_rate_idle = fuel_rate_idle

        ''' wealth '''
        if income >= 0:
            self.income = income
        if balance >= 0:
            self.balance = balance

    @property
    def alive(self) -> bool:
        return self.active

    def is_alive(self) -> bool:
        """
        Check whether agent is alive
        """
        result = True
        resource_zeros = self.resource.find_zeros(VITAL_RESOURCES)
        if len(resource_zeros) > 0:
            result = False
            self.active = False
            self.death_reason = resource_zeros
        return result
    
    def reduce_resource(self, resource: Resource) -> None:
        """
        Reduce the *resource* from agent and check whether its alive
        """
        self.resource, remaining = self.resource - resource
        self.active = self.is_alive()

    def idle_time_pass(self, duration) -> None:
        """
        Reduce the idle_fuel_consumption from agent's resource
        """
        if isinstance(duration, DT):
            duration = duration.total_seconds()
        if self.alive is True:
            self.reduce_resource(self.fuel_rate_idle * duration)

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'active': self.active,
            'start_date': date_to_dict(self.start_date),
            'end_date': date_to_dict(self.end_date),
            'death_reason': self.death_reason,
            'origin': self.origin,
            'transportation': self.transportation.to_dict(),
            'queue': self.queue.to_dict(), #
            #'resource': self.resource.to_dict(), #
            #'fuel_rate_idle': self.fuel_rate_idle.to_dict(), #
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
        self.transportation = load_transportation(dictionary['transportation'])
        queue = Queue()
        queue.from_dict(dictionary['queue']) ##
        self.queue = queue
        #resource = Resource()
        #resource.from_dict(dictionary['resource']) ##
        #self.resource = resource
        #self.fuel_rate_idle = dictionary['fuel_rate_idle']
        self.income = dictionary['income']
        self.balance = dictionary['balance']
        self.type = dictionary['type']


if __name__ == "__main__":
    resource = Resource(
        current_resource={
            'food': 20,
            'water': 30,
            'energy': 40
        },
        max_resource={
            'food': 100,
            'water': 100,
            'energy': 100
        }
    )
    agent = Agent(
        name='John',
        resource=resource
    )
    print(agent)
    agent.idle_time_pass(3600 * 24 * 8)
    print(agent.resource)
    print('alive: ', agent.alive)
    print('reason of death: ', agent.death_reason)