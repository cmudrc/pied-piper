import numpy as np


class Degradation:

    def adjustment_factor(self, usage_impact: float, weather_impact: float) -> float:
        """
        Calculate adjustment factor
        """
        coeff_usage = 1 / 1000
        coeff_weather = 1
        return 1 + (coeff_usage * usage_impact) + (coeff_weather * weather_impact)

    def calculate_adjusted_length(self, length: float, usage_impact: float, weather_impact: float) -> float:
        """
        Calculate adjusted length
        """
        return length * self.adjustment_factor(
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
            length = self.edge_length(ids=edge_ids)
            total_length += length
            edge_info = {
                'ids': edge_ids,
                'degradation': self.edge_degradation(ids=edge_ids),
                'length': length
            }
            edges_info.append(edge_info)
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