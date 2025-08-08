from piperabm.infrastructure.degradation import Degradation


class CustomDegradation(Degradation):

    def calculate_adjustment_factor(
        self, usage_impact: float, age_impact: float
    ) -> float:
        """
        Calculate adjustment factor using a custom formula.
        """
        return (
            1 + (self.coeff_usage * usage_impact**1.2) + (self.coeff_age * age_impact)
        )
