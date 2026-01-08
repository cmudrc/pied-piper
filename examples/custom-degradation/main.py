import piperabm as pa
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


def setup_model():
    model = pa.Model(seed=2)

    # Set up the infrastructure
    model.infrastructure.coeff_usage = 1
    model.infrastructure.coeff_age = 1
    model.infrastructure.add_street(pos_1=[0, 0], pos_2=[-60, 40], name="road")
    model.infrastructure.add_home(pos=[5, 0], id=1, name="home")
    model.infrastructure.add_market(
        pos=[-60, 45],
        id=2,
        name="market",
        resources={
            "food": 100,
            "water": 100,
            "energy": 100,
        },
    )
    model.infrastructure.bake()

    # Set up the society
    model.society.average_income = 1
    agent_id = 1
    home_id = model.infrastructure.homes[0]
    model.society.add_agent(
        id=agent_id,
        home_id=home_id,
        socioeconomic_status=1,
        resources={
            "food": 1,
            "water": 1,
            "energy": 1,
        },
        balance=100,
    )

    return model

edge = (8042686386972756495, 478254495130285640)

# Run the simulation with default degradation
model_default = setup_model()
model_default.run(n=80, step_size=1)

# Run the simulation with custom degradation
model_custom = setup_model()
model_custom.infrastructure.set_degradation(CustomDegradation)  # Set the custom degradation class
model_custom.run(n=80, step_size=1)

# Compare the results
print("Default adjusted length formula:", model_default.infrastructure.get_adjusted_length(ids=edge))
print("Custom adjusted length formula:",model_custom.infrastructure.get_adjusted_length(ids=edge))
