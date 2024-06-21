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
            weather_impact = self.get_edge_attribute(ids=ids, attribute='weather_impact')
            weather_impact += rate * duration
            self.set_edge_attribute(ids=ids, attribute='weather_impact', value=weather_impact)

        # Update adjusted length (streets only)
        for ids in self.streets:
            adjusted_length = self.calculate_adjusted_length(
                length=self.get_edge_attribute(ids=ids, attribute='length'),
                usage_impact=self.get_edge_attribute(ids=ids, attribute='usage_impact'),
                weather_impact=self.get_edge_attribute(ids=ids, attribute='weather_impact')
            )
            self.set_edge_attribute(ids=ids, attribute='adjusted_length', value=adjusted_length)