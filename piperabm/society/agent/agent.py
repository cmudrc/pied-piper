from copy import deepcopy

from piperabm.resource import Resource
from piperabm.actions.action.transportation import Walk
from piperabm.actions import Queue
from piperabm.unit import Unit, DT


class Agent:

    def __init__(
            self,
            index: int = None,
            name: str = '',
            origin_node=None,
            transportation=None,
            queue=None,
            resource: Resource = None,
            idle_fuel_rate: Resource = None,
            balance: float = 0,
            wealth_factor: float = 1
    ):
        ''' identity '''
        self.index = index
        self.name = name
        self.alive = True
        ''' location '''
        self.origin_node = origin_node
        self.current_node = deepcopy(origin_node)
        ''' transporation '''
        if transportation is None:
            self.transportation = Walk()
        else:
            self.transporation = transportation
        ''' queue '''
        if queue is None or not isinstance(queue, Queue):
            self.queue = Queue()
        else:
            self.queue = queue
        ''' assset '''
        if idle_fuel_rate is None or not isinstance(idle_fuel_rate, Resource):
            self.idle_fuel_rate = deepcopy(human_idle_fuel_rate)
        else:
            self.idle_fuel_rate = idle_fuel_rate
        if resource is None or not isinstance(resource, Resource):
            self.resource = deepcopy(default_resource)
        else:
            self.resource = resource
        if balance >= 0:
            self.balance = balance
        if wealth_factor >= 0:
            self.wealth_factor = wealth_factor
        

    def is_alive(self) -> bool:
        """
        Check whether agent is alive
        """
        result = True
        #if self.resource.has_zero(['food', 'water']):
        if self.resource.has_zero(['food', 'water']):
            result = False
        return result
    
    def reduce_resource(self, resource: Resource) -> None:
        """
        Reduce the *resource* from agent and check whether its alive
        """
        self.resource, remaining = self.resource - resource
        self.alive = self.is_alive()

    def idle_time_pass(self, duration) -> None:
        """
        Reduce the idle_fuel_consumption from agent's resource
        """
        if isinstance(duration, DT):
            duration = duration.total_seconds()
        self.reduce_resource(self.idle_fuel_rate * duration)
        
    def __str__(self) -> str:
        txt = 'agent' + ' ' + str(self.index)
        if self.name != '':
            txt += ' '
            txt += '(' + self.name + ')'
        return txt


human_idle_fuel_rate = Resource(
    {
        'food': Unit(2, 'kg/day').to_SI(),
        'water': Unit(4, 'kg/day').to_SI(),
        'energy': 0
    }
)

default_resource = Resource(['food', 'water', 'energy'])


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
        origin_node='1',
        transportation=None,
        queue=None,
        resource=resource,
        idle_fuel_rate=None,
        balance=0,
        wealth_factor=1
    )
    agent.idle_time_pass(3600 * 24 * 8)
    print(agent.resource)
    print(agent.is_alive())