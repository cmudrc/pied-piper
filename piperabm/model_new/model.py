from piperabm.object import PureObject
from piperabm.model_new.graphics import Graphics
from piperabm.infrastructure_new import Infrastructure
from piperabm.society_new import Society
from piperabm.time import DeltaTime, Date, date_serialize, date_deserialize
from piperabm.tools import Delta
from piperabm.tools.file_manager import JsonFile


class Model(PureObject, Graphics):

    type = "model"

    def __init__(
        self,
        step_size = DeltaTime(hours=1),
        date: Date = Date(year=2000, month=1, day=1),
        infrastructure: Infrastructure = None,
        society: Society = None,
        thawing: float = 0.01 # thawing rate
    ):
        super().__init__()
        self.set_step_size(step_size)
        self.date = date
        if infrastructure is None:
            infrastructure = Infrastructure()
        self.infrastructure = infrastructure
        self.infrastructure.model = self # Binding
        if society is None:
            society = Society()
        self.society = society
        self.society.model = self # Binding
        self.thawing = thawing
        self.path = None # File saving
        self.paths = None # Paths graph

    def set_step_size(self, step_size):
        """
        Set step size
        """
        if isinstance(step_size, (float, int)):
            self.step_size = DeltaTime(seconds=step_size)
        elif isinstance(step_size, DeltaTime):
            self.step_size = step_size
        else:
            print("object not recognized")
            raise ValueError
        
    def add(self, object):
        if object.section == "infrastructure":
            self.infrastructure.add(object=object, id=id)
        elif object.section == "society":
            self.society.add(object=object, id=id)
        else:
            print("object not recognized")
            raise ValueError

    def run(self, n: int = None, save=False, report=True):
        """
        Update model for multiple steps in time
        """
        # Run until all agents die
        if n is None:
            while True:
                self.update(save=save)
                if len(self.society.alive_agents) == 0:
                    break
        # Run for a certain steps
        else:
            for i in range(n):
                if report is True and n is not None:
                    print(f"Progress: {i / n * 100:.1f}% complete")
                self.update(save=save)
        #self.save_final()

    def update(self, save=False):
        """
        Update model for single step in time
        """
        duration = self.step_size
        self.paths = self.infrastructure.paths()

        # Delta handling
        if save is True:
            old = self.serialize()

        # Agents
        agents = self.society.agents
        for id in agents:
            agent = self.society.get(id)
            agent.update(duration)

        # Thawing
        thawing_rate = self.thawing
        edges_id = self.infrastructure.edges_id
        for id in edges_id:
            object = self.infrastructure.get(id)
            object.degradation += thawing_rate * duration.total_seconds()

        self.date += duration

        # Delta handling
        if save is True:
            current = self.serialize()
            delta = Delta.create(old, current)
            self.append_delta(delta)

    def append_delta(self, delta):
        """
        Create and append new delta to file
        """
        filename = "simulation"
        deltas_file = JsonFile(self.path, filename)
        if deltas_file.exists() is False:
            deltas = []
            deltas_file.save(deltas)
        deltas_file.append(delta)

    def load_deltas(self, name: str = 'simulation', _from=None, _to=None):
        deltas_file = JsonFile(self.path, filename=name)
        deltas = deltas_file.load()
        if _from is None:
            _from = 0
        if _to is None:
            _to = len(deltas) # Apply all
        return deltas[_from:_to]

    def apply_delta(self, delta):
        dictionary = self.serialize()
        dictionary_new = Delta.apply(dictionary, delta)
        self.deserialize(dictionary_new)

    def apply_deltas(self, name: str = 'simulation', _from=None, _to=None):
        """
        Load deltas from file and apply the deltas between _from to _to
        """
        deltas = self.load_deltas(name, _from, _to)
        for delta in deltas:
            self.apply_delta(delta)

    def save(self, name: str = 'model'):
        """
        Load model to file
        """
        data = self.serialize()
        file = JsonFile(self.path, filename=name)
        file.save(data)

    def load(self, name: str = 'model'):
        """
        Load model from file
        """
        file = JsonFile(self.path, filename=name)
        data = file.load()
        self.deserialize(data)

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['step_size'] = self.step_size.total_seconds()
        dictionary['date'] = date_serialize(self.date)
        dictionary['infrastructure'] = self.infrastructure.serialize()
        dictionary['society'] = self.society.serialize()
        dictionary['thawing'] = self.thawing
        dictionary['type'] = self.type
        return dictionary
        
    def deserialize(self, dictionary: dict) -> None:
        self.step_size = DeltaTime(seconds=dictionary['step_size'])
        self.date = date_deserialize(dictionary['date'])
        infrastructure = Infrastructure()
        infrastructure.deserialize(dictionary['infrastructure'])
        infrastructure.model = self
        self.infrastructure = infrastructure
        society = Society()
        society.deserialize(dictionary['society'])
        society.model = self
        self.society = society
        self.thawing = dictionary['thawing']
        

if __name__ == "__main__":
    model = Model()
    print(model)
