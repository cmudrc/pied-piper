from piperabm.society.actions.action_queue import ActionQueue
from piperabm.tools.nx_serializer import nx_serialize, nx_deserialize


class Serialize:
    """
    Serialization methods
    """

    def serialize(self) -> dict:
        """
        Serialize
        """
        data = {}
        actions_serialized = {}
        for id in self.actions:
            action_queue = self.actions[id]
            actions_serialized[id] = action_queue.serialize()
        data["actions"] = actions_serialized
        data["G"] = nx_serialize(self.G)
        data["average_income"] = self.average_income
        data["neighbor_radius"] = self.neighbor_radius
        data["max_time_outside"] = self.max_time_outside
        data["activity_cycle"] = self.activity_cycle
        data["idle_resource_rates"] = self.idle_resource_rates
        data["transportation_resource_rates"] = self.transportation_resource_rates
        data["speed"] = self.speed
        data["transportation_degradation"] = self.transportation_degradation
        data["type"] = self.type
        return data
    
    def deserialize(self, data: dict) -> None:
        """
        Deserialize
        """
        actions_serialized = data["actions"]
        self.actions = {}
        for id in actions_serialized:
            action_queue = ActionQueue(id)
            action_queue.society = self # Binding
            action_queue.deserialize(actions_serialized[id])
            self.actions[id] = action_queue
        self.G = nx_deserialize(data["G"])
        self.average_income = data["average_income"]
        self.neighbor_radius = data["neighbor_radius"]
        self.max_time_outside = data["max_time_outside"]
        self.activity_cycle = data["activity_cycle"]
        self.idle_resource_rates = data["idle_resource_rates"]
        self.transportation_resource_rates = data["transportation_resource_rates"]
        self.transportation_degradation = data["transportation_degradation"]
        self.speed = data["speed"]


if __name__ == "__main__":
    
    from piperabm.infrastructure.samples.infrastructure_0 import model

    model.set_seed(1)
    model.society.generate(num=2)
    society_serialized = model.society.serialize()

    print("society serialized:\n", society_serialized)