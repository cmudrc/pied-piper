from piperabm.infrastructure.grammar.rules.rule import Rule
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
        node_object = self.get(node_id)
        other_node_object = self.get(other_node_id)
        if node_object.type == "junction" or other_node_object.type == "junction":
            #print(node_item.pos, other_node_item.pos)
            distance = ds.point_to_point(
                point_1=node_object.pos,
                point_2=other_node_object.pos
            )
            if distance < self.proximity_radius:
                result = True
        return result
    
    def apply(self, report=False):
        anything_happened = False
        for node_id in self.nodes:
            for other_node_id in self.nodes:
                if node_id != other_node_id:
                    if self.check(node_id, other_node_id):
                        node_object = self.get(node_id)
                        if node_object.type == 'junction':
                            node_id_remove = node_id
                            node_id_replacement = other_node_id
                        else:
                            node_id_remove = other_node_id
                            node_id_replacement = node_id
                        if report is True:
                            print(">>> remove: " + str(node_id_remove))
                        
                        # Update
                        self.model.remove(node_id_remove)
                        edges_from_node = self.infrastructure.edges_from_node(node_id_remove)
                        for edge in edges_from_node:
                            ids = edge[0:2]
                            id = edge[2]['id']
                            self.infrastructure.remove_edge(*ids)
                            index = ids.index(node_id_remove)  # Find the index of the element to replace
                            ids[index] = node_id_replacement
                            self.infrastructure.add_edge(ids[0], ids[1], id)
                        self.infrastructure.remove_node(node_id_remove)

                        anything_happened = True
                        break
                        
            if anything_happened is True:
                break    

        return anything_happened
    

if __name__ == "__main__":
    from piperabm.model import Model
    from piperabm.infrastructure import Junction

    model = Model(proximity_radius=1)
    object_1 = Junction(pos=[0, 0])
    object_2 = Junction(pos=[0.5, 0])
    model.add(object_1, object_2)

    rule = Rule_0(model.infrastructure)
    rule.apply(report=True)
