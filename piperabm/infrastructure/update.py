class Update:
    """
    Update the network
    """

    def update(self, duration: float):
        """
        Update the network
        """
        # Update degradation from climate change (streets only)
        rate = 0.00001
        for ids in self.streets:
            # Update weather impact
            climate_impact = self.get_climate_impact(ids=ids)
            climate_impact += rate * duration
            self.set_climate_impact(ids=ids, value=climate_impact)
            # Update corresponding edge
            self.update_adjusted_length(ids=ids)


if __name__ == "__main__":

    from piperabm.society.samples.society_1 import model

    model.update(10)
    model.show()