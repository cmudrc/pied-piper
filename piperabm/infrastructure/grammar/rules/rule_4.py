import numpy as np

from piperabm.infrastructure.grammar.rules.rule import Rule, Log
from piperabm.infrastructure import Road, Junction
from piperabm.tools.coordinate import distance as ds
from piperabm.tools.linear_algebra import vector as vc


class Rule_4(Rule):
    """
    Condition for connecting isolated non-junction items to the rest
    """

    def __init__(self, model):
        name = "rule 4"
        super().__init__(model, name)

    def check(self, node_id):
        result = False
        smallest_distance_vector = None
        node_object = self.get(node_id)
        # Has to be non-junction and be isolated
        if node_object.type != "junction" and \
        self.model.is_isolated(node_id):
            # Calculate distance_vectors from all edges
            distances = []
            for edge_index in self.edges:
                edge_item = self.get(edge_index)
                distance_vector = ds.point_to_line(
                    point=node_object.pos,
                    line=[edge_item.pos_1, edge_item.pos_2],
                    segment=True,
                    vector=True
                )
                distances.append([edge_index, distance_vector])
            # Find the nearest edge
            smallest_distance = None
            for element in distances:
                distance_vector = element[1]
                distance = vc.magnitude(distance_vector)
                if smallest_distance is None:
                    smallest_distance = distance
                    smallest_distance_vector = distance_vector
                elif distance < smallest_distance:
                    smallest_distance = distance
                    smallest_distance_vector = distance_vector

            if smallest_distance is not None: # When there is no roads available
                #if smallest_distance > self.proximity_radius:
                    #result = True
                result = True

        return result, smallest_distance_vector
    
    def apply(self, report=False):
        anything_happened = False
        for node_id in self.nodes:
            check_result, smallest_distance_vector = self.check(node_id)
            if check_result is True:
                # Update
                node_object = self.get(node_id)
                pos_1 = node_object.pos
                id_1 = node_object.id
                pos_2 = list(np.array(pos_1) + np.array(smallest_distance_vector))
                junction = Junction(pos=pos_2)
                id_2 = self.add(junction)
                road = Road(pos_1=pos_1, pos_2=pos_2)
                road.id_1 = id_1
                road.id_2 = id_2
                id = self.model.add_object_to_library(road)
                if report is True:
                    logs = []
                    log = Log(self.model, id_2, 'added')
                    logs.append(log)
                    log = Log(self.model, id, 'added')
                    logs.append(log)
                # Report
                if report is True:
                    self.report(logs)
                # Inform an activity
                anything_happened = True
            # Inform an activity
            if anything_happened is True:
                break
        return anything_happened
    

if __name__ == "__main__":
    from piperabm.model import Model
    from piperabm.infrastructure import Road, Settlement

    model = Model(proximity_radius=1)
    item_1 = Road(pos_1=[0, 0], pos_2=[10, 0])
    item_2 = Settlement(pos=[5, 4])
    model.add(item_1, item_2)

    rule = Rule_4(model)
    rule.apply(report=True)