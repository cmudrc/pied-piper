from core.degradation import DegradationProperty


class Infrastructure(DegradationProperty):
    def __init__(
        self,
        start_node,
        end_node,
        double_sided=True,
        name=None,
        active=True,
        initial_cost=None,
        initiation_date=None,
        distribution=None,
        seed=None
        ):
        super().__init__(
            active=active,
            initial_cost=initial_cost,
            initiation_date=initiation_date,
            distribution=distribution,
            seed=seed
        )
        self.name = name
        self.start_node = start_node
        self.end_node = end_node
        self.double_sided = double_sided
        