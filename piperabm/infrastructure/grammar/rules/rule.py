class Rule:

    def __init__(self, model, name: str):
        self.model = model
        self.name = name

    @property
    def proximity_radius(self):
        return self.model.proximity_radius

    @property
    def nodes(self):
        return self.model.all_environment_nodes
    
    @property
    def edges(self):
        return self.model.all_environment_edges
    
    def get(self, index):
        return self.model.get(index)
    
    def remove(self, index):
        self.model.remove(index)

    def add(self, item):
        self.model.add(item)

    def check(self):
        print("NOT IMPLEMENTED YET.")

    def apply(self, report=False):
        print("NOT IMPLEMENTED YET.")

    