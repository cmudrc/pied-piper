class Rule:

    def __init__(self, model, name: str):
        self.model = model
        self.name = name

    @property
    def proximity_radius(self):
        return self.model.proximity_radius

    @property
    def nodes(self):
        return self.model.infrastructure_nodes
    
    @property
    def edges(self):
        return self.model.infrastructure_edges
    
    def get(self, id):
        return self.model.get(id)
    
    def remove(self, id):
        self.model.remove(id)

    def replace_node(self, id, new_id):
        for edge_id in self.edges:
            object = self.get(edge_id)
            if object.id_1 == id:
                object.id_1 = new_id
            elif object.id_2 == id:
                object.id_2 = new_id

    def add(self, object):
        return self.model.add_infrastructure_object(object)

    def check(self):
        print("NOT IMPLEMENTED YET.")

    def apply(self, report=False):
        print("NOT IMPLEMENTED YET.")