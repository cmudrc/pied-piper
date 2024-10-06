class Interaction:
    """
    Manage interactions graph
    """

    type = 'interaction'

    def __init__(self, measurement):
        self.measurement = measurement
        self.values = {}

    def add(self, id_from: int, id_to: int, resource_name: str, resource_amount: float) -> None:
        """
        Add new accessibility value
        """
        if not id_from in self.values:
            self.values[id_from] = {}
        if not id_to in self.values[id_from]:
            self.values[id_from][id_to] = {}
        if not resource_name in self.values[id_from][id_to]:
            self.values[id_from][id_to][resource_name] = []
        self.values[id_from][id_to][resource_name].append(resource_amount)

    def serialize(self) -> dict:
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