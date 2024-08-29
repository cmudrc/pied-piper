import os
import matplotlib.pyplot as plt
from copy import deepcopy

from piperabm.tools.average import average as avg


class Accessibility:
    """
    Manage accessibility measurement
    """

    type = 'accessibility'

    def __init__(self, measurement):
        self.measurement = measurement
        self.values = {}
        self.resource_names = ['food', 'water', 'energy']

    def add(self, id: int, value: float) -> None:
        """
        Add new accessibility value
        """
        if not id in self.values:
            self.values[id] = []
        self.values[id].append(value)

    def get(self, agent: int, resource: str, time_step: int):
        """
        Get the desired entry
        """
        return self.values[agent][time_step][resource]

    @property
    def agents(self):
        """
        Return a list of agents id
        """
        return list(self.values.keys())
    
    def rearrange(self, agents='all', resources='all', _from=None, _to=None):
        """
        Return accessibility values for all resources for across agents
        """
        if agents == 'all':
            ids = self.agents
        elif isinstance(agents, list):
            ids = agents
        elif isinstance(agents, int):
            ids = [agents]
        elif agents is None:
            ids = self.agents
        else:
            raise ValueError
        
        if resources == 'all':
            resource_names = self.resource_names
        elif isinstance(resources, list):
            resource_names = resources
        elif isinstance(resources, str) and \
        resources != 'all':
            resource_names = [resources]
        elif resources is None:
            resource_names = self.resource_names
        else:
            raise ValueError
        
        if _from is None:
            _from = 0

        if _to is None:
            _to = self.len
        
        result = {}
        for agent_id in ids:
            result[agent_id] = {}
            for resource_name in resource_names:
                values = []
                for i in range(_from, _to):
                    value = self.get(
                            agent=agent_id,
                            resource=resource_name,
                            time_step=i
                        )
                    values.append(value)
                result[agent_id][resource_name] = values

        return result
    
    @property
    def len(self) -> int:
        """
        Return total number of entries
        """
        return self.measurement.len

    def sum_resources(self, agents='all', resources='all', _from=None, _to=None) -> dict:
        """
        Sum resources
        """
        data = self.rearrange(agents=agents, resources=resources, _from=_from, _to=_to)
        if _from is None:
            _from = 0
        if _to is None:
            _to = self.len
        length = _to - _from
        result = {}
        for agent_id in data:
            result[agent_id] = []
            agent_data = data[agent_id]
            for i in range(length):
                vals = []
                for resource_name in agent_data:
                    acc_vals = agent_data[resource_name]
                    vals.append(acc_vals[i])
                result[agent_id].append(avg.geometric(values=vals))
        return result
    
    def sum_agents(self, agents='all', resources='all', _from=None, _to=None) -> list:
        """
        Sum agents
        """
        data = self.sum_resources(agents=agents, resources=resources, _from=_from, _to=_to)
        if _from is None:
            _from = 0
        if _to is None:
            _to = self.len
        length = _to - _from
        result = []
        for i in range(length):
            vals = []
            for agent_id in data:
                agent_data = data[agent_id]
                vals.append(agent_data[i])
            result.append(avg.arithmetic(values=vals))
        return result
    
    def __call__(self, agents='all', resources='all', _from=None, _to=None) -> list:
        return self.sum_agents(agents=agents, resources=resources, _from=_from, _to=_to)
    
    def average(self, agents='all', resources='all', _from=None, _to=None) -> float:
        """
        Calculate total average
        """
        values = self.__call__(agents=agents, resources=resources, _from=_from, _to=_to)
        weights = self.measurement.delta_times(_from=_from, _to=_to)
        result = avg.arithmetic(values=values, weights=weights)
        if isinstance(result, complex):
            result = float(result.real)
        return result
    
    def create_plot(self, agents='all', resources='all', _from=None, _to=None, info=None):
        """
        Create plot
        """
        fig, ax = plt.subplots()
        title = "Accessibility"
        ylabel = deepcopy(title)
        if info is not None:
            title += info
        ax.set_title(title)
        xs = self.measurement.filter_times(_from=_from, _to=_to)
        yx = self.__call__(agents=agents, resources=resources, _from=_from, _to=_to)
        ax.plot(xs, yx, color='blue')
        ax.set_xlabel("Time")
        ax.set_ylabel(ylabel)
        return fig

    def show(self, agents='all', resources='all', _from=None, _to=None, info=None):
        """
        Draw plot
        """
        fig = self.create_plot(
            agents=agents,
            resources=resources,
            _from=_from,
            _to=_to,
            info=info
        )
        plt.show()

    def save(self, agents='all', resources='all', _from=None, _to=None, info=None):
        """
        Save plot
        """
        fig = self.create_plot(
            agents=agents,
            resources=resources,
            _from=_from,
            _to=_to,
            info=info
        )
        path = self.measurement.result_directory
        filepath = os.path.join(path, self.type)
        fig.savefig(filepath)

    def serialize(self) -> dict:
        """
        Serialize
        """
        return {
            'values': self.values,
            'type': self.type
        }
    
    def deserialize(self, data: dict) -> None:
        """
        Deserialize
        """
        self.values = data['values']

    
if __name__ == "__main__":
    
    from piperabm.model.measurement import Measurement

    measure = Measurement()
    hour = 3600
    measure.add_time(0 * hour) # Base

    # 1
    measure.add_time(value=1*hour)
    measure.accessibility.add(id=1, value={'food': 1, 'water': 1, 'energy': 1})
    measure.accessibility.add(id=2, value={'food': 0.8, 'water': 0.7, 'energy': 0.6})
    # 2
    measure.add_time(value=2*hour)
    measure.accessibility.add(id=1, value={'food': 0.9, 'water': 0.8, 'energy': 0.7})
    measure.accessibility.add(id=2, value={'food': 0.5, 'water': 0.6, 'energy': 0.4})
    # 3
    measure.add_time(value=3*hour)
    measure.accessibility.add(id=1, value={'food': 0.8, 'water': 0.7, 'energy': 0.6})
    measure.accessibility.add(id=2, value={'food': 0.2, 'water': 0.4, 'energy': 0.3})
    # 4
    measure.add_time(value=4*hour)
    measure.accessibility.add(id=1, value={'food': 0.7, 'water': 0.6, 'energy': 0.5})
    measure.accessibility.add(id=2, value={'food': 0, 'water': 0.3, 'energy': 0.2})
    # 5
    measure.add_time(value=5*hour)
    measure.accessibility.add(id=1, value={'food': 0.6, 'water': 0.5, 'energy': 0.4})
    measure.accessibility.add(id=2, value={'food': 0, 'water': 0.3, 'energy': 0.2})

    agents = 'all'
    resources = 'all'
    _from = None
    _to = None
    print("accessibilities: ", measure.accessibility(agents=agents, resources=resources, _from=_from, _to=_to))
    print("average: ", measure.accessibility.average(agents=agents, resources=resources, _from=_from, _to=_to))
    measure.accessibility.show(agents=agents, resources=resources, _from=_from, _to=_to)
