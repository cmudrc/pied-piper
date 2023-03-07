import matplotlib.pyplot as plt

from piperabm.unit import DT
from piperabm.resource import DeltaResource


class Accessibility:

    def __init__(self):
        self.total_current_resource_list = []
        self.total_max_resource_list = []
        self.duration_list = []

    def read(self, society, start_date, end_date):
        """
        Read all the required parameters from society
        """
        agents = society.all_agents()
        total_current_resource = society.all_resource_from(agents)
        total_max_resource = society.all_max_resource_from(agents)
        duration = end_date - start_date
        self.add(total_current_resource, total_max_resource, duration)

    def add(self, total_current_resource, total_max_resource, duration):
        """
        
        Args:
            current_resources: sum of all agents current_resource
            max_resources: sum of all agents max_resource
        """
        if isinstance(total_current_resource, dict):
            total_current_resource = DeltaResource(total_current_resource)
        self.total_max_resource_list.append(total_max_resource)
        self.total_current_resource_list.append(total_current_resource)
        if isinstance(duration, DT):
            duration = duration.total_seconds()
        self.duration_list.append(duration)

    def accessibility_ideal(self):
        ideals = []
        for i, _ in enumerate(self.duration_list):
            val = self.total_max_resource_list[i] * self.duration_list[i]
            ideals.append(val)
        return ideals

    def accessibility_current(self):
        currents = []
        for i, _ in enumerate(self.duration_list):
            val = self.total_current_resource_list[i] * self.duration_list[i]
            currents.append(val)
        return currents
    
    def efficiency(self):
        currents = self.accessibility_current()
        result_real = DeltaResource(
            {
                'food': 0,
                'water': 0,
                'energy': 0
            }
        )
        for current in self.total_current_resource_list:
            result_real, _ = result_real + current
        ideals = self.accessibility_ideal()
        result_ideal = DeltaResource(
            {
                'food': 0,
                'water': 0,
                'energy': 0
            }
        )
        for ideals in self.total_max_resource_list:
            result_ideal, _ = result_ideal + ideals
        return result_real / result_ideal
    
    def overall_efficiency(self):
        efficiency = self.efficiency()
        overall = 1
        for key in efficiency:
            overall *= efficiency[key]
        return overall ** (1 / len(efficiency))

    def to_plt(self, resource_name):
        """
        Plot the accessibility over time
        """
        def create_x():
            result = []
            for i, _ in enumerate(self.duration_list):
                val = sum(self.duration_list[1:i+1])
                result.append(val)
            return result

        def create_y():
            result_current = {
                'food': [],
                'water': [],
                'energy': [],
            }
            result_ideal = {
                'food': [],
                'water': [],
                'energy': [],
            }
            for i, _ in enumerate(self.duration_list):
                for name in result_current:
                    current = self.total_current_resource_list[i].batch[name]
                    result_current[name].append(current)
                    ideal = self.total_max_resource_list[i].batch[name]
                    result_ideal[name].append(ideal)
            return result_current, result_ideal

        title = resource_name + ' ' + "accessibility vs. time"
        plt.title(title)
        plt.xlabel('Time')
        plt.ylabel('Accessibity')
        x = create_x()
        y_current, y_ideal = create_y()
        plt.plot(x, y_current[resource_name], color='r', label='real')
        plt.plot(x, y_ideal[resource_name], color='b', label='ideal')
        #plt.xlim([25, 50])
        plt.ylim(bottom=0)
        plt.legend()

    def show(self, resource_name='food'):
        """
        Show the plt plot
        """
        self.to_plt(resource_name)
        plt.show()
