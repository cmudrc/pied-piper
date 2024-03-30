from piperabm.infrastructure_new.grammar.rules.rule import Rule, Log
from piperabm.infrastructure_new import Street, NeighborhoodAccess
from piperabm.tools.coordinate import distance as ds


class Rule_1(Rule):
    """
    Condition for node to edge proximity
    """

    def __init__(self, infrastructure):
        name = "rule 1"
        super().__init__(infrastructure, name)

    def check(self, node_id, edge_id):
        result = False
        node_object = self.get(node_id)
        edge_object = self.get(edge_id)
        distance = ds.point_to_line(
            point=node_object.pos,
            line=[edge_object.pos_1, edge_object.pos_2],
            segment=True
        )
        distance_1 = ds.point_to_point(
            point_1=node_object.pos,
            point_2=edge_object.pos_1
        )
        distance_2 = ds.point_to_point(
            point_1=node_object.pos,
            point_2=edge_object.pos_2
        )
        if distance is not None and \
        distance < self.proximity_radius and \
        distance_1 > self.proximity_radius and \
        distance_2 > self.proximity_radius:
            result = True
        return result
    
    def apply(self, node_id, edge_id, report=False):
        logs = []
        # Create new objects
        node_object = self.get(node_id)
        edge_object = self.get(edge_id)
        if edge_object.type == "street":
            new_edge_object_1 = Street(pos_1=edge_object.pos_1, pos_2=node_object.pos)
            new_edge_object_2 = Street(pos_1=node_object.pos, pos_2=edge_object.pos_2)
        elif edge_object.type == "neighborhood_access":
            new_edge_object_1 = NeighborhoodAccess(pos_1=edge_object.pos_1, pos_2=node_object.pos)
            new_edge_object_2 = NeighborhoodAccess(pos_1=node_object.pos, pos_2=edge_object.pos_2)
        else:
            print("object type not recognized.")
            raise ValueError
        new_edge_id_1 = self.add(new_edge_object_1)
        new_edge_id_2 = self.add(new_edge_object_2)

        if report is True:
            log = Log(self.infrastructure, new_edge_id_1, 'added')
            logs.append(log)
            log = Log(self.infrastructure, new_edge_id_2, 'added')
            logs.append(log)
            log = Log(self.infrastructure, edge_id, 'removed')
            logs.append(log)

        # Remove
        self.infrastructure.remove_edge(edge_id)
        self.infrastructure.delete_object(edge_id)

        # Report
        if report is True:
            self.report(logs)

    def find(self, report=False):
        anything_happened = False
        nodes = self.infrastructure.junctions
        edges = self.infrastructure.edges_id
        for node_id in nodes:
            for edge_id in edges:
                if self.check(node_id, edge_id) is True:
                    self.apply(node_id, edge_id, report)
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
    
    from piperabm.infrastructure_new import Infrastructure, Junction, Street

    infrastructure = Infrastructure(proximity_radius=1)
    object_1 = Street(pos_1=[0, 0], pos_2=[10, 0])
    object_2 = Junction(pos=[5, 0.5])
    infrastructure.add(object_1)
    infrastructure.add(object_2)

    rule = Rule_1(infrastructure)
    rule.find(report=True)
