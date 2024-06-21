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
        dictionary['coeff_usage'] = self.coeff_usage
        dictionary['coeff_weather'] = self.coeff_weather
        dictionary['baked_streets'] = self.baked_streets
        dictionary['baked_neighborhood'] = self.baked_neighborhood
        dictionary['heuristic_paths'] = self.heuristic_paths.serialize()
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary):
        """
        Deserialize
        """
        self.G = nx_deserialize(dictionary['G'])
        self.coeff_usage = dictionary['coeff_usage']
        self.coeff_weather = dictionary['coeff_weather']
        self.baked_streets = dictionary['baked_streets']
        self.baked_neighborhood = dictionary['baked_neighborhood']
        self.heuristic_paths.deserialize(dictionary['heuristic_paths'])


if __name__ == "__main__":

    from piperabm.infrastructure.samples import model_0 as model

    print(model.infrastructure.serialize())