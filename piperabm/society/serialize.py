from piperabm.society.actions.action_queue import ActionQueue
from piperabm.tools.nx_serializer import nx_serialize, nx_deserialize


class Serialize:
    """
    Serialization methods
    """

    def serialize(self) -> dict:
        dictionary = {}
        actions_serialized = {}
        for id in self.actions:
            action_queue = self.actions[id]
            actions_serialized[id] = action_queue.serialize()
        dictionary['actions'] = actions_serialized
        dictionary['G'] = nx_serialize(self.G)
        dictionary['food_price'] = self.food_price
        dictionary['water_price'] = self.water_price
        dictionary['energy_price'] = self.energy_price
        dictionary['average_income'] = self.average_income
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        actions_serialized = dictionary['actions']
        self.actions = {}
        for id in actions_serialized:
            action_queue = ActionQueue(id)
            action_queue.society = self # Binding
            action_queue.deserialize(actions_serialized[id])
            self.actions[id] = action_queue
        self.G = nx_deserialize(dictionary['G'])
        self.food_price = dictionary['food_price']
        self.water_price = dictionary['water_price']
        self.energy_price = dictionary['energy_price']
        self.average_income = dictionary['average_income']


if __name__ == "__main__":
    
    from piperabm.model import Model

    model = Model()
    model.infrastructure.add_home(pos=[0, 0])
    model.bake()
    model.society.generate_agents(num=1)
    society_serialized = model.society.serialize()
    print(society_serialized)