import numpy as np

from piperabm.infrastructure.grammar.rules.rule import Rule
from piperabm.infrastructure import Road
from piperabm.tools.coordinate import distance as ds
from piperabm.tools.linear_algebra import vector as vc
#from piperabm.tools.coordinate.distance import point_to_line_segment_vector, vector_magnitude


class Rule_4(Rule):
    """
    Condition for connecting isolated non-junction items to the rest
    """

    def __init__(self, model):
        name = "rule 4"
        super().__init__(model, name)

    def check(self, node_item):
        result = False
        smallest_distance_vector = None
        # Has to be non-junction
        if node_item.type != "junction":
            # Must be isolated
            distances = []
            for edge_index in self.edges:
                edge_item = self.get(edge_index)
                distance_vector = ds.point_to_line(
                    point=node_item.pos,
                    line=[edge_item.pos_1, edge_item.pos_2],
                    segment=True,
                    vector=True
                )
                distances.append([edge_index, distance_vector])

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
                if smallest_distance > self.proximity_radius:
                    result = True

        return result, smallest_distance_vector
    
    def apply(self, report=False):
        anything_happened = False
        for node_index in self.nodes:
            node_item = self.get(node_index)
            check_result, smallest_distance_vector = self.check(node_item)
            if check_result is True:

                pos_1 = node_item.pos
                pos_2 = list(np.array(pos_1) + np.array(smallest_distance_vector))
                item = Road(pos_1, pos_2)
                self.add(item)
                if report is True:
                    print(">>> add: " + str(item))
                
                anything_happened = True

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