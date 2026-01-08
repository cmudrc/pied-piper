# Custom Degradation

In this example, we see how the user can customize degradation behavior of the infrastrcture elements of the model by providing a custom degradation class. Then, the impact of this change is compared to default model behavior.

This is how the custom degradation file is being served:

```python
from piperabm.infrastructure.degradation import Degradation

class CustomDegradation(Degradation):

    def calculate_adjustment_factor(
        self, usage_impact: float, age_impact: float
    ) -> float:
        """
        Calculate adjustment factor using a custom formula.
        """
        return (
            1 + (self.infrastructure.coeff_usage * usage_impact) + (self.infrastructure.coeff_age * (age_impact ** 2))
        )
        
model.infrastructure.set_degradation(CustomDegradation)
```

When edges degrade, they will become less efficient to be used. It is equivalent of having longer length, since it will take longer (and require more fuel) for the agents to pass through. This is called `adjusted_length` and using custom degradation, the formula to calculate it is customized.