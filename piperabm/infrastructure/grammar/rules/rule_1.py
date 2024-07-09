from copy import deepcopy

from piperabm.tools.coordinate import distance as ds


class Rule1:
    """
    Condition for node to edge proximity
    """

    name = "rule 1"

    def __init__(self, infrastructure, proximity_radius: float = 1):
        self.infrastructure = infrastructure
        self.proximity_radius = proximity_radius

    def check(self, node_id, edge_ids):
        result = False
        if node_id not in edge_ids:
            distance = ds.point_to_line(
                point=self.infrastructure.get_pos(node_id),
                line=[self.infrastructure.get_pos(edge_ids[0]), self.infrastructure.get_pos(edge_ids[1])],
                segment=True,
                perpendicular_only=True
            )
            if distance is not None and \
            distance < self.proximity_radius:
                result = True
                '''
                distance_1 = ds.point_to_point(
                    point_1=self.infrastructure.get_pos(node_id),
                    point_2=self.infrastructure.get_pos(edge_ids[0])
                )
                distance_2 = ds.point_to_point(
                    point_1=self.infrastructure.get_pos(node_id),
                    point_2=self.infrastructure.get_pos(edge_ids[1])
                )
                if distance_1 > self.proximity_radius and \
                distance_2 > self.proximity_radius:
                    result = True
                '''
        return result
    
    def apply(self, node_id, edge_ids, report=False):
        data = self.infrastructure.get_edge_attributes(ids=edge_ids)
        #edge_type = self.infrastructure.edge_type(ids=edge_ids)
        #degradation = self.infrastructure.edge_degradation(ids=edge_ids)
        data_1 = deepcopy(data)
        data_1['length'] = ds.point_to_point(
            self.infrastructure.get_pos(node_id),
            self.infrastructure.get_pos(edge_ids[0])
        )
        adjustment_factor = self.infrastructure.calculate_adjustment_factor(
            usage_impact=data_1['usage_impact'],
            climate_impact=data_1['climate_impact']
        )
        data_1['adjusted_length'] = self.infrastructure.calculate_adjusted_length(
            length=data_1['length'],
            adjustment_factor=adjustment_factor
        )
        self.infrastructure.G.add_edge(
            node_id,
            edge_ids[0],
            **data_1
        )
        data_2 = deepcopy(data)
        data_2['length'] = ds.point_to_point(
            self.infrastructure.get_pos(node_id),
            self.infrastructure.get_pos(edge_ids[1])
        )
        adjustment_factor = self.infrastructure.calculate_adjustment_factor(
            usage_impact=data_1['usage_impact'],
            climate_impact=data_1['climate_impact']
        )
        data_2['adjusted_length'] = self.infrastructure.calculate_adjusted_length(
            length=data_2['length'],
            adjustment_factor=adjustment_factor
        )
        self.infrastructure.G.add_edge(
            node_id,
            edge_ids[1],
            **data_2
        )
        if report is True:
            print(f">>> {data_1['type']} edge at positions {self.infrastructure.get_pos(node_id)} - {self.infrastructure.get_pos(edge_ids[0])} added.")
            print(f">>> {data_2['type']} edge at positions {self.infrastructure.get_pos(node_id)} - {self.infrastructure.get_pos(edge_ids[1])} added.")
        self.infrastructure.remove_edge(ids=edge_ids, report=report)

    def find(self, report=False):
        anything_happened = False
        nodes = self.infrastructure.junctions
        edges = self.infrastructure.edges
        for node_id in nodes:
            for edge_ids in edges:
                if self.check(node_id, edge_ids) is True:
                    if report is True:
                        print(f"# {self.name}:")
                    self.apply(node_id, edge_ids, report)
                    # Inform an activity
                    anything_happened = True
                # Inform an activity     
                if anything_happened is True:
                    break
            # Inform an activity     
            if anything_happened is True:
                break
        return anything_happened


if __name__ == "__main__":

    from piperabm.infrastructure import Infrastructure

    infrastructure = Infrastructure()
    infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
    infrastructure.add_junction(pos=[5, 0.5])

    rule = Rule1(infrastructure, proximity_radius=1)
    rule.find(report=True)
    print(infrastructure)
