from piperabm.tools.nx_serializer import nx_serialize, nx_deserialize


class Serialize:
    """
    Serialization methods
    """

    def serialize(self):
        """
        Serialize
        """
        data = {}
        data['G'] = nx_serialize(self.G)
        data['coeff_usage'] = self.coeff_usage
        data['coeff_weather'] = self.coeff_weather
        data['baked_streets'] = self.baked_streets
        data['baked_neighborhood'] = self.baked_neighborhood
        data['heuristic_paths'] = self.heuristic_paths.serialize()
        data['type'] = self.type
        return data
    
    def deserialize(self, data):
        """
        Deserialize
        """
        self.G = nx_deserialize(data['G'])
        self.coeff_usage = data['coeff_usage']
        self.coeff_weather = data['coeff_weather']
        self.baked_streets = data['baked_streets']
        self.baked_neighborhood = data['baked_neighborhood']
        self.heuristic_paths.deserialize(data['heuristic_paths'])


if __name__ == "__main__":

    from piperabm.infrastructure.samples.infrastructure_0 import model

    print(model.infrastructure.serialize())