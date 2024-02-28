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
            node_object_new = self.get(new_id)
            if object.id_1 == id:
                object.id_1 = new_id
                object.pos_1 = node_object_new.pos
            elif object.id_2 == id:
                object.id_2 = new_id
                object.pos_2 = node_object_new.pos

    def add(self, object):
        return self.model.add_infrastructure_object(object)
    
    def report(self, logs: list):
        if len(logs) > 0:
            print(">>>" + " " + self.name + ":")
            for log in logs:
                print(log)
        
    def check(self):
        print("NOT IMPLEMENTED YET.")

    def apply(self, report=False):
        print("NOT IMPLEMENTED YET.")


class Log:

    def __init__(self, model, id, activity):
        object = model.get(id)
        self.object_info = self.create_object_info(object)
        self.activity = activity

    def create_object_info(self, object):
        txt = object.category + " "
        if object.category == 'node':
            txt += "in" + " "
            txt += str(object.pos)
        elif object.category == 'edge':
            txt += "between" + " "
            txt += str(object.pos_1) + " and "
            txt += str(object.pos_2)
        return txt

    def __str__(self):
        return "#" + " " + self.activity + ":" + " " + self.object_info
    

if __name__ == "__main__":
    from piperabm.model import Model
    from piperabm.infrastructure import Settlement, Road

    model = Model()
    object_1 = Settlement(pos=[0, 0])
    object_1.id = 1
    model.add(object_1)
    object_2 = Road(pos_1=[5, 5], pos_2=[10, 10])
    object_2.id = 2
    model.add(object_2)

    log = Log(model, id=1, activity='add')
    print(log)
    log = Log(model, id=2, activity='add')
    print(log)