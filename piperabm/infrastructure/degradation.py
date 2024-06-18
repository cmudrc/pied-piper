import numpy as np


class Degradation:

    def adjustment_factor(self, degradation: float) -> float:
        k = 1000
        return float(np.exp(degradation / k))

    def calculate_adjusted_length(self, length: float, degradation: float) -> float:
        return length * self.adjustment_factor(degradation)
    
    def top_degraded_edges(self, percent: float = 0):
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