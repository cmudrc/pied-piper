import matplotlib.pyplot as plt

from piperabm.unit import DT
from piperabm.resource import DeltaResource


class Accessibility:
    def __init__(self):
        self.current_resources_list = []
        self.max_resources_list = []
        self.durations_list = []

    def add(self, current_resources, max_resources, duration):
        """
        
        Args:
            current_resources: sum of all agents current_resource
            max_resources: sum of all agents max_resource
        """
        self.max_resources_list.append(max_resources)
        self.current_resources_list.append(current_resources)
        if isinstance(duration, DT):
            duration = duration.total_seconds()
        self.durations_list.append(duration)

    def accessibility_ideal(self):
        ideals = []
        for i, _ in enumerate(self.durations_list):
            val = self.max_resources_list[i] * self.durations_list[i]
            ideals.append(val)
        return ideals

    def accessibility_current(self):
        currents = []
        for i, _ in enumerate(self.durations_list):
            val = self.current_resources_list[i] * self.durations_list[i]
            currents.append(val)
        return currents
    
    def calculate(self):
        currents = self.accessibility_current()
        current = DeltaResource(
            {
                'food': 0,
                'water': 0,
                'energy': 0
            }
        )
        for currents in self.current_resources_list:
            current += currents
        ideals = self.accessibility_ideal()
        ideal = DeltaResource(
            {
                'food': 0,
                'water': 0,
                'energy': 0
            }
        )
        for ideals in self.max_resources_list:
            ideal += ideals
        return current / ideal

    def to_plt(self, resource_name):
        """
        Plot the accessibility over time
        """
        def create_x():
            result = []
            for i, _ in enumerate(self.durations_list):
                val = sum(self.durations_list[1:i+1])
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
            for i, _ in enumerate(self.durations_list):
                for name in result_current:
                    current = self.current_resources_list[i].batch[name]
                    result_current[name].append(current)
                    ideal = self.max_resources_list[i].batch[name]
                    result_ideal[name].append(ideal)
            return result_current, result_ideal

        title = resource_name + ' ' + "accessibility over time"
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

    def show(self, resource_name):
        """
        Show the plt plot
        """
        self.to_plt(resource_name)
        plt.show()
