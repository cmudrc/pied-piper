class Serialize:
    """
    Serialization methods
    """

    def serialize(self) -> dict:
        """
        Serialize
        """
        dictionary = {}
        dictionary['time'] = self.time
        dictionary['step'] = self.step
        dictionary['infrastructure'] = self.infrastructure.serialize()
        #dictionary['society'] = self.society.serialize()
        dictionary['name'] = self.name
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        """
        Deserialize
        """
        self.time = dictionary['time']
        self.step = dictionary['step']
        self.infrastructure.deserialize(dictionary['infrastructure'])
        #self.society.deserialize(dictionary['society'])
        self.name = dictionary['name']