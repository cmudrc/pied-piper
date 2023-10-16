from copy import deepcopy

from piperabm.unit import DT
from piperabm.resources import Resource
from piperabm.resources import resource_sum

try: from .graphics import Graphics
except: from graphics import Graphics


class Accessibility(Graphics):

    def __init__(self):
        self.total_current_resource_list = []
        self.total_max_resource_list = []
        self.duration_list = []
        self.name = 'accessibility'
        super().__init__()

    def read_data(self, society, start_date, end_date):
        """
        Read all the required parameters from society
        """
        agents = society.all_agents()
        total_current_resource = society.all_resource_from(agents)
        total_max_resource = society.all_max_resource_from(agents)
        duration = end_date - start_date
        #print(total_current_resource, total_max_resource, duration)
        self.add(total_current_resource, total_max_resource, duration)

    def add(self, total_current_resource, total_max_resource, duration):
        """
        Args:
            current_resources: sum of all agents current_resource
            max_resources: sum of all agents max_resource
        """
        total_current_resource = deepcopy(total_current_resource)
        total_max_resource = deepcopy(total_max_resource)
        duration = deepcopy(duration)
        if isinstance(total_current_resource, dict):
            total_current_resource = Resource(total_current_resource)
        if isinstance(total_max_resource, dict):
            total_max_resource = Resource(total_max_resource)
        self.total_max_resource_list.append(total_max_resource)
        self.total_current_resource_list.append(total_current_resource)
        if isinstance(duration, DT):
            duration = duration.total_seconds()
        self.duration_list.append(duration)

    def accessibility_ideal(self) -> list:
        ideals = []
        for i, _ in enumerate(self.duration_list):
            val = self.total_max_resource_list[i] * self.duration_list[i]
            ideals.append(val)
        return ideals

    def accessibility_real(self) -> list:
        reals = []
        for i, _ in enumerate(self.duration_list):
            val = self.total_current_resource_list[i] * self.duration_list[i]
            reals.append(val)
        return reals
    
    def efficiency(self, resource_name='all'):
        """
        Calculate efficiency for a certain resource or all
        """
        result = None
        reals = self.accessibility_real()
        result_real = resource_sum(reals)
        ideals = self.accessibility_ideal()
        result_ideal = resource_sum(ideals)
        efficiency = result_real / result_ideal
        if resource_name == 'all':
            result = self.overall_efficiency(efficiency)
        else:
            result = efficiency(resource_name)
        return result
    
    def overall_efficiency(self, efficiency):
        """
        Calculate overall efficiency
        """
        overall = 1
        for key in efficiency.current_resource:
            overall *= efficiency(key)
        return overall ** (1 / len(efficiency.current_resource))
    

if __name__ == "__main__":
    accessibility = Accessibility()
    total_1 = Resource(
        {
            'food': 2,
            'water': 3,
            'energy': 4
        },
        max_resource={
            'food': 10,
            'water': 10,
            'energy': 10
        }
    )
    accessibility.add(
        total_current_resource=total_1.current_resource,
        total_max_resource=total_1.max_resource,
        duration=1
    )
    total_2 = Resource(
        {
            'food': 5,
            'water': 6,
            'energy': 7
        },
        max_resource={
            'food': 10,
            'water': 10,
            'energy': 10
        }
    )
    accessibility.add(
        total_current_resource=total_2.current_resource,
        total_max_resource=total_2.max_resource,
        duration=1
    )
    total_3 = Resource(
        {
            'food': 8,
            'water': 9,
            'energy': 10
        },
        max_resource={
            'food': 10,
            'water': 10,
            'energy': 10
        }
    )
    accessibility.add(
        total_current_resource=total_3.current_resource,
        total_max_resource=total_3.max_resource,
        duration=1
    )
    eff = accessibility.efficiency()
    print(eff)
    #accessibility.show()

