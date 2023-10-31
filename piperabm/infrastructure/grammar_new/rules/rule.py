class Rule:

    def __init__(self, model=None, check=None):
        self.check = check
        self.model = model

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

    def apply(self):
        print("NOT IMPLEMENTED YET.")


if __name__ == "__main__":
    def fun(a):
        return a > 0
    
    r = Rule(check=fun)
    print(r.check(4))