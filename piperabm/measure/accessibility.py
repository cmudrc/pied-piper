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
            current_resources: sum of all current_resource
            max_resources: sum of all max_resource
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
    
    def efficiency(self):
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

    def show(self):
        keys = ['food', 'water', 'energy']
        x = []
        y = []
        plt.plot(x,y)
        plt.xlabel('Accessibity')
        plt.ylabel('Time')
        plt.title("Accessibility over Time")
        plt.show()
