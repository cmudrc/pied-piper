import numpy as np

from piperabm.infrastructure_new.grammar.rules.rule import Rule, Log
from piperabm.infrastructure_new import Junction, NeighborhoodAccess
from piperabm.tools.coordinate import distance as ds
from piperabm.tools.linear_algebra import vector as vc


class Rule_3(Rule):
    """
    Condition for connecting isolated non-junction items to the rest
    """

    def __init__(self, infrastructure):
        name = "rule 3"
        super().__init__(infrastructure, name)

    def check(self, node_id):
        result = False
        # Has to be isolated
        if self.infrastructure.is_isolate(node_id):
            result = True
        return result

    def apply(self, node_id, report=False):
        logs = []
        node_object = self.get(node_id)

        # Find the smallest_distance_vector
        distances = []
        for edge_id in self.infrastructure.edges_id:
            edge_object = self.get(edge_id)
            distance_vector = ds.point_to_line(
                point=node_object.pos,
                line=[edge_object.pos_1, edge_object.pos_2],
                segment=True,
                vector=True
            )
            #distances.append([edge_id, distance_vector])
            distances.append(distance_vector)
        # Find the nearest edge
        smallest_distance = None
        for distance_vector in distances:
            distance = vc.magnitude(distance_vector)
            if smallest_distance is None or \
            distance < smallest_distance:
                smallest_distance = distance
                smallest_distance_vector = distance_vector
        
        # Create new objects
        pos_1 = node_object.pos
        pos_2 = list(np.array(pos_1) + np.array(smallest_distance_vector))
        junction = Junction(pos=pos_2)
        id = self.add(junction)
        new_object = NeighborhoodAccess(pos_1=pos_1, pos_2=pos_2)
        new_id = self.infrastructure.new_id
        self.infrastructure.library[new_id] = new_object
        self.infrastructure.G.add_edge(
            id,
            node_id,
            id=new_id
        )
        
        # Report
        if report is True:
            logs = []
            log = Log(self.infrastructure, new_id, 'added')
            logs.append(log)
            log = Log(self.infrastructure, id, 'added')
            logs.append(log)
        
        # Report
        if report is True:
            self.report(logs)
    
    def find(self, report=False):
        anything_happened = False
        nodes = self.infrastructure.nonjunctions
        for node_id in nodes:
            if self.check(node_id) is True:
                self.apply(node_id, report)
                # Inform an activity
                anything_happened = True
            # Inform an activity
            if anything_happened is True:
                break
        return anything_happened
    

if __name__ == "__main__":
    
    from piperabm.infrastructure_new import Infrastructure, Street, Home

    infrastructure = Infrastructure(proximity_radius=1)
    object_1 = Street(pos_1=[0, 0], pos_2=[10, 0])
    object_2 = Home(pos=[5, 4])
    infrastructure.add(object_1)
    infrastructure.add(object_2)

    rule = Rule_3(infrastructure)
    rule.find(report=True)