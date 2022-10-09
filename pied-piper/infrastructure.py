import numpy as np

from tools import DegradationProperty


class Road(DegradationProperty):
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
        self.transportation_needs = [
            'foot',
            'vehicle',
        ]

    def length_calc(self, all_nodes):
        start_x, start_y = None, None
        end_x, end_y = None, None
        for node in all_nodes:
            if node.name == self.start_node:
                start_x = node.pos[0]
                start_y = node.pos[1]
            elif node.name == self.end_node:
                end_x = node.pos[0]
                end_y = node.pos[1]
        if start_x and start_y and end_x and end_y:
            val_1 = np.power(end_x - start_x, 2)
            val_2 = np.power(end_y - start_y, 2)
            dist = np.power(val_1 + val_2, 0.5)
        else:
            dist = None
        return dist