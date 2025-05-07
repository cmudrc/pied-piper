import os
from copy import deepcopy

from piperabm.model import Model
from piperabm.model.measurement.accessibility import Accessibility
from piperabm.model.measurement.travel_distance import TravelDistance
#from piperabm.model.measurement.interaction import Interaction
from piperabm.tools.json_file import JsonFile
from piperabm.tools.coordinate import distance as ds


class Measurement:

    type = "measurement"

    def __init__(self, path=None, name: str = ''):
        self.path = path
        self.name = name
        self.times = []
        self.accessibility = Accessibility(measurement=self)
        self.travel_distance = TravelDistance(measurement=self)
        #self.interaction = Interaction(measurement=self)
        
    @property
    def result_directory(self):
        """
        Return result directory
        """
        if self.path is None:
            raise ValueError("define path to continue")
        result = os.path.join(self.path, 'result')
        if self.name != '':
            result = os.path.join(result, self.name)
        return result

    @property
    def len(self) -> int:
        """
        Return total number of entries
        """
        return len(self.times) - 1
    
    def add_time(self, value: float) -> None:
        """
        Add new point in time
        """
        self.times.append(deepcopy(value))

    def filter_times(self, _from: int = None, _to: int = None) -> list:
        """
        Filter times list
        """
        times = self.times[1:]
        if _from is None:
            _from = 0
        if _to is None:
            _to = len(times)
        return times[_from:_to]
    
    def delta_times(self, _from: int = None, _to: int = None) -> list:
        """
        Return delta times
        """
        times = self.times[1:]
        if _from is None:
            _from = 0
        if _to is None:
            _to = len(times)
        result = []
        for i in range(_from, _to):
            delta = self.times[i + 1] - self.times[i]
            result.append(delta)
        return result

    def add_accessibility(self, id: int, value: float) -> None:
        """
        Add new accessibility value
        """
        self.accessibility.add(id=id, value=value)
    
    def add_travel_distance(self, value: float) -> None:
        """
        Add new travel distance value
        """
        self.travel_distance.add(value=value)
    '''
    def add_interaction(self, id_from: int, id_to: int, resource_name: str, resource_amount: float) -> None:
        """
        Add new interaction value
        """
        self.interaction.add(id_from=id_from, id_to=id_to, resource_name=resource_name, resource_amount=resource_amount)
    '''
    def measure(self, report=True, resume=False):
        if resume is False:  # Restart the measurement
            file = JsonFile(path=self.path, filename='measurement')
            #if file.exists() is True:
            file.remove()  # Delete the previous measurement if exists
            model = Model(path=self.path, name=self.name)
            model.load_initial()  # Load initial state of model
            self.add_time(model.time)  # First date entry
        elif resume is True:  # Continue the measurement
            raise ValueError("Feature not tested yet.")
            '''
            file = JsonFile(path=self.path, filename=self.name+'_'+'measurement')
            if file.exists() is False:  # Restart the measurement if previous doesn't exist
                self.measure(report=report, resume=False)
            else:
                model = Model(path=self.path, name=self.name)
                model.load_final()  # Load final state of model
                self.load()  # Load final state of measurement
            '''

        deltas = model.load_deltas()
        previous = deepcopy(model)
        n = len(deltas)
        for i, delta in enumerate(deltas):
            model.apply_delta(delta) # Push model a single step forward
            self.add_time(model.time)
            total_travel = 0
            for id in model.society.agents:
                # Accessibility
                self.add_accessibility(
                    id=id,
                    value=model.society.accessibility(id=id)
                )
                # Travel distance
                previous_pos = previous.society.get_pos(id=id)
                current_pos = model.society.get_pos(id=id)
                travel = ds.point_to_point(
                    point_1=previous_pos,
                    point_2=current_pos
                )
                total_travel += travel
            self.add_travel_distance(value=total_travel)
            previous = deepcopy(model) # Push previous forward
            if report is True:
                print(f"Progress: {(i + 1) / n * 100:.1f}% complete")
        self.save()

    def save(self):
        """
        Save to file
        """
        data = self.serialize()
        file = JsonFile(path=self.result_directory, filename='measurement')
        file.save(data)
    
    def load(self):
        """
        Load to file
        """
        file = JsonFile(path=self.result_directory, filename='measurement')
        if file.exists() is False:
            raise ValueError("File not found:\n" + file.filepath)
        data = file.load()
        self.deserialize(data=data)

    def serialize(self) -> dict:
        """
        Serialize
        """
        return {
            'accessibility': self.accessibility.serialize(),
            'travel_distance': self.travel_distance.serialize(),
            'times': self.times,
            'type': self.type,
        }
    
    def deserialize(self, data: dict) -> None:
        """
        Deerialize
        """
        self.accessibility.deserialize(data['accessibility'])
        self.travel_distance.deserialize(data['travel_distance'])
        self.times = data['times']


if __name__ == "__main__":
    
    from piperabm.model.measurement import Measurement

    measure = Measurement()
    hour = 3600
    measure.add_time(0 * hour) # Base

    # 1
    measure.add_time(value=1*hour)
    measure.add_accessibility(id=1, value={'food': 1, 'water': 1, 'energy': 1})
    measure.add_accessibility(id=2, value={'food': 0.8, 'water': 0.7, 'energy': 0.6})
    measure.add_travel_distance(value=1.1)
    # 2
    measure.add_time(value=2*hour)
    measure.add_accessibility(id=1, value={'food': 0.9, 'water': 0.8, 'energy': 0.7})
    measure.add_accessibility(id=2, value={'food': 0.5, 'water': 0.6, 'energy': 0.4})
    measure.add_travel_distance(value=0.9)
    # 3
    measure.add_time(value=3*hour)
    measure.add_accessibility(id=1, value={'food': 0.8, 'water': 0.7, 'energy': 0.6})
    measure.add_accessibility(id=2, value={'food': 0.2, 'water': 0.4, 'energy': 0.3})
    measure.add_travel_distance(value=0.3)
    # 4
    measure.add_time(value=4*hour)
    measure.add_accessibility(id=1, value={'food': 0.7, 'water': 0.6, 'energy': 0.5})
    measure.add_accessibility(id=2, value={'food': 0, 'water': 0.3, 'energy': 0.2})
    measure.add_travel_distance(value=0.46)
    # 5
    measure.add_time(value=5*hour)
    measure.add_accessibility(id=1, value={'food': 0.6, 'water': 0.5, 'energy': 0.4})
    measure.add_accessibility(id=2, value={'food': 0, 'water': 0.3, 'energy': 0.2})
    measure.add_travel_distance(value=0.2)

    agents = 'all'
    resources = 'all'
    _from = None
    _to = None
    print("travel distances: ", measure.travel_distance(_from=_from, _to=_to))
    print("accessibilities: ", measure.accessibility(agents=agents, resources=resources, _from=_from, _to=_to))
    print("average: ", measure.accessibility.average(agents=agents, resources=resources))
    