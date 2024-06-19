class Degradation:
    """
    Manage edge dergradation methods
    """

    def adjustment_factor(self, usage_impact: float, weather_impact: float) -> float:
        """
        Calculate adjustment factor
        """
        return 1 + (self.coeff_usage * usage_impact) + (self.coeff_weather * weather_impact)

    def calculate_adjusted_length(self, length: float, usage_impact: float, weather_impact: float) -> float:
        """
        Calculate adjusted length
        """
        return length * self.adjustment_factor(
                    usage_impact=usage_impact,
                    weather_impact=weather_impact
                )
    
    def degradation(self, ids: list) -> float:
        """
        Calculate current degradation for an edge
        """
        usage_impact = self.get_edge_attribute(ids=ids, attribute='usage_impact')
        weather_impact = self.get_edge_attribute(ids=ids, attribute='weather_impact')
        return self.adjustment_factor(
            usage_impact=usage_impact,
            weather_impact=weather_impact
        )
    
    def top_degraded_edges(self, percent: float = 0):
        """
        Filter most degradaded edges by their length percentage
        """
        edges_ids = self.streets
        total_length = 0
        edges_info = []
        for edge_ids in edges_ids:
            length = self.get_edge_attribute(ids=edge_ids, attribute='length')
            edge_info = {
                'ids': edge_ids,
                'degradation': self.degradation(id=edge_ids),
                'length': length
            }
            edges_info.append(edge_info)
            total_length += length
        sorted_edges_info = sorted(edges_info, key=lambda x: x['degradation'], reverse=True)
        remaining_length = (percent / 100) * total_length
        result = []
        for edge_info in sorted_edges_info:
            remaining_length -= edge_info['length']
            if remaining_length < 0:
                break
            else:
                result.append(edge_info['ids'])
        return result