from copy import deepcopy

from piperabm.actions import Queue
from piperabm.resource import Resource
from piperabm.actions.action.transportation import Walk
from piperabm.unit import Unit
from piperabm.economy import GiniGenerator


class Add:
    """
    Contains methods for Society class
    Add new elements to the society
    """

    def add(
        self,
        name: str = '',
        settlement=None,
        transportation=None,
        queue=None,
        resource=None,
        idle_fuel_rate=None,
        wealth=0,
        wealth_factor=1
    ):
        """
        Add a new agent to the society
        """
        index = self.find_next_index()
        self.index_list.append(index)
        if resource is None:
            resource = Resource(
                current_resource={
                    'food': 0,
                    'water': 0,
                    'energy': 0
                },
                max_resource={
                    'food': None,
                    'water': None,
                    'energy': None
                }
            )
        if idle_fuel_rate is None: idle_fuel_rate = human_idle_fuel_rate
        if settlement is None: settlement_index = self.env.random_settlement()
        else: settlement_index = self.env.find_node(settlement)
        if transportation is None: transportation = Walk()
        if queue is None: queue = Queue()
        settlement_node = self.env.G.nodes[settlement_index]
        pos = settlement_node['boundary'].center
        
        self.G.add_node(
            index,
            name=name,
            settlement=settlement_index,
            current_settlement=deepcopy(settlement_index),
            pos=pos,
            active=True,
            transportation=transportation,
            queue=queue,
            resource=resource,
            idle_fuel_rate=idle_fuel_rate,
            wealth_factor=wealth_factor,
            wealth=wealth,
            ready_for_trade=False
        )

    def add_agents(self, n, average_resource):
        for _ in range(n):
            name = name_generator()
            settlement = None  # default
            idle_fuel_rate = None  # default
            queue = None # default
            wealth_factor = calculate_wealth_factor(self.gini)
            wealth = wealth_generator(wealth_factor, self.average_income)
            resource = resource_generator(wealth_factor, average_resource)
            self.add(
                name=name,
                settlement=settlement,
                queue=queue,
                resource=resource,
                idle_fuel_rate=idle_fuel_rate,
                wealth=wealth,
                wealth_factor=wealth_factor
            )

human_idle_fuel_rate = Resource(
    {
        'food': Unit(2, 'kg/day').to_SI(),
        'water': Unit(4, 'kg/day').to_SI(),
        'energy': 0
    }
)

def name_generator():
    result = ''
    return result

def calculate_wealth_factor(gini):
    gg = GiniGenerator(gini, 1)
    sample = gg.generate()
    return sample[0]

def wealth_generator(wealth_factor, average_income):
    return wealth_factor * average_income

def resource_generator(wealth_factor, average_resource):
    return average_resource * wealth_factor


if __name__ == "__main__":
    average_resource = Resource(
        current_resource={
            'food': 20,
            'water': 40,
            'energy': 60,
        },
        max_resource={
            'food': 100,
            'water': 200,
            'energy': 300,
        }
    )
    result = resource_generator(2, average_resource)
    #result = average_resource * 2
    print(result)
