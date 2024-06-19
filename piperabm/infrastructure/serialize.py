from piperabm.tools import nx_serialize, nx_deserialize


class Serialize:
    """
    Serialization methods
    """

    def serialize(self):
        """
        Serialize
        """
        dictionary = {}
        dictionary['G'] = nx_serialize(self.G)
        dictionary['heuristic_paths'] = self.heuristic_paths.serialize()
        dictionary['baked_streets'] = self.baked_streets
        dictionary['baked_neighborhood'] = self.baked_neighborhood
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary):
        """
        Deserialize
        """
        self.G = nx_deserialize(dictionary['G'])
        self.heuristic_paths.deserialize(dictionary['heuristic_paths'])
        self.baked_streets = dictionary['baked_streets']
        self.baked_neighborhood = dictionary['baked_neighborhood']