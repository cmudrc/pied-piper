from piperabm.infrastructure_new.grammar.rules.rule import Rule, Log
from piperabm.infrastructure_new import Junction
from piperabm.tools.coordinate import distance as ds


class Rule_0(Rule):
    """
    Condition for node to node proximity
    """

    def __init__(self, infrastructure):
        name = "rule 0"
        super().__init__(infrastructure, name)

    def check(self, node_id, other_node_id):
        result = False
        edge_constraint = True
        edge_id = self.infrastructure.edge_id(node_id, other_node_id)
        if edge_id is not None:
            edge_object = self.get(edge_id)
            if edge_object.type == "neighborhood_access":
                edge_constraint = False
        if edge_constraint is True:
            node_object = self.get(node_id)
            other_node_object = self.get(other_node_id)
            distance = ds.point_to_point(
                point_1=node_object.pos,
                point_2=other_node_object.pos
            )
            if distance < self.proximity_radius:
                result = True
        return result
    
    def apply(self, node_id, other_node_id, report=False):
        logs = []
        # Remove possible edge object between nodes
        edge_id = self.infrastructure.edge_id(node_id, other_node_id)
        if edge_id is not None:
            if report is True:
                log = Log(self.infrastructure, edge_id, 'removed')
                logs.append(log)
            self.infrastructure.remove_edge(edge_id)
            self.infrastructure.delete_object(edge_id)

        # Find edges that will overlap after merging
        def end(edge_ids, id):
            """
            Find the other end of edge_ids
            """
            result = None
            if id == edge_ids[0]:
                result = edge_ids[1]
            elif id == edge_ids[1]:
                result = edge_ids[0]
            return result
        
        edges_ids = self.infrastructure.adjacents_ids(node_id)
        other_edges_ids = self.infrastructure.adjacents_ids(other_node_id)
        for edge_ids in edges_ids:
            edge_ids_end = end(edge_ids, node_id)
            for other_edge_ids in other_edges_ids:
                other_edge_ids_end = end(other_edge_ids, other_node_id)
                if edge_ids_end == other_edge_ids_end:
                    other_edge_id = self.infrastructure.edge_id(*other_edge_ids)
                    if report is True:
                        log = Log(self.infrastructure, other_edge_id, 'removed')
                        logs.append(log)
                    self.infrastructure.remove_edge(other_edge_id)
                    self.infrastructure.delete_object(other_edge_id)

        # Merge nodes
        node_object = self.get(node_id)
        other_node_object = self.get(other_node_id)
        pos_node = node_object.pos
        pos_other_node = other_node_object.pos
        pos_new = [
            (pos_node[0] + pos_other_node[0]) / 2,
            (pos_node[1] + pos_other_node[1]) / 2,
        ]
        junction = Junction(pos=pos_new)
        new_id = self.add(junction)
        if report is True:
            log = Log(self.infrastructure, new_id, 'added')
            logs.append(log) 
            log = Log(self.infrastructure, node_id, 'removed')
            logs.append(log)
            log = Log(self.infrastructure, other_node_id, 'removed')
            logs.append(log)
        self.infrastructure.replace_node(node_id, new_id)
        self.infrastructure.replace_node(other_node_id, new_id)

        # Report
        if report is True:
            self.report(logs)
    
    def find(self, report=False):
        anything_happened = False
        nodes = self.infrastructure.junctions
        for node_id in nodes:
            for other_node_id in nodes:
                if node_id != other_node_id:
                    if self.check(node_id, other_node_id) is True:
                        self.apply(node_id, other_node_id, report)
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

    from piperabm.infrastructure_new import Infrastructure, Street

    infrastructure = Infrastructure(proximity_radius=1)
    object_1 = Street(pos_1=[0, 0.1], pos_2=[0, 10])
    object_2 = Street(pos_1=[0.1, 0], pos_2=[10, 0])
    infrastructure.add(object_1)
    infrastructure.add(object_2)
    
    rule = Rule_0(infrastructure)
    rule.find(report=True)
    
