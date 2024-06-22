from piperabm.society.actions.queue import ActionQueue
from piperabm.tools import nx_serialize, nx_deserialize


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