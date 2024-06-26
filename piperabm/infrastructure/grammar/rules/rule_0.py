from piperabm.tools.coordinate import distance as ds


class Rule0:
    """
    Condition for node to node proximity
    """

    name = "rule 0"

    def __init__(self, infrastructure, proximity_radius: float = 1):
        self.infrastructure = infrastructure
        self.proximity_radius = proximity_radius

    def check(self, node_id, other_node_id):
        result = False
        edge_constraint = True
        if self.infrastructure.has_edge(ids=[node_id, other_node_id]):
            if self.infrastructure.get_edge_type(ids=[node_id, other_node_id]) == "neighborhood_access":
                edge_constraint = False
        if edge_constraint is True:
            distance = ds.point_to_point(
                point_1=self.infrastructure.get_pos(node_id),
                point_2=self.infrastructure.get_pos(other_node_id)
            )
            if distance < self.proximity_radius:
                result = True
        return result
    
    def apply(self, node_id, other_node_id, report=False):
        # Remove any edge object between nodes
        if self.infrastructure.has_edge(ids=[node_id, other_node_id]) is True:
            self.infrastructure.remove_edge(ids=[node_id, other_node_id], report=report)

        # Merge nodes
        pos_node = self.infrastructure.get_pos(node_id)
        pos_other_node = self.infrastructure.get_pos(other_node_id)
        pos_new = [
            (pos_node[0] + pos_other_node[0]) / 2,
            (pos_node[1] + pos_other_node[1]) / 2,
        ]
        new_id = self.infrastructure.add_junction(pos=pos_new)
        self.infrastructure.replace_node(node_id, new_id, report=report)
        self.infrastructure.replace_node(other_node_id, new_id, report=report)
    
    def find(self, report=False):
        anything_happened = False
        nodes = self.infrastructure.junctions
        for node_id in nodes:
            for other_node_id in nodes:
                if node_id != other_node_id:
                    if self.check(node_id, other_node_id) is True:
                        if report is True:
                            print(f"\n# {self.name} for nodes at {self.infrastructure.get_pos(node_id)} and {self.infrastructure.get_pos(other_node_id)}")
                        self.apply(node_id, other_node_id, report=report)
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
    infrastructure.add_street(pos_1=[0, 0.1], pos_2=[0, 10])
    infrastructure.add_street(pos_1=[0.1, 0], pos_2=[10, 0])
    
    rule = Rule0(infrastructure, proximity_radius=1)
    rule.find(report=True)
    print(infrastructure)
    