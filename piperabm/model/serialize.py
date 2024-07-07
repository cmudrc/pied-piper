import numpy as np


class Serialize:
    """
    Serialization methods
    """

    def serialize(self) -> dict:
        """
        Serialize
        """
        data = {}
        data['time'] = self.time
        data['step'] = self.step
        data['infrastructure'] = self.infrastructure.serialize()
        data['society'] = self.society.serialize()
        data['name'] = self.name
        data['prices'] = self.prices
        data['seed'] = self.seed
        data['state'] = self.serialize_state()
        data['type'] = self.type
        return data
    
    def deserialize(self, data: dict) -> None:
        """
        Deserialize
        """
        self.time = data['time']
        self.step = data['step']
        self.infrastructure.deserialize(data['infrastructure'])
        self.society.deserialize(data['society'])
        self.set_seed(data['seed'])
        self.deserialize_state(state=data['state'])
        self.name = data['name']
        self.prices = data['prices']

    def serialize_state(self):
        """
        Serialize numpy random generator state
        """
        state = np.random.get_state()
        return [
            state[0],
            state[1].tolist(),  # Convert numpy array to list
            state[2],
            state[3],
            state[4]
        ]
    
    def deserialize_state(self, state):
        """
        Deserialize numpy random generator state
        """
        restored_state = (
            state[0],
            np.array(state[1], dtype=np.uint32),  # Convert list back to numpy array
            state[2],
            state[3],
            state[4]
        )
        np.random.set_state(restored_state)


if __name__ == "__main__":

    import piperabm as pa

    model = pa.Model(seed=1)
    #print(model.infrastructure.new_id())
    #print(model.infrastructure.new_id())
    data = model.serialize()

    print(data)

    model_new = pa.Model()
    model_new.deserialize(data)
    #print(model_new.infrastructure.new_id())
    #print(model_new.infrastructure.new_id())
    #print(model_new.seed)