class Degradation:
    """
    Manage edge dergradation methods
    """

    def calculate_adjustment_factor(
        self, usage_impact: float, age_impact: float
    ) -> float:
        """
        Calculate adjustment factor
        """
        return 1 + (self.infrastructure.coeff_usage * usage_impact) + (self.infrastructure.coeff_age * age_impact)

    def adjustment_factor(self, ids: list) -> float:
        """
        Return edge *adjustment_factor*
        """
        return self.calculate_adjustment_factor(
            usage_impact=self.infrastructure.get_usage_impact(ids=ids),
            age_impact=self.infrastructure.get_age_impact(ids=ids),
        )

    def calculate_adjusted_length(
        self, length: float, adjustment_factor: float
    ) -> float:
        """
        Calculate edge *adjusted_length*
        """
        return length * adjustment_factor

    def adjusted_length(self, ids: list) -> float:
        """
        Return edge *adjusted_length*
        """
        return self.calculate_adjusted_length(
            length=self.infrastructure.get_length(ids=ids),
            adjustment_factor=self.adjustment_factor(ids=ids),
        )

    def update_adjusted_length(self, ids: list):
        """
        Update *adjusted_length* value
        """
        adjusted_length = self.adjusted_length(ids=ids)
        self.infrastructure.set_adjusted_length(ids=ids, value=adjusted_length)

    def top_degraded_edges(self, percent: float = 0):
        """
        Filter most degradaded edges by their length percentage
        """
        if percent > 100:
            raise ValueError("enter a value between 0 and 100")
        edges_ids = self.infrastructure.streets
        total_length = 0
        edges_info = []
        for edge_ids in edges_ids:
            length = self.infrastructure.get_edge_attribute(ids=edge_ids, attribute="length")
            edge_info = {
                "ids": edge_ids,
                "degradation": self.adjustment_factor(ids=edge_ids),
                "length": length,
            }
            edges_info.append(edge_info)
            total_length += length
        sorted_edges_info = sorted(
            edges_info, key=lambda x: x["degradation"], reverse=True
        )
        remaining_length = (percent / 100) * total_length
        result = []
        for edge_info in sorted_edges_info:
            remaining_length -= edge_info["length"]
            if remaining_length < 0:
                break
            else:
                result.append(edge_info["ids"])
        return result
